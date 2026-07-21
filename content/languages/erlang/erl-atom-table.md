---
title: "[Solution] Erlang Atom Table"
description: "Atom table overflow errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Atom Table

Atom table overflow errors.

### Common Causes
Too many atoms; not garbage collected

### How to Fix
```erlang
% Atoms are never garbage collected
% Use binaries for dynamic strings
```

### Examples
```erlang
% Convert atom to string when needed
atom_to_list(my_atom).
```
