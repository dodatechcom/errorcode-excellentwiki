---
title: "[Solution] Go JSON Unmarshal Invalid Character — Runtime Error Fix"
description: "Fix Go json.Unmarshal invalid character errors. Handle malformed JSON, type mismatches, and encoding issues safely."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["json", "unmarshal", "invalid-character", "encoding", "decoding", "syntax"]
weight: 5
---

# JSON Unmarshal — Invalid Character Error

The error `json.Unmarshal: invalid character` occurs when Go's JSON decoder encounters unexpected bytes while parsing JSON input. This is a syntax error in the JSON data, not a Go type error.

## Description

Go's `encoding/json` package expects严格 valid JSON. The error message includes the byte position and the offending character. Common issues include trailing commas, single quotes instead of double quotes, comments in JSON, and non-UTF-8 bytes.

While this is typically an `error` return rather than a panic, it is one of the most frequently encountered errors when working with APIs, configuration files, and user input.

## Common Causes

- **Trailing commas** — JSON does not allow commas after the last element: `{"a": 1,}`
- **Single quotes** — JSON requires double quotes for keys and string values
- **Comments in JSON** — `//` and `/* */` are not valid JSON syntax
- **Non-UTF-8 input** — binary data or incorrect encoding in JSON strings

## How to Fix

### Fix 1: Validate JSON before unmarshalling

```go
func isValidJSON(data []byte) bool {
    var js json.RawMessage
    return json.Unmarshal(data, &js) == nil
}
```

### Fix 2: Strip trailing commas (use a JSON5 library)

```go
// Use github.com/tdewolff/mini/v2 or similar
import "github.com/tdewolff/mini/v2"

func parseRelaxedJSON(input string) (map[string]interface{}, error) {
    // mini.json5 can handle trailing commas
    var result map[string]interface{}
    err := json.Unmarshal([]byte(minijson5.ToJSON(input)), &result)
    return result, err
}
```

### Fix 3: Handle encoding issues

```go
// Force UTF-8 before unmarshalling
data = bytes.ReplaceAll(data, []byte{0xc2, 0xa0}, []byte{' '})

var result map[string]interface{}
if err := json.Unmarshal(data, &result); err != nil {
    log.Printf("invalid JSON: %v", err)
}
```

### Fix 4: Use a lenient decoder

```go
decoder := json.NewDecoder(bytes.NewReader(data))
decoder.UseNumber() // preserves numeric precision
if err := decoder.Decode(&result); err != nil {
    log.Printf("JSON decode error: %v", err)
}
```

## Examples

```go
package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    // Trailing comma — invalid JSON
    data := []byte(`{"name": "Alice", "age": 30,}`)

    var result map[string]interface{}
    err := json.Unmarshal(data, &result)
    if err != nil {
        fmt.Println(err)
    }
}
```

Output:
```
invalid character '}' looking for beginning of value
```

## Related Errors

- [strconv-parse]({{< relref "/languages/go/strconv-parse" >}}) — string-to-number conversion errors.
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — unexpected end of JSON input.
- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — incorrect type assertion after unmarshalling.
