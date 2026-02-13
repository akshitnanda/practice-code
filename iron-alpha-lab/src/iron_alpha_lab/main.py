from __future__ import annotations

import argparse
from textwrap import dedent

from .signals import IndicatorSnapshot, build_snapshot, generate_price_series
from .stubs import MockPitchBundle, build_pitch_bundle


def build_ai_brief(snapshot: IndicatorSnapshot) -> str:
    stance = {
        "bullish": "accumulation bias with controlled risk",
        "bearish": "capital-protection bias and tighter stops",
        "neutral": "wait-for-confirmation bias",
    }[snapshot.bias]

    return dedent(
        f"""
        === Iron Alpha Lab Brief ===
        Symbol: {snapshot.symbol}
        Price: {snapshot.latest_price:.2f}

        Deterministic Signal State
        - RSI(14): {snapshot.rsi_14:.2f}
        - MACD: {snapshot.macd:.4f}
        - MACD Signal: {snapshot.macd_signal:.4f}
        - MACD Histogram: {snapshot.macd_histogram:.4f}
        - Composite Score: {snapshot.score:.1f}/100
        - Market Bias: {snapshot.bias.upper()}

        GenAI-Style Tactical Narrative
        Current posture suggests {stance}.
        Suggested workflow:
        1) Validate with fresh catalyst/news flow.
        2) Position in tranches instead of all-in execution.
        3) Pre-define invalidation level and size risk before entry.

        This output is educational and not financial advice.
        """
    ).strip()


def build_elevator_pitch(snapshot: IndicatorSnapshot, bundle: MockPitchBundle) -> str:
    top_news_block = "\n".join(
        [f"- {item.headline} ({item.sentiment}, impact {item.impact_score}/100)" for item in bundle.top_news]
    )
    return dedent(
        f"""
        === Iron Alpha Lab | F22 Supercharged Demo Pitch ===
        What it is:
        AI market copilot that fuses technical indicators + catalyst context + explainable strategy output.

        Live Demo Snapshot
        - Symbol: {snapshot.symbol}
        - Price: {snapshot.latest_price:.2f}
        - Composite Signal Score: {snapshot.score:.1f}/100 ({snapshot.bias})
        - RSI(14): {snapshot.rsi_14:.2f}
        - MACD Histogram: {snapshot.macd_histogram:.4f}

        Mock Catalyst Layer (demo-ready stubs)
        News Pulse ({bundle.news_source}):
        {top_news_block}

        On-Chain Pulse:
        - Active addresses Δ: {bundle.onchain.active_addresses_change_pct:+.1f}%
        - Exchange netflow: {bundle.onchain.exchange_netflow_musd:+.1f} MUSD
        - Stablecoin supply Δ: {bundle.onchain.stablecoin_supply_change_pct:+.1f}%

        Operator Workflow
        - Watchlist: {", ".join(bundle.watchlist)}
        - Decision model: signal score + catalyst pulse + risk checklist
        - Next sprint hooks: live exchange adapters, sentiment embeddings, alert routing

        Elevator close:
        "Iron Alpha Lab turns fragmented market noise into explainable, auditable AI-assisted decisions in under 60 seconds."
        """
    ).strip()


def cli() -> None:
    parser = argparse.ArgumentParser(description="Iron Alpha Lab CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    demo = sub.add_parser("demo", help="Run the market + AI demo flow")
    demo.add_argument("--symbol", default="BTC-USD")
    demo.add_argument("--days", type=int, default=120)
    demo.add_argument("--seed", type=int, default=42)

    pitch = sub.add_parser("pitch", help="Run an elevator-pitch ready flow with mock business stubs")
    pitch.add_argument("--symbol", default="BTC-USD")
    pitch.add_argument("--days", type=int, default=120)
    pitch.add_argument("--seed", type=int, default=42)
    pitch.add_argument("--live-news", action="store_true", help="Try fetching live RSS headlines")
    pitch.add_argument(
        "--rss-url",
        default="https://cointelegraph.com/rss",
        help="RSS endpoint used when --live-news is enabled",
    )

    args = parser.parse_args()

    prices = generate_price_series(days=args.days, seed=args.seed)
    snapshot = build_snapshot(symbol=args.symbol, prices=prices)

    if args.command == "demo":
        print(build_ai_brief(snapshot))
    elif args.command == "pitch":
        bundle = build_pitch_bundle(
            symbol=args.symbol,
            use_live_news=args.live_news,
            rss_url=args.rss_url,
        )
        print(build_elevator_pitch(snapshot=snapshot, bundle=bundle))


if __name__ == "__main__":
    cli()
