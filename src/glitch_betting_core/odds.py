from __future__ import annotations


def decimal_to_probability(decimal_odds: float) -> float:
    if decimal_odds <= 1.0:
        raise ValueError("decimal_odds must be greater than 1.0")
    return 1.0 / decimal_odds


def probability_to_decimal(probability: float) -> float:
    if probability <= 0.0 or probability >= 1.0:
        raise ValueError("probability must be between 0 and 1")
    return 1.0 / probability


def american_to_probability(american_odds: int) -> float:
    if american_odds == 0:
        raise ValueError("american_odds cannot be 0")
    if american_odds > 0:
        return 100.0 / (american_odds + 100.0)
    return abs(american_odds) / (abs(american_odds) + 100.0)
