---
title: "[Solution] Erlang Dialyzer"
description: "Dialyzer type analysis errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Dialyzer

Dialyzer type analysis errors.

### Common Causes
Type mismatch; unknown function

### How to Fix
```erlang
-spec add(integer(), integer()) -> integer().
add(A, B) -> A + B.
```

### Examples
```erlang
$ dialyzer --plt plt/file.plt -r ebin/
```
