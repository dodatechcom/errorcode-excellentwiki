---
title: "[Solution] React forwardRef Expects a Render Function — Fix Guide"
description: "Fix React forwardRef expects a render function error. Understand forwardRef usage, ref forwarding, and correct component patterns."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["react", "forwardref", "ref", "render", "callback", "component", "function"]
weight: 5
---

# forwardRef Expects a Render Function

The error `forwardRef expects a render function` occurs when you pass something other than a function to `React.forwardRef()`. The argument must be a function that receives `props` and `ref` as parameters and returns JSX.

## Description

`React.forwardRef` is a higher-order component that lets a parent component access the DOM node of a child component through `ref`. It takes a single argument: a render function with the signature `(props, ref) => JSX.Element`.

Common mistakes include passing a class component, an object, or calling `forwardRef` incorrectly.

## Common Causes

- **Passing a class component** — `forwardRef` only works with function components
- **Incorrect function signature** — not providing `(props, ref)` parameters
- **Wrapping already-wrapped component** — double-wrapping with forwardRef
- **Import mistake** — importing a different `forwardRef` or misspelling it

## How to Fix

### Fix 1: Use the correct forwardRef signature

```jsx
// Wrong — missing ref parameter
const MyInput = forwardRef((props) => {
  return <input />;
});

// Correct
const MyInput = forwardRef((props, ref) => {
  return <input ref={ref} {...props} />;
});
```

### Fix 2: Don't use forwardRef with class components

```jsx
// Wrong — forwardRef doesn't work with class components
class MyInput extends Component {
  render() {
    return <input ref={this.props.ref} />;
  }
}
const WrappedInput = forwardRef(MyInput); // Error

// Correct — use function component
const MyInput = forwardRef((props, ref) => {
  return <input ref={ref} {...props} />;
});
```

### Fix 3: Use ref with custom components correctly

```jsx
const FancyInput = forwardRef((props, ref) => {
  return (
    <div className="fancy">
      <input ref={ref} {...props} />
    </div>
  );
});

function App() {
  const inputRef = useRef(null);

  const focus = () => inputRef.current?.focus();

  return (
    <div>
      <FancyInput ref={inputRef} />
      <button onClick={focus}>Focus</button>
    </div>
  );
}
```

### Fix 4: Use callback refs for non-forwardRef components

```jsx
function App() {
  const setInputRef = (el) => {
    if (el) el.focus();
  };

  return <input ref={setInputRef} />;
}
```

## Examples

```jsx
import React, { forwardRef } from 'react';

// Wrong — passing a string instead of a function
const BadInput = forwardRef("input");

function App() {
  return <BadInput />;
}
```

Output:
```
forwardRef expects a render function but received [object String]
```

## Related Errors

- [react-undefined-prop]({{< relref "/languages/javascript/react-undefined-prop" >}}) — undefined ref or prop access.
- [react-invariant]({{< relref "/languages/javascript/react-invariant" >}}) — invariant violations from invalid API usage.
- [react-hooks]({{< relref "/languages/javascript/react-hooks" >}}) — hooks violations in component functions.
