---
title: "[Solution] Erlang External Term"
description: "External term format errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang External Term

External term format errors.

### Common Causes
Wrong encoding; not portable

### How to Fix
```erlang
Term = {ok, data},
Binary = term_to_binary(Term),
Decoded = binary_to_term(Binary).
```

### Examples
```erlang
file:write_file("data.bin", term_to_binary(MyTerm)).
{ok, Bin} = file:read_file("data.bin"),
MyTerm = binary_to_term(Bin).
```
