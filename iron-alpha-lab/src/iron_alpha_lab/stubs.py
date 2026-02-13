from __future__ import annotations

from dataclasses import dataclass

from .news import NewsItem, safe_fetch_rss_news


@dataclass(frozen=True)
class MockOnChainPulse:
    active_addresses_change_pct: float
    exchange_netflow_musd: float
    stablecoin_supply_change_pct: float


@dataclass(frozen=True)
class MockPitchBundle:
    symbol: str
    top_news: list[NewsItem]
    onchain: MockOnChainPulse
    watchlist: list[str]
    news_source: str


def mock_news_feed(symbol: str) -> list[NewsItem]:
    """Deterministic market-news stubs for demo usage."""
    symbol_root = symbol.split("-")[0]
    return [
        NewsItem(
            headline=f"{symbol_root} ecosystem sees rising developer activity this week",
            sentiment="positive",
            impact_score=74,
        ),
        NewsItem(
            headline="Macro rate-volatility may pressure high-beta assets near term",
            sentiment="mixed",
            impact_score=61,
        ),
        NewsItem(
            headline="Large on-chain transfers trigger short-term risk monitoring",
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
        news_source="mock",
    )


def build_pitch_bundle(symbol: str, use_live_news: bool = False, rss_url: str | None = None) -> MockPitchBundle:
    if use_live_news and rss_url:
        live_items, source = safe_fetch_rss_news(url=rss_url, limit=3)
        if live_items:
            return MockPitchBundle(
                symbol=symbol,
                top_news=live_items,
                onchain=mock_onchain_pulse(),
                watchlist=mock_watchlist(symbol),
                news_source=source,
            )

    fallback = build_mock_pitch_bundle(symbol)
    return MockPitchBundle(
        symbol=fallback.symbol,
        top_news=fallback.top_news,
        onchain=fallback.onchain,
        watchlist=fallback.watchlist,
        news_source="mock_fallback",
    )
