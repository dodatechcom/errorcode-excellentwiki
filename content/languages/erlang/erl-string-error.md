---
title: "[Solution] Erlang String Error"
description: "String operations errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang String Error

String operations errors.

### Common Causes
Wrong type; encoding; concatenation

### How to Fix
```erlang
Str = "hello",
Length = string:length(Str).
```

### Examples
```erlang
string:concat("hello", " world").
string:to_upper("hello").
```
