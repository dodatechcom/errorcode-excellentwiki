---
title: "[Solution] Erlang If Error"
description: "if expression errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang If Error

if expression errors.

### Common Causes
Missing else clause; guard issues

### How to Fix
```erlang
Result = if
    X > 0 -> positive;
    X < 0 -> negative;
    true -> zero
end.
```

### Examples
```erlang
if
    Length > 10 -> long;
    Length > 5 -> medium;
    true -> short
end.
```
