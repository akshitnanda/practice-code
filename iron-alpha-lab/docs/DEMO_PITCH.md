# Demo Pitch Runbook (F22 Supercharged)

## 60-second elevator flow

1. Run `iron-alpha-lab pitch --symbol BTC-USD --days 120`.
2. Read the output sections in this order:
   - Live Demo Snapshot
   - Mock Catalyst Layer
   - On-Chain Pulse
   - Operator Workflow
3. Close with the final elevator statement.

## Why this is demo-ready

- Fully deterministic output (no external dependency risk during demos)
- Business language included, not just technical metrics
- Mock stubs mirror real product contracts so replacement with live APIs is easy

## Swap mocks for production connectors

- `mock_news_feed` -> news/RSS sentiment service
- `mock_onchain_pulse` -> on-chain analytics API
- `mock_watchlist` -> user portfolio/watchlist service
