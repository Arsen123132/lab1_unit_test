"""!
@file temperature_converter.py
@brief Module for converting temperatures between Celsius, Fahrenheit, and Kelvin.
@author Arsenii Holoborodko
@date 2025
"""

class TemperatureConverter:
    """!
    @brief A utility class for converting temperatures between Celsius, Fahrenheit, and Kelvin.
    
    Supports conversion between all three temperature scales with proper validation
    and precision handling.
    """
    
    ## Absolute zero in Celsius
    ABSOLUTE_ZERO_CELSIUS = -273.15
    ## Absolute zero in Fahrenheit
    ABSOLUTE_ZERO_FAHRENHEIT = -459.67
    ## Absolute zero in Kelvin
    ABSOLUTE_ZERO_KELVIN = 0.0
    
    def __init__(self):
        """!
        @brief Initialize the TemperatureConverter.
        """
        pass
    
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """!
        @brief Convert Celsius to Fahrenheit.
        
        Formula: \f$ F = C \times \frac{9}{5} + 32 \f$
        
        @param celsius Temperature in Celsius.
        @return Temperature in Fahrenheit.
        @throws ValueError If temperature is below absolute zero.
        """
        if celsius < self.ABSOLUTE_ZERO_CELSIUS:
            raise ValueError(f"Temperature cannot be below absolute zero ({self.ABSOLUTE_ZERO_CELSIUS}°C)")
        
        return (celsius * 9/5) + 32
    
    def celsius_to_kelvin(self, celsius: float) -> float:
        """!
        @brief Convert Celsius to Kelvin.
        
        Formula: \f$ K = C + 273.15 \f$
        
        @param celsius Temperature in Celsius.
        @return Temperature in Kelvin.
        @throws ValueError If temperature is below absolute zero.
        """
        if celsius < self.ABSOLUTE_ZERO_CELSIUS:
            raise ValueError(f"Temperature cannot be below absolute zero ({self.ABSOLUTE_ZERO_CELSIUS}°C)")
        
        return celsius + 273.15
    
    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        """!
        @brief Convert Fahrenheit to Celsius.
        
        Formula: \f$ C = (F - 32) \times \frac{5}{9} \f$
        
        @param fahrenheit Temperature in Fahrenheit.
        @return Temperature in Celsius.
        @throws ValueError If temperature is below absolute zero.
        """
        if fahrenheit < self.ABSOLUTE_ZERO_FAHRENHEIT:
            raise ValueError(f"Temperature cannot be below absolute zero ({self.ABSOLUTE_ZERO_FAHRENHEIT}°F)")
        
        return (fahrenheit - 32) * 5/9
    
    def fahrenheit_to_kelvin(self, fahrenheit: float) -> float:
        """!
        @brief Convert Fahrenheit to Kelvin.
        
        @param fahrenheit Temperature in Fahrenheit.
        @return Temperature in Kelvin.
        @throws ValueError If temperature is below absolute zero.
        """
        if fahrenheit < self.ABSOLUTE_ZERO_FAHRENHEIT:
            raise ValueError(f"Temperature cannot be below absolute zero ({self.ABSOLUTE_ZERO_FAHRENHEIT}°F)")
        
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return self.celsius_to_kelvin(celsius)
    
    def kelvin_to_celsius(self, kelvin: float) -> float:
        """!
        @brief Convert Kelvin to Celsius.
        
        Formula: \f$ C = K - 273.15 \f$
        
        @param kelvin Temperature in Kelvin.
        @return Temperature in Celsius.
        @throws ValueError If temperature is below absolute zero.
        """
        if kelvin < self.ABSOLUTE_ZERO_KELVIN:
            raise ValueError(f"Temperature cannot be below absolute zero ({self.ABSOLUTE_ZERO_KELVIN} K)")
        
        return kelvin - 273.15
    
    def kelvin_to_fahrenheit(self, kelvin: float) -> float:
        """!
        @brief Convert Kelvin to Fahrenheit.
        
        @param kelvin Temperature in Kelvin.
        @return Temperature in Fahrenheit.
        @throws ValueError If temperature is below absolute zero.
        """
        if kelvin < self.ABSOLUTE_ZERO_KELVIN:
            raise ValueError(f"Temperature cannot be below absolute zero ({self.ABSOLUTE_ZERO_KELVIN} K)")
        
        celsius = self.kelvin_to_celsius(kelvin)
        return self.celsius_to_fahrenheit(celsius)
    
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """!
        @brief Generic conversion method that converts between any two temperature units.
        
        @param value Temperature value to convert.
        @param from_unit Source unit ('C', 'F', or 'K').
        @param to_unit Target unit ('C', 'F', or 'K').
        @return Converted temperature value.
        @throws TypeError If value is not numeric.
        @throws ValueError If units are invalid or temperature is below absolute zero.
        """
        # Validate input type
        if not isinstance(value, (int, float)):
            raise TypeError(f"Temperature value must be numeric, got {type(value).__name__}")
        
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        valid_units = {'C', 'F', 'K'}
        if from_unit not in valid_units:
            raise ValueError(f"Invalid source unit: {from_unit}. Must be 'C', 'F', or 'K'")
        if to_unit not in valid_units:
            raise ValueError(f"Invalid target unit: {to_unit}. Must be 'C', 'F', or 'K'")
        
        # Same unit conversion
        if from_unit == to_unit:
            return value
        
        # Define conversion mapping
        conversions = {
            ('C', 'F'): self.celsius_to_fahrenheit,
            ('C', 'K'): self.celsius_to_kelvin,
            ('F', 'C'): self.fahrenheit_to_celsius,
            ('F', 'K'): self.fahrenheit_to_kelvin,
            ('K', 'C'): self.kelvin_to_celsius,
            ('K', 'F'): self.kelvin_to_fahrenheit,
        }
        
        conversion_func = conversions.get((from_unit, to_unit))
        return conversion_func(value)
    
    def is_below_absolute_zero(self, value: float, unit: str) -> bool:
        """!
        @brief Check if a temperature value is below absolute zero.
        
        @param value Temperature value.
        @param unit Temperature unit ('C', 'F', or 'K').
        @return True if below absolute zero, False otherwise.
        """
        unit = unit.upper()
        
        if unit == 'C':
            return value < self.ABSOLUTE_ZERO_CELSIUS
        elif unit == 'F':
            return value < self.ABSOLUTE_ZERO_FAHRENHEIT
        elif unit == 'K':
            return value < self.ABSOLUTE_ZERO_KELVIN
        else:
            raise ValueError(f"Invalid unit: {unit}. Must be 'C', 'F', or 'K'")