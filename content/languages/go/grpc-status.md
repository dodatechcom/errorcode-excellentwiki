---
title: "[Solution] gRPC Status Codes Fix"
description: "Fix Go gRPC status code errors. Handle status codes, error details, and proper error propagation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# gRPC Status Codes

gRPC uses canonical status codes to communicate error types between client and server. Unlike HTTP, gRPC status codes carry rich error details through status messages and error details. Understanding these codes is essential for proper error handling in gRPC services.

## Common Causes

```go
// Cause 1: Generic error without status code
return nil, errors.New("something went wrong")
// gRPC defaults to codes.Unknown — not specific enough

// Cause 2: Wrong status code for the error type
return nil, status.Error(codes.InvalidArgument, "not found")
// should be codes.NotFound, not codes.InvalidArgument

// Cause 3: Missing error details
return nil, status.Error(codes.Internal, "error")
// no structured error info for client to handle

// Cause 4: Status not converted to gRPC status
return nil, fmt.Errorf("error: %w", err)
// gRPC cannot extract proper status from fmt.Errorf

// Cause 5: Status code lost in interceptors
// interceptor modifies error, status code becomes Unknown
```

## How to Fix

### Fix 1: Use proper gRPC status codes

```go
import (
    "context"
    "fmt"

    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/status"
)

type server struct{}

func (s *server) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.User, error) {
    user, err := findUser(req.Id)
    if err != nil {
        if errors.Is(err, ErrNotFound) {
            return nil, status.Errorf(codes.NotFound, "user %s not found", req.Id)
        }
        if errors.Is(err, ErrPermission) {
            return nil, status.Errorf(codes.PermissionDenied, "access denied to user %s", req.Id)
        }
        return nil, status.Errorf(codes.Internal, "failed to get user: %v", err)
    }
    return user, nil
}
```

### Fix 2: Attach rich error details

```go
import (
    "google.golang.org/genproto/googleapis/rpc/errdetails"
    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/status"
)

func validateRequest(req *pb.CreateUserRequest) error {
    st := status.New(codes.InvalidArgument, "validation failed")

    var details []*errdetails.BadRequest_FieldViolation
    if req.Name == "" {
        details = append(details, &errdetails.BadRequest_FieldViolation{
            Field:       "name",
            Description: "name is required",
        })
    }
    if req.Email == "" {
        details = append(details, &errdetails.BadRequest_FieldViolation{
            Field:       "email",
            Description: "email is required",
        })
    }

    st, _ = st.WithDetails(details...)
    return st.Err()
}
```

### Fix 3: Handle gRPC status on client side

```go
func handleGRPCError(err error) {
    st, ok := status.FromError(err)
    if !ok {
        // Not a gRPC status error
        log.Printf("non-gRPC error: %v", err)
        return
    }

    switch st.Code() {
    case codes.NotFound:
        log.Printf("not found: %s", st.Message())
    case codes.InvalidArgument:
        log.Printf("invalid argument: %s", st.Message())
    case codes.Unavailable:
        log.Printf("service unavailable: %s", st.Message())
    default:
        log.Printf("gRPC error [%s]: %s", st.Code(), st.Message())
    }
}
```

## Examples

```go
package main

import (
    "context"
    "log"
    "net"

    "google.golang.org/grpc"
    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/status"
)

type server struct{}

func (s *server) DoWork(ctx context.Context, req *pb.WorkRequest) (*pb.WorkResponse, error) {
    if req.Data == "" {
        return nil, status.Error(codes.InvalidArgument, "data is required")
    }

    result, err := process(req.Data)
    if err != nil {
        return nil, status.Errorf(codes.Internal, "processing failed: %v", err)
    }

    return &pb.WorkResponse{Result: result}, nil
}

func main() {
    lis, _ := net.Listen("tcp", ":50051")
    gs := grpc.NewServer()
    pb.RegisterWorkServiceServer(gs, &server{})
    log.Fatal(gs.Serve(lis))
}
```

## Related Errors

- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — codes.Unavailable
- [grpc-unauthenticated]({{< relref "/languages/go/grpc-unauthenticated" >}}) — codes.Unauthenticated
- [grpc-permission]({{< relref "/languages/go/grpc-permission" >}}) — codes.PermissionDenied
