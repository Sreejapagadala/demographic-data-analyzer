import unittest
from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTestCase(unittest.TestCase):

    def test_calculate_demographic_data(self):

        actual = calculate_demographic_data(print_data=False)

        self.assertEqual(
            actual['average_age_men'],
            39.4
        )

        self.assertEqual(
            actual['percentage_bachelors'],
            16.4
        )

        self.assertEqual(
            actual['highest_earning_country'],
            'Iran'
        )


if __name__ == "__main__":
    unittest.main()
