# -*- coding: utf-8 -*-
"""Tests del empaquetador del paquete claude.ai (corre contra el árbol real del repo)."""
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


if __name__ == "__main__":
    unittest.main()
