"""!
@file test_temperature_converter.py
@brief Unit tests for the TemperatureConverter class.

This module contains a comprehensive suite of tests to verify the correctness,
robustness, and error handling of the TemperatureConverter class.

@author Arsenii Holoborodko
@date 2025
"""

import unittest
from temperature_converter import TemperatureConverter


class TestTemperatureConverter(unittest.TestCase):
    """!
    @brief Test suite for the TemperatureConverter class.
    
    Inherits from unittest.TestCase. Covers the following scenarios:
    - Standard conversions (freezing/boiling points).
    - Boundary values (absolute zero).
    - Error handling (exceptions).
    - Round-trip conversions.
    """
    
    def setUp(self):
        """!
        @brief Create a fresh converter instance before each test.
        
        This ensures that tests remain isolated and do not share state.
        """
        self.converter = TemperatureConverter()
    
    # === Celsius to Fahrenheit Tests ===
    
    def test_celsius_to_fahrenheit_freezing_point(self):
        """!
        @brief Test conversion: Water freezing point.
        @details Verifies that 0°C is correctly converted to 32°F.
        """
        result = self.converter.celsius_to_fahrenheit(0)
        self.assertEqual(result, 32.0)
    
    def test_celsius_to_fahrenheit_boiling_point(self):
        """!
        @brief Test conversion: Water boiling point.
        @details Verifies that 100°C is correctly converted to 212°F.
        """
        result = self.converter.celsius_to_fahrenheit(100)
        self.assertEqual(result, 212.0)
    
    def test_celsius_to_fahrenheit_negative(self):
        """!
        @brief Test conversion: Negative temperature.
        @details Verifies that -40°C is correctly converted to -40°F (the crossover point).
        """
        result = self.converter.celsius_to_fahrenheit(-40)
        self.assertEqual(result, -40.0)
    
    # === Fahrenheit to Celsius Tests ===
    
    def test_fahrenheit_to_celsius_freezing_point(self):
        """!
        @brief Test conversion: Water freezing point.
        @details Verifies that 32°F is correctly converted to 0°C.
        """
        result = self.converter.fahrenheit_to_celsius(32)
        self.assertAlmostEqual(result, 0.0, places=6)
    
    def test_fahrenheit_to_celsius_boiling_point(self):
        """!
        @brief Test conversion: Water boiling point.
        @details Verifies that 212°F is correctly converted to 100°C.
        """
        result = self.converter.fahrenheit_to_celsius(212)
        self.assertAlmostEqual(result, 100.0, places=6)
    
    # === Kelvin Conversion Tests ===
    
    def test_celsius_to_kelvin_absolute_zero(self):
        """!
        @brief Test conversion: Absolute zero (C -> K).
        @details Verifies that -273.15°C is correctly converted to 0 K.
        """
        result = self.converter.celsius_to_kelvin(-273.15)
        self.assertAlmostEqual(result, 0.0, places=6)
    
    def test_celsius_to_kelvin_freezing_point(self):
        """!
        @brief Test conversion: Water freezing point (C -> K).
        @details Verifies that 0°C is correctly converted to 273.15 K.
        """
        result = self.converter.celsius_to_kelvin(0)
        self.assertAlmostEqual(result, 273.15, places=6)
    
    def test_kelvin_to_celsius_room_temperature(self):
        """!
        @brief Test conversion: Room temperature (K -> C).
        @details Verifies that 293.15 K is correctly converted to 20°C.
        """
        result = self.converter.kelvin_to_celsius(293.15)
        self.assertAlmostEqual(result, 20.0, places=6)
    
    def test_fahrenheit_to_kelvin_freezing_point(self):
        """!
        @brief Test conversion: Water freezing point (F -> K).
        @details Verifies that 32°F is correctly converted to 273.15 K.
        """
        result = self.converter.fahrenheit_to_kelvin(32)
        self.assertAlmostEqual(result, 273.15, places=6)
    
    def test_kelvin_to_fahrenheit_boiling_point(self):
        """!
        @brief Test conversion: Water boiling point (K -> F).
        @details Verifies that 373.15 K is correctly converted to 212°F.
        """
        result = self.converter.kelvin_to_fahrenheit(373.15)
        self.assertAlmostEqual(result, 212.0, places=6)
    
    # === Error Handling Tests ===
    
    def test_celsius_below_absolute_zero(self):
        """!
        @brief Test error handling: Celsius below absolute zero.
        @throws ValueError Should be raised when input is below -273.15°C.
        """
        with self.assertRaisesRegex(ValueError, "below absolute zero"):
            self.converter.celsius_to_fahrenheit(-300)
    
    def test_fahrenheit_below_absolute_zero(self):
        """!
        @brief Test error handling: Fahrenheit below absolute zero.
        @throws ValueError Should be raised when input is below -459.67°F.
        """
        with self.assertRaisesRegex(ValueError, "below absolute zero"):
            self.converter.fahrenheit_to_celsius(-500)
    
    def test_kelvin_below_absolute_zero(self):
        """!
        @brief Test error handling: Kelvin below absolute zero.
        @throws ValueError Should be raised when input is negative.
        """
        with self.assertRaisesRegex(ValueError, "below absolute zero"):
            self.converter.kelvin_to_celsius(-1)
    
    def test_celsius_at_absolute_zero(self):
        """!
        @brief Test boundary condition: Exact absolute zero (Celsius).
        @details Should NOT raise an error for -273.15°C.
        """
        result = self.converter.celsius_to_kelvin(-273.15)
        self.assertAlmostEqual(result, 0.0, places=6)
    
    def test_fahrenheit_at_absolute_zero(self):
        """!
        @brief Test boundary condition: Exact absolute zero (Fahrenheit).
        @details Should NOT raise an error for -459.67°F.
        """
        result = self.converter.fahrenheit_to_kelvin(-459.67)
        self.assertAlmostEqual(result, 0.0, places=6)
    
    def test_kelvin_at_absolute_zero(self):
        """!
        @brief Test boundary condition: Exact absolute zero (Kelvin).
        @details Should NOT raise an error for 0 K.
        """
        result = self.converter.kelvin_to_celsius(0)
        self.assertAlmostEqual(result, -273.15, places=6)
    
    # === Generic Convert Method Tests ===
    
    def test_convert_celsius_to_fahrenheit(self):
        """!
        @brief Test generic convert method: C -> F.
        """
        result = self.converter.convert(100, 'C', 'F')
        self.assertEqual(result, 212.0)
    
    def test_convert_same_unit(self):
        """!
        @brief Test generic convert method: Same unit conversion.
        @details Verifies that converting C to C returns the original value.
        """
        result = self.converter.convert(25, 'C', 'C')
        self.assertEqual(result, 25)
    
    def test_convert_invalid_source_unit(self):
        """!
        @brief Test error handling: Invalid source unit.
        @throws ValueError Should raise error for unknown unit code.
        """
        with self.assertRaisesRegex(ValueError, "Invalid source unit"):
            self.converter.convert(100, 'X', 'F')
    
    def test_convert_invalid_target_unit(self):
        """!
        @brief Test error handling: Invalid target unit.
        @throws ValueError Should raise error for unknown unit code.
        """
        with self.assertRaisesRegex(ValueError, "Invalid target unit"):
            self.converter.convert(100, 'C', 'Z')
    
    def test_convert_case_insensitive(self):
        """!
        @brief Test generic convert method: Case insensitivity.
        @details Verifies that 'c' and 'f' work same as 'C' and 'F'.
        """
        result = self.converter.convert(0, 'c', 'f')
        self.assertEqual(result, 32.0)
    
    def test_convert_kelvin_case_insensitive(self):
        """!
        @brief Test generic convert method: Case insensitivity for Kelvin.
        """
        result = self.converter.convert(273.15, 'k', 'c')
        self.assertAlmostEqual(result, 0.0, places=6)
    
    def test_convert_non_numeric_input(self):
        """!
        @brief Test error handling: Non-numeric input.
        @throws TypeError Should raise error when input is a string.
        """
        with self.assertRaises(TypeError):
            self.converter.convert("100", 'C', 'F')
    
    def test_convert_none_input(self):
        """!
        @brief Test error handling: None input.
        @throws TypeError Should raise error when input is None.
        """
        with self.assertRaises(TypeError):
            self.converter.convert(None, 'C', 'F')
    
    # === Round-trip Conversion Tests ===
    
    def test_roundtrip_celsius_fahrenheit_celsius(self):
        """!
        @brief Test round-trip conversion: C -> F -> C.
        @details Ensures mathematical consistency across transformations.
        """
        original = 25.0
        fahrenheit = self.converter.celsius_to_fahrenheit(original)
        back_to_celsius = self.converter.fahrenheit_to_celsius(fahrenheit)
        self.assertAlmostEqual(back_to_celsius, original, places=6)
    
    def test_roundtrip_kelvin_celsius_kelvin(self):
        """!
        @brief Test round-trip conversion: K -> C -> K.
        @details Ensures mathematical consistency across transformations.
        """
        original = 300.0
        celsius = self.converter.kelvin_to_celsius(original)
        back_to_kelvin = self.converter.celsius_to_kelvin(celsius)
        self.assertAlmostEqual(back_to_kelvin, original, places=6)
    
    def test_is_below_absolute_zero_true(self):
        """!
        @brief Test validation helper: Value below absolute zero.
        @details Should return True for -300°C.
        """
        result = self.converter.is_below_absolute_zero(-300, 'C')
        self.assertTrue(result)
    
    def test_is_below_absolute_zero_false_celsius(self):
        """!
        @brief Test validation helper: Value above absolute zero.
        @details Should return False for 0°C.
        """
        result = self.converter.is_below_absolute_zero(0, 'C')
        self.assertFalse(result)
    
    def test_is_below_absolute_zero_false_kelvin(self):
        """!
        @brief Test validation helper: Kelvin value.
        @details Should return False for 100 K.
        """
        result = self.converter.is_below_absolute_zero(100, 'K')
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()