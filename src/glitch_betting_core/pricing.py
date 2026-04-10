from __future__ import annotations


def no_vig_two_way(prob_a: float, prob_b: float) -> tuple[float, float]:
    total = prob_a + prob_b
    if total <= 0.0:
        raise ValueError("probabilities must sum to a positive number")
    return prob_a / total, prob_b / total


def edge_percent(model_probability: float, market_probability: float) -> float:
    return (model_probability - market_probability) * 100.0
