---
title: "[Solution] Deprecated Function Migration: http.ListenAndServe to graceful shutdown"
description: "Migrate from deprecated http.ListenAndServe to graceful shutdown."
deprecated_function: "http.ListenAndServe()"
replacement_function: "server.ListenAndServe with context"
languages: ["go"]
deprecated_since: "Go 1.8+"
---

# [Solution] Deprecated Function Migration: http.ListenAndServe to graceful shutdown

The `http.ListenAndServe(":8080", nil)` has been deprecated in favor of `server.ListenAndServe with context`.

## Migration Guide

Graceful shutdown handles SIGTERM.

## Before (Deprecated)

```go
log.Fatal(http.ListenAndServe(":8080", nil))
```

## After (Modern)

```go
server := &http.Server{Addr: ":8080"}
go func() {
    sigChan := make(chan os.Signal, 1)
    signal.Notify(sigChan, syscall.SIGTERM)
    <-sigChan
    server.Shutdown(context.Background())
}()
log.Fatal(server.ListenAndServe())
```

## Key Differences

- Graceful shutdown handles SIGTERM
