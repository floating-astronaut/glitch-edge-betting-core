import unittest

from glitch_betting_core.types import ExecutionPayload, SignalPayload, StakingRecommendation


class PayloadTypeTests(unittest.TestCase):
    def test_signal_payload_to_dict(self) -> None:
        recommendation = StakingRecommendation(
            stake=10.0,
            kelly_fraction=0.0,
            recommended_fraction=0.0,
            bankroll=0.0,
            edge_percent=4.1,
            decimal_odds=2.15,
        )
        payload = SignalPayload(
            dedupe_key="abc",
            market_type="moneyline",
            selection="Heat",
            line=None,
            edge_pct=0.041,
            stake_recommendation=recommendation,
            metadata={"match_name": "Celtics @ Heat"},
        ).to_dict()
        self.assertEqual(payload["dedupe_key"], "abc")
        self.assertEqual(payload["stake_amount"], 10.0)
        self.assertEqual(payload["stake_recommendation"]["decimal_odds"], 2.15)
        self.assertEqual(payload["match_name"], "Celtics @ Heat")

    def test_execution_payload_to_dict(self) -> None:
        recommendation = StakingRecommendation(
            stake=12.5,
            kelly_fraction=0.0,
            recommended_fraction=0.0,
            bankroll=0.0,
            edge_percent=5.0,
            decimal_odds=1.95,
        )
        payload = ExecutionPayload(
            stake_currency="USD",
            stake_recommendation=recommendation,
            metadata={"selection": "Under 227.5"},
        ).to_dict()
        self.assertEqual(payload["stake_amount"], 12.5)
        self.assertEqual(payload["stake_currency"], "USD")
        self.assertEqual(payload["selection"], "Under 227.5")


if __name__ == "__main__":
    unittest.main()
