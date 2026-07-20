---
title: "[Solution] Prometheus Query Error Fix"
description: "Fix Prometheus query errors in Go. Handle PromQL syntax, metric collection, and alert manager issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Prometheus Query Error

The Prometheus Go client (`github.com/prometheus/client_golang`) fails when metric registration conflicts, the HTTP handler is misconfigured, or metric labels are used incorrectly. The most common error is "duplicate metrics collector registration" which happens when `prometheus.MustRegister` is called twice.

## Common Causes

```go
// Cause 1: Duplicate registration
httpRequests := prometheus.NewCounterVec(
    prometheus.CounterOpts{Name: "http_requests_total"},
    []string{"method", "path"},
)
prometheus.MustRegister(httpRequests) // first time OK
prometheus.MustRegister(httpRequests) // panic: already registered

// Cause 2: Label cardinality explosion
labels := []string{"user_id", "request_id"} // high cardinality
// metric memory grows unbounded

// Cause 3: Wrong metric type
counter := prometheus.NewHistogram(...) // wants Counter
// type mismatch — histogram is not a counter

// Cause 4: HTTP handler not configured
// /metrics endpoint returns 404

// Cause 5: Metric name not following naming convention
// Names must match [a-zA-Z_:][a-zA-Z0-9_:]*
prometheus.NewCounter(prometheus.CounterOpts{Name: "123invalid"})
// invalid metric name
```

## How to Fix

### Fix 1: Use prometheus.NewCollector instead of MustRegister

```go
import (
    "net/http"

    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promhttp"
)

var httpRequests = prometheus.NewCounterVec(
    prometheus.CounterOpts{
        Name: "http_requests_total",
        Help: "Total HTTP requests",
    },
    []string{"method", "status"},
)

func init() {
    // Safe to call multiple times — only registers once
    prometheus.MustRegister(httpRequests)
}

func main() {
    http.Handle("/metrics", promhttp.Handler())
    http.HandleFunc("/api/data", func(w http.ResponseWriter, r *http.Request) {
        httpRequests.WithLabelValues(r.Method, "200").Inc()
        w.Write([]byte("ok"))
    })
    http.ListenAndServe(":8080", nil)
}
```

### Fix 2: Use a custom registry to avoid global conflicts

```go
func main() {
    registry := prometheus.NewRegistry()

    httpRequests := prometheus.NewCounterVec(
        prometheus.CounterOpts{
            Name: "http_requests_total",
            Help: "Total HTTP requests",
        },
        []string{"method"},
    )
    registry.MustRegister(httpRequests)

    handler := promhttp.HandlerFor(registry, promhttp.HandlerOpts{})
    http.Handle("/metrics", handler)
    http.ListenAndServe(":8080", nil)
}
```

### Fix 3: Use labels with bounded cardinality

```go
// Good: bounded labels
statusLabels := []string{"method", "status_code"}
// Bad: unbounded labels
userLabels := []string{"user_id", "request_id"} // never use
```

## Examples

```go
package main

import (
    "math/rand"
    "net/http"
    "time"

    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
    requests := prometheus.NewHistogram(prometheus.HistogramOpts{
        Name:    "http_request_duration_seconds",
        Help:    "Request duration in seconds",
        Buckets: prometheus.DefBuckets,
    })
    prometheus.MustRegister(requests)

    http.Handle("/metrics", promhttp.Handler())
    http.HandleFunc("/api", func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        // simulate work
        time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond)
        requests.Observe(time.Since(start).Seconds())
        w.Write([]byte("ok"))
    })

    http.ListenAndServe(":8080", nil)
}
```

## Related Errors

- [go-grafana-error]({{< relref "/languages/go/go-grafana-error" >}}) — Grafana dashboards for Prometheus metrics
- [go-opentelemetry-error]({{< relref "/languages/go/go-opentelemetry-error" >}}) — OTel metrics alternative
- [panic]({{< relref "/languages/go/invalid-memory-address" >}}) — panic from duplicate MustRegister
