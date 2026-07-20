---
title: "[Solution] encoding/gob Decode Error Fix"
description: "Fix Go gob decode errors. Handle encoding/decoding issues, type registration, and stream errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# encoding/gob Decode Error

The `encoding/gob` package fails to decode data when the encoder and decoder types are mismatched, the stream is corrupted, exported fields are missing, or the `GobEncode`/`GobDecode` methods are implemented incorrectly. Gob is Go's native binary serialization format.

## Common Causes

```go
// Cause 1: Type mismatch between encoder and decoder
type V1 struct { Name string }
type V2 struct { Name string; Age int }
// Encode V1, decode into V2 — age field gets zero value

// Cause 2: Unexported fields not encoded
type user struct {  // lowercase 'u' — unexported
    Name string
}
// gob: type user has no exported fields

// Cause 3: Stream corruption
var buf bytes.Buffer
gob.NewEncoder(&buf).Encode(data)
// if buf is partially written or corrupted, decode fails

// Cause 4: Interface type not registered
type Animal interface { Speak() string }
type Dog struct { Name string }
// gob: type Animal is not registered

// Cause 5: Nil pointer dereference
var u *User
gob.NewEncoder(&buf).Encode(u) // nil pointer — may panic
```

## How to Fix

### Fix 1: Register types for interface encoding

```go
import (
    "bytes"
    "encoding/gob"
)

type Animal interface {
    Speak() string
}

type Dog struct{ Name string }
type Cat struct{ Name string }

func (d Dog) Speak() string { return "Woof" }
func (c Cat) Speak() string { return "Meow" }

func init() {
    gob.Register(Dog{})
    gob.Register(Cat{})
}
```

### Fix 2: Ensure exported fields and proper encoding

```go
type User struct {
    Name  string `gob:"name"`
    Email string `gob:"email"`
    Age   int    `gob:"age"`
}

func encodeUser(u User) ([]byte, error) {
    var buf bytes.Buffer
    if err := gob.NewEncoder(&buf).Encode(u); err != nil {
        return nil, err
    }
    return buf.Bytes(), nil
}

func decodeUser(data []byte) (User, error) {
    var u User
    if err := gob.NewDecoder(bytes.NewReader(data)).Decode(&u); err != nil {
        return User{}, err
    }
    return u, nil
}
```

### Fix 3: Use stream encoding for large data

```go
func encodeStream(w io.Writer, items []User) error {
    enc := gob.NewEncoder(w)
    for _, item := range items {
        if err := enc.Encode(item); err != nil {
            return err
        }
    }
    return nil
}
```

## Examples

```go
package main

import (
    "bytes"
    "encoding/gob"
    "fmt"
    "log"
)

type User struct {
    Name  string
    Email string
    Age   int
}

func main() {
    original := User{Name: "Alice", Email: "alice@example.com", Age: 30}

    // Encode
    var buf bytes.Buffer
    if err := gob.NewEncoder(&buf).Encode(original); err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Encoded %d bytes\n", buf.Len())

    // Decode
    var decoded User
    if err := gob.NewDecoder(&buf).Decode(&decoded); err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Decoded: %+v\n", decoded)
}
```

## Related Errors

- [encoding-binary]({{< relref "/languages/go/go-binary-error" >}}) — binary encoding with endianness issues
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — JSON encoding alternative to gob
- [go-protobuf-error]({{< relref "/languages/go/go-protobuf-error" >}}) — protobuf encoding for cross-language data
