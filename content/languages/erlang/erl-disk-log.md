---
title: "[Solution] Erlang Disk Log"
description: "Disk log errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Disk Log

Disk log errors.

### Common Causes
Wrong type; not opened; full

### How to Fix
```erlang
disk_log:open([{name, my_log}, {file, "log.txt"}, {type, halt}]).
```

### Examples
```erlang
disk_log:log(my_log, "log entry").
```
