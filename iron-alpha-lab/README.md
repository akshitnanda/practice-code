# Iron Alpha Lab 🚀

A **demoable, professional GenAI + market intelligence product starter** built for rapid learning and strong engineering habits.

Iron Alpha Lab helps you blend:
- **Market indicators** (RSI, MACD)
- **News + catalyst context** (manual or API-fed)
- **LLM reasoning** for explainable trade/business narratives

## Why this idea?

Most demos are either:
1. just charts, or
2. just AI chat.

This project combines both into a clear product concept:

> "An AI strategy co-pilot for crypto/stocks that turns noisy data into explainable tactical insights."

This is perfect for hands-on Codex work because you can iteratively add:
- data connectors,
- model prompts,
- evaluation loops,
- UI polish,
- and deployment automation.

---

## V1 demo scope (implemented)

- Deterministic synthetic market data generator
- Technical indicators: **RSI(14)** and **MACD(12,26,9)**
- Signal scoring engine
- GenAI-ready insight generator (structured prompt payload + local mock narrative)
- CLI command to run a complete demo scenario
- Unit tests for core indicator logic

This means you can demo the full product workflow without waiting on external APIs.

Now includes **F22 supercharged mock stubs** for pitch-ready flows:
- mock news catalyst feed
- mock on-chain pulse
- mock watchlist + operator workflow

---

## Quickstart

```bash
cd iron-alpha-lab
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
iron-alpha-lab demo --symbol BTC-USD --days 120
iron-alpha-lab pitch --symbol BTC-USD --days 120
```

Run tests:

```bash
pytest -q
```

---


## Running on GitHub (CI)

This repo includes a GitHub Actions workflow: `../.github/workflows/iron-alpha-lab-ci.yml`.

It automatically runs on push/PR when files in `iron-alpha-lab/` change, and executes:
- editable install with dev dependencies
- `pytest -q`
- `iron-alpha-lab demo --symbol BTC-USD --days 120`
- `iron-alpha-lab pitch --symbol BTC-USD --days 120`

To enable in your own GitHub repo:
1. Push this repository to GitHub.
2. Open the **Actions** tab and enable workflows if prompted.
3. Create a branch + PR touching `iron-alpha-lab/` and verify checks pass.

---

## What to build next (Codex roadmap)

1. **Live market connectors**
   - `yfinance` for equities
   - `ccxt` for crypto exchanges
2. **News ingestion + sentiment**
   - RSS + market news APIs
   - embedding-based clustering for duplicate stories
3. **LLM augmentation**
   - convert deterministic signal state into structured prompts
   - generate trade thesis + risk checklist + confidence explanation
4. **Web app**
   - FastAPI backend + React/Next.js frontend
   - strategy cards, watchlists, and alert center
5. **Production-hardening**
   - Redis cache
   - background workers
   - evaluation suite for prompt quality + hallucination risk

See [`docs/PRODUCT_BRIEF.md`](docs/PRODUCT_BRIEF.md) for architecture and product narrative.

---

## Professional engineering principles used

- Reproducible demo mode
- Typed Python code
- Clear data contracts (`dataclass` models)
- Small test suite covering core quant logic
- Modular design ready for API/UI expansion
