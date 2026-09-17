# Rank Tracker API

> Track keyword positions over time: create trackers, check ranks, and pull history programmatically.

Part of the **DataLeads** API suite (Monitoring category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/rank/check` | V1 Rank Check |
| POST | `/rank/trackers/create` | V1 Rank Trackers Create |
| POST | `/rank/trackers/list` | V1 Rank Trackers List |
| POST | `/rank/trackers/results` | V1 Rank Trackers Results |
| POST | `/rank/trackers/check-now` | V1 Rank Trackers Check Now |
| POST | `/rank/trackers/delete` | V1 Rank Trackers Delete |

## Quick start

```bash
curl -X POST https://data.dataleads.pro/v1/rank/check \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "domain": "example.com", "keywords": ["example", "test"]}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://data.dataleads.pro](https://data.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://data.dataleads.pro/mcp/rank-tracker`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/rank-tracker-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://data.dataleads.pro](https://data.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
