---
title: "[Solution] Erlang Atom Error"
description: "Atom creation and comparison errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Atom Error

Atom creation and comparison errors.

### Common Causes
Atoms not garbage collected; wrong comparison

### How to Fix
```erlang
Atom = my_atom,
Atom == my_atom.  % true
```

### Examples
```erlang
list_to_atom("dynamic_name").  % Use cautiously
atom_to_list(my_atom).
```
