---
title: "[Solution] Go HTTP Client Error — How to Fix"
description: "Fix Go net/http client errors. Handle connection pooling, timeouts, redirect policies, TLS verification, and response body management."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go HTTP Client Error

Fix Go net/http client errors. Handle connection pooling, timeouts, redirect policies, TLS verification, and response body management.

## Why It Happens

- The HTTP client has no timeouts configured causing requests to hang indefinitely
- Response bodies are not closed after use causing connection pool exhaustion
- The default redirect policy follows too many redirects in infinite loops
- TLS certificate verification fails in development with self-signed certs

## Common Error Messages

```
Get <url>: context deadline exceeded (Client.Timeout exceeded)
```
```
Get <url>: dial tcp: lookup: no such host
```
```
Get <url>: x509: certificate signed by unknown authority
```
```
http: superfluous response.WriteHeader call
```

## How to Fix It

### Solution 1: Configure HTTP client with proper timeouts

```go
client := &http.Client{
    Timeout: 30 * time.Second,
    Transport: &http.Transport{
        MaxIdleConns: 100, MaxIdleConnsPerHost: 10,
        IdleConnTimeout: 90 * time.Second,
    },
}
```

### Solution 2: Always close and drain response bodies

```go
resp, err := client.Get(url)
if err != nil { return err }
defer resp.Body.Close()
defer io.Copy(io.Discard, resp.Body)
body, err := io.ReadAll(resp.Body)
```

### Solution 3: Customize redirect policy

```go
client := &http.Client{
    CheckRedirect: func(req *http.Request, via []*http.Request) error {
        if len(via) >= 5 { return fmt.Errorf("too many redirects") }
        return nil
    },
}
```

### Solution 4: Skip TLS verification for development only

```go
transport := &http.Transport{
    TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
}
client := &http.Client{Transport: transport}
```

## Common Scenarios

- A microservice exhausts its connection pool because response bodies are never closed
- An HTTP client hangs forever because no timeout is set
- An API client fails with TLS error due to self-signed certificate

## Prevent It

- Always defer resp.Body.Close() and drain with io.Copy(io.Discard, resp.Body)
- Set client.Timeout for overall deadline and Transport timeouts for connection limits
- Create a reusable http.Client with a configured Transport rather than using http.DefaultClient
