---
title: "[Solution] Erlang Binary Error"
description: "Binary construction and matching errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Binary Error

Binary construction and matching errors.

### Common Causes
Wrong syntax; encoding; size mismatch

### How to Fix
```erlang
Bin = <<1, 2, 3>>,
<<A, B, C>> = Bin.
```

### Examples
```erlang
<<Len:16, Data/binary>> = <<0, 5, "hello">>.
```
