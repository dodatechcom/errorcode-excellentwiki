---
title: "[Solution] gRPC: DeadlineExceeded — Request Timeout Fix"
description: "Fix gRPC DeadlineExceeded errors when requests time out. Handle context deadlines, streaming timeouts, and slow backends."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["grpc", "timeout", "deadline", "context", "streaming"]
weight: 5
---

# gRPC: DeadlineExceeded — Request Timeout

This error occurs when a gRPC RPC call exceeds its deadline. Unlike HTTP timeouts, gRPC deadlines are propagated through the entire call chain from client to server.

## What This Error Means

Common error messages:

- `rpc error: code = DeadlineExceeded desc = context deadline exceeded`
- `rpc error: code = DeadlineExceeded desc = context canceled`
- `ERROR: Deadline Exceeded in /package.Service/Method`

gRPC deadlines are absolute points in time (not durations) that propagate with every RPC hop. If the server doesn't respond before the deadline, both client and server receive the error.

## Common Causes

```go
// Cause 1: Short client deadline
ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
defer cancel()
resp, err := client.GetData(ctx, req) // server takes 500ms

// Cause 2: Server slow due to heavy computation
// Server processes for 5s, client deadline is 2s

// Cause 3: Database query timeout on server
// Server makes slow DB call that blocks the handler

// Cause 4: Cascading timeouts
// Client → Server A → Server B, each with separate timeouts

// Cause 5: Clock skew between client and server
// Deadline set on client but server clock is ahead
```

## How to Fix

### Fix 1: Set appropriate deadlines

```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()

resp, err := client.GetData(ctx, &pb.GetDataRequest{Id: 1})
if err != nil {
    if status.Code(err) == codes.DeadlineExceeded {
        log.Println("RPC timed out — check server performance")
    }
    return err
}
```

### Fix 2: Propagate deadline from incoming request

```go
func (s *server) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.User, error) {
    // Forward the deadline to downstream calls
    ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    defer cancel()

    user, err := s.db.GetUser(ctx, req.Id)
    if err != nil {
        return nil, status.Errorf(codes.Internal, "db error: %v", err)
    }
    return user, nil
}
```

### Fix 3: Use per-RPC credentials with deadline

```go
conn, err := grpc.Dial(
    "server:50051",
    grpc.WithTransportCredentials(insecure.NewCredentials()),
    grpc.WithDefaultCallOptions(
        grpc.MaxCallRecvMsgSize(4*1024*1024),
    ),
)

// Set deadline per call
ctx, cancel := context.WithTimeout(context.Background(), 60*time.Second)
defer cancel()

resp, err := pb.NewMyServiceClient(conn).ProcessData(ctx, req)
```

### Fix 4: Handle streaming timeouts

```go
func receiveStream(stream pb.MyService_WatchClient) {
    for {
        ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
        resp, err := stream.Recv()

        cancel()

        if err == io.EOF {
            break
        }
        if err != nil {
            if status.Code(err) == codes.DeadlineExceeded {
                log.Println("Stream receive timed out")
            }
            break
        }
        processEvent(resp)
    }
}
```

### Fix 5: Use deadline interceptor

```go
func deadlineInterceptor(deadline time.Duration) grpc.UnaryClientInterceptor {
    return func(
        ctx context.Context,
        method string,
        req, reply interface{},
        cc *grpc.ClientConn,
        invoker grpc.UnaryInvoker,
        opts ...grpc.CallOption,
    ) error {
        if _, ok := ctx.Deadline(); !ok {
            var cancel context.CancelFunc
            ctx, cancel = context.WithTimeout(ctx, deadline)
            defer cancel()
        }
        return invoker(ctx, method, req, reply, cc, opts...)
    }
}

conn, err := grpc.Dial(
    "server:50051",
    grpc.WithInsecure(),
    grpc.WithUnaryInterceptor(deadlineInterceptor(30*time.Second)),
)
```

## Examples

```
rpc error: code = DeadlineExceeded desc = context deadline exceeded
```

```go
// Fix: check if deadline is reasonable before calling
func safeCall(ctx context.Context, client pb.ServiceClient, req *pb.Request) error {
    deadline, ok := ctx.Deadline()
    if ok && time.Until(deadline) < 1*time.Second {
        return fmt.Errorf("insufficient time for RPC: %v remaining", time.Until(deadline))
    }
    _, err := client.DoWork(ctx, req)
    return err
}
```

## Related Errors

- [go-grpc-unavailable-v2]({{< relref "/languages/go/go-grpc-unavailable-v2" >}}) — server down
- [go-http-timeout-v2]({{< relref "/languages/go/go-http-timeout-v2" >}}) — context deadline exceeded
- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context deadline exceeded
