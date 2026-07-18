---
title: "[Solution] Python Prometheus Error — How to Fix"
description: "Fix Python Prometheus monitoring errors. Resolve metric, exposition, and scrape issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Prometheus Error

A `prometheus_client.exceptions` or `ValueError` occurs when Prometheus fails to expose metrics, encounters configuration errors, or when the metric registry is misconfigured.

## Why It Happens

Prometheus client for Python exposes metrics. Errors arise when metric names are invalid, when the registry has duplicate metrics, when the exposition format is wrong, or when the HTTP server is not started.

## Common Error Messages

- `ValueError: Duplicated timeseries in CollectorRegistry`
- `prometheus_client.exceptions.InvalidMetricName`
- `ValueError: Metric name must match regex`
- `RuntimeError: HTTP server not started`

## How to Fix It

### Fix 1: Define metrics correctly

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Wrong — invalid metric name
# counter = Counter("my-metric!", "Description")

# Correct — valid metric name
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["method", "endpoint"],
)

# Use metrics
REQUEST_COUNT.labels(method="GET", endpoint="/api").inc()
REQUEST_LATENCY.labels(method="GET", endpoint="/api").observe(0.5)
```

### Fix 2: Start HTTP server

```python
from prometheus_client import start_http_server

# Wrong — not starting server
# metrics not exposed

# Correct — start HTTP server
start_http_server(8000)
print("Prometheus metrics available at http://localhost:8000/metrics")
```

### Fix 3: Handle registry

```python
from prometheus_client import CollectorRegistry, Counter, generate_latest

# Wrong — duplicate metrics in default registry
# counter = Counter("test", "Test")
# counter2 = Counter("test", "Test")  # ValueError

# Correct — use custom registry
registry = CollectorRegistry()
counter = Counter("test_total", "Test", registry=registry)

# Generate output
output = generate_latest(registry)
print(output.decode())
```

### Fix 4: Use labels correctly

```python
from prometheus_client import Counter, Histogram

# Wrong — high cardinality labels
# counter = Counter("requests", "Requests", ["url", "user_id"])

# Correct — bounded label values
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "status_code"],
)

REQUEST_COUNT.labels(method="GET", status_code="200").inc()
REQUEST_COUNT.labels(method="POST", status_code="201").inc()
```

## Common Scenarios

- **Duplicate metrics** — Same metric name registered twice in default registry.
- **Invalid metric name** — Metric name contains special characters.
- **High cardinality** — Label values create too many time series.

## Prevent It

- Always use `snake_case` for metric names.
- Use bounded label values to prevent high cardinality.
- Use custom registries to avoid conflicts between modules.

## Related Errors

- [ValueError](/languages/python/valueerror/) — invalid metric configuration
- [DuplicateMetric](/languages/python/duplicate-metric/) — metric already registered
- [InvalidMetricName](/languages/python/invalid-name/) — metric name invalid
