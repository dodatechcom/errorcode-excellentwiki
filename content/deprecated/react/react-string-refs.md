---
title: "[Solution] Deprecated Function Migration: string refs to createRef/useRef"
description: "Migrate from deprecated string refs to React.createRef or useRef in React."
deprecated_function: "ref=myRef"
replacement_function: "React.createRef() / useRef()"
languages: ["javascript"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: string refs to createRef/useRef

The `ref="myRef"` has been deprecated in favor of `React.createRef() / useRef()`.

## Migration Guide

String refs are deprecated and removed in React 19. Use createRef or useRef instead.

## Before (Deprecated)

```javascript
class MyComponent extends React.Component {
    componentDidMount() {
        this.refs.input.focus();
    }
    render() {
        return <input ref="input" />;
    }
}
```

## After (Modern)

```javascript
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
        this.inputRef = React.createRef();
    }
    componentDidMount() {
        this.inputRef.current.focus();
    }
    render() {
        return <input ref={this.inputRef} />;
    }
}

// Function component with useRef
function MyComponent() {
    const inputRef = useRef(null);
    useEffect(() => { inputRef.current?.focus(); }, []);
    return <input ref={inputRef} />;
}
```

## Key Differences

- String refs removed in React 19
- React.createRef() for class components
- useRef() for function components
