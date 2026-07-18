---
title: "[Solution] Go HTTP Redirect Error — How to Fix"
description: "Fix Go HTTP redirect errors. Handle redirect policies, too many redirects, relative URLs, cross-origin redirects, and header preservation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go HTTP Redirect Error

Fix Go HTTP redirect errors. Handle redirect policies, too many redirects, relative URLs, cross-origin redirects, and header preservation.

## Why It Happens

- The default redirect policy follows unlimited redirects causing infinite loops
- Redirected requests lose custom headers or authentication tokens
- Relative redirect URLs are not resolved correctly by the HTTP client
- Cross-origin redirects fail because cookies or credentials are not forwarded

## Common Error Messages

```
Get <url>: stopped after 10 redirects
```
```
http: redirect failed: too many redirects
```
```
Get <url>: redirect loop detected
```
```
Post <url>: redirect with status 307/308 requires body re-send
```

## How to Fix It

### Solution 1: Implement custom redirect policy with limits

```go
client := &http.Client{
    CheckRedirect: func(req *http.Request, via []*http.Request) error {
        if len(via) >= 10 { return fmt.Errorf("stopped after %d redirects", len(via)) }
        if len(via) > 0 {
            origAuth := via[0].Header.Get("Authorization")
            if origAuth != "" { req.Header.Set("Authorization", origAuth) }
        }
        return nil
    },
}
```

### Solution 2: Handle POST redirects properly

```go
req, _ := http.NewRequest("POST", url, body)
req.Header.Set("Content-Type", "application/json")
resp, err := client.Do(req)
// For 307/308 Go re-sends body; for 301/302 it changes POST to GET
```

### Solution 3: Disable automatic redirects to handle manually

```go
client := &http.Client{
    CheckRedirect: func(req *http.Request, via []*http.Request) error {
        return http.ErrUseLastResponse
    },
}
resp, _ := client.Get(url)
if resp.StatusCode >= 300 && resp.StatusCode < 400 {
    location := resp.Header.Get("Location")
    resp2, _ := client.Get(location)
}
```

### Solution 4: Log and monitor redirect chains

```go
type RedirectLogger struct {
    mu     sync.Mutex
    chains map[string]int
}
func (rl *RedirectLogger) Track(original string, hops int) {
    rl.mu.Lock(); defer rl.mu.Unlock()
    rl.chains[original] = hops
    if hops > 5 { log.Printf("excessive redirects: %s: %d hops", original, hops) }
}
```

## Common Scenarios

- An HTTP client enters an infinite redirect loop when two URLs point to each other
- A POST request loses its body and headers after following a 301 redirect to GET
- A monitoring tool counts 15 redirects for a URL that should only redirect once

## Prevent It

- Always set a maximum redirect count in CheckRedirect to prevent infinite loops
- Use http.ErrUseLastResponse to disable automatic redirects when you need manual control
- Log redirect chains in production to detect misconfigured redirect rules early
