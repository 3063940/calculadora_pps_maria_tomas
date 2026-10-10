#importamos unittest para poder realizar los tests de la aplicación
import unittest
#importamos las funciones que queremos probar
from programa import calcular_total, pedir_cantidad, pedir_precio, mostrar_resultado 

"""
BLOQUE C: Implementación de pruebas reales
Implementa y ejecuta al menos tres pruebas reales sobre tu aplicación.
Una prueba unitaria.
Una prueba de integración o de sistema.
Una tercera prueba de seguridad (por ejemplo, una validación de acceso o una autorización basada en roles y permisos)
"""

# Prueba Unitaria:

class TestCalcularTotal(unittest.TestCase):
    def test_calcular_total(self):
        """Prueba unitaria para la función calcular_total."""
        self.assertEqual(calcular_total(5, 10), 90)
        self.assertEqual(calcular_total(0, 10), 440)
        self.assertEqual(calcular_total(3, 0), -8)
        self.assertEqual(calcular_total(2, 2.5), 99)


if __name__ == '__main__':
    unittest.main()