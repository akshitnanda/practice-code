from __future__ import annotations

from dataclasses import dataclass
import re
from urllib.error import URLError
from urllib.request import urlopen
import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class NewsItem:
    headline: str
    sentiment: str
    impact_score: int


POSITIVE_TERMS = {"surge", "record", "approval", "adoption", "breakout", "rally", "growth"}
CAUTIOUS_TERMS = {"hack", "drop", "probe", "lawsuit", "selloff", "risk", "decline"}


def infer_sentiment(headline: str) -> tuple[str, int]:
    text = headline.lower()
    if any(term in text for term in POSITIVE_TERMS):
        return "positive", 76
    if any(term in text for term in CAUTIOUS_TERMS):
        return "cautious", 64
    return "mixed", 60


def parse_rss_items(xml_text: str, limit: int = 3) -> list[NewsItem]:
    root = ET.fromstring(xml_text)
    items = root.findall(".//item")
    parsed: list[NewsItem] = []

    for item in items[:limit]:
        title = item.findtext("title") or "Untitled news item"
        headline = re.sub(r"\s+", " ", title).strip()
        sentiment, impact = infer_sentiment(headline)
        parsed.append(NewsItem(headline=headline, sentiment=sentiment, impact_score=impact))

    return parsed


def fetch_rss_news(url: str, limit: int = 3, timeout_s: float = 4.0) -> list[NewsItem]:
    with urlopen(url, timeout=timeout_s) as response:  # nosec B310 demo-only remote read
        xml_data = response.read().decode("utf-8", errors="ignore")
    return parse_rss_items(xml_data, limit=limit)


def safe_fetch_rss_news(url: str, limit: int = 3) -> tuple[list[NewsItem], str]:
    try:
        items = fetch_rss_news(url=url, limit=limit)
        if not items:
            return [], "live_rss_empty"
        return items, "live_rss"
    except (URLError, TimeoutError, ET.ParseError, ValueError):
        return [], "live_rss_failed"
