# Log Report Task

An Apache-style access log is available at `/app/access.log`.

Parse the log and write a JSON report to `/app/report.json` with exactly these fields:

- `total_requests`: integer — total number of log lines
- `unique_ips`: integer — number of distinct client IP addresses
- `top_path`: string — the URL path that appears most often in requests

## Success criteria

1. `/app/report.json` exists.
2. `/app/report.json` contains valid JSON.
3. `total_requests` is a positive integer.
4. `unique_ips` is a positive integer.
5. `top_path` is a non-empty string.