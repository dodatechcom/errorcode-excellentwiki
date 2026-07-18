---
title: "[Solution] Go Environment Variable Error — How to Fix"
description: "Fix Go environment variable errors. Handle missing vars, type conversion, defaults, validation, and multi-environment configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Environment Variable Error

Fix Go environment variable errors. Handle missing vars, type conversion, defaults, validation, and multi-environment configuration.

## Why It Happens

- os.Getenv returns an empty string when the variable is not set causing silent failures
- Type conversion from string to int or bool fails without validation
- Required environment variables are not checked at startup causing runtime panics
- Different environments use different variable naming conventions

## Common Error Messages

```
strconv.Atoi: parsing "": invalid syntax
```
```
environment variable <NAME> not set
```
```
panic: runtime error: index out of range
```
```
invalid value for environment variable
```

## How to Fix It

### Solution 1: Parse environment variables with validation

```go
func GetEnvInt(key string, defaultVal int) (int, error) {
    val := os.Getenv(key)
    if val == "" { return defaultVal, nil }
    result, err := strconv.Atoi(val)
    if err != nil { return 0, fmt.Errorf("env %s: invalid int: %w", key, err) }
    return result, nil
}
```

### Solution 2: Use a config struct with defaults

```go
type EnvConfig struct {
    Port        int    `env:"PORT" envDefault:"8080"`
    DatabaseURL string `env:"DATABASE_URL"`
    Debug       bool   `env:"DEBUG" envDefault:"false"`
}
```

### Solution 3: Validate all env vars at startup

```go
func ValidateEnv() error {
    required := []string{"DATABASE_URL", "JWT_SECRET"}
    var missing []string
    for _, key := range required {
        if os.Getenv(key) == "" { missing = append(missing, key) }
    }
    if len(missing) > 0 {
        return fmt.Errorf("missing env vars: %s", strings.Join(missing, ", "))
    }
    return nil
}
```

### Solution 4: Handle environment-specific overrides

```go
cfg := &Config{Port: 8080}
if port := os.Getenv("PORT"); port != "" {
    p, err := strconv.Atoi(port)
    if err != nil { return nil, err }
    cfg.Port = p
}
```

## Common Scenarios

- An application starts but fails at runtime because DATABASE_URL is not set
- strconv.Atoi panics because PORT is set to a non-numeric value
- Debug mode is accidentally enabled in production because DEBUG=true is set

## Prevent It

- Always validate environment variables at startup and fail fast on missing required vars
- Use os.LookupEnv to distinguish between a variable being set to empty vs not being set
- Provide sensible defaults for optional environment variables to reduce configuration burden
