---
title: "[Solution] Deprecated Function Migration: React.Children.map with index to flatMap"
description: "Migrate from deprecated React.Children.map with complex index logic to flatMap."
deprecated_function: "React.Children.map(children, (child, index) => child)"
replacement_function: "React.Children.toArray(children).flatMap(child => child)"
languages: ["react"]
deprecated_since: "React 16+"
---

# [Solution] Deprecated Function Migration: React.Children.map with index to flatMap

The `React.Children.map(children, (child, index) => child)` has been deprecated in favor of `React.Children.toArray(children).flatMap(child => child)`.

## Migration Guide

toArray + flatMap is more flexible.

## Before (Deprecated)

```react
React.Children.map(children, (child, index) => {
    return [child, <Separator key={index} />];
})
```

## After (Modern)

```react
React.Children.toArray(children).flatMap((child, index) => [
    child,
    <Separator key={index} />
])
```

## Key Differences

- toArray + flatMap is more flexible
