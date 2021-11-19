import unittest
from city_functions import city_country


class NameTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country(self):
        """能否正确显示城市和国家名吗"""
        formatted_name = city_country('shanghai', 'China')
        self.assertEqual(formatted_name, 'shanghai, China')

    def test_city_country_population(self):
        """能否显示城市，国家和人口"""
        formatted_name = city_country('shanghai', 'China', 5000)
        self.assertEqual(formatted_name, 'shanghai, China-population 5000')


if __name__ == '__main__':
    unittest.main()
