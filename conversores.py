def celsius_para_fahreneit(celsius):
    """
    Converte Celsius para Fahrenheit.
    :param celsius: Temperatura em Celsius
    :return: Temperatura em Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """
    Converte Fahrenheit para Celsius.
    :param fahrenheit: Temperatura em Fahrenheit
    :return: Temperatura em Celsius
    """
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    """
    Converte Celsius para Kelvin.
    :param celsius: Temperatura em Celsius
    :return: Temperatura em Kelvin
    """
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    """
    Converte Kelvin para Celsius.
    :param kelvin: Temperatura em Kelvin
    :return: Temperatura em Celsius
    """
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    """
    Converte Fahrenheit para Kelvin.
    :param fahrenheit: Temperatura em Fahrenheit
    :return: Temperatura em Kelvin
    """
    return (fahrenheit - 32) * 5/9 + 273.15