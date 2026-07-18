---
title: "[Solution] Go JSON Encoder Error — How to Fix"
description: "Fix Go JSON encoder errors. Handle encoding failures, circular references, special types, stream encoding, and buffer overflow issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go JSON Encoder Error

Fix Go JSON encoder errors. Handle encoding failures, circular references, special types, stream encoding, and buffer overflow issues.

## Why It Happens

- A struct contains circular references causing the encoder to recurse infinitely
- A channel, func, or complex type is passed to the encoder which cannot serialize it
- The encoder writes to a closed writer causing a broken pipe error
- Large payloads cause memory allocation failures during encoding

## Common Error Messages

```
json: unsupported type: chan int
```
```
json: unsupported type: func()
```
```
json: error calling json.Marshaler.MarshalJSON
```
```
write: broken pipe
```

## How to Fix It

### Solution 1: Handle unsupported types before encoding

```go
func validateType(v interface{}) error {
    val := reflect.ValueOf(v)
    switch val.Kind() {
    case reflect.Chan, reflect.Func, reflect.UnsafePointer:
        return fmt.Errorf("unsupported type: %T", v)
    case reflect.Ptr:
        if val.IsNil() { return nil }
        return validateType(val.Elem().Interface())
    }
    return nil
}
```

### Solution 2: Implement custom MarshalJSON for complex types

```go
type Timestamp struct{ time.Time }
func (t Timestamp) MarshalJSON() ([]byte, error) {
    if t.IsZero() { return []byte("null"), nil }
    return []byte(fmt.Sprintf(`"%s"`, t.Format(time.RFC3339))), nil
}
```

### Solution 3: Stream encode large datasets efficiently

```go
func encodeLargeDataset(w io.Writer, records []Record) error {
    encoder := json.NewEncoder(w)
    w.Write([]byte("[\n"))
    for i, r := range records {
        encoder.Encode(r)
        if i < len(records)-1 { w.Write([]byte(",\n")) }
    }
    w.Write([]byte("\n]"))
    return nil
}
```

### Solution 4: Use json.RawMessage for pre-encoded data

```go
type Event struct {
    ID      string          `json:"id"`
    Payload json.RawMessage `json:"payload"`
}
```

## Common Scenarios

- An API response fails to encode because a struct contains a channel field
- A large JSON payload causes an out-of-memory error because everything is buffered in memory
- A JSON response contains unescaped HTML characters breaking the frontend parser

## Prevent It

- Always check for unsupported types (channels, functions, unsafe pointers) before encoding
- Use json:"-" tag on fields that should never be serialized
- Use streaming json.Encoder for large payloads instead of json.Marshal
