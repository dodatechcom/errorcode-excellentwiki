---
title: "[Solution] Deprecated Function Migration: findDOMNode to ref callbacks"
description: "Migrate from deprecated findDOMNode to ref callbacks."
deprecated_function: "findDOMNode(this)"
replacement_function: "createRef / useRef"
languages: ["react"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: findDOMNode to ref callbacks

The `findDOMNode(this)` has been deprecated in favor of `createRef / useRef`.

## Migration Guide

findDOMNode is deprecated in Strict Mode.

## Before (Deprecated)

```react
componentDidMount() {
    const node = ReactDOM.findDOMNode(this);
    node.focus();
}
```

## After (Modern)

```react
constructor(props) {
    super(props);
    this.myRef = React.createRef();
}
componentDidMount() {
    this.myRef.current.focus();
}
```

## Key Differences

- Use ref instead of findDOMNode
