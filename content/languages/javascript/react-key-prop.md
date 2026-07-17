---
title: "[Solution] React Warning: Each child needs unique key Prop"
description: "Fix React key prop warning. Add unique keys to list items, understand key usage, and avoid common key mistakes."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["react", "key", "warning", "list", "iterator"]
weight: 5
---

# React Warning: Each child needs unique key

This warning occurs when rendering a list of elements without providing unique `key` props. React uses keys to identify which items changed, were added, or removed.

## What This Error Means

Common error messages:

- `Warning: Each child in a list should have a unique "key" prop.`
- `Warning: Encountered two children with the same key`
- `key` prop is required for list rendering

Keys help React efficiently update the DOM when list items change. Without proper keys, React may re-render incorrectly.

## Common Causes

```jsx
// Cause 1: Using array index as key (with reordering)
function List({ items }) {
  return items.map((item, index) => (
    <li key={index}>{item.name}</li>
  ));
}

// Cause 2: No key at all
function List({ items }) {
  return items.map(item => (
    <li>{item.name}</li> // missing key
  ));
}

// Cause 3: Duplicate keys
function List() {
  return (
    <>
      <li key="a">First</li>
      <li key="a">Second</li> // duplicate key
    </>
  );
}

// Cause 4: Using random values as keys
<li key={Math.random()}>{item.name}</li>
```

## How to Fix

### Fix 1: Use unique IDs as keys

```jsx
function List({ items }) {
  return items.map(item => (
    <li key={item.id}>{item.name}</li>
  ));
}
```

### Fix 2: Use index only for static lists

```jsx
// OK: list is static and won't reorder
function StaticList({ items }) {
  return items.map((item, index) => (
    <li key={index}>{item}</li>
  ));
}

// Not OK: list can be reordered, filtered, or changed
function DynamicList({ items }) {
  return items.map(item => (
    <li key={item.id}>{item.name}</li>
  ));
}
```

### Fix 3: Generate stable keys

```jsx
function List({ items }) {
  return items.map(item => (
    <li key={`${item.type}-${item.id}`}>{item.name}</li>
  ));
}
```

### Fix 4: Fix Fragment keys

```jsx
// Wrong: Fragment without key
items.map(item => (
  <React.Fragment>
    <dt>{item.term}</dt>
    <dd>{item.description}</dd>
  </React.Fragment>
));

// Correct
items.map(item => (
  <React.Fragment key={item.id}>
    <dt>{item.term}</dt>
    <dd>{item.description}</dd>
  </React.Fragment>
));
```

## Examples

```jsx
// This triggers warning
const todos = [{ id: 1, text: 'Learn React' }];

function TodoList() {
  return (
    <ul>
      {todos.map(todo => (
        <li>{todo.text}</li> // Warning: missing key
      ))}
    </ul>
  );
}

// Fix
function TodoList() {
  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
}
```

## Related Errors

- [React Error Boundary]({{< relref "/languages/javascript/react-error-boundary" >}}) — error boundary
- [React State Update]({{< relref "/languages/javascript/react-state-update" >}}) — unmounted component
- [React Invalid Element]({{< relref "/languages/javascript/react-invalid-element" >}}) — invalid element type
