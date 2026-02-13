from __future__ import annotations

from dataclasses import dataclass
import math
import random


@dataclass(frozen=True)
class IndicatorSnapshot:
    symbol: str
    latest_price: float
    rsi_14: float
    macd: float
    macd_signal: float
    macd_histogram: float
    score: float
    bias: str


def generate_price_series(days: int, seed: int = 42) -> list[float]:
    if days < 30:
        raise ValueError("days must be >= 30")

    rng = random.Random(seed)
    prices = [100.0]

    for i in range(1, days):
        trend_component = 0.0008
        cycle_component = math.sin(i / 9.0) * 0.0022
        noise_component = rng.uniform(-0.012, 0.012)
        daily_return = trend_component + cycle_component + noise_component
        prices.append(max(1.0, prices[-1] * (1 + daily_return)))

    return prices


def _ema(values: list[float], period: int) -> list[float]:
    if len(values) < period:
        raise ValueError("Not enough values to compute EMA")

    multiplier = 2 / (period + 1)
    seed = sum(values[:period]) / period
    ema_values = [seed]

    for price in values[period:]:
        ema_values.append((price - ema_values[-1]) * multiplier + ema_values[-1])

    return ema_values


def calculate_rsi(prices: list[float], period: int = 14) -> float:
    if len(prices) <= period:
        raise ValueError("Not enough prices for RSI")

    deltas = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    gains = [max(delta, 0) for delta in deltas]
    losses = [abs(min(delta, 0)) for delta in deltas]

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    for i in range(period, len(gains)):
        avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
        avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def calculate_macd(
    prices: list[float], fast_period: int = 12, slow_period: int = 26, signal_period: int = 9
) -> tuple[float, float, float]:
    if len(prices) < slow_period + signal_period:
        raise ValueError("Not enough prices for MACD")

    fast_ema = _ema(prices, fast_period)
    slow_ema = _ema(prices, slow_period)

    offset = slow_period - fast_period
    macd_line = [fast_ema[i + offset] - slow_ema[i] for i in range(len(slow_ema))]
    signal_line = _ema(macd_line, signal_period)

    macd_latest = macd_line[-1]
    signal_latest = signal_line[-1]
    histogram_latest = macd_latest - signal_latest

    return macd_latest, signal_latest, histogram_latest


def score_snapshot(rsi: float, macd: float, histogram: float) -> tuple[float, str]:
    score = 50.0

    if rsi < 30:
        score += 18
    elif rsi > 70:
        score -= 18
    elif 45 <= rsi <= 60:
        score += 5

    if macd > 0:
        score += 12
    else:
        score -= 12

    if histogram > 0:
        score += 10
    else:
        score -= 10

    score = max(0.0, min(100.0, score))

    if score >= 65:
        bias = "bullish"
    elif score <= 35:
        bias = "bearish"
    else:
        bias = "neutral"

    return score, bias


def build_snapshot(symbol: str, prices: list[float]) -> IndicatorSnapshot:
    rsi = calculate_rsi(prices)
    macd, macd_signal, histogram = calculate_macd(prices)
    score, bias = score_snapshot(rsi=rsi, macd=macd, histogram=histogram)

    return IndicatorSnapshot(
        symbol=symbol,
        latest_price=prices[-1],
        rsi_14=rsi,
        macd=macd,
        macd_signal=macd_signal,
        macd_histogram=histogram,
        score=score,
        bias=bias,
    )
