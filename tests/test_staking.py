import unittest

from glitch_betting_core.staking import (
    capped_kelly_fraction,
    kelly_fraction_from_edge,
    recommend_stake_from_edge,
)


class StakingTests(unittest.TestCase):
    def test_capped_kelly_fraction(self) -> None:
        value = capped_kelly_fraction(0.55, 2.10, cap=0.05)
        self.assertGreaterEqual(value, 0.0)
        self.assertLessEqual(value, 0.05)

    def test_kelly_fraction_from_edge(self) -> None:
        value = kelly_fraction_from_edge(8.0, 2.0, fraction=0.25)
        self.assertAlmostEqual(value, 0.02)

    def test_recommend_stake_from_edge(self) -> None:
        recommendation = recommend_stake_from_edge(
            edge_percent=8.0,
            decimal_odds=2.0,
            bankroll=1000.0,
            fraction=0.25,
            market_multiplier=1.5,
            max_bankroll_fraction=0.025,
            max_stake=100.0,
            min_stake=10.0,
        )
        self.assertEqual(recommendation.stake, 25.0)
        self.assertAlmostEqual(recommendation.kelly_fraction, 0.02)
        self.assertAlmostEqual(recommendation.recommended_fraction, 0.025)
        self.assertTrue(recommendation.capped)
        self.assertTrue(recommendation.min_stake_met)


if __name__ == "__main__":
    unittest.main()
