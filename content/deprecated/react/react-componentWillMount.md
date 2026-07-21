---
title: "[Solution] Deprecated Function Migration: componentWillMount to componentDidMount"
description: "Migrate from deprecated componentWillMount to componentDidMount."
deprecated_function: "componentWillMount()"
replacement_function: "componentDidMount()"
languages: ["react"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: componentWillMount to componentDidMount

The `componentWillMount()` has been deprecated in favor of `componentDidMount()`.

## Migration Guide

componentWillMount is renamed to UNSAFE.

## Before (Deprecated)

```react
componentWillMount() {
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

- componentDidMount is the safe alternative
