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
