---
title: "[Solution] HTTP 401 Unauthorized Fix"
description: "Fix Go HTTP 401 unauthorized errors. Handle authentication failures, missing credentials, and token validation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP 401 Unauthorized

A Go HTTP server returns 401 when the client fails to provide valid credentials or the authentication token is missing, expired, or malformed. In Go's `net/http` server, this is typically returned by authentication middleware that checks `Authorization` headers, cookies, or API keys.

## Common Causes

```go
// Cause 1: Missing Authorization header
func authMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        token := r.Header.Get("Authorization")
        if token == "" {
            http.Error(w, "unauthorized", http.StatusUnauthorized)
            return
        }
        next.ServeHTTP(w, r)
    })
}

// Cause 2: Expired JWT token
token, err := jwt.Parse(tokenString, func(t *jwt.Token) (interface{}, error) {
    return signingKey, nil
})
// token is expired — validation fails silently

// Cause 3: Wrong authentication scheme
// Client sends: Authorization: Basic xxx
// Server expects: Authorization: Bearer xxx

// Cause 4: Cookie-based auth with missing or expired cookie
cookie, err := r.Cookie("session")
if err != nil { // http.ErrNoCookie
    http.Error(w, "unauthorized", http.StatusUnauthorized)
}

// Cause 5: API key not in expected header or query param
apiKey := r.URL.Query().Get("api_key")
// Client sends it in X-API-Key header instead
```

## How to Fix

### Fix 1: Implement proper auth middleware with token extraction

```go
import (
    "context"
    "net/http"
    "strings"
)

type contextKey string
const userIDKey contextKey = "userID"

func AuthMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        authHeader := r.Header.Get("Authorization")
        if authHeader == "" {
            http.Error(w, `{"error":"missing Authorization header"}`, http.StatusUnauthorized)
            return
        }

        parts := strings.SplitN(authHeader, " ", 2)
        if len(parts) != 2 || parts[0] != "Bearer" {
            http.Error(w, `{"error":"invalid Authorization format"}`, http.StatusUnauthorized)
            return
        }

        userID, err := validateToken(parts[1])
        if err != nil {
            http.Error(w, `{"error":"invalid token"}`, http.StatusUnauthorized)
            return
        }

        ctx := context.WithValue(r.Context(), userIDKey, userID)
        next.ServeHTTP(w, r.WithContext(ctx))
    })
}
```

### Fix 2: Use secure cookie-based sessions

```go
import "net/http"

func setSessionCookie(w http.ResponseWriter, sessionID string) {
    http.SetCookie(w, &http.Cookie{
        Name:     "session",
        Value:    sessionID,
        Path:     "/",
        HttpOnly: true,
        Secure:   true,
        SameSite: http.SameSiteStrictMode,
        MaxAge:   3600,
    })
}

func getSessionUser(r *http.Request) (string, error) {
    cookie, err := r.Cookie("session")
    if err != nil {
        return "", err
    }
    return validateSessionID(cookie.Value)
}
```

### Fix 3: Return proper 401 response with WWW-Authenticate header

```go
func unauthorizedHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("WWW-Authenticate", `Bearer realm="api", error="invalid_token"`)
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusUnauthorized)
    w.Write([]byte(`{"error":"authentication required"}`))
}
```

## Examples

```go
package main

import (
    "fmt"
    "net/http"
    "strings"
)

func main() {
    mux := http.NewServeMux()
    mux.Handle("/protected", AuthMiddleware(http.HandlerFunc(protectedHandler)))
    mux.HandleFunc("/login", loginHandler)

    http.ListenAndServe(":8080", mux)
}

func AuthMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        token := r.Header.Get("Authorization")
        if !strings.HasPrefix(token, "Bearer ") {
            http.Error(w, "unauthorized", http.StatusUnauthorized)
            return
        }
        if token[7:] != "valid-token" {
            http.Error(w, "invalid token", http.StatusUnauthorized)
            return
        }
        next.ServeHTTP(w, r)
    })
}

func protectedHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Welcome to protected area!")
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, `{"token":"valid-token"}`)
}
```

## Related Errors

- [go-jwt-error]({{< relref "/languages/go/go-jwt-error" >}}) — JWT token validation failures
- [go-oauth-error]({{< relref "/languages/go/go-oauth-error" >}}) — OAuth2 token exchange errors
- [go-vault-error]({{< relref "/languages/go/go-vault-error" >}}) — Vault authentication failures
