---
title: "[Solution] Erlang Unicode Error"
description: "Unicode/encoding errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Unicode Error

Unicode/encoding errors.

### Common Causes
Wrong encoding; conversion

### How to Fix
```erlang
Str = "caf\xc3\xa9",
Utf8Bin = unicode:characters_to_binary(Str).
```

### Examples
```erlang
unicode:characters_to_list(<<"hello">>).
```
