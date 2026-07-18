---
title: "[Solution] Go gRPC Error — How to Fix"
description: "Fix Go gRPC errors. Handle connection failures, deadline errors, status codes, interceptor issues, and stream management."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go gRPC Error

Fix Go gRPC errors. Handle connection failures, deadline errors, status codes, interceptor issues, and stream management.

## Why It Happens

- gRPC server is not running or the address is incorrect
- RPC deadline is not set causing requests to hang indefinitely
- Status codes are not properly mapped to business errors
- Unary or stream interceptors have bugs causing request failures

## Common Error Messages

```
rpc error: code = Unavailable desc = connection refused
```
```
rpc error: code = DeadlineExceeded
```
```
rpc error: code = Internal desc = transport is closing
```
```
rpc error: code = Unknown desc = unexpected EOF
```

## How to Fix It

### Solution 1: Set gRPC dial options with timeouts

```go
conn, err := grpc.Dial(
    "localhost:50051",
    grpc.WithTransportCredentials(insecure.NewCredentials()),
    grpc.WithBlock(),
    grpc.WithTimeout(5*time.Second),
)
```

### Solution 2: Use per-RPC timeouts with context

```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
resp, err := client.GetUser(ctx, &pb.GetUserRequest{Id: 123})
if err != nil {
    st, ok := status.FromError(err)
    if ok {
        switch st.Code() {
        case codes.NotFound: log.Println("user not found")
        case codes.DeadlineExceeded: log.Println("timed out")
        }
    }
}
```

### Solution 3: Map business errors to gRPC status codes

```go
func (s *server) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.User, error) {
    user, err := s.db.GetUser(req.Id)
    if err != nil {
        return nil, status.Errorf(codes.NotFound, "user %d not found", req.Id)
    }
    return user, nil
}
```

### Solution 4: Handle streaming errors properly

```go
stream, err := client.WatchEvents(ctx, &pb.WatchRequest{})
if err != nil { return err }
for {
    event, err := stream.Recv()
    if err == io.EOF { break }
    if err != nil {
        st, _ := status.FromError(err)
        if st.Code() == codes.Canceled { break }
        return err
    }
    processEvent(event)
}
```

## Common Scenarios

- A gRPC client times out because no deadline is set on the context
- A gRPC server returns generic Internal errors instead of specific business errors
- A gRPC stream silently drops events because the server does not handle send errors

## Prevent It

- Always set a deadline on gRPC client contexts using context.WithTimeout
- Map business errors to appropriate gRPC status codes (NotFound, InvalidArgument, etc.)
- Handle stream errors explicitly by checking io.EOF and status codes
