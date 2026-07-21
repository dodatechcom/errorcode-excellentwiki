---
title: "[Solution] Erlang Map Error"
description: "Map operations errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Map Error

Map operations errors.

### Common Causes
Key not found; wrong syntax

### How to Fix
```erlang
Map = #{name => "John", age => 30},
Name = maps:get(name, Map).
```

### Examples
```erlang
NewMap = maps:put(email, "j@x.com", Map),
UpdatedMap = maps:update(age, 31, Map).
```
