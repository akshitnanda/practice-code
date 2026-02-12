# Start Here: Day 1 Build Sprint

## Goal
Ship an end-to-end alpha prototype in one day.

## Sprint Checklist
- [ ] Initialize monorepo with `apps/web` (Next.js) and `apps/api` (FastAPI).
- [ ] Implement `/health` and `/signals` in API.
- [ ] Add fake data pipeline that updates every 30s.
- [ ] Render signals table + mini sparkline in web app.
- [ ] Add one command to run all services locally.

## API Shape (draft)
```json
{
  "generated_at": "2026-01-01T10:00:00Z",
  "signals": [
    {
      "symbol": "BTCUSD",
      "direction": "long",
      "confidence": 0.82,
      "entry_zone": [104200, 104650],
      "stop": 103300,
      "targets": [105800, 106900],
      "why_now": [
        "RSI reset to 46 on 1h",
        "exchange outflows up 18%",
        "positive ETF-related news momentum"
      ]
    }
  ]
}
```

## Definition of Done
- The UI refreshes with API signals.
- At least one unit test passes in API.
- README includes setup commands.
