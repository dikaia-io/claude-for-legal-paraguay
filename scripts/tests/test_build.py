# -*- coding: utf-8 -*-
"""Tests del empaquetador del paquete claude.ai (corre contra el árbol real del repo)."""
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile as zf
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_project_knowledge as bpk


class TestRecolectar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = bpk.recolectar()
        cls.por_tipo = {}
        for it in cls.items:
            cls.por_tipo.setdefault(it["tipo"], []).append(it)
        cls.destinos = {it["destino"] for it in cls.items}

    def test_conteos_por_tipo(self):
        self.assertEqual(len(self.por_tipo["skill"]), 20)
        self.assertEqual(len(self.por_tipo["ref"]), 21)
        self.assertEqual(len(self.por_tipo["asset"]), 2)
        self.assertEqual(len(self.por_tipo["yaml"]), 6)
        self.assertEqual(len(self.por_tipo["glosario"]), 1)
        self.assertEqual(len(self.por_tipo["plantilla"]), 1)
        self.assertEqual(len(self.por_tipo["seguridad"]), 1)
        self.assertEqual(len(self.por_tipo["log"]), 1)
        self.assertEqual(len(self.items), 53)

    def test_destinos_clave(self):
        for esperado in [
            "SKILL-setup.md",
            "SKILL-liquidaciones.md",
            "REF-inconstitucionalidad--vias-y-plazos.md",
            "REF-revision-contractual--ficha-servicios.md",
            "ASSET-dictamenes--template_dictamen.txt",
            "plantilla-perfil.md",
            "seguridad-y-privacidad.md",
            "leyes.yaml",
            "terminologia-paraguay.md",
            "verification-log.md",
        ]:
            self.assertIn(esperado, self.destinos, esperado)

    def test_sin_destinos_duplicados(self):
        self.assertEqual(len(self.destinos), len(self.items))

    def test_todo_plugin_conocido(self):
        for it in self.items:
            if it["plugin"] is not None:
                self.assertIn(it["plugin"], bpk.ESTADO_PLUGINS)


class TestReescritura(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = bpk.recolectar()
        cls.mapa = bpk.mapa_reescritura(cls.items)

    def test_mapa_basico(self):
        self.assertEqual(self.mapa["references/ficha-servicios.md"],
                         "REF-revision-contractual--ficha-servicios.md")
        self.assertEqual(self.mapa["references/vias-y-plazos.md"],
                         "REF-inconstitucionalidad--vias-y-plazos.md")
        self.assertEqual(self.mapa["shared/authorities/leyes.yaml"], "leyes.yaml")
        self.assertEqual(self.mapa["shared/templates/legal.local.md.template"],
                         "plantilla-perfil.md")
        self.assertEqual(self.mapa["docs/seguridad-y-privacidad.md"],
                         "seguridad-y-privacidad.md")

    def test_reescritura_cruzada_entre_skills(self):
        # plazos (core) cita references/vias-y-plazos.md, que vive en inconstitucionalidad
        texto = "ver `references/vias-y-plazos.md` y `shared/authorities/leyes.yaml`"
        out = bpk.reescribir(texto, self.mapa)
        self.assertIn("REF-inconstitucionalidad--vias-y-plazos.md", out)
        self.assertIn("`leyes.yaml`", out)
        bpk.validar_sin_residuos("prueba", out)  # no debe lanzar

    def test_residuos_detectados(self):
        with self.assertRaises(bpk.BuildError):
            bpk.validar_sin_residuos("prueba", "leer references/no-existe.md")
        with self.assertRaises(bpk.BuildError):
            bpk.validar_sin_residuos("prueba", "ver shared/authorities/leyes.yaml")


class TestInstruccionesYBanner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = bpk.recolectar()
        cls.mapa = bpk.mapa_reescritura(cls.items)

    def _item(self, destino):
        return next(it for it in self.items if it["destino"] == destino)

    def test_banner_solo_en_beta(self):
        beta = bpk.contenido_destino(self._item("SKILL-red-flags.md"), self.mapa)
        estable = bpk.contenido_destino(self._item("SKILL-liquidaciones.md"), self.mapa)
        self.assertTrue(beta.decode("utf-8").startswith("> ⚠️ **BETA"))
        self.assertFalse(estable.decode("utf-8").startswith("> ⚠️"))

    def test_asset_no_md_intacto(self):
        item = self._item("ASSET-dictamenes--template_dictamen.txt")
        self.assertEqual(bpk.contenido_destino(item, self.mapa),
                         item["origen"].read_bytes())

    def test_instrucciones(self):
        texto = bpk.generar_instrucciones(self.mapa)
        self.assertTrue(texto.startswith("# Perfil de práctica"))
        self.assertIn("## Arranque del asistente", texto)
        self.assertIn("perfil-del-abogado.md", texto)
        self.assertIn("configuración exprés", texto)
        self.assertNotIn("shared/authorities/", texto)
        self.assertNotIn("docs/seguridad-y-privacidad.md", texto)
        sello = re.search(r"Paquete v(\d+\.\d+\.\d+) — commit (\S+) — generado el "
                          r"(\d{4}-\d{2}-\d{2})\. Contrato de instalación v(\d+)\.", texto)
        self.assertIsNotNone(sello)
        self.assertEqual(sello.group(1), bpk.leer_version())
        self.assertEqual(sello.group(4), bpk.leer_contrato())


class TestConstruirYZip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name) / "paquete"
        cls.manifiesto = bpk.construir(cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_estructura(self):
        for nombre in ["LEEME-PRIMERO.md", "instrucciones-del-proyecto.md",
                       "manifiesto.json", "LICENSE", "NOTICE"]:
            self.assertTrue((self.out / nombre).exists(), nombre)
        self.assertEqual(len(list((self.out / "knowledge").iterdir())), 53)

    def test_manifiesto(self):
        import hashlib
        self.assertEqual(self.manifiesto["version"], bpk.leer_version())
        self.assertEqual(self.manifiesto["estado_plugins"], bpk.ESTADO_PLUGINS)
        self.assertEqual(self.manifiesto["total_archivos"],
                         len(self.manifiesto["archivos"]))
        for entrada in self.manifiesto["archivos"]:
            ruta = self.out / entrada["destino"]
            self.assertTrue(ruta.exists(), entrada["destino"])
            self.assertEqual(hashlib.sha256(ruta.read_bytes()).hexdigest(),
                             entrada["sha256"], entrada["destino"])

    def test_zip(self):
        destino_zip = Path(self.tmp.name) / "paquete-claude-ai.zip"
        bpk.empaquetar_zip(self.out, destino_zip)
        with zf.ZipFile(destino_zip) as z:
            nombres = z.namelist()
            self.assertIn("LEEME-PRIMERO.md", nombres)
            self.assertIn("knowledge/SKILL-setup.md", nombres)
            leeme = z.read("LEEME-PRIMERO.md").decode("utf-8")
            self.assertIn("Contrato de instalación v1", leeme)

    def test_yaml_como_txt(self):
        out2 = Path(self.tmp.name) / "paquete-txt"
        bpk.construir(out2, yaml_como_txt=True)
        nombres = {p.name for p in (out2 / "knowledge").iterdir()}
        self.assertIn("leyes.yaml.txt", nombres)
        self.assertNotIn("leyes.yaml", nombres)


class TestScriptsDeVerificacion(unittest.TestCase):
    def _correr(self, *args):
        return subprocess.run([sys.executable, *args], capture_output=True,
                              text=True, encoding="utf-8", errors="replace", cwd=bpk.REPO)

    def test_paquete_ok_y_tag_mal(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "paquete"
            bpk.construir(out)
            destino_zip = Path(tmp) / "paquete-claude-ai.zip"
            bpk.empaquetar_zip(out, destino_zip)
            ok = self._correr("scripts/test_paquete.py", str(destino_zip))
            self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
            mal = self._correr("scripts/test_paquete.py", str(destino_zip),
                               "--tag", "v9.9.9")
            self.assertEqual(mal.returncode, 1)

    def test_check_versiones(self):
        version = bpk.leer_version()
        ok = self._correr("scripts/check_versiones.py", f"v{version}")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        mal = self._correr("scripts/check_versiones.py", "v9.9.9")
        self.assertEqual(mal.returncode, 1)

    def test_controles_estaticos(self):
        for script, argumentos in [
            ("scripts/check_project_status.py", []),
            ("scripts/validate_plugins.py", []),
            ("scripts/validate_authorities.py", ["--strict"]),
        ]:
            resultado = self._correr(script, *argumentos)
            self.assertEqual(
                resultado.returncode,
                0,
                f"{script}\n{resultado.stdout}{resultado.stderr}",
            )


if __name__ == "__main__":
    unittest.main()
