---
title: "[Solution] Deprecated Function Migration: http.Get to http.Client with context"
description: "Migrate from deprecated http.Get to http.Client with context."
deprecated_function: "http.Get(url)"
replacement_function: "http.Client with context"
languages: ["go"]
deprecated_since: "Go 1.13+"
---

# [Solution] Deprecated Function Migration: http.Get to http.Client with context

The `http.Get(url)` has been deprecated in favor of `http.Client with context`.

## Migration Guide

Client provides timeout and context support.

## Before (Deprecated)

```go
resp, err := http.Get(url)
if err != nil { log.Fatal(err) }
```

## After (Modern)

```go
client := &http.Client{Timeout: 10 * time.Second}
req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
resp, err := client.Do(req)
```

## Key Differences

- Client provides timeout
