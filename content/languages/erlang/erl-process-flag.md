---
title: "[Solution] Erlang Process Flag"
description: "Process flag errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Process Flag

Process flag errors.

### Common Causes
Wrong flag; trap_exit; priority

### How to Fix
```erlang
process_flag(trap_exit, true).
process_flag(priority, high).
```

### Examples
```erlang
process_flag(dictionary, [{key, value}]).
```
