---
title: "[Solution] Go JSON Marshal Error — How to Fix"
description: "Fix Go JSON marshal errors. Handle unsupported types, circular references, encoding precision, nil pointers, and custom serializers."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go JSON Marshal Error

Fix Go JSON marshal errors. Handle unsupported types, circular references, encoding precision, nil pointers, and custom serializers.

## Why It Happens

- A struct contains a field with a type that json.Marshal cannot serialize such as channels or funcs
- A struct contains a circular reference causing infinite recursion during marshaling
- Float64 precision is lost during JSON encoding because of default formatting
- A nil pointer field causes a panic when the encoder tries to access its value

## Common Error Messages

```
json: unsupported type: chan int
```
```
json: unsupported type: func()
```
```
json: error calling MarshalJSON
```
```
json: unsupported value: NaN or Infinity
```

## How to Fix It

### Solution 1: Handle all unsupported types before marshaling

```go
func safeMarshal(v interface{}) ([]byte, error) {
    data, err := json.Marshal(v)
    if err != nil && strings.Contains(err.Error(), "unsupported type") {
        return marshalSafe(v)
    }
    return data, err
}
```

### Solution 2: Use json.Number for precise number handling

```go
type Amount struct {
    Value    json.Number `json:"value"`
    Currency string      `json:"currency"`
}
```

### Solution 3: Implement json.Marshaler for custom serialization

```go
type Coordinate struct{ Lat, Lng float64 }
func (c Coordinate) MarshalJSON() ([]byte, error) {
    return json.Marshal(fmt.Sprintf("%.6f,%.6f", c.Lat, c.Lng))
}
```

### Solution 4: Handle circular references with pointer tracking

```go
type Node struct {
    Name     string  `json:"name"`
    Children []*Node `json:"children,omitempty"`
    Parent   *Node   `json:"-"`
}
```

## Common Scenarios

- A struct with sync.Mutex fails to marshal because mutex cannot be serialized
- A float64 with NaN value causes json.Marshal to return an error breaking the API response
- A circular pointer reference between parent and child nodes causes a stack overflow during marshaling

## Prevent It

- Always check for unsupported types (channels, functions, unsafe pointers) before passing to json.Marshal
- Use the json:"-" tag on fields that should never be serialized such as internal state
- Replace NaN and Infinity float values with null or zero before marshaling to prevent encoding errors
