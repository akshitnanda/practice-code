from iron_alpha_lab.signals import (
    build_snapshot,
    calculate_macd,
    calculate_rsi,
    generate_price_series,
)


def test_generate_price_series_length_and_floor() -> None:
    prices = generate_price_series(days=120, seed=7)
    assert len(prices) == 120
    assert min(prices) >= 1.0


def test_rsi_in_expected_range() -> None:
    prices = generate_price_series(days=140, seed=13)
    rsi = calculate_rsi(prices)
    assert 0 <= rsi <= 100


def test_macd_tuple_shape() -> None:
    prices = generate_price_series(days=140, seed=13)
    macd, signal, hist = calculate_macd(prices)
    assert isinstance(macd, float)
    assert isinstance(signal, float)
    assert hist == macd - signal


def test_snapshot_bias_expected_values() -> None:
    prices = generate_price_series(days=160, seed=11)
    snapshot = build_snapshot("ETH-USD", prices)
    assert snapshot.bias in {"bullish", "bearish", "neutral"}
    assert 0 <= snapshot.score <= 100
