---
title: "[Solution] OpenTelemetry Trace Export Error Fix"
description: "Fix OpenTelemetry trace export errors. Handle span processing, exporter configuration, and sampling."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# OpenTelemetry Trace Export Error

The OpenTelemetry Go SDK fails to export traces to the configured collector. This happens when the OTLP exporter cannot connect to the collector endpoint, the exporter is not shut down (buffered spans are lost), the span queue overflows, or the collector rejects traces due to missing resource attributes.

## Common Causes

```go
// Cause 1: Collector endpoint unreachable
exporter, err := otlptracegrpc.New(ctx,
    otlptracegrpc.WithEndpoint("wrong-host:4317"),
    otlptracegrpc.WithInsecure(),
)
// context deadline exceeded: cannot connect to collector

// Cause 2: Exporter not shut down — spans lost
tp, _ := initTracer()
// forgot: tp.Shutdown(ctx) — buffered spans never exported

// Cause 3: Queue full due to burst of spans
exporter, err := otlptracegrpc.New(ctx,
    otlptracegrpc.WithSpanProcessor(batch.NewBatchSpanProcessor(exporter)),
)
// default queue size 2048, bursts overflow silently

// Cause 4: Missing resource attributes — collector rejects
tp := sdktrace.NewTracerProvider(
    sdktrace.WithResource(nil), // no service.name
)

// Cause 5: gRPC insecure vs TLS mismatch
exporter, err := otlptracegrpc.New(ctx,
    otlptracegrpc.WithEndpoint("collector:4317"),
    // missing WithInsecure() when collector expects plain gRPC
)
```

## How to Fix

### Fix 1: Configure exporter with proper endpoint and timeout

```go
import (
    "context"
    "time"

    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    "go.opentelemetry.io/otel/sdk/resource"
    sdktrace "go.opentelemetry.io/otel/sdk/trace"
    semconv "go.opentelemetry.io/otel/semconv/v1.24.0"
)

func initTracer(ctx context.Context) (*sdktrace.TracerProvider, error) {
    exporter, err := otlptracegrpc.New(ctx,
        otlptracegrpc.WithEndpoint("localhost:4317"),
        otlptracegrpc.WithInsecure(),
        otlptracegrpc.WithTimeout(10*time.Second),
    )
    if err != nil {
        return nil, err
    }

    res, _ := resource.Merge(
        resource.Default(),
        resource.NewWithAttributes(semconv.SchemaURL,
            semconv.ServiceNameKey.String("my-service"),
        ),
    )

    tp := sdktrace.NewTracerProvider(
        sdktrace.WithBatcher(exporter),
        sdktrace.WithResource(res),
    )
    return tp, nil
}
```

### Fix 2: Always shut down the provider to flush spans

```go
tp, err := initTracer(ctx)
if err != nil {
    log.Fatal(err)
}
defer func() {
    if err := tp.Shutdown(ctx); err != nil {
        log.Printf("tracer shutdown error: %v", err)
    }
}()
```

### Fix 3: Increase the span processor queue size

```go
exporter, _ := otlptracegrpc.New(ctx,
    otlptracegrpc.WithEndpoint("localhost:4317"),
    otlptracegrpc.WithInsecure(),
)

sp := batch.NewBatchSpanProcessor(exporter,
    batch.WithMaxQueueSize(8192),
    batch.WithBatchTimeout(5*time.Second),
    batch.WithMaxExportBatchSize(1024),
)

tp := sdktrace.NewTracerProvider(
    sdktrace.WithSpanProcessor(sp),
)
```

## Examples

```go
package main

import (
    "context"
    "log"
    "time"

    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    "go.opentelemetry.io/otel/sdk/resource"
    sdktrace "go.opentelemetry.io/otel/sdk/trace"
    semconv "go.opentelemetry.io/otel/semconv/v1.24.0"
)

func main() {
    ctx := context.Background()

    exporter, err := otlptracegrpc.New(ctx,
        otlptracegrpc.WithEndpoint("localhost:4317"),
        otlptracegrpc.WithInsecure(),
    )
    if err != nil {
        log.Fatal(err)
    }

    res, _ := resource.New(ctx,
        resource.WithAttributes(semconv.ServiceNameKey.String("demo")),
    )

    tp := sdktrace.NewTracerProvider(
        sdktrace.WithBatcher(exporter),
        sdktrace.WithResource(res),
    )
    defer tp.Shutdown(ctx)

    otel.SetTracerProvider(tp)
    tracer := otel.Tracer("demo")

    ctx, span := tracer.Start(ctx, "main-operation")
    defer span.End()

    time.Sleep(100 * time.Millisecond)
    span.AddEvent("work completed")
}
```

## Related Errors

- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — export times out before collector responds
- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — gRPC transport to collector is down
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection to collector port fails
