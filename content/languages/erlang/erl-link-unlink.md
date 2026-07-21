---
title: "[Solution] Erlang Link/Unlink"
description: "Process link/unlink errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Link/Unlink

Process link/unlink errors.

### Common Causes
Not linked; wrong cleanup

### How to Fix
```erlang
link(Pid),
unlink(Pid).
```

### Examples
```erlang
process_flag(trap_exit, true),
link(Pid),
receive
    {'EXIT', Pid, Reason} -> handle_exit(Reason)
end.
```
