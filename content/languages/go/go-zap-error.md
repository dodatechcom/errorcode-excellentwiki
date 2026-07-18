---
title: "[Solution] Go Zap Error — How to Fix"
description: "Fix Go Zap errors. Handle logger initialization, structured logging, encoding, and level configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Zap Error

Fix Go Zap errors. Handle logger initialization, structured logging, encoding, and level configuration.

## Why It Happens

- Zap logger is not initialized causing nil pointer dereference
- Sugar and logger APIs are mixed causing inconsistent output
- Log encoding is wrong (JSON vs console) causing parsing failures
- Logger is not synced causing lost log entries

## Common Error Messages

```
zap: logger is nil
```
```
zap: invalid log level
```
```
zap: encoder not configured
```
```
zap: logger must be synchronized
```

## How to Fix It

### Solution 1: Initialize Zap logger

```go
logger, _ := zap.NewProduction()
defer logger.Sync()

// Or use sugar for printf-style logging
sugar := logger.Sugar()
sugar.Infof("user %s logged in", username)

// Or use structured logger
logger.Info("user logged in",
    zap.String("user", username),
    zap.Int("attempts", 3),
)
```

### Solution 2: Configure log levels

```go
level := zap.NewAtomicLevelAt(zap.InfoLevel)
config := zap.Config{
    Level: level,
    Encoding: "json",
    OutputPaths: []string{"stdout"},
}
logger, _ := config.Build()
```

### Solution 3: Use with HTTP middleware

```go
func ZapMiddleware(logger *zap.Logger) gin.HandlerFunc {
    return func(c *gin.Context) {
        start := time.Now()
        c.Next()
        logger.Info("request",
            zap.String("method", c.Request.Method),
            zap.String("path", c.Request.URL.Path),
            zap.Duration("latency", time.Since(start)),
        )
    }
}
```

### Solution 4: Sync logger on shutdown

```go
logger, _ := zap.NewProduction()
defer logger.Sync()
// Or for os.Stderr
os.Stdout.Sync()
```

## Common Scenarios

- Zap logger panics because it was not initialized
- Log output is not formatted as expected (JSON vs plain text)
- Log entries are lost because the logger is not synced

## Prevent It

- Always call logger.Sync() in a defer after initialization
- Use zap.Config to set encoding and output format
- Use NewProduction for JSON logging and NewDevelopment for debug
