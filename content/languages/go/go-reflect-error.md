---
title: "[Solution] Go reflect Error — How to Fix"
description: "Fix Go reflect errors. Handle type inspection, value manipulation, and reflection-based code generation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go reflect Error

Fix Go reflect errors. Handle type inspection, value manipulation, and reflection-based code generation.

## Why It Happens

- reflect: ValueOf on nil pointer causes panic
- reflect: cannot set value obtained from unexported struct field
- reflect: type assertion fails because of interface wrapping
- reflect operation is too slow causing performance degradation

## Common Error Messages

```
reflect: call of reflect.ValueOf on nil
```
```
reflect: reflect.Value.Set using unexported field
```
```
reflect: interface conversion
```
```
reflect: Kind mismatch
```

## How to Fix It

### Solution 1: Use reflect safely

```go
import "reflect"

var x interface{} = "hello"
v := reflect.ValueOf(x)
fmt.Println(v.Kind())  // string
fmt.Println(v.String()) // hello
```

### Solution 2: Set values with reflect

```go
var s string = "old"
v := reflect.ValueOf(&s).Elem()
v.SetString("new")
fmt.Println(s) // new
```

### Solution 3: Handle struct fields

```go
type User struct {
    Name string
    age  int  // unexported - cannot set
}
u := User{"Alice", 30}
v := reflect.ValueOf(&u).Elem()
field := v.FieldByName("Name")
field.SetString("Bob")
```

### Solution 4: Use reflect for validation

```go
func validate(obj interface{}) error {
    v := reflect.ValueOf(obj)
    for i := 0; i < v.NumField(); i++ {
        field := v.Type().Field(i)
        tag := field.Tag.Get("validate")
        if tag == "required" && v.Field(i).IsZero() {
            return fmt.Errorf("%s is required", field.Name)
        }
    }
    return nil
}
```

## Common Scenarios

- reflect.ValueOf panics on nil pointer
- Cannot set unexported struct fields via reflection
- Reflection is much slower than direct access

## Prevent It

- Always check for nil before using reflect.ValueOf
- Only export fields that need to be set via reflection
- Use code generation instead of reflect for performance-critical code
