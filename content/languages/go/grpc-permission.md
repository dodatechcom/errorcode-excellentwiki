---
title: "[Solution] gRPC PermissionDenied Fix"
description: "Fix Go gRPC permission denied errors. Handle authorization, access control, and interceptor errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# gRPC PermissionDenied

A gRPC server returns `codes.PermissionDenied` when the client lacks required authorization, the interceptor rejects the request, or the service account does not have access to the requested resource. This maps to HTTP 403 and is distinct from `Unauthenticated` (HTTP 401).

## Common Causes

```go
// Cause 1: Missing or invalid metadata (authorization token)
md, _ := metadata.FromOutgoingContext(ctx)
// no "authorization" key in metadata

// Cause 2: Server interceptor rejects based on missing role
func authInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
    md, ok := metadata.FromIncomingContext(ctx)
    if !ok {
        return nil, status.Error(codes.PermissionDenied, "missing metadata")
    }
}

// Cause 3: Service account lacks permission in IAM

// Cause 4: mTLS client certificate not trusted

// Cause 5: Method-level access control blocks the call
```

## How to Fix

### Fix 1: Attach authorization token to every RPC call

```go
import (
    "context"

    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials/insecure"
    "google.golang.org/grpc/metadata"
)

func dialWithToken(addr, token string) (*grpc.ClientConn, error) {
    return grpc.Dial(addr,
        grpc.WithTransportCredentials(insecure.NewCredentials()),
        grpc.WithPerRPCCredentials(&tokenProvider{token: token}),
    )
}

type tokenProvider struct {
    token string
}

func (t *tokenProvider) GetRequestMetadata(ctx context.Context, uri ...string) (map[string]string, error) {
    return map[string]string{"authorization": t.token}, nil
}

func (t *tokenProvider) RequireTransportSecurity() bool { return false }
```

### Fix 2: Implement server-side authorization interceptor

```go
func authorizeInterceptor() grpc.UnaryServerInterceptor {
    return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
        md, ok := metadata.FromIncomingContext(ctx)
        if !ok {
            return nil, status.Error(codes.Unauthenticated, "missing metadata")
        }

        token := md.Get("authorization")
        if len(token) == 0 {
            return nil, status.Error(codes.Unauthenticated, "missing token")
        }

        role, err := validateToken(token[0])
        if err != nil {
            return nil, status.Error(codes.PermissionDenied, "insufficient permissions")
        }

        ctx = context.WithValue(ctx, "role", role)
        return handler(ctx, req)
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
    "google.golang.org/grpc/metadata"
    "google.golang.org/grpc/status"
)

type server struct{}

func (s *server) GetSecret(ctx context.Context, req *pb.GetSecretRequest) (*pb.Secret, error) {
    md, ok := metadata.FromIncomingContext(ctx)
    if !ok {
        return nil, status.Error(codes.Unauthenticated, "no metadata")
    }

    token := md.Get("x-api-key")
    if len(token) == 0 || token[0] != "valid-key" {
        return nil, status.Error(codes.PermissionDenied, "invalid API key")
    }

    return &pb.Secret{Value: "super-secret"}, nil
}

func main() {
    lis, _ := net.Listen("tcp", ":50051")
    gs := grpc.NewServer()
    pb.RegisterSecretServiceServer(gs, &server{})
    log.Fatal(gs.Serve(lis))
}
```

## Related Errors

- [grpc-unauthenticated]({{< relref "/languages/go/grpc-unauthenticated" >}}) — missing credentials entirely
- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — server unreachable
- [go-vault-error]({{< relref "/languages/go/go-vault-error" >}}) — Vault permission denied for secret access
