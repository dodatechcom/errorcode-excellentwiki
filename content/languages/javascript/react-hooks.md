---
title: "[Solution] React Invalid Hook Call / Rules of Hooks Violation Fix"
description: "Fix React 'Invalid hook call' and 'Rules of Hooks' errors. Understand why hooks must be called at the top level and inside React components."
languages: ["javascript"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["react", "hooks", "rules-of-hooks", "invalid-hook-call", "useState", "useEffect"]
weight: 5
---

# React: Invalid Hook Call / Rules of Hooks Violation

The **"Invalid hook call"** or **"Rules of Hooks"** error occurs when you call a React hook (`useState`, `useEffect`, etc.) outside a React function component, inside a loop, condition, or nested function, or from a regular JavaScript function. Hooks must be called at the top level of a React component, in the same order every render.

## Common Causes

- **Hook called inside a condition or loop** — hooks must always be called in the same order
- **Hook called from a regular function** — only React function components and custom hooks can use hooks
- **Multiple React instances** — two copies of React loaded, causing hooks to fail
- **Hook called inside a callback** — `onClick` handler calling `useState` directly

## How to Fix

```jsx
// Cause 1: Hook inside a condition
function Component({ showName }) {
  if (showName) {
    const [name, setName] = useState("");  // WRONG — hook in condition
  }
}

// Fix: always call hooks at the top level
function Component({ showName }) {
  const [name, setName] = useState("");
  return showName ? <p>{name}</p> : null;
}

// Cause 2: Hook inside a loop
function BadComponent({ items }) {
  items.forEach(item => {
    const [selected, setSelected] = useState(false);  // WRONG
  });
}

// Fix: move hooks to top level, use array state
function GoodComponent({ items }) {
  const [selectedIds, setSelectedIds] = useState(new Set());

  const toggle = (id) => {
    setSelectedIds(prev => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>
          <button onClick={() => toggle(item.id)}>
            {selectedIds.has(item.id) ? "Selected" : "Select"}
          </button>
        </li>
      ))}
    </ul>
  );
}

// Cause 3: Hook called from a regular function
function processItems(items) {
  const [count, setCount] = useState(0);  // WRONG — not a component
}

// Fix: only use hooks inside components or custom hooks
function ItemCounter({ items }) {
  const [count, setCount] = useState(0);
  return <p>{count} items</p>;
}
```

```jsx
// Cause 4: Hook inside a callback (wrong pattern)
function Button() {
  const handleClick = () => {
    const [value, setValue] = useState(0);  // WRONG
  };
  return <button onClick={handleClick}>Click</button>;
}

// Fix: call useState at component top level
function Button() {
  const [value, setValue] = useState(0);
  const handleClick = () => setValue(v => v + 1);
  return <button onClick={handleClick}>Count: {value}</button>;
}
```

## Custom Hook Pattern

```jsx
// Correct: custom hooks follow the same rules
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  const increment = () => setCount(c => c + 1);
  const decrement = () => setCount(c => c - 1);
  return { count, increment, decrement };
}

// Usage inside a component
function Counter() {
  const { count, increment, decrement } = useCounter(0);
  return (
    <div>
      <button onClick={decrement}>-</button>
      <span>{count}</span>
      <button onClick={increment}>+</button>
    </div>
  );
}
```

## Related Errors

- [React Key Warning]({{< relref "/languages/javascript/react-keys" >}}) — missing keys in list rendering
- [React State Update on Unmounted]({{< relref "/languages/javascript/react-state-update" >}}) — state updates on unmounted components
- [Cannot Read Properties of undefined]({{< relref "/languages/javascript/react-undefined-prop" >}}) — undefined access in components
