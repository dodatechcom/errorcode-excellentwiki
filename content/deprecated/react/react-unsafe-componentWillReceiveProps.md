---
title: "[Solution] Deprecated Function Migration: UNSAFE_componentWillReceiveProps to getDerivedStateFromProps"
description: "Migrate from deprecated UNSAFE_componentWillReceiveProps to getDerivedStateFromProps."
deprecated_function: "UNSAFE_componentWillReceiveProps(nextProps)"
replacement_function: "static getDerivedStateFromProps(props, state)"
languages: ["react"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: UNSAFE_componentWillReceiveProps to getDerivedStateFromProps

The `UNSAFE_componentWillReceiveProps(nextProps)` has been deprecated in favor of `static getDerivedStateFromProps(props, state)`.

## Migration Guide

getDerivedStateFromProps is static.

## Before (Deprecated)

```react
UNSAFE_componentWillReceiveProps(nextProps) {
    this.setState({ value: nextProps.value });
}
```

## After (Modern)

```react
static getDerivedStateFromProps(props, state) {
    return { value: props.value };
}
```

## Key Differences

- getDerivedStateFromProps is static
