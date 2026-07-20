---
title: "[Solution] gRPC DeadlineExceeded Fix"
description: "Fix Go gRPC deadline exceeded errors. Handle timeouts, context deadlines, and slow responses."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# gRPC DeadlineExceeded

A gRPC client receives `codes.DeadlineExceeded` when the RPC call takes longer than the configured deadline. This is gRPC's version of a timeout — every RPC should have a deadline to prevent resource exhaustion and slow cascading failures.

## Common Causes

```go
// Cause 1: No deadline set on context
ctx := context.Background()
resp, err := client.GetData(ctx, req)
// no timeout — may run forever

// Cause 2: Deadline too short for the operation
ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
defer cancel()
resp, err := client.GetData(ctx, req)
// operation takes 200ms, deadline of 100ms exceeded

// Cause 3: Server processing too slow
// Server does heavy computation, deadline is tight
// DeadlineExceeded at client, server still processing

// Cause 4: Clock skew between client and server
// Client deadline set for 5s, but clock skew causes premature expiry

// Cause 5: Deadline set but not propagated to downstream calls
func getData(ctx context.Context) {
    newCtx := context.Background() // lost original deadline
    client.Call(newCtx, req) // no timeout
}
```

## How to Fix

### Fix 1: Always set deadline on context

```go
import (
    "context"
    "time"

    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials/insecure"
)

func callWithTimeout(addr string, req *pb.Request) (*pb.Response, error) {
    conn, err := grpc.Dial(addr,
        grpc.WithTransportCredentials(insecure.NewCredentials()),
    )
    if err != nil {
        return nil, err
    }
    defer conn.Close()

    client := pb.NewDataServiceClient(conn)

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    return client.GetData(ctx, req)
}
```

### Fix 2: Use deadline propagation for chained calls

```go
func handleRequest(ctx context.Context, req *pb.Request) (*pb.Response, error) {
    // Original deadline propagates to downstream calls
    ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    defer cancel()

    user, err := userClient.GetUser(ctx, &pb.GetUserRequest{Id: req.UserId})
    if err != nil {
        return nil, err // deadline exceeded propagates
    }

    return client.GetData(ctx, &pb.GetDataRequest{User: user})
}
```

### Fix 3: Use per-RPC timeout with interceptors

```go
func timeoutInterceptor() grpc.UnaryClientInterceptor {
    return func(ctx context.Context, method string, req, reply interface{},
        cc *grpc.ClientConn, invoker grpc.UnaryInvoker, opts ...grpc.CallOption) error {

        ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
        defer cancel()

        return invoker(ctx, method, req, reply, cc, opts...)
    }
}

conn, _ := grpc.Dial(addr,
    grpc.WithUnaryInterceptor(timeoutInterceptor()),
)
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
    "google.golang.org/grpc/status"
)

func main() {
    conn, _ := grpc.Dial("localhost:50051", grpc.WithInsecure())
    defer conn.Close()

    client := pb.NewMyServiceClient(conn)

    ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
    defer cancel()

    resp, err := client.DoWork(ctx, &pb.WorkRequest{Data: "test"})
    if err != nil {
        if st, ok := status.FromError(err); ok && st.Code() == codes.DeadlineExceeded {
            log.Fatal("RPC timed out")
        }
        log.Fatal(err)
    }
    log.Printf("Response: %v", resp)
}
```

## Related Errors

- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — Go context deadline exceeded
- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — server unreachable
- [http-timeout]({{< relref "/languages/go/http-timeout" >}}) — HTTP client timeout
