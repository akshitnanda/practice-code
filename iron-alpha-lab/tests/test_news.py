from iron_alpha_lab.news import infer_sentiment, parse_rss_items
from iron_alpha_lab.stubs import build_pitch_bundle


SAMPLE_RSS = """
<rss>
  <channel>
    <item><title>Bitcoin adoption surge after ETF approval</title></item>
    <item><title>Market risk rises after exchange probe</title></item>
  </channel>
</rss>
"""


def test_infer_sentiment_positive_and_cautious() -> None:
    assert infer_sentiment("Token rally on growth") == ("positive", 76)
    assert infer_sentiment("Exchange hack risk grows") == ("cautious", 64)


def test_parse_rss_items_extracts_titles() -> None:
    items = parse_rss_items(SAMPLE_RSS, limit=2)
    assert len(items) == 2
    assert "Bitcoin adoption surge" in items[0].headline


def test_build_pitch_bundle_fallback_without_live() -> None:
    bundle = build_pitch_bundle(symbol="BTC-USD", use_live_news=False)
    assert bundle.news_source == "mock_fallback"
    assert len(bundle.top_news) == 3
