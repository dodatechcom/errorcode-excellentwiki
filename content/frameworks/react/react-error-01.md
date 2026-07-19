---
title: "Each child in a list should have a unique key prop"
description: "React warning that occurs when rendering lists without unique keys for each element. This happens when using array indices as keys for dynamic lists that change order, or when rendering elements without any key prop at all."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "list-rendering", "performance"]
severity: "warning"
solution: "Always provide a unique, stable identifier as the key prop when rendering lists. Avoid using array indices as keys if the list items can be reordered, added, or removed. Use unique IDs from your data, or generate stable keys using a library like uuid."
---

React warning that occurs when rendering lists without unique keys for each element. This happens when using array indices as keys for dynamic lists that change order, or when rendering elements without any key prop at all.

## Solution

Always provide a unique, stable identifier as the key prop when rendering lists. Avoid using array indices as keys if the list items can be reordered, added, or removed. Use unique IDs from your data, or generate stable keys using a library like uuid.

## Code Example

```javascript
  import { v4 as uuidv4 } from 'uuid';
  
  function TodoList({ todos }) {
    return (
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            {todo.text}
          </li>
        ))}
      </ul>
    );
  }
  
  // BAD: Using index as key
  function BadTodoList({ todos }) {
    return (
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo.text}
          </li>
        ))}
      </ul>
    );
  }
```
