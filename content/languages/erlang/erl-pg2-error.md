---
title: "[Solution] Erlang PG2 Error"
description: "Process group errors (deprecated)"
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang PG2 Error

Process group errors (deprecated)

### Common Causes
Use pg module instead

### How to Fix
```erlang
% Deprecated - use pg
pg2:create_group(my_group).
pg2:join(my_group, self()).
```

### Examples
```erlang
pg:start_link().
pg:join(my_group, self()).
```
