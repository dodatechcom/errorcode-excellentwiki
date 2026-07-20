---
title: "[Solution] Kitex Transport Error Fix"
description: "Fix Kitex transport errors. Handle Thrift protocol, connection management, and timeout configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Kitex Transport Error

The CloudWeGo Kitex RPC framework fails during transport when the service registry is unreachable, the codec cannot serialize the message, the connection pool is exhausted, or the timeout configuration is too aggressive. Kitex uses a custom transport layer optimized for high performance.

## Common Causes

```go
// Cause 1: Registry unreachable
opts := []client.Option{
    client.WithHostPorts("wrong-host:8888"),
}
client, err := kitex.NewClient("my-service", opts...)
// dial tcp: lookup wrong-host: no such host

// Cause 2: Serialization mismatch
// Server uses Thrift, client uses Protobuf
// codec: unsupported codec

// Cause 3: Connection pool exhaustion
opts := []client.Option{
    client.WithConnectTimeout(100 * time.Millisecond), // too short
}
// all connections busy, new requests timeout

// Cause 4: Max message size exceeded
// sending large payload without configuring size limit
// transport: message too large

// Cause 5: Service name mismatch in discovery
// Client looks for "service-a", server registers as "service_a"
```

## How to Fix

### Fix 1: Configure client with proper options

```go
import (
    "context"
    "time"

    "github.com/cloudwego/kitex/client"
    "github.com/cloudwego/kitex/pkg/rpcinfo"
    "github.com/cloudwego/kitex/transport"
)

func createClient() (MyServiceClient, error) {
    opts := []client.Option{
        client.WithHostPorts("localhost:8888"),
        client.WithConnectTimeout(5 * time.Second),
        client.WithRPCTimeout(10 * time.Second),
        client.WithTransportProtocol(transport.TTHeader),
    }

    return NewMyServiceClient("my-service", opts...)
}
```

### Fix 2: Configure server with proper limits

```go
import (
    "github.com/cloudwego/kitex/server"
    "github.com/cloudwego/kitex/pkg/limit"
)

func createServer() error {
    opts := []server.Option{
        server.WithServiceAddr(&net.TCPAddr{Port: 8888}),
        server.WithLimit(&limit.Option{
            MaxConnections: 1000,
            MaxQPS:         10000,
        }),
    }

    svr := NewMyService(handler, opts...)
    return svr.Run()
}
```

### Fix 3: Use retry with backoff for transient failures

```go
import "github.com/cloudwego/kitex/client"

func callWithRetry(ctx context.Context, req *MyRequest) (*MyResponse, error) {
    var lastErr error
    for i := 0; i < 3; i++ {
        resp, err := client.MyMethod(ctx, req)
        if err == nil {
            return resp, nil
        }
        lastErr = err
        time.Sleep(time.Duration(i+1) * 100 * time.Millisecond)
    }
    return nil, fmt.Errorf("failed after 3 retries: %w", lastErr)
}
```

## Examples

```go
package main

import (
    "context"
    "log"
    "net"

    "github.com/cloudwego/kitex/server"
)

func main() {
    addr, _ := net.ResolveTCPAddr("tcp", "localhost:8888")
    svr := NewMyService(
        new(MyServiceImpl),
        server.WithServiceAddr(addr),
    )

    if err := svr.Run(); err != nil {
        log.Fatalf("server stopped with error: %v", err)
    }
}
```

## Related Errors

- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — gRPC transport similar issues
- [grpc-timeout]({{< relref "/languages/go/grpc-timeout" >}}) — RPC deadline exceeded
- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — timeout before Kitex responds
