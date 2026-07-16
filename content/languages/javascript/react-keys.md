---
title: "[Solution] React Warning: Each Child in a List Needs Unique Key Prop"
description: "Fix React 'Each child in a list should have a unique key prop' warning. Understand why keys matter, how to choose them, and avoid common key mistakes."
languages: ["javascript"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["react", "key-prop", "list-rendering", "reconciliation", "warning"]
weight: 5
---

# React Warning: Each Child in a List Should Have a Unique "Key" Prop

This warning occurs when you render a list of elements without providing a unique `key` prop to each child. React uses keys to track which items have changed, been added, or removed during re-renders. Without stable, unique keys, React cannot efficiently update the DOM and may produce incorrect UI state.

## Common Causes

- **Using array index as key** — when the list can be reordered, filtered, or items added/removed
- **Missing key entirely** — rendering elements from `.map()` without a key
- **Using non-unique values as keys** — duplicate IDs, names, or indices
- **Using `Math.random()` as key** — generates new keys every render, defeating the purpose

## How to Fix

```jsx
// Cause 1: No key prop at all
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => (
        <li>{user.name}</li>  // Warning: Each child needs a unique key
      ))}
    </ul>
  );
}

// Fix: use a unique identifier
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

// Cause 2: Using array index as key (problematic if list reorders)
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo, index) => (
        <TodoItem key={index} todo={todo} />
      ))}
    </ul>
  );
}

// Fix: use a stable unique identifier
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map(todo => (
        <TodoItem key={todo.id} todo={todo} />
      ))}
    </ul>
  );
}
```

```jsx
// Cause 3: Using Math.random() as key
function BadList({ items }) {
  return (
    <ul>
      {items.map(item => (
        <li key={Math.random()}>{item.name}</li>  // new key every render
      ))}
    </ul>
  );
}

// Fix: use item's unique property
function GoodList({ items }) {
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
}
```

## When Array Index IS Acceptable

Using index as key is acceptable when:
- The list is static and never reordered
- Items don't have unique IDs
- The list is not filtered or have items added/removed

```jsx
// OK — static list, never changes
const colors = ["red", "green", "blue"];
{colors.map((color, index) => (
  <span key={index}>{color}</span>
))}
```

## Related Errors

- [React Hook Rules Violation]({{< relref "/languages/javascript/react-hooks" >}}) — hooks called outside React components
- [React State Update on Unmounted]({{< relref "/languages/javascript/react-state-update" >}}) — state updates on unmounted components
- [Cannot Read Properties of undefined]({{< relref "/languages/javascript/react-undefined-prop" >}}) — undefined property access
