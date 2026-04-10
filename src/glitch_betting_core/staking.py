from __future__ import annotations

from .types import StakingRecommendation


def kelly_fraction(win_probability: float, decimal_odds: float) -> float:
    if decimal_odds <= 1.0:
        raise ValueError("decimal_odds must be greater than 1.0")
    lose_probability = 1.0 - win_probability
    b = decimal_odds - 1.0
    return max(0.0, (b * win_probability - lose_probability) / b)


def kelly_fraction_from_edge(edge_percent: float, decimal_odds: float, fraction: float = 1.0) -> float:
    if decimal_odds <= 1.0:
        raise ValueError("decimal_odds must be greater than 1.0")
    if fraction <= 0.0:
        raise ValueError("fraction must be positive")
    edge = edge_percent / 100.0
    return max(0.0, (edge / (decimal_odds - 1.0)) * fraction)


def recommend_stake_from_edge(
    edge_percent: float,
    decimal_odds: float,
    bankroll: float,
    fraction: float = 1.0,
    market_multiplier: float = 1.0,
    max_bankroll_fraction: float | None = None,
    max_stake: float | None = None,
    min_stake: float = 0.0,
) -> StakingRecommendation:
    if bankroll <= 0.0:
        raise ValueError("bankroll must be positive")
    if market_multiplier <= 0.0:
        raise ValueError("market_multiplier must be positive")
    if min_stake < 0.0:
        raise ValueError("min_stake must be non-negative")
    if max_bankroll_fraction is not None and max_bankroll_fraction <= 0.0:
        raise ValueError("max_bankroll_fraction must be positive")
    if max_stake is not None and max_stake <= 0.0:
        raise ValueError("max_stake must be positive")

    base_kelly_fraction = kelly_fraction_from_edge(edge_percent, decimal_odds, fraction)
    stake = bankroll * base_kelly_fraction * market_multiplier
    capped = False

    if max_bankroll_fraction is not None:
        bankroll_cap = bankroll * max_bankroll_fraction
        if stake > bankroll_cap:
            stake = bankroll_cap
            capped = True

    if max_stake is not None and stake > max_stake:
        stake = max_stake
        capped = True

    min_stake_met = stake >= min_stake
    if not min_stake_met:
        stake = 0.0

    rounded_stake = round(stake, 2)
    recommended_fraction = rounded_stake / bankroll if bankroll > 0.0 else 0.0
    return StakingRecommendation(
        stake=rounded_stake,
        kelly_fraction=base_kelly_fraction,
        recommended_fraction=recommended_fraction,
        bankroll=bankroll,
        edge_percent=edge_percent,
        decimal_odds=decimal_odds,
        market_multiplier=market_multiplier,
        capped=capped,
        min_stake_met=min_stake_met,
    )


def capped_kelly_fraction(win_probability: float, decimal_odds: float, cap: float = 0.05) -> float:
    if cap <= 0.0:
        raise ValueError("cap must be positive")
    return min(cap, kelly_fraction(win_probability, decimal_odds))
