---
title: "[Solution] Deprecated Function Migration: UNSAFE_componentWillMount to componentDidMount"
description: "Migrate from deprecated UNSAFE_componentWillMount to componentDidMount."
deprecated_function: "UNSAFE_componentWillMount()"
replacement_function: "componentDidMount()"
languages: ["react"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: UNSAFE_componentWillMount to componentDidMount

The `UNSAFE_componentWillMount()` has been deprecated in favor of `componentDidMount()`.

## Migration Guide

componentDidMount is safe.

## Before (Deprecated)

```react
UNSAFE_componentWillMount() {
    this.loadData();
}
```

## After (Modern)

```react
componentDidMount() {
    this.loadData();
}
```

## Key Differences

- componentDidMount is safe
