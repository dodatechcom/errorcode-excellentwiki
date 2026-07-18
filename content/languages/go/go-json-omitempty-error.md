---
title: "[Solution] Go JSON omitempty Error — How to Fix"
description: "Fix Go JSON omitempty issues. Handle zero-value encoding, pointer fields, false booleans, empty slices, and custom zero values."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go JSON omitempty Error

Fix Go JSON omitempty issues. Handle zero-value encoding, pointer fields, false booleans, empty slices, and custom zero values.

## Why It Happens

- omitempty treats zero values (0, false, empty string) as absent from JSON output
- A pointer field with omitempty omits the field when the value is nil instead of zero
- An empty slice is omitted when you need to include it as an empty array in JSON
- Boolean fields set to false are omitted because false is the zero value for bool

## Common Error Messages

```
json: omitempty on zero value: field always omitted when false
```
```
json: field unexpectedly omitted from response
```
```
json: expected object but got null for field
```
```
json: empty array omitted when null expected
```

## How to Fix It

### Solution 1: Use pointers for fields where nil vs zero matters

```go
type Config struct {
    Debug *bool   `json:"debug,omitempty"`
    Count *int    `json:"count,omitempty"`
}
debug := false
cfg := Config{Debug: &debug} // output: {"debug": false}
cfg2 := Config{} // output: {}
```

### Solution 2: Use json.RawMessage to force empty arrays

```go
type Response struct {
    Items json.RawMessage `json:"items"`
}
resp := Response{Items: json.RawMessage("[]")} // always includes empty array
```

### Solution 3: Implement custom MarshalJSON for non-zero semantics

```go
type User struct {
    Name  string `json:"name"`
    Bio   string `json:"bio"` // No omitempty - always included
    Email string `json:"email,omitempty"`
}
```

### Solution 4: Handle omitempty with custom types

```go
type NonZeroTime struct{ time.Time }
func (t NonZeroTime) MarshalJSON() ([]byte, error) {
    if t.IsZero() { return []byte(`"0001-01-01T00:00:00Z"`), nil }
    return json.Marshal(t.Time.Format(time.RFC3339))
}
```

## Common Scenarios

- A boolean field set to false is missing from the JSON response because omitempty treats false as zero
- An empty array is omitted from the JSON output but the client expects an empty array instead of null
- A zero-value timestamp is omitted from the response but the API contract requires it always be present

## Prevent It

- Use pointer types (*bool, *int, *string) when you need to distinguish between absent and zero-value fields
- Avoid omitempty on boolean fields if false is a valid and meaningful value in your API
- Use json.RawMessage to force specific JSON representations like empty arrays or zero timestamps
