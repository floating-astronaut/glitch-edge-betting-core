import unittest

from glitch_betting_core.staking import capped_kelly_fraction, kelly_fraction_from_edge


class StakingTests(unittest.TestCase):
    def test_capped_kelly_fraction(self) -> None:
        value = capped_kelly_fraction(0.55, 2.10, cap=0.05)
        self.assertGreaterEqual(value, 0.0)
        self.assertLessEqual(value, 0.05)

    def test_kelly_fraction_from_edge(self) -> None:
        value = kelly_fraction_from_edge(8.0, 2.0, fraction=0.25)
        self.assertAlmostEqual(value, 0.02)


if __name__ == "__main__":
    unittest.main()
