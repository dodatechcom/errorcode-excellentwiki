---
title: "[Solution] go-kit Endpoint Error Fix"
description: "Fix go-kit endpoint errors. Handle transport, encoding, and service layer errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# go-kit Endpoint Error

The go-kit microservice toolkit fails when endpoint function signatures are wrong, transport layer (HTTP/gRPC) does not match the endpoint definition, middleware does not wrap correctly, or the service interface is not properly implemented. go-kit uses a layered architecture: Transport -> Endpoint -> Service.

## Common Causes

```go
// Cause 1: Endpoint function signature wrong
type StringRequest struct {
    S string
}
type StringResponse struct {
    V string
    Err error
}

// Endpoint must return endpoint.Endpoint
func makeEndpoint(svc StringService) endpoint.Endpoint {
    return func(ctx context.Context, request interface{}) (interface{}, error) {
        req := request.(StringRequest)
        v, err := svc.Uppercase(ctx, req.S)
        return StringResponse{V: v, Err: err}, nil
    }
}

// Cause 2: Service interface not fully implemented
type StringService interface {
    Uppercase(ctx context.Context, s string) (string, error)
    Count(ctx context.Context, s string) int
}
// Forgot Count method — compile error

// Cause 3: HTTP transport decode error
func decodeRequest(r *http.Request) (interface{}, error) {
    var req StringRequest
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        return nil, err
    }
    return req, nil
}

// Cause 4: gRPC transport proto mismatch
// go-kit generates transport code from proto
// If proto changes, transport breaks

// Cause 5: Endpoint middleware does not return same type
func loggingMiddleware(next endpoint.Endpoint) endpoint.Endpoint {
    return func(ctx context.Context, req interface{}) (interface{}, error) {
        log.Printf("calling endpoint with %v", req)
        return next(ctx, req) // must return same signature
    }
}
```

## How to Fix

### Fix 1: Define proper service, endpoint, and transport layers

```go
import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "net/http"

    "github.com/go-kit/kit/endpoint"
    "github.com/go-kit/kit/transport/http"
)

type StringService interface {
    Uppercase(ctx context.Context, s string) (string, error)
    Count(ctx context.Context, s string) int
}

type stringService struct{}

func (s *stringService) Uppercase(ctx context.Context, str string) (string, error) {
    if str == "" {
        return "", fmt.Errorf("empty string")
    }
    return strings.ToUpper(str), nil
}

func (s *stringService) Count(ctx context.Context, str string) int {
    return len(str)
}

type uppercaseRequest struct {
    S string `json:"s"`
}

type uppercaseResponse struct {
    V   string `json:"v"`
    Err string `json:"err,omitempty"`
}

func makeUppercaseEndpoint(svc StringService) endpoint.Endpoint {
    return func(ctx context.Context, request interface{}) (interface{}, error) {
        req := request.(uppercaseRequest)
        v, err := svc.Uppercase(ctx, req.S)
        if err != nil {
            return uppercaseResponse{Err: err.Error()}, nil
        }
        return uppercaseResponse{V: v}, nil
    }
}
```

## Examples

```go
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    "strings"

    kithttp "github.com/go-kit/kit/transport/http"
)

type StringService interface {
    Uppercase(ctx context.Context, s string) (string, error)
}

func main() {
    svc := &stringService{}
    uppercaseHandler := kithttp.NewServer(
        makeUppercaseEndpoint(svc),
        decodeUppercaseRequest,
        encodeResponse,
    )

    http.Handle("/uppercase", uppercaseHandler)
    log.Println("Server listening on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func decodeUppercaseRequest(_ context.Context, r *http.Request) (interface{}, error) {
    var req uppercaseRequest
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        return nil, err
    }
    return req, nil
}

func encodeResponse(_ context.Context, w http.ResponseWriter, response interface{}) error {
    return json.NewEncoder(w).Encode(response)
}
```

## Related Errors

- [go-go-micro-error]({{< relref "/languages/go/go-go-micro-error" >}}) — similar microservice framework issues
- [grpc-status]({{< relref "/languages/go/grpc-status" >}}) — gRPC status codes in endpoints
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — endpoint request decode failures
