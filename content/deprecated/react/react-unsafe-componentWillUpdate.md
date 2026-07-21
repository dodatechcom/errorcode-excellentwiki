---
title: "[Solution] Deprecated Function Migration: UNSAFE_componentWillUpdate to getSnapshotBeforeUpdate"
description: "Migrate from deprecated UNSAFE_componentWillUpdate to getSnapshotBeforeUpdate."
deprecated_function: "UNSAFE_componentWillUpdate(nextProps, nextState)"
replacement_function: "getSnapshotBeforeUpdate(prevProps, prevState)"
languages: ["react"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: UNSAFE_componentWillUpdate to getSnapshotBeforeUpdate

The `UNSAFE_componentWillUpdate(nextProps, nextState)` has been deprecated in favor of `getSnapshotBeforeUpdate(prevProps, prevState)`.

## Migration Guide

getSnapshotBeforeUpdate is safer.

## Before (Deprecated)

```react
UNSAFE_componentWillUpdate(nextProps, nextState) {
    this.scrollHeight = document.body.scrollHeight;
}
```

## After (Modern)

```react
getSnapshotBeforeUpdate(prevProps, prevState) {
    return document.body.scrollHeight;
}
```

## Key Differences

- getSnapshotBeforeUpdate is safer
