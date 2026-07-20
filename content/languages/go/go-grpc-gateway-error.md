---
title: "[Solution] grpc-gateway Transcode Error Fix"
description: "Fix grpc-gateway transcoding errors. Handle HTTP/gRPC mapping, path patterns, and body encoding."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# grpc-gateway Transcode Error

The `grpc-gateway` reverse proxy fails to transcode HTTP/JSON requests to gRPC when the proto-generated gateway code is missing, the request body does not match the proto message schema, HTTP route mappings are wrong, or custom protobuf marshaling fails. The gateway acts as a translator between REST and gRPC.

## Common Causes

```go
// Cause 1: Missing RegisterXxxHandlerFromEndpoint call
// Proto generated code must register the gateway handler
pb.RegisterUserServiceHandlerFromEndpoint(ctx, mux, "localhost:50051", opts)

// Cause 2: Content-Type not set to application/json
req.Header.Set("Content-Type", "text/plain")
// grpc-gateway expects application/json

// Cause 3: HTTP route does not match proto annotations
// proto: rpc GetUser(GetUserRequest) returns (User)
// HTTP: GET /users/{user_id} — must match google.api.http annotation

// Cause 4: Required field missing in JSON body
// proto: message CreateUserRequest { string name = 1; }
// JSON: {} — name is required but empty

// Cause 5: Field number mismatch after proto regeneration
// Old client sends field numbers that no longer exist
```

## How to Fix

### Fix 1: Set up gateway with proper annotations

```protobuf
// user.proto
syntax = "proto3";
package user;

import "google/api/annotations.proto";

service UserService {
    rpc GetUser(GetUserRequest) returns (User) {
        option (google.api.http) = {
            get: "/v1/users/{user_id}"
        };
    }

    rpc CreateUser(CreateUserRequest) returns (User) {
        option (google.api.http) = {
            post: "/v1/users"
            body: "*"
        };
    }
}

message GetUserRequest {
    string user_id = 1;
}

message CreateUserRequest {
    string name = 1;
    string email = 2;
}

message User {
    string user_id = 1;
    string name = 2;
    string email = 3;
}
```

### Fix 2: Initialize gateway with error handling

```go
import (
    "context"
    "log"
    "net"

    "github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials/insecure"
)

func runGateway() error {
    ctx := context.Background()

    mux := runtime.NewServeMux()
    opts := []grpc.DialOption{grpc.WithTransportCredentials(insecure.NewCredentials())}

    err := pb.RegisterUserServiceHandlerFromEndpoint(ctx, mux, "localhost:50051", opts)
    if err != nil {
        return err
    }

    lis, _ := net.Listen("tcp", ":8080")
    return http.Serve(lis, mux)
}
```

### Fix 3: Use proper error codes in gateway responses

```go
import (
    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/status"
)

func (s *server) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.User, error) {
    user, err := s.findUser(req.UserId)
    if err != nil {
        return nil, status.Errorf(codes.NotFound, "user %s not found", req.UserId)
    }
    return user, nil
}
```

## Examples

```go
package main

import (
    "context"
    "log"
    "net"

    "github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials/insecure"
)

func main() {
    ctx := context.Background()
    mux := runtime.NewServeMux()
    opts := []grpc.DialOption{grpc.WithTransportCredentials(insecure.NewCredentials())}

    if err := pb.RegisterUserServiceHandlerFromEndpoint(ctx, mux, "localhost:50051", opts); err != nil {
        log.Fatal(err)
    }

    log.Println("Gateway listening on :8080")
    log.Fatal(http.ListenAndServe(":8080", mux))
}
```

## Related Errors

- [go-protobuf-error]({{< relref "/languages/go/go-protobuf-error" >}}) — protobuf marshal/unmarshal failures
- [grpc-status]({{< relref "/languages/go/grpc-status" >}}) — gRPC status codes in gateway responses
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — JSON parsing fails in gateway
