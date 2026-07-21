---
title: "[Solution] Deprecated Function Migration: componentWillReceiveProps to getDerivedStateFromProps"
description: "Migrate from deprecated componentWillReceiveProps to getDerivedStateFromProps in React."
deprecated_function: "componentWillReceiveProps"
replacement_function: "getDerivedStateFromProps"
languages: ["javascript"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: componentWillReceiveProps to getDerivedStateFromProps

The `componentWillReceiveProps` has been deprecated in favor of `getDerivedStateFromProps`.

## Migration Guide

getDerivedStateFromProps is a static method that runs before every render.

## Before (Deprecated)

```javascript
class MyComponent extends React.Component {
    componentWillReceiveProps(nextProps) {
        if (nextProps.value !== this.props.value) {
            this.setState({ derived: computeValue(nextProps.value) });
        }
    }
}
```

## After (Modern)

```javascript
class MyComponent extends React.Component {
    static getDerivedStateFromProps(props, state) {
        if (props.value !== state.prevValue) {
            return { derived: computeValue(props.value), prevValue: props.value };
        }
        return null;
    }
}

// Or with hooks
function MyComponent({ value }) {
    const [derived, setDerived] = useState(() => computeValue(value));
    useEffect(() => { setDerived(computeValue(value)); }, [value]);
}
```

## Key Differences

- getDerivedStateFromProps is static
- Return null to skip state update
- Track previous props in state
- useEffect with deps is the hooks equivalent
