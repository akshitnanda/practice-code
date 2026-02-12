# MarketNeuron

**Tagline:** AI copilot for cross-market alpha — fusing stocks, crypto, on-chain flows, macro news, and technical indicators into real-time trade intelligence.

## Why this idea is worth building
Most traders and builders jump across 7–10 tools to answer a single question:

> "Is this move real, narrative-driven, or just noise?"

MarketNeuron can be the **single decision engine** that:
- Ingests market + blockchain + news data streams.
- Uses LLM + quant pipelines to summarize what changed.
- Scores opportunities by confidence, risk regime, and catalyst quality.
- Produces explainable playbooks (entry, invalidation, position size hints).

## v1 Product Wedge (ship in 2-3 weeks)

### 1) Multi-source signal ingestion
- **Stocks:** price/volume, sector breadth, volatility indices.
- **Crypto:** spot/futures basis, funding rates, open interest.
- **On-chain:** large wallet flows, exchange inflow/outflow anomalies.
- **News:** macro + earnings + crypto narratives.

### 2) "Regime + Catalyst" AI scoring
Each tradable asset gets:
- **Regime score** (trend, chop, risk-off, squeeze risk)
- **Catalyst score** (news/on-chain/event strength)
- **Execution score** (liquidity + spread + slippage estimate)

Final output: **0-100 Opportunity Score** with explanation.

### 3) Codex-first workflow
Use Codex agents to:
- Generate new indicators quickly from prompts.
- Auto-propose backtest experiments and parameter sweeps.
- Draft release notes and model-card updates from git diffs.

## Suggested Tech Stack
- **Frontend:** Next.js + Tailwind + shadcn/ui
- **Backend APIs:** FastAPI + WebSockets
- **Streaming:** Kafka or Redpanda (lightweight dev path)
- **Feature store:** Postgres + Timescale
- **Model layer:**
  - LLM summarizer (OpenAI API)
  - LightGBM/XGBoost for structured alpha ranking
- **Execution adapters (later):** Alpaca + Binance + Coinbase Advanced

## Initial Folder Blueprint

```text
market-neuron/
├─ apps/
│  ├─ web/                  # Next.js dashboard
│  └─ api/                  # FastAPI scoring + inference APIs
├─ services/
│  ├─ ingest/               # data connectors + normalization
│  ├─ features/             # indicator and feature pipelines
│  ├─ scoring/              # regime/catalyst/execution models
│  └─ alerts/               # trigger + notification service
├─ research/
│  ├─ notebooks/            # hypothesis and backtests
│  └─ datasets/             # sample snapshots (small)
├─ infra/
│  ├─ docker/
│  └─ terraform/
└─ docs/
   ├─ prd.md
   ├─ architecture.md
   └─ runbooks/
```

## First 5 Build Tickets (start here)
1. **Data contract schema** for candles, ticks, news, and on-chain events.
2. **Signal normalizer** that maps raw inputs to standardized features.
3. **Opportunity scoring endpoint** (`/score/{asset}`) with explainable JSON output.
4. **Dashboard watchlist** with sortable score columns and drill-down rationale.
5. **Backtest harness** that replays data and logs model decisions.

## A very practical MVP loop
1. Pull 25 assets (15 equities ETFs/stocks + 10 crypto majors).
2. Recompute scores every 5 minutes.
3. Alert only top decile score changes.
4. Track paper-trade outcomes and tune feature weights weekly.

## What makes this "supercharged"
- **Cross-domain context:** on-chain + tradfi + macro in one pane.
- **Explainable AI:** no black-box "buy" calls without rationale.
- **Agentic development:** Codex assists rapid idea-to-backtest iteration.
- **Business ready:** premium terminal + API subscription model.

## Next Command To Run

```bash
mkdir -p market-neuron/{apps/web,apps/api,services/{ingest,features,scoring,alerts},research/{notebooks,datasets},infra/{docker,terraform},docs/runbooks}
```

Then scaffold `apps/web` and `apps/api` as the first executable milestone.
