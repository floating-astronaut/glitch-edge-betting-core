import unittest

from glitch_betting_core.pricing import edge_percent, no_vig_two_way


class PricingTests(unittest.TestCase):
    def test_no_vig_two_way(self) -> None:
        a, b = no_vig_two_way(0.55, 0.55)
        self.assertAlmostEqual(a, 0.5)
        self.assertAlmostEqual(b, 0.5)

    def test_edge_percent(self) -> None:
        self.assertAlmostEqual(edge_percent(0.54, 0.50), 4.0)


if __name__ == "__main__":
    unittest.main()
