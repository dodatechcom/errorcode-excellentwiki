---
title: "[Solution] gRPC Unavailable Connection Refused Fix"
description: "Fix Go gRPC unavailable errors when connection is refused. Handle service discovery, retries, and load balancing."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# gRPC Unavailable Connection Refused

A gRPC client receives `codes.Unavailable` when the server is not reachable, the connection is closed, or the load balancer cannot find healthy backends. This code indicates a transport-level failure, not an application error.

## Common Causes

```go
// Cause 1: Server not running
conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
// connection refused

// Cause 2: Server shut down gracefully
// Server called GracefulStop(), client still has old connection

// Cause 3: Network partition
// Client cannot reach server due to network issues

// Cause 4: Load balancer has no healthy backends
// All backend servers are down

// Cause 5: DNS resolution failure
// Service name not found
```

## How to Fix

### Fix 1: Configure retry and backoff

```go
import (
    "google.golang.org/grpc"
    "google.golang.org/grpc/backoff"
    "google.golang.org/grpc/credentials/insecure"
)

func connectWithRetry(addr string) (*grpc.ClientConn, error) {
    return grpc.Dial(addr,
        grpc.WithTransportCredentials(insecure.NewCredentials()),
        grpc.WithConnectParams(grpc.ConnectParams{
            Backoff: backoff.Config{
                BaseDelay:  100 * time.Millisecond,
                Multiplier: 1.6,
                Jitter:     0.2,
                MaxDelay:   5 * time.Second,
            },
            MinConnectTimeout: 5 * time.Second,
        }),
        grpc.WithDefaultServiceConfig(`{"loadBalancingPolicy":"round_robin"}`),
    )
}
```

### Fix 2: Use health checking for connection management

```go
import "google.golang.org/grpc/health/grpc_health_v1"

func checkHealth(conn *grpc.ClientConn) error {
    client := grpc_health_v1.NewHealthClient(conn)
    resp, err := client.Check(context.Background(), &grpc_health_v1.HealthCheckRequest{})
    if err != nil {
        return fmt.Errorf("health check failed: %w", err)
    }
    if resp.Status != grpc_health_v1.HealthCheckResponse_SERVING {
        return fmt.Errorf("service not serving")
    }
    return nil
}
```

### Fix 3: Implement connection lifecycle management

```go
type GRPCPool struct {
    conns   []*grpc.ClientConn
    current int
    mu      sync.Mutex
}

func (p *GRPCPool) Get() *grpc.ClientConn {
    p.mu.Lock()
    defer p.mu.Unlock()
    conn := p.conns[p.current%len(p.conns)]
    p.current++
    return conn
}
```

## Examples

```go
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/grpc"
    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/credentials/insecure"
    "google.golang.org/grpc/status"
)

func main() {
    conn, err := grpc.Dial("localhost:50051",
        grpc.WithTransportCredentials(insecure.NewCredentials()),
        grpc.WithBlock(),
    )
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close()

    client := pb.NewMyServiceClient(conn)

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    resp, err := client.GetData(ctx, &pb.Request{Id: "123"})
    if err != nil {
        st, ok := status.FromError(err)
        if ok && st.Code() == codes.Unavailable {
            log.Fatal("Service unavailable, please try again later")
        }
        log.Fatal(err)
    }
    log.Printf("Response: %v", resp)
}
```

## Related Errors

- [grpc-timeout]({{< relref "/languages/go/grpc-timeout" >}}) — DeadlineExceeded during connection
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection to gRPC port fails
- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — context timeout during dial
