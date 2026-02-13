from iron_alpha_lab.main import build_elevator_pitch
from iron_alpha_lab.signals import build_snapshot, generate_price_series
from iron_alpha_lab.news import NewsItem
from iron_alpha_lab.stubs import build_mock_pitch_bundle, build_pitch_bundle, mock_watchlist


def test_mock_watchlist_contains_symbol() -> None:
    symbol = "BTC-USD"
    watchlist = mock_watchlist(symbol)
    assert symbol in watchlist
    assert len(watchlist) >= 4


def test_build_mock_pitch_bundle_shape() -> None:
    bundle = build_mock_pitch_bundle("ETH-USD")
    assert bundle.symbol == "ETH-USD"
    assert len(bundle.top_news) == 3
    assert bundle.onchain.exchange_netflow_musd < 0


def test_elevator_pitch_contains_sections() -> None:
    prices = generate_price_series(days=140, seed=9)
    snapshot = build_snapshot(symbol="BTC-USD", prices=prices)
    bundle = build_mock_pitch_bundle("BTC-USD")

    pitch = build_elevator_pitch(snapshot=snapshot, bundle=bundle)
    assert "F22 Supercharged Demo Pitch" in pitch
    assert "Mock Catalyst Layer" in pitch
    assert "Operator Workflow" in pitch


def test_build_pitch_bundle_live_path(monkeypatch) -> None:
    def _fake_fetch(url: str, limit: int = 3):
        return [NewsItem(headline="Live headline", sentiment="mixed", impact_score=60)], "live_rss"

    monkeypatch.setattr("iron_alpha_lab.stubs.safe_fetch_rss_news", _fake_fetch)
    bundle = build_pitch_bundle(symbol="BTC-USD", use_live_news=True, rss_url="https://example.com/rss")
    assert bundle.news_source == "live_rss"
    assert bundle.top_news[0].headline == "Live headline"
