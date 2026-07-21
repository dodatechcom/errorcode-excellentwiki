---
title: "[Solution] Deprecated Function Migration: componentWillReceiveProps to getDerivedStateFromProps"
description: "Migrate from deprecated componentWillReceiveProps to getDerivedStateFromProps."
deprecated_function: "componentWillReceiveProps(nextProps)"
replacement_function: "static getDerivedStateFromProps(props, state)"
languages: ["react"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: componentWillReceiveProps to getDerivedStateFromProps

The `componentWillReceiveProps(nextProps)` has been deprecated in favor of `static getDerivedStateFromProps(props, state)`.

## Migration Guide

componentWillReceiveProps is renamed to UNSAFE.

## Before (Deprecated)

```react
componentWillReceiveProps(nextProps) {
    if (nextProps.value !== this.props.value) {
        this.setState({ derived: nextProps.value * 2 });
    }
}
```

## After (Modern)

```react
static getDerivedStateFromProps(props, state) {
    if (props.value !== state.prevValue) {
        return { derived: props.value * 2, prevValue: props.value };
    }
    return null;
}
```

## Key Differences

- getDerivedStateFromProps is static
