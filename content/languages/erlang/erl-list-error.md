---
title: "[Solution] Erlang List Error"
description: "List creation and manipulation errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang List Error

List creation and manipulation errors.

### Common Causes
Wrong syntax; cons operator; append

### How to Fix
```erlang
List = [1, 2, 3],
[H | T] = List.
```

### Examples
```erlang
NewList = List ++ [4, 5],
ShortList = List -- [2].
```
