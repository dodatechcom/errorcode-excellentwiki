---
title: "[Solution] json Cannot Unmarshal Fix"
description: "Fix Go JSON unmarshal errors. Handle invalid JSON, type mismatches, and field mapping issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# json Cannot Unmarshal

The `encoding/json` package fails to unmarshal JSON data into Go structs when field types don't match, `json:"-"` tags hide fields, the JSON has trailing commas (invalid), or `interface{}` receives unexpected types. Unmarshal is lenient about missing fields but strict about type mismatches.

## Common Causes

```go
// Cause 1: Type mismatch — JSON number into Go string
type User struct {
    Age string `json:"age"`
}
var u User
json.Unmarshal([]byte(`{"age": 25}`), &u) // age is number, wants string

// Cause 2: JSON object into Go struct without matching tags
type Config struct {
    DatabaseHost string `json:"db_host"`
}
json.Unmarshal([]byte(`{"database_host": "localhost"}`), &u)
// db_host remains empty — JSON key is "database_host" not "db_host"

// Cause 3: Null JSON value into non-nullable Go type
var s string
json.Unmarshal([]byte(`null`), &s) // s stays empty

// Cause 4: Nested JSON without nested struct
type User struct {
    Name string `json:"name"`
}
var u User
json.Unmarshal([]byte(`{"name": {"first": "Alice"}}`), &u)
// name is object, wants string

// Cause 5: Leading zeros in JSON numbers
json.Unmarshal([]byte(`{"id": 007}`), &u) // invalid JSON number
```

## How to Fix

### Fix 1: Use correct struct tags and types

```go
import (
    "encoding/json"
    "fmt"
)

type User struct {
    Name  string  `json:"name"`
    Age   int     `json:"age"`
    Email string  `json:"email"`
    Score float64 `json:"score,omitempty"`
}

func parseUser(data []byte) (*User, error) {
    var u User
    if err := json.Unmarshal(data, &u); err != nil {
        return nil, fmt.Errorf("unmarshal user: %w", err)
    }
    return &u, nil
}
```

### Fix 2: Use map[string]interface{} for dynamic JSON

```go
func parseDynamic(data []byte) (map[string]interface{}, error) {
    var result map[string]interface{}
    if err := json.Unmarshal(data, &result); err != nil {
        return nil, err
    }
    return result, nil
}

// Access nested values
func getNested(m map[string]interface{}, keys ...string) interface{} {
    var current interface{} = m
    for _, key := range keys {
        m, ok := current.(map[string]interface{})
        if !ok {
            return nil
        }
        current = m[key]
    }
    return current
}
```

### Fix 3: Handle multiple possible types with json.RawMessage

```go
type Event struct {
    Type    string          `json:"type"`
    Payload json.RawMessage `json:"payload"`
}

func processEvent(data []byte) error {
    var event Event
    json.Unmarshal(data, &event)

    switch event.Type {
    case "user_created":
        var u User
        json.Unmarshal(event.Payload, &u)
        // handle user
    case "order_placed":
        var o Order
        json.Unmarshal(event.Payload, &o)
        // handle order
    }
    return nil
}
```

## Examples

```go
package main

import (
    "encoding/json"
    "fmt"
    "log"
)

type Response struct {
    Status  int    `json:"status"`
    Message string `json:"message"`
    Data    struct {
        Users []User `json:"users"`
    } `json:"data"`
}

type User struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
}

func main() {
    jsonData := []byte(`{
        "status": 200,
        "message": "success",
        "data": {
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ]
        }
    }`)

    var resp Response
    if err := json.Unmarshal(jsonData, &resp); err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Status: %d, Users: %d\n", resp.Status, len(resp.Data.Users))
    for _, u := range resp.Data.Users {
        fmt.Printf("  %d: %s\n", u.ID, u.Name)
    }
}
```

## Related Errors

- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — generic unmarshal error
- [go-xml-error]({{< relref "/languages/go/go-xml-error" >}}) — XML unmarshal has similar tag issues
- [go-yaml-error]({{< relref "/languages/go/go-yaml-error" >}}) — YAML parsing errors
