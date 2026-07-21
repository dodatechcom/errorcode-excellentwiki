---
title: "[Solution] Erlang Guard Error"
description: "Guard expression syntax errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Guard Error

Guard expression syntax errors.

### Common Causes
Missing is_* function; wrong operator

### How to Fix
```erlang
is_positive(X) when X > 0 -> true;
is_positive(_) -> false.
```

### Examples
```erlang
is_valid(X) when is_integer(X), X > 0 -> true.
```
