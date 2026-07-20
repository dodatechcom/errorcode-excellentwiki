---
title: "[Solution] Jaeger Collector Error Fix"
description: "Fix Jaeger collector errors in Go. Handle trace collection, span reporting, and sampling configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jaeger Collector Error

The Jaeger Go client fails to send traces when the collector endpoint is unreachable, the agent cannot flush spans, the batch size exceeds limits, or the service name is not configured. Jaeger uses UDP for agent-to-collector communication and HTTP/gRPC for direct collector submission.

## Common Causes

```go
// Cause 1: Collector endpoint unreachable
sender, err := jaeger.NewHTTPTransport("http://wrong-host:14268/api/traces")
// post "http://wrong-host:14268/api/traces": dial tcp: lookup wrong-host

// Cause 2: Service name not set
tracer, _, _ := jaeger.NewTracer(
    "",  // empty service name
    jaeger.NewConstReporter(jaeger.NewNullReporter()),
)
// Jaeger requires non-empty service name

// Cause 3: Agent UDP buffer too small
sender, err := jaeger.NewUDPTransport("agent:6831")
// default buffer 65535 bytes — large spans get truncated

// Cause 4: Batch size too large
// Sending 10000 spans in one batch
// collector rejects with "too many spans"

// Cause 5: Jaeger not running or wrong port
sender, err := jaeger.NewUDPTransport("localhost:6831")
// send error: connection refused
```

## How to Fix

### Fix 1: Configure Jaeger client properly

```go
import (
    "fmt"
    "time"

    "github.com/uber/jaeger-client-go"
    "github.com/uber/jaeger-client-go/config"
)

func initTracer(serviceName string) (*jaeger.Tracer, error) {
    cfg := config.Configuration{
        ServiceName: serviceName,
        Sampler: &config.SamplerConfig{
            Type:  jaeger.SamplerTypeConst,
            Param: 1, // sample 100% in dev
        },
        Reporter: &config.ReporterConfig{
            LogSpans:           true,
            CollectorEndpoint:  "http://localhost:14268/api/traces",
            BufferMaxBytes:     1048576, // 1MB
        },
    }

    tracer, closer, err := cfg.NewTracer(
        config.Logger(jaegerlog.StdLogger),
    )
    if err != nil {
        return nil, fmt.Errorf("create tracer: %w", err)
    }

    return tracer, nil
}
```

### Fix 2: Use UDP transport for agent communication

```go
func udpTransport() (jaeger.Transport, error) {
    return jaeger.NewUDPTransport(
        "jaeger-agent:6831",
        "0.0.0.0",       // local bind address
        65535,            // max packet size
        0,                // wait between flushes (0 = default)
    )
}
```

### Fix 3: Use OpenTelemetry with Jaeger exporter

```go
import (
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/jaeger"
    sdktrace "go.opentelemetry.io/otel/sdk/trace"
)

func init() {
    exporter, _ := jaeger.New(jaeger.WithCollectorEndpoint(
        jaeger.WithEndpoint("http://localhost:14268/api/traces"),
    ))

    tp := sdktrace.NewTracerProvider(
        sdktrace.WithBatcher(exporter),
        sdktrace.WithSampler sdktrace.AlwaysSample(),
    )
    otel.SetTracerProvider(tp)
}
```

## Examples

```go
package main

import (
    "fmt"
    "time"

    "github.com/uber/jaeger-client-go"
    "github.com/uber/jaeger-client-go/config"
)

func main() {
    cfg := config.Configuration{
        ServiceName: "my-service",
        Sampler: &config.SamplerConfig{
            Type:  jaeger.SamplerTypeConst,
            Param: 1,
        },
        Reporter: &config.ReporterConfig{
            CollectorEndpoint: "http://localhost:14268/api/traces",
        },
    }

    tracer, _, _ := cfg.NewTracer()
    defer tracer.Close()

    span := tracer.StartSpan("main-operation")
    defer span.Finish()

    span.SetTag("key", "value")
    span.LogFields(jaeger.String("event", "processing"))

    time.Sleep(100 * time.Millisecond)
    fmt.Println("Operation completed")
}
```

## Related Errors

- [go-opentelemetry-error]({{< relref "/languages/go/go-opentelemetry-error" >}}) — OTel trace export failures
- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — gRPC transport to Jaeger collector
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — UDP connection to Jaeger agent fails
