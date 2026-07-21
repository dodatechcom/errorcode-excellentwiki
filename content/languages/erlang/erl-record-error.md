---
title: "[Solution] Erlang Record Error"
description: "Record definition and usage errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Record Error

Record definition and usage errors.

### Common Causes
Missing include; wrong field access

### How to Fix
```erlang
-record(person, {name, age, email}).
P = #person{name = "John", age = 30},
Name = P#person.name.
```

### Examples
```erlang
update(P, #person{age = 31}).
```
