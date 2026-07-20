---
title: "[Solution] HTTP 429 Too Many Requests Fix"
description: "Fix Go HTTP 429 too many requests errors. Handle rate limiting, backoff strategies, and request throttling."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP 429 Too Many Requests

A Go HTTP server returns 429 when the client exceeds the rate limit. This commonly happens with API endpoints, login attempts, or external service calls. Proper rate limiting requires tracking request counts per client and returning `Retry-After` headers.

## Common Causes

```go
// Cause 1: No rate limiting configured
// Server receives burst traffic, no protection
// Clients get 503 or 429 from load balancer

// Cause 2: Rate limiter too aggressive
limiter := rate.NewLimiter(rate.Limit(1), 1) // 1 req/sec, burst 1
// legitimate requests get rejected

// Cause 3: Retry-After header not sent
// Client does not know when to retry
// 429 without Retry-After is unhelpful

// Cause 4: Rate limit by wrong key
// Rate limiting by IP when clients share IP (NAT)
// all clients behind same IP share one limit

// Cause 5: No per-endpoint rate limiting
// Same limit for /login and /api/data
```

## How to Fix

### Fix 1: Implement rate limiting middleware

```go
import (
    "net/http"
    "sync"
    "time"

    "golang.org/x/time/rate"
)

type RateLimiter struct {
    visitors map[string]*rate.Limiter
    mu       sync.Mutex
    rate     rate.Limit
    burst    int
}

func NewRateLimiter(rps float64, burst int) *RateLimiter {
    return &RateLimiter{
        visitors: make(map[string]*rate.Limiter),
        rate:     rate.Limit(rps),
        burst:    burst,
    }
}

func (rl *RateLimiter) getLimiter(ip string) *rate.Limiter {
    rl.mu.Lock()
    defer rl.mu.Unlock()

    limiter, exists := rl.visitors[ip]
    if !exists {
        limiter = rate.NewLimiter(rl.rate, rl.burst)
        rl.visitors[ip] = limiter
    }
    return limiter
}

func (rl *RateLimiter) Middleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        limiter := rl.getLimiter(r.RemoteAddr)
        if !limiter.Allow() {
            w.Header().Set("Retry-After", "60")
            http.Error(w, "rate limit exceeded", http.StatusTooManyRequests)
            return
        }
        next.ServeHTTP(w, r)
    })
}
```

### Fix 2: Use token bucket per-client

```go
func main() {
    limiter := NewRateLimiter(10, 20) // 10 req/s, burst 20
    http.Handle("/", limiter.Middleware(handler))
    http.ListenAndServe(":8080", nil)
}
```

### Fix 3: Return proper 429 response with headers

```go
func rateLimitedResponse(w http.ResponseWriter) {
    w.Header().Set("Content-Type", "application/json")
    w.Header().Set("Retry-After", "30")
    w.Header().Set("X-RateLimit-Limit", "100")
    w.Header().Set("X-RateLimit-Remaining", "0")
    w.Header().Set("X-RateLimit-Reset", fmt.Sprintf("%d", time.Now().Add(30*time.Second).Unix()))
    w.WriteHeader(http.StatusTooManyRequests)
    w.Write([]byte(`{"error":"rate limit exceeded","retry_after":30}`))
}
```

## Examples

```go
package main

import (
    "net/http"
    "sync"
    "time"

    "golang.org/x/time/rate"
)

func main() {
    limiter := rate.NewLimiter(rate.Every(100*time.Millisecond), 10) // 10 req/s

    http.HandleFunc("/api", func(w http.ResponseWriter, r *http.Request) {
        if !limiter.Allow() {
            w.Header().Set("Retry-After", "1")
            http.Error(w, "too many requests", http.StatusTooManyRequests)
            return
        }
        w.Write([]byte("ok"))
    })

    http.ListenAndServe(":8080", nil)
}
```

## Related Errors

- [http-status-401]({{< relref "/languages/go/http-status-401" >}}) — authentication required
- [http-status-500]({{< relref "/languages/go/http-status-500" >}}) — server overload
- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — client timeout during retry
