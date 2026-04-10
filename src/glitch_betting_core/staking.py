from __future__ import annotations


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


def capped_kelly_fraction(win_probability: float, decimal_odds: float, cap: float = 0.05) -> float:
    if cap <= 0.0:
        raise ValueError("cap must be positive")
    return min(cap, kelly_fraction(win_probability, decimal_odds))
