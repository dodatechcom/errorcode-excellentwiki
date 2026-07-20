---
title: "[Solution] OpenAPI Validation Error Fix"
description: "Fix Go OpenAPI validation errors. Handle request/response validation, schema mismatches, and format errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# OpenAPI Validation Error

The OpenAPI/Swagger validation in Go fails when request bodies do not match the schema, required fields are missing, enum values are invalid, or the response does not conform to the documented contract. OpenAPI validators enforce API contracts at runtime.

## Common Causes

```go
// Cause 1: Required field missing in request body
// OpenAPI schema requires "name" field
// JSON: {"email": "a@b.com"}
// validation error: name is required

// Cause 2: Type mismatch
// Schema: age: integer
// JSON: {"age": "twenty"}
// validation error: age must be integer

// Cause 3: Enum value not in allowed list
// Schema: status: ["active", "inactive"]
// JSON: {"status": "pending"}
// validation error: status must be one of: active, inactive

// Cause 4: String format violation
// Schema: email: format: email
// JSON: {"email": "not-an-email"}
// validation error: email must match format

// Cause 5: Response schema mismatch
// Server returns extra fields not in schema
// validation error: unexpected field "internal_id"
```

## How to Fix

### Fix 1: Validate requests against OpenAPI schema

```go
import (
    "fmt"
    "github.com/getkin/kin-openapi/openapi3filter"
)

func validateRequest(r *http.Request) error {
    router, _ := openapi3filter.NewRouter().WithSwaggerFromFile("openapi.yaml")

    input := &openapi3filter.RequestValidationInput{
        Request:    r,
        PathParams: extractPathParams(r),
        Router:     router,
    }

    if err := openapi3filter.ValidateRequest(context.Background(), input); err != nil {
        return fmt.Errorf("validation error: %w", err)
    }
    return nil
}
```

### Fix 2: Use middleware for automatic validation

```go
func OpenAPIMiddleware(router *openapi3filter.Router) func(http.Handler) http.Handler {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            input := &openapi3filter.RequestValidationInput{
                Request: r,
                Router:  router,
            }
            if err := openapi3filter.ValidateRequest(r.Context(), input); err != nil {
                http.Error(w, err.Error(), http.StatusBadRequest)
                return
            }
            next.ServeHTTP(w, r)
        })
    }
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "log"
    "net/http"

    "github.com/getkin/kin-openapi/openapi3"
    "github.com/getkin/kin-openapi/openapi3filter"
    "github.com/gorilla/mux"
)

func main() {
    loader := openapi3.NewLoader()
    doc, err := loader.LoadFromFile("openapi.yaml")
    if err != nil {
        log.Fatal(err)
    }

    router := mux.NewRouter()
    router.HandleFunc("/users", createUser).Methods("POST")

    log.Println("Server listening on :8080")
    log.Fatal(http.ListenAndServe(":8080", router))
}

func createUser(w http.ResponseWriter, r *http.Request) {
    // Process validated request
    fmt.Fprintln(w, "user created")
}
```

## Related Errors

- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — JSON parsing before validation
- [http-status-400]({{< relref "/languages/go/http-status-404" >}}) — validation returns 400 Bad Request
- [go-protobuf-error]({{< relref "/languages/go/go-protobuf-error" >}}) — protobuf schema validation
