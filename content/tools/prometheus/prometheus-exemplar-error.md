---
title: "[Solution] Prometheus Exemplar Error"
description: "Fix Prometheus exemplar errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Exemplar Error

Prometheus exemplar errors occur when exemplar data fails to attach to metrics correctly.

## Why This Happens

- Exemplar not found
- Trace ID missing
- Exemplar format invalid
- Storage issue

## Common Error Messages

- `exemplar_not_found_error`
- `exemplar_trace_error`
- `exemplar_format_error`
- `exemplar_storage_error`

## How to Fix It

### Solution 1: Attach exemplars

Add exemplars to metrics:

```go
metric.With(prometheus.Exemplar{
    LabelPairs: []*dto.LabelPair{
        {Name: proto.String("traceID"), Value: proto.String("abc123")},
    },
})
```

### Solution 2: Check exemplar storage

Verify exemplar storage is enabled.

### Solution 3: Query with exemplars

Use exemplars in queries:

```promql
http_requests_total{method="GET"}
```


## Common Scenarios

- **Exemplar not found:** Check if exemplars are being recorded.
- **Trace ID missing:** Verify the trace ID is being passed.

## Prevent It

- Record exemplars with traces
- Query exemplars in UI
- Monitor exemplar storage
