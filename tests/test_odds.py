import unittest

from glitch_betting_core.odds import american_to_probability, decimal_to_probability, probability_to_decimal


class OddsTests(unittest.TestCase):
    def test_decimal_to_probability(self) -> None:
        self.assertAlmostEqual(decimal_to_probability(2.0), 0.5)

    def test_probability_to_decimal(self) -> None:
        self.assertAlmostEqual(probability_to_decimal(0.5), 2.0)

    def test_american_to_probability_positive(self) -> None:
        self.assertAlmostEqual(american_to_probability(150), 0.4)

    def test_american_to_probability_negative(self) -> None:
        self.assertAlmostEqual(american_to_probability(-150), 0.6)


if __name__ == "__main__":
    unittest.main()
