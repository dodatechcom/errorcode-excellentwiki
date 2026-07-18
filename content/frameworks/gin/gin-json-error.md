---
title: "[Solution] Gin JSON Error — How to Fix"
description: "Fix Gin JSON serialization errors. Resolve JSON encoding, decoding, and response formatting issues."
frameworks: ["gin"]
error-types: ["response-error"]
severities: ["error"]
weight: 5
comments: true
---

A Gin JSON error occurs when the framework encounters problems serializing or deserializing JSON data.

## Why It Happens

JSON errors happen due to invalid struct tags, unmarshalable types (channels, functions), circular references, or encoding issues.

## Common Error Messages

```
json: unsupported type
```

```
json: invalid UTF-8
```

```
json: invalid character
```

```
cannot unmarshal number into Go value of type
```

## How to Fix It

### 1. Check Struct Tags

Ensure struct fields have proper json tags.

```go
type Response struct {
    Data  interface{} `json:"data"`
    Error string      `json:"error,omitempty"`
    Count int         `json:"count"`
}
```

### 2. Handle Unmarshalable Types

Avoid or convert unsupported types.

```go
type Response struct {
    Timestamp time.Time `json:"timestamp"`
    Status    string    `json:"status"`
    // Don't use channels or functions here
}
```

### 3. Use MarshalJSON

Implement custom marshaling.

```go
type CustomTime struct {
    time.Time
}

func (t CustomTime) MarshalJSON() ([]byte, error) {
    return []byte(fmt.Sprintf(""%s"", t.Format("2006-01-02"))), nil
}
```

### 4. Check for UTF-8 Issues

Validate input data.

```go
if !utf8.Valid(inputData) {
    c.JSON(400, gin.H{"error": "invalid UTF-8"})
    return
}
```

## Common Scenarios

**Scenario 1: JSON response missing fields.**
Check json tags on struct.

**Scenario 2: Cannot marshal function type.**
Remove functions from JSON-serialized structs.

**Scenario 3: Garbled JSON output.**
Check for UTF-8 encoding issues.

## Prevent It

1. **Test JSON serialization regularly.**


2. **Use omitempty for optional fields.**


3. **Validate data before serialization.**


