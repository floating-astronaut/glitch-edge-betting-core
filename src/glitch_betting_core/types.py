from __future__ import annotations

from dataclasses import dataclass


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
