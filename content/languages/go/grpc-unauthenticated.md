---
title: "[Solution] gRPC Unauthenticated Fix"
description: "Fix Go gRPC unauthenticated errors. Handle token validation, credentials, and authentication interceptors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# gRPC Unauthenticated

A gRPC server returns `codes.Unauthenticated` when the client has not provided valid credentials, the token is missing, or the authentication interceptor rejects the request. This is distinct from `PermissionDenied` — Unauthenticated means "who are you?", PermissionDenied means "you can't do that".

## Common Causes

```go
// Cause 1: Missing metadata (no token sent)
// Client does not attach authorization token to context

// Cause 2: Empty or malformed token
md := metadata.Pairs("authorization", "")
// token is empty string

// Cause 3: Authentication interceptor rejects
func authInterceptor(ctx context.Context, ...) {
    md, ok := metadata.FromIncomingContext(ctx)
    if !ok {
        return nil, status.Error(codes.Unauthenticated, "missing metadata")
    }
}

// Cause 4: Token expired
// JWT token's exp claim is in the past

// Cause 5: Wrong authentication scheme
// Client sends "Basic xxx" but server expects "Bearer xxx"
```

## How to Fix

### Fix 1: Attach credentials to every RPC call

```go
import (
    "context"

    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials"
    "google.golang.org/grpc/metadata"
)

func dialWithCredentials(addr, token string) (*grpc.ClientConn, error) {
    return grpc.Dial(addr,
        grpc.WithTransportCredentials(insecure.NewCredentials()),
        grpc.WithPerRPCCredentials(&staticToken{token: token}),
    )
}

type staticToken struct {
    token string
}

func (t *staticToken) GetRequestMetadata(ctx context.Context, uri ...string) (map[string]string, error) {
    return map[string]string{
        "authorization": "Bearer " + t.token,
    }, nil
}

func (t *staticToken) RequireTransportSecurity() bool { return false }
```

### Fix 2: Implement server-side authentication

```go
func authInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
    md, ok := metadata.FromIncomingContext(ctx)
    if !ok {
        return nil, status.Error(codes.Unauthenticated, "missing metadata")
    }

    authHeader := md.Get("authorization")
    if len(authHeader) == 0 {
        return nil, status.Error(codes.Unauthenticated, "missing authorization")
    }

    token := strings.TrimPrefix(authHeader[0], "Bearer ")
    claims, err := validateJWT(token)
    if err != nil {
        return nil, status.Errorf(codes.Unauthenticated, "invalid token: %v", err)
    }

    ctx = context.WithValue(ctx, "claims", claims)
    return handler(ctx, req)
}
```

### Fix 3: Use TLS credentials for certificate-based auth

```go
creds, _ := credentials.NewClientTLSFromFile("ca.pem", "")
conn, _ := grpc.Dial(addr, grpc.WithTransportCredentials(creds))
```

## Examples

```go
package main

import (
    "context"
    "log"
    "net"
    "strings"

    "google.golang.org/grpc"
    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/metadata"
    "google.golang.org/grpc/status"
)

func main() {
    gs := grpc.NewServer(
        grpc.UnaryInterceptor(authInterceptor),
    )
    lis, _ := net.Listen("tcp", ":50051")
    pb.RegisterServiceServer(gs, &server{})
    log.Fatal(gs.Serve(lis))
}

func authInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
    md, ok := metadata.FromIncomingContext(ctx)
    if !ok {
        return nil, status.Error(codes.Unauthenticated, "no metadata")
    }

    token := md.Get("authorization")
    if len(token) == 0 || !strings.HasPrefix(token[0], "Bearer ") {
        return nil, status.Error(codes.Unauthenticated, "invalid credentials")
    }

    return handler(ctx, req)
}
```

## Related Errors

- [grpc-permission]({{< relref "/languages/go/grpc-permission" >}}) — PermissionDenied vs Unauthenticated
- [http-status-401]({{< relref "/languages/go/http-status-401" >}}) — HTTP equivalent of Unauthenticated
- [go-jwt-error]({{< relref "/languages/go/go-jwt-error" >}}) — JWT token validation
