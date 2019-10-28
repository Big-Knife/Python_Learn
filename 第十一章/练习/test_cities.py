import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """测试city_functions.py。"""

    def test_city_country(self):
        """传入简单的城市和国家可行吗？"""
        santiago_chile = city_country('santiago', 'chile')

    def test_city_country_population(self):
        """可向形参population传递值吗？"""
        santiago_chile = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago,Chile - population 5000000')


unitt