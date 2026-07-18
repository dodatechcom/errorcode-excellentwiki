---
title: "[Solution] Go Logrus Error — How to Fix"
description: "Fix Go Logrus errors. Handle logger configuration, hooks, formatters, and output destinations."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Logrus Error

Fix Go Logrus errors. Handle logger configuration, hooks, formatters, and output destinations.

## Why It Happens

- Logrus logger is not configured with correct output causing logs to go to wrong destination
- Custom hook does not implement the correct interface
- Logrus formatter is not set causing logs to be in wrong format
- Logrus entries are not being flushed causing lost logs

## Common Error Messages

```
logrus: invalid log level
```
```
logrus: hook failed
```
```
logrus: formatter not set
```
```
logrus: output not configured
```

## How to Fix It

### Solution 1: Configure Logrus

```go
log.SetLevel(log.InfoLevel)
log.SetFormatter(&log.JSONFormatter{})
log.SetOutput(os.Stdout)

// Or use with context
logger := log.WithFields(log.Fields{
    "service": "myapp",
    "version": "1.0.0",
})
logger.Info("application started")
```

### Solution 2: Add hooks

```go
type SentryHook struct{}
func (h *SentryHook) Levels() []log.Level { return log.AllLevels }
func (h *SentryHook) Fire(entry *log.Entry) error {
    sentry.CaptureMessage(entry.Message)
    return nil
}
log.AddHook(&SentryHook{})
```

### Solution 3: Use structured logging

```go
log.WithFields(log.Fields{
    "user": "alice",
    "action": "login",
}).Info("user logged in")
```

### Solution 4: Set output

```go
// Write to file
f, _ := os.OpenFile("app.log", os.O_CREATE|os.O_WRONLY, 0644)
log.SetOutput(f)
// Write to both stdout and file
mw := io.MultiWriter(os.Stdout, f)
log.SetOutput(mw)
```

## Common Scenarios

- Logrus output is not visible because output is not configured
- Custom formatter does not produce the expected log format
- Hooks are not executed because they are registered after the logger is used

## Prevent It

- Set log output explicitly with log.SetOutput
- Use WithFields for structured logging instead of Printf
- ['Add hooks before using the logger', '```go\nlog.AddHook(&MyHook{})\nlog.Info("this will trigger the hook")\n```']
