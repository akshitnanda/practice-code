from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MockNewsItem:
    headline: str
    sentiment: str
    impact_score: int


@dataclass(frozen=True)
class MockOnChainPulse:
    active_addresses_change_pct: float
    exchange_netflow_musd: float
    stablecoin_supply_change_pct: float


@dataclass(frozen=True)
class MockPitchBundle:
    symbol: str
    top_news: list[MockNewsItem]
    onchain: MockOnChainPulse
    watchlist: list[str]


def mock_news_feed(symbol: str) -> list[MockNewsItem]:
    """Deterministic market-news stubs for demo usage."""
    symbol_root = symbol.split("-")[0]
    return [
        MockNewsItem(
            headline=f"{symbol_root} ecosystem sees rising developer activity this week",
            sentiment="positive",
            impact_score=74,
        ),
        MockNewsItem(
            headline=f"Macro rate-volatility may pressure high-beta assets near term",
            sentiment="mixed",
            impact_score=61,
        ),
        MockNewsItem(
            headline=f"Large on-chain transfers trigger short-term risk monitoring",
            sentiment="cautious",
            impact_score=67,
        ),
    ]


def mock_onchain_pulse() -> MockOnChainPulse:
    """Deterministic on-chain pulse values for pitch demonstrations."""
    return MockOnChainPulse(
        active_addresses_change_pct=3.8,
        exchange_netflow_musd=-42.5,
        stablecoin_supply_change_pct=1.2,
    )


def mock_watchlist(symbol: str) -> list[str]:
    symbol_root = symbol.split("-")[0]
    return [symbol, "ETH-USD", "SOL-USD", f"{symbol_root}-PERP"]


def build_mock_pitch_bundle(symbol: str) -> MockPitchBundle:
    return MockPitchBundle(
        symbol=symbol,
        top_news=mock_news_feed(symbol),
        onchain=mock_onchain_pulse(),
        watchlist=mock_watchlist(symbol),
    )
