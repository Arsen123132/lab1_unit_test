import unittest
from temperature_converter import TemperatureConverter


class TestTemperatureConverter(unittest.TestCase):
    
    def setUp(self):
        """Create a fresh converter instance before each test."""
        self.converter = TemperatureConverter()
    
    # === Celsius to Fahrenheit Tests ===
    
    def test_celsius_to_fahrenheit_freezing_point(self):
        """Water freezing point: 0°C should equal 32°F."""
        result = self.converter.celsius_to_fahrenheit(0)
        self.assertEqual(result, 32.0)
    
    def test_celsius_to_fahrenheit_boiling_point(self):
        """Water boiling point: 100°C should equal 212°F."""
        result = self.converter.celsius_to_fahrenheit(100)
        self.assertEqual(result, 212.0)
    
    def test_celsius_to_fahrenheit_negative(self):
        """Negative temperature: -40°C should equal -40°F."""
        result = self.converter.celsius_to_fahrenheit(-40)
        self.assertEqual(result, -40.0)
    
    # === Fahrenheit to Celsius Tests ===
    
    def test_fahrenheit_to_celsius_freezing_point(self):
        """Water freezing point: 32°F should equal 0°C."""
        result = self.converter.fahrenheit_to_celsius(32)
        self.assertAlmostEqual(result, 0.0, places=10)
    
    def test_fahrenheit_to_celsius_boiling_point(self):
        """Water boiling point: 212°F should equal 100°C."""
        result = self.converter.fahrenheit_to_celsius(212)
        self.assertAlmostEqual(result, 100.0, places=10)
    
    # === Kelvin Conversion Tests ===
    
    def test_celsius_to_kelvin_absolute_zero(self):
        """Absolute zero: -273.15°C should equal 0 K."""
        result = self.converter.celsius_to_kelvin(-273.15)
        self.assertAlmostEqual(result, 0.0, places=10)
    
    def test_celsius_to_kelvin_freezing_point(self):
        """Water freezing point: 0°C should equal 273.15 K."""
        result = self.converter.celsius_to_kelvin(0)
        self.assertAlmostEqual(result, 273.15, places=10)
    
    def test_kelvin_to_celsius_room_temperature(self):
        """Room temperature: 293.15 K should equal 20°C."""
        result = self.converter.kelvin_to_celsius(293.15)
        self.assertAlmostEqual(result, 20.0, places=10)
    
    def test_fahrenheit_to_kelvin_freezing_point(self):
        """Water freezing point: 32°F should equal 273.15 K."""
        result = self.converter.fahrenheit_to_kelvin(32)
        self.assertAlmostEqual(result, 273.15, places=10)
    
    def test_kelvin_to_fahrenheit_boiling_point(self):
        """Water boiling point: 373.15 K should equal 212°F."""
        result = self.converter.kelvin_to_fahrenheit(373.15)
        self.assertAlmostEqual(result, 212.0, places=10)
    
    # === Error Handling Tests ===
    
    def test_celsius_below_absolute_zero(self):
        """Temperature below absolute zero in Celsius should raise ValueError."""
        with self.assertRaises(ValueError):
            self.converter.celsius_to_fahrenheit(-300)
    
    def test_fahrenheit_below_absolute_zero(self):
        """Temperature below absolute zero in Fahrenheit should raise ValueError."""
        with self.assertRaises(ValueError):
            self.converter.fahrenheit_to_celsius(-500)
    
    def test_kelvin_below_absolute_zero(self):
        """Negative Kelvin temperature should raise ValueError."""
        with self.assertRaises(ValueError):
            self.converter.kelvin_to_celsius(-1)
    
    # === Generic Convert Method Tests ===
    
    def test_convert_celsius_to_fahrenheit(self):
        """Generic convert method: C to F."""
        result = self.converter.convert(100, 'C', 'F')
        self.assertEqual(result, 212.0)
    
    def test_convert_same_unit(self):
        """Converting to the same unit should return the same value."""
        result = self.converter.convert(25, 'C', 'C')
        self.assertEqual(result, 25)
    
    def test_convert_invalid_source_unit(self):
        """Invalid source unit should raise ValueError."""
        with self.assertRaises(ValueError):
            self.converter.convert(100, 'X', 'F')
    
    def test_convert_case_insensitive(self):
        """Convert method should handle lowercase units."""
        result = self.converter.convert(0, 'c', 'f')
        self.assertEqual(result, 32.0)
    
    # === Round-trip Conversion Tests ===
    
    def test_roundtrip_celsius_fahrenheit_celsius(self):
        """Converting C -> F -> C should return original value."""
        original = 25.0
        fahrenheit = self.converter.celsius_to_fahrenheit(original)
        back_to_celsius = self.converter.fahrenheit_to_celsius(fahrenheit)
        self.assertAlmostEqual(back_to_celsius, original, places=10)
    
    def test_roundtrip_kelvin_celsius_kelvin(self):
        """Converting K -> C -> K should return original value."""
        original = 300.0
        celsius = self.converter.kelvin_to_celsius(original)
        back_to_kelvin = self.converter.celsius_to_kelvin(celsius)
        self.assertAlmostEqual(back_to_kelvin, original, places=10)
    
    def test_is_below_absolute_zero_true(self):
        """Check if -300°C is below absolute zero (should be True)."""
        result = self.converter.is_below_absolute_zero(-300, 'C')
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)