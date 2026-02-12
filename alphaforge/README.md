# AlphaForge

**AlphaForge** is a GenAI-powered market intelligence and execution copilot for crypto + equities.

## Product idea (supercharged)

Build a "Bloomberg Terminal x Onchain Radar x Autonomous Analyst" for retail and small funds:

- Ingest market data (stocks, crypto, macro, rates), on-chain data, and live news/social feeds.
- Use LLM agents to generate structured theses, risk tags, and trade playbooks.
- Let users simulate strategies with indicators and event filters before sending orders.
- Provide verifiable citations and confidence scores for every AI recommendation.

## Why this is a strong hands-on Codex + GenAI project

- **End-to-end AI app**: data pipeline, retrieval, multi-agent orchestration, evaluation.
- **Actionable outputs**: not just chat—screeners, alerts, backtests, and optional execution.
- **Business upside**: subscription tiers for terminal features + API access.
- **Defensible moat**: proprietary feature store + agent evaluations + user feedback loops.

## Core modules

1. **Data Fabric**
   - Prices: equities, crypto spot/perps, options IV.
   - Fundamentals + macro calendars.
   - News + social sentiment.
   - On-chain metrics (wallet flows, DEX/CEX flow, stablecoin mint/burn).

2. **Indicator & Signal Engine**
   - TA indicators (RSI, MACD, Bollinger, VWAP).
   - Regime detection (trend/range/volatility clusters).
   - Cross-asset correlation shocks.

3. **Agent Stack**
   - **News Analyst Agent**: summarize catalyst impact by ticker/token.
   - **Quant Agent**: propose entry/exit/risk parameters from signal stack.
   - **Onchain Agent**: explain wallet, liquidity, and flow anomalies.
   - **Risk Agent**: enforce constraints and kill-switch rules.

4. **Execution & Simulation**
   - Paper trading first.
   - Broker/exchange adapters later.
   - Playbook simulation before any live action.

5. **Trust Layer**
   - Every response ships with:
     - source citations,
     - confidence score,
     - scenario assumptions,
     - invalidation conditions.

## Suggested stack

- **Monorepo**: Turborepo (or pnpm workspaces).
- **Frontend**: Next.js + Tailwind + lightweight charting.
- **Backend**: FastAPI or NestJS.
- **Streaming**: Kafka/Redpanda (optional in v1).
- **Database**: Postgres + Timescale (or ClickHouse for events).
- **Vector DB**: pgvector or Qdrant.
- **Orchestration**: Temporal or queue workers.
- **LLM layer**: provider abstraction + eval harness.

## 30-day build plan

### Week 1: Foundation
- Repo setup, environments, and schema.
- Ingest two sources: one market feed + one news feed.
- Build first dashboard with watchlists.

### Week 2: Signals
- Implement 10 indicators and scan jobs.
- Add rule builder: "if X + Y + catalyst then alert".

### Week 3: Agent MVP
- Add RAG over market/news snapshots.
- Implement analyst + risk agents.
- Return JSON outputs with confidence and citations.

### Week 4: Productization
- Paper-trade simulator + alert routing (email/Telegram/Slack).
- Evaluate agent quality (precision of catalyst tagging, thesis consistency).
- Ship closed alpha to 5-10 users.

## MVP success criteria

- 80%+ of generated theses include at least one valid catalyst citation.
- Alert precision above baseline indicator-only strategy.
- Users can go from question to simulated playbook in under 90 seconds.

## Next steps for this repo

- [ ] Add docker-compose for Postgres + pgvector + API.
- [ ] Seed historical candles for BTC, ETH, SPY, QQQ.
- [ ] Implement `/research/query` endpoint with citation format.
- [ ] Build first "Catalyst + Technical Alignment" screener page.
