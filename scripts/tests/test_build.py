# -*- coding: utf-8 -*-
"""Tests del empaquetador del paquete claude.ai (corre contra el árbol real del repo)."""
import re
import sys
import unittest
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
        self.assertEqual(len(self.items), 52)

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


if __name__ == "__main__":
    unittest.main()
