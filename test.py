import unittest
from app import app


class TestTrigCalculator(unittest.TestCase):
    # Настройка тестового клиента Flask
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Тест для вычисления синуса
    def test_sin_function(self):
        response = self.app.post('/', data={
            'angle': '30',
            'function': 'sin',
            'precision': '5',
            'unit': 'degrees'
        })
        # Проверяем, что результат вычисления правильный (sin(30°) = 0.5)
        self.assertIn('0.5', response.get_data(as_text=True))

    # Тест для вычисления косинуса
    def test_cos_function(self):
        response = self.app.post('/', data={
            'angle': '60',
            'function': 'cos',
            'precision': '5',
            'unit': 'degrees'
        })
        # Проверяем, что результат вычисления правильный (cos(60°) = 0.5)
        self.assertIn('0.5', response.get_data(as_text=True))

    # Тест для вычисления тангенса
    def test_tan_function(self):
        response = self.app.post('/', data={
            'angle': '45',
            'function': 'tan',
            'precision': '5',
            'unit': 'degrees'
        })
        # Проверяем, что результат вычисления правильный (tan(45°) = 1)
        self.assertIn('1.0', response.get_data(as_text=True))

    # Тест для неправильного ввода угла (например, текст вместо числа)
    def test_invalid_angle(self):
        response = self.app.post('/', data={
            'angle': 'abc',
            'function': 'sin',
            'precision': '5',
            'unit': 'degrees'
        })
        # Проверяем, что появилась ошибка
        self.assertIn('Ошибка ввода данных. Проверьте правильность значений.', response.get_data(as_text=True))

    # Тест для неверного значения функции
    def test_invalid_function(self):
        response = self.app.post('/', data={
            'angle': '30',
            'function': 'invalid_function',
            'precision': '5',
            'unit': 'degrees'
        })
        # Проверяем, что появилась ошибка
        self.assertIn('Неизвестная функция', response.get_data(as_text=True))

    # Тест для вычисления синуса в радианах
    def test_sin_function_radians(self):
        response = self.app.post('/', data={
            'angle': '0.5235987756',  # Это 30 градусов в радианах
            'function': 'sin',
            'precision': '5',
            'unit': 'radians'
        })
        # Проверяем, что результат вычисления правильный (sin(0.5236 rad) ≈ 0.5)
        self.assertIn('0.5', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
