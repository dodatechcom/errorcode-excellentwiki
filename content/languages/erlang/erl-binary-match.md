---
title: "[Solution] Erlang Binary Match"
description: "Binary pattern matching errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Binary Match

Binary pattern matching errors.

### Common Causes
Wrong size; encoding; incomplete match

### How to Fix
```erlang
<<Len:8, Data:Len/binary>> = Bin.
```

### Examples
```erlang
<<16#FF, Rest/binary>> = <<16#FF, 1, 2, 3>>.
```
