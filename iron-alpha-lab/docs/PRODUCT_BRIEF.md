# Iron Alpha Lab — Product Brief

## One-liner

**Iron Alpha Lab** is an AI market copilot that fuses technical indicators, macro/news catalysts, and explainable LLM output to help users make faster, better, and auditable trading/investing decisions.

## Ideal users

- Independent traders (crypto + equities)
- Research analysts at small funds
- Fintech builders prototyping AI-native terminals
- Learners who want pro-level architecture while staying demo-friendly

## Problem

Market participants struggle with:
- Indicator overload (too many disconnected signals)
- News velocity (hard to contextualize fast-moving events)
- Non-explainable AI outputs (can't trust black-box suggestions)

## Solution

A structured pipeline:
1. Collect data (prices, volumes, news, macro events)
2. Compute deterministic signals (RSI, MACD, trend states)
3. Rank opportunity/risk score
4. Ask LLM for narrative synthesis and scenario analysis
5. Present recommendation + confidence + "why"

## Demo architecture (V1)

```text
Market Data Simulator -> Indicator Engine -> Signal Score -> Insight Composer -> CLI Output
```

## Demo-ready mock layer

To keep demos professional and reliable, V1 now includes deterministic mock stubs for:
- market news catalysts
- on-chain pulse metrics
- operator watchlist context

These stubs are wired into a dedicated `iron-alpha-lab pitch` command for elevator-style demos.

## Future architecture (V2+)

```text
[Ingestion Layer]
  - Equities feed (yfinance/polygon)
  - Crypto feed (ccxt/exchange APIs)
  - News feed (RSS / paid APIs)

[Feature + Signal Layer]
  - TA indicators
  - regime detection
  - catalyst tagging

[AI Layer]
  - prompt templates
  - retrieval context windows
  - output guardrails

[Application Layer]
  - FastAPI service
  - web dashboard
  - alert engine

[Ops Layer]
  - Redis cache
  - Postgres + Timescale
  - observability + evaluations
```

## Demo script for stakeholders

1. Pick symbol and date range.
2. Show latest RSI + MACD state.
3. Show deterministic signal score (no AI).
4. Show generated AI-style brief with risks and action plan.
5. Explain how live feeds and guardrails are next incremental layer.

## Why this is great for Codex practice

- Easy entry point (runs locally in minutes)
- Real-world complexity (finance + AI + product UX)
- Modular tasks Codex can accelerate:
  - connector implementation
  - prompt evaluations
  - testing and refactoring
  - frontend wiring
