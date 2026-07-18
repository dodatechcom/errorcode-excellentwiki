---
title: "[Solution] Go JSON Unknown Field Error — How to Fix"
description: "Fix Go JSON unknown field errors. Handle DisallowUnknownFields, forward compatibility, partial decoding, and schema evolution."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go JSON Unknown Field Error

Fix Go JSON unknown field errors. Handle DisallowUnknownFields, forward compatibility, partial decoding, and schema evolution.

## Why It Happens

- DisallowUnknownFields is enabled but the JSON payload contains new fields from API updates
- A client sends extra fields that the server struct does not define causing decode failures
- API versioning introduces new fields but old clients cannot handle them
- Embedded structs have overlapping field names causing ambiguous decoding

## Common Error Messages

```
json: unknown field <name>
```
```
json: cannot unmarshal object into Go struct field
```
```
json: duplicate field <name>
```
```
json: unknown field in embedded struct
```

## How to Fix It

### Solution 1: Allow unknown fields for forward compatibility

```go
var data = []byte(`{"name": "Alice", "age": 30, "new_field": "value"}`)
type User struct { Name string `json:"name"`; Age int `json:"age"` }
var user User
json.Unmarshal(data, &user) // works - new_field is ignored
```

### Solution 2: Use separate structs for strict and permissive decoding

```go
type UserStrict struct { Name string `json:"name"` }
type UserPermissive struct {
    Name  string                 `json:"name"`
    Extra map[string]interface{} `json:"-"`
}
func DecodeUser(data []byte, strict bool) (*UserPermissive, error) {
    var u UserPermissive
    if strict {
        d := json.NewDecoder(bytes.NewReader(data))
        d.DisallowUnknownFields()
        return &u, d.Decode(&u)
    }
    return &u, json.Unmarshal(data, &u)
}
```

### Solution 3: Handle embedded struct field conflicts

```go
type Base struct { ID string `json:"id"` }
type Extended struct {
    Base
    ExtendedName string `json:"extended_name"`
}
```

### Solution 4: Validate unknown fields in strict API mode

```go
type APIRequest struct { Name string `json:"name"` }
func ValidateRequest(data []byte) (*APIRequest, error) {
    var req APIRequest
    d := json.NewDecoder(bytes.NewReader(data))
    d.DisallowUnknownFields()
    if err := d.Decode(&req); err != nil {
        return nil, fmt.Errorf("unexpected field: %w", err)
    }
    return &req, nil
}
```

## Common Scenarios

- An API client fails to decode responses because the server added new fields to the JSON schema
- A strict API validator rejects valid requests because clients send extra metadata fields
- An embedded struct causes JSON field conflicts when parent and child have the same field name

## Prevent It

- Do not use DisallowUnknownFields on clients that consume evolving APIs
- Use DisallowUnknownFields only on the server side for strict input validation
- Document which fields are required and which are optional in API schemas
