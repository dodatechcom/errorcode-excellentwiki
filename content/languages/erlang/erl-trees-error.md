---
title: "[Solution] Erlang Trees"
description: "Tree data structure errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Trees

Tree data structure errors.

### Common Causes
Wrong operations; not balanced

### How to Fix
```erlang
Tree = trees:empty(),
Tree1 = trees:insert(5, Tree),
Tree2 = trees:insert(3, Tree1).
```

### Examples
```erlang
trees:member(5, Tree).
```
