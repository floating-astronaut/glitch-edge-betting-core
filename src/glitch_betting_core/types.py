from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class MarketPrice:
    selection: str
    decimal_odds: float
    implied_probability: float


@dataclass(frozen=True)
class PricingDecision:
    selection: str
    model_probability: float
    market_probability: float
    edge_percent: float
    recommended_fraction: float


@dataclass(frozen=True)
class StakingRecommendation:
    stake: float
    kelly_fraction: float
    recommended_fraction: float
    bankroll: float
    edge_percent: float
    decimal_odds: float
    market_multiplier: float = 1.0
    capped: bool = False
    min_stake_met: bool = True


@dataclass(frozen=True)
class SignalPayload:
    dedupe_key: str
    market_type: str
    selection: str
    line: float | None
    edge_pct: float
    stake_recommendation: StakingRecommendation
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = dict(self.metadata)
        payload.update(
            {
                "dedupe_key": self.dedupe_key,
                "market_type": self.market_type,
                "selection": self.selection,
                "line": self.line,
                "edge_pct": self.edge_pct,
                "stake_amount": self.stake_recommendation.stake,
                "stake_recommendation": asdict(self.stake_recommendation),
            }
        )
        return payload


@dataclass(frozen=True)
class ExecutionPayload:
    stake_currency: str
    stake_recommendation: StakingRecommendation
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = dict(self.metadata)
        payload.update(
            {
                "stake_amount": self.stake_recommendation.stake,
                "stake_currency": self.stake_currency,
                "stake_recommendation": asdict(self.stake_recommendation),
            }
        )
        return payload
