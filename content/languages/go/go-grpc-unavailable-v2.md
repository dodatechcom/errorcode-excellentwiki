---
title: "[Solution] gRPC: Unavailable — Server Down Fix"
description: "Fix gRPC Unavailable errors when the server is down or unreachable. Handle connection failures, load balancing, and reconnection."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# gRPC: Unavailable — Server Down

This error occurs when a gRPC client cannot reach the server. The `Unavailable` status indicates the service is not accepting RPCs, typically because the server process is down or the network path is broken.

## What This Error Means

Common error messages:

- `rpc error: code = Unavailable desc = connection error: dial tcp 127.0.0.1:50051: connect: connection refused`
- `rpc error: code = Unavailable desc = last connection error: connection error: desc = "transport: ...`
- `rpc error: code = Unavailable desc = DNS resolution failed for "grpc.example.com:50051"`
- `context deadline exceeded`

gRPC uses HTTP/2 under the hood. An `Unavailable` error means the client's transport layer cannot establish or maintain a connection to the gRPC server.

## Common Causes

```go
// Cause 1: Server not running
conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
// connection refused

// Cause 2: Wrong address or port
conn, err := grpc.Dial("localhost:50052", grpc.WithInsecure())
// server on 50051

// Cause 3: TLS mismatch
conn, err := grpc.Dial("server:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
// server requires TLS

// Cause 4: Server shutting down
// Server received SIGTERM, stopped accepting connections

// Cause 5: Network issue
// Firewall blocking port, DNS resolution failing
```

## How to Fix

### Fix 1: Use retry policy with backoff

```go
conn, err := grpc.Dial(
    "localhost:50051",
    grpc.WithTransportCredentials(insecure.NewCredentials()),
    grpc.WithConnectParams(grpc.ConnectParams{
        Backoff: backoff.Config{
            BaseDelay:  500 * time.Millisecond,
            Multiplier: 1.5,
            Jitter:     0.2,
            MaxDelay:   5 * time.Second,
        },
        MinConnectTimeout: 5 * time.Second,
    }),
)
if err != nil {
    log.Fatalf("Failed to connect: %v", err)
}
defer conn.Close()
```

### Fix 2: Add health checking

```go
import (
    "google.golang.org/grpc/health"
    healthpb "google.golang.org/grpc/health/grpc_health_v1"
)

conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
if err != nil {
    log.Fatal(err)
}

healthClient := healthpb.NewHealthClient(conn)
resp, err := healthClient.Check(context.Background(), &healthpb.HealthCheckRequest{
    Service: "",
})
if err != nil || resp.Status != healthpb.HealthCheckResponse_SERVING {
    log.Fatal("Server is not healthy")
}
```

### Fix 3: Use keepalive for long-lived connections

```go
conn, err := grpc.Dial(
    "localhost:50051",
    grpc.WithKeepaliveParams(keepalive.ClientParameters{
        Time:                10 * time.Second,
        Timeout:             3 * time.Second,
        PermitWithoutStream: true,
    }),
    grpc.WithTransportCredentials(insecure.NewCredentials()),
)
```

### Fix 4: Handle server graceful shutdown

```go
// Server side
func main() {
    lis, err := net.Listen("tcp", ":50051")
    if err != nil {
        log.Fatal(err)
    }

    srv := grpc.NewServer()
    pb.RegisterMyServiceServer(srv, &service{})

    // Register health service
    healthpb.RegisterHealthServer(srv, health.NewServer())

    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGTERM)

    go func() {
        <-quit
        log.Println("Shutting down gRPC server...")
        srv.GracefulStop()
    }()

    if err := srv.Serve(lis); err != nil {
        log.Fatal(err)
    }
}
```

### Fix 5: Use connection pooling

```go
var conns = make([]*grpc.ClientConn, 3)

func init() {
    addrs := []string{"server1:50051", "server2:50051", "server3:50051"}
    for i, addr := range addrs {
        conn, err := grpc.Dial(addr, grpc.WithInsecure())
        if err != nil {
            log.Printf("Failed to connect to %s: %v", addr, err)
            continue
        }
        conns[i] = conn
    }
}
```

## Examples

```
rpc error: code = Unavailable desc = connection error:
dial tcp 127.0.0.1:50051: connect: connection refused
```

```go
// Fix: check server before calling
func callWithCheck(client pb.MyServiceClient) error {
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    resp, err := client.GetData(ctx, &pb.GetDataRequest{Id: 1})
    if err != nil {
        if status.Code(err) == codes.Unavailable {
            return fmt.Errorf("server unavailable: %w", err)
        }
        return err
    }
    _ = resp
    return nil
}
```

## Related Errors

- [grpc-status]({{< relref "/languages/go/grpc-status" >}}) — gRPC status codes
- [grpc-unauthenticated]({{< relref "/languages/go/grpc-unauthenticated" >}}) — authentication error
- [go-grpc-timeout-v2]({{< relref "/languages/go/go-grpc-timeout-v2" >}}) — deadline exceeded
