---
title: "[Solution] Go Zerolog Error — How to Fix"
description: "Fix Go Zerolog errors. Handle logger setup, structured fields, sub-loggers, and output configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Zerolog Error

Fix Go Zerolog errors. Handle logger setup, structured fields, sub-loggers, and output configuration.

## Why It Happens

- Zerolog logger writes to wrong output causing log entries to be lost
- Sub-loggers add fields that are not present in parent logger
- Log level is not configured correctly causing all logs to be printed
- Zerolog context is not properly passed between goroutines

## Common Error Messages

```
zerolog: invalid log level
```
```
zerolog: output not configured
```
```
zerolog: field type mismatch
```
```
zerolog: logger already initialized
```

## How to Fix It

### Solution 1: Initialize zerolog

```go
// Console output for development
logger := zerolog.New(zerolog.ConsoleWriter{Out: os.Stderr}).With().Timestamp().Logger()

// JSON output for production
logger := zerolog.New(os.Stdout).With().Timestamp().Logger()

// Global logger
zerolog.SetGlobalLevel(zerolog.InfoLevel)
```

### Solution 2: Use structured fields

```go
logger.Info().Str("user", "alice").Int("count", 42).Msg("user logged in")
logger.Error().Err(err).Str("component", "db").Msg("connection failed")
```

### Solution 3: Create sub-loggers

```go
subLogger := logger.With().Str("component", "auth").Logger()
subLogger.Info().Msg("authentication successful")
```

### Solution 4: Pass logger in context

```go
ctx := logger.WithContext(ctx)
// Retrieve later
logger := zerolog.Ctx(ctx)
logger.Info().Msg("using context logger")
```

## Common Scenarios

- Zerolog logger produces no output because output was not configured
- Fields are missing from log entries because the sub-logger was not used
- Log level filtering is not working because SetGlobalLevel was not called

## Prevent It

- Always configure zerolog output (os.Stdout or os.Stderr)
- Use sub-loggers to add component-specific fields
- Set log level with zerolog.SetGlobalLevel at startup
