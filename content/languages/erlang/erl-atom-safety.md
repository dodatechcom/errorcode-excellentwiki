---
title: "[Solution] Erlang Atom Safety"
description: "Atom safety errors; injection"
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Atom Safety

Atom safety errors; injection

### Common Causes
Dynamic atom creation; DoS

### How to Fix
```erlang
% Avoid list_to_atom with untrusted input
Safe = list_to_existing_atom(Str).
```

### Examples
```erlang
% Use binaries or atoms from trusted sources only
```
