---
title: "[Solution] HTTP 502 Bad Gateway in Go Fix"
description: "Fix HTTP 502 Bad Gateway errors in Go applications. Handle upstream failures, proxy misconfigurations, and connection resets."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP 502: Bad Gateway in Go

This error occurs when a Go application acting as a gateway or proxy receives an invalid response from an upstream server, or when the upstream server is unreachable.

## What This Error Means

Common error messages:

- `502 Bad Gateway`
- `upstream connect error or disconnect/reset before headers`
- `connection reset by peer`
- `invalid HTTP response from upstream`

A 502 means the intermediary (reverse proxy, load balancer, or Go gateway) received an invalid, incomplete, or no response from the backend server it connected to.

## Common Causes

```go
// Cause 1: Upstream server crashed mid-request
// Backend process killed or panicked

// Cause 2: Upstream closed connection prematurely
// Server writes partial response then closes

// Cause 3: Mismatched HTTP versions
// Upstream speaks HTTP/1.0, gateway expects HTTP/1.1

// Cause 4: Upstream returned malformed response
// Broken headers, invalid Transfer-Encoding

// Cause 5: Load balancer target unreachable
// Backend container stopped or port changed
```

## How to Fix

### Fix 1: Add upstream health checks

```go
func isUpstreamHealthy(url string) bool {
    client := &http.Client{Timeout: 2 * time.Second}
    resp, err := client.Get(url + "/health")
    if err != nil {
        return false
    }
    defer resp.Body.Close()
    return resp.StatusCode == 200
}
```

### Fix 2: Use proper error handling with retries

```go
func proxyRequest(w http.ResponseWriter, r *http.Request) {
    var resp *http.Response
    var err error

    for i := 0; i < 3; i++ {
        resp, err = http.DefaultTransport.RoundTrip(r)
        if err == nil && resp.StatusCode < 502 {
            break
        }
        if resp != nil {
            resp.Body.Close()
        }
        time.Sleep(time.Duration(i+1) * 100 * time.Millisecond)
    }

    if err != nil || (resp != nil && resp.StatusCode >= 502) {
        http.Error(w, "Bad Gateway", 502)
        return
    }
    defer resp.Body.Close()

    for key, values := range resp.Header {
        for _, value := range values {
            w.Header().Add(key, value)
        }
    }
    w.WriteHeader(resp.StatusCode)
    io.Copy(w, resp.Body)
}
```

### Fix 3: Use reverse proxy with timeout configuration

```go
proxy := &httputil.ReverseProxy{
    Director: func(req *http.Request) {
        req.URL.Scheme = "http"
        req.URL.Host = "upstream-service:8080"
    },
    Transport: &http.Transport{
        ResponseHeaderTimeout: 10 * time.Second,
        IdleConnTimeout:       90 * time.Second,
        MaxIdleConns:          100,
    },
    ErrorHandler: func(w http.ResponseWriter, r *http.Request, err error) {
        log.Printf("Proxy error: %v", err)
        http.Error(w, "Bad Gateway", 502)
    },
}
```

### Fix 4: Validate upstream response

```go
func validateResponse(resp *http.Response) error {
    if resp == nil {
        return fmt.Errorf("nil response from upstream")
    }
    if resp.StatusCode >= 500 {
        body, _ := io.ReadAll(io.LimitReader(resp.Body, 1024))
        return fmt.Errorf("upstream error %d: %s", resp.StatusCode, string(body))
    }
    return nil
}
```

## Examples

```bash
$ curl -v http://localhost:8080/api/data
< HTTP/1.1 502 Bad Gateway
< Content-Type: text/plain
Bad Gateway
```

```go
// Fix: log the upstream error for debugging
func gatewayHandler(w http.ResponseWriter, r *http.Request) {
    resp, err := proxyRequest(r)
    if err != nil {
        log.Printf("upstream error: %v, url: %s", err, r.URL.Path)
        http.Error(w, "Bad Gateway", 502)
        return
    }
    defer resp.Body.Close()
    io.Copy(w, resp.Body)
}
```

## Related Errors

- [http-status-503]({{< relref "/languages/go/http-status-503" >}}) — service unavailable
- [go-http-timeout-v2]({{< relref "/languages/go/go-http-timeout-v2" >}}) — context deadline exceeded
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP timeout
