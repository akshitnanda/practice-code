# AlphaForge AI

**AlphaForge AI** is a market intelligence copilot that fuses:
- real-time **crypto + equities** market data,
- **technical indicators** (RSI, MACD, VWAP, ATR, volume profiles),
- **on-chain signals** (DEX flows, whale wallets, stablecoin mint/burn, gas/fees), and
- **news + social narratives** (headlines, filings, X/Reddit sentiment)

into one **actionable decision engine**.

## The Product Idea (supercharged)

AlphaForge AI helps traders and operators answer:
1. **What moved this market right now?**
2. **Is this move likely to continue or mean-revert?**
3. **What is the highest-conviction setup with defined risk?**

### Signature UX
- **Pulse Feed**: AI-generated “market episodes” every 5 minutes with confidence and evidence.
- **Why It Moved**: attribution panel linking price spikes to catalysts (on-chain events, macro news, earnings, ETF flows).
- **Playbook Builder**: natural-language strategy prompts -> backtest-ready rules.
- **Guardrails**: position sizing suggestions, stop-loss zones, and risk warnings.

## Tech Stack (Codex-friendly)
- **Frontend**: Next.js + Tailwind + shadcn/ui
- **Backend API**: FastAPI (Python) + websockets
- **Data**: PostgreSQL + TimescaleDB + Redis
- **AI Layer**: LLM orchestration for summarization, signal explanation, and strategy drafting
- **Pipelines**: Prefect or lightweight cron workers
- **Optional Chain Indexing**: Dune, Flipside, or custom indexers

## GenAI + Codex Hands-on Plan

### Phase 0 — Bootstrapped MVP (1 weekend)
- [ ] Live watchlist for BTC, ETH, SPY, NVDA, TSLA.
- [ ] Technical indicators service (RSI, MACD, ATR).
- [ ] “What changed?” feed generated every 5 minutes.
- [ ] Basic alerting to Telegram/Discord.

### Phase 1 — Explainability Engine
- [ ] News ingestion + sentiment tagging.
- [ ] On-chain anomaly detector (large transfers, exchange inflows/outflows).
- [ ] LLM-generated causal summary with references.

### Phase 2 — Strategy Studio
- [ ] Prompt-to-strategy (e.g., “buy breakouts only when RSI resets”).
- [ ] Backtest sandbox with sharpe/max drawdown.
- [ ] Auto-generated post-trade journal and improvement suggestions.

## Suggested Monorepo Structure

```text
alphaforge-ai/
  apps/
    web/                 # Next.js dashboard
    api/                 # FastAPI app
  services/
    market-ingestion/    # price/news/on-chain collectors
    indicators/          # RSI/MACD/VWAP calculations
    signal-engine/       # scoring + ranking
    narrative-ai/        # LLM summaries/explanations
  packages/
    schemas/             # shared pydantic / TS types
    ui/                  # shared components
  infra/
    docker/
    terraform/
  docs/
    architecture.md
    roadmap.md
```

## First Codex Tasks to Run Next
1. Scaffold `apps/web` and `apps/api`.
2. Add a `/signals` endpoint returning mocked ranked trade setups.
3. Create a dashboard with:
   - top 5 assets,
   - confidence score,
   - “why now” explanation.
4. Add one integration test for the ranking logic.

## Why this can be a business
- Traders pay for **speed + clarity + confidence**.
- Funds and DAOs need explainable signals, not black-box outputs.
- Teams can license API access for internal tooling.

---

> Disclaimer: educational tooling only; not financial advice.
