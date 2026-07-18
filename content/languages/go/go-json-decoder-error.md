---
title: "[Solution] Go JSON Decoder Error — How to Fix"
description: "Fix Go JSON decoder errors. Handle stream decoding, buffer management, type mismatches, and unknown field handling."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go JSON Decoder Error

Fix Go JSON decoder errors. Handle stream decoding, buffer management, type mismatches, and unknown field handling.

## Why It Happens

- The JSON decoder reads from a closed or empty reader causing unexpected EOF
- Type mismatches between JSON values and Go struct fields cause decode failures
- A single json.Decoder is reused across multiple requests without resetting
- DisallowUnknownFields is set but the JSON contains keys not in the target struct

## Common Error Messages

```
json: cannot unmarshal string into Go struct field
```
```
json: unexpected end of JSON input
```
```
json: invalid character looking for beginning of value
```
```
json: cannot unmarshal number into Go struct field of type string
```

## How to Fix It

### Solution 1: Use json.Decoder with proper error handling

```go
func decodeJSON(r io.Reader, v interface{}) error {
    decoder := json.NewDecoder(r)
    decoder.DisallowUnknownFields()
    if err := decoder.Decode(v); err != nil {
        var syntaxErr *json.SyntaxError
        var unmarshalErr *json.UnmarshalTypeError
        switch {
        case errors.As(err, &syntaxErr):
            return fmt.Errorf("syntax error at offset %d: %w", syntaxErr.Offset, err)
        case errors.As(err, &unmarshalErr):
            return fmt.Errorf("type mismatch for %s: %w", unmarshalErr.Field, err)
        }
        return err
    }
    return nil
}
```

### Solution 2: Handle streaming JSON decoding

```go
func decodeMultipleObjects(r io.Reader) ([]User, error) {
    decoder := json.NewDecoder(r)
    var users []User
    token, _ := decoder.Token()
    for decoder.More() {
        var user User
        if err := decoder.Decode(&user); err != nil { return nil, err }
        users = append(users, user)
    }
    return users, nil
}
```

### Solution 3: Use map[string]interface for dynamic JSON

```go
var result map[string]interface{}
decoder := json.NewDecoder(r)
decoder.UseNumber()
decoder.Decode(&result)
```

### Solution 4: Handle partial JSON for large payloads

```go
limitedReader := io.LimitReader(r, 10<<20)
buf := new(bytes.Buffer)
buf.ReadFrom(limitedReader)
if buf.Len() >= 10<<20 {
    return nil, fmt.Errorf("payload too large")
}
```

## Common Scenarios

- A JSON decoder fails because the response body is gzipped and not decompressed
- A struct field has type int but the JSON contains a string value
- A streaming decoder reads partial JSON because the connection was closed mid-transmission

## Prevent It

- Always check for json.SyntaxError and json.UnmarshalTypeError for meaningful error messages
- Use json.Decoder for streaming data and json.Unmarshal for complete payloads
- Set decoder.DisallowUnknownFields() to catch unexpected JSON keys during development
