---
title: "[Solution] Go JSON Unmarshal Invalid Character Fix"
description: "Fix Go JSON unmarshal error with invalid characters. Validate JSON input, handle encoding issues, and use proper unmarshaling techniques."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# JSON Unmarshal Invalid Character Fix

The `invalid character 'X' looking for beginning of value` error occurs when `json.Unmarshal` receives input that is not valid JSON.

## Description

Go's `encoding/json` package requires input to be well-formed JSON. The unmarshaler expects JSON values to start with `{`, `[`, `"`, a digit, `t`, `f`, or `n`. When it encounters unexpected characters, it reports the position and character that caused the failure.

Common scenarios:

- **HTML or plain text passed as JSON** — API returns an error page instead of JSON.
- **BOM (Byte Order Mark) at start** — UTF-8 BOM before JSON content.
- **Trailing commas** — not allowed in strict JSON.
- **Single quotes instead of double quotes** — JavaScript-style JSON.
- **Comments in JSON** — JSON doesn't support comments.

## Common Causes

```go
// Cause 1: Response is HTML, not JSON
func main() {
    resp, _ := http.Get("https://api.example.com/data")
    var result MyStruct
    json.NewDecoder(resp.Body).Decode(&result)
    // Error: invalid character '<' looking for beginning of value
}

// Cause 2: Trailing comma
func main() {
    data := []byte(`{"name": "Alice", "age": 30,}`)
    var m map[string]interface{}
    json.Unmarshal(data, &m)
    // Error: invalid character '}' looking for beginning of value
}

// Cause 3: Single quotes
func main() {
    data := []byte(`{'name': 'Alice'}`)
    var m map[string]interface{}
    json.Unmarshal(data, &m)
    // Error: invalid character '\'' looking for beginning of value
}

// Cause 4: JSON with comments
func main() {
    data := []byte(`{
        // This is a comment
        "name": "Alice"
    }`)
    var m map[string]interface{}
    json.Unmarshal(data, &m)
}
```

## How to Fix

### Fix 1: Validate response content type

```go
func fetchJSON(url string, target interface{}) error {
    resp, err := http.Get(url)
    if err != nil {
        return err
    }
    defer resp.Body.Close()

    if resp.Header.Get("Content-Type") != "application/json" {
        return fmt.Errorf("expected JSON, got %s", resp.Header.Get("Content-Type"))
    }

    return json.NewDecoder(resp.Body).Decode(target)
}
```

### Fix 2: Sanitize JSON input

```go
func parseJSON(data []byte, v interface{}) error {
    // Remove BOM if present
    data = bytes.TrimPrefix(data, []byte("\xef\xbb\xbf"))
    return json.Unmarshal(data, v)
}
```

### Fix 3: Use a JSON5 library for lenient parsing

```go
import "github.com/claedia/json5"

func main() {
    data := []byte(`{
        // comment
        'name': 'Alice',
    }`)
    var m map[string]interface{}
    json5.Unmarshal(data, &m)
}
```

### Fix 4: Read the body to debug

```go
func debugJSON(resp *http.Response) {
    body, _ := io.ReadAll(resp.Body)
    fmt.Printf("Response body: %q\n", string(body))
    // Check for HTML error pages, empty responses, etc.
}
```

## Examples

```go
// This triggers: invalid character 'h' looking for beginning of value
package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    data := []byte(`<html><body>Error</body></html>`)
    var result map[string]interface{}
    err := json.Unmarshal(data, &result)
    fmt.Println(err)
}
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — unexpected end of input.
- [io-pipe-broken]({{< relref "/languages/go/io-pipe-broken" >}}) — broken pipe during read/write.
- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — wrong type after unmarshaling.
