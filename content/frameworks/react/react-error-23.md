---
title: "React key prop performance issues"
description: "Performance issues related to improper use of key props in React lists. Using array indices as keys for dynamic lists can cause unnecessary re-renders and state preservation issues."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "performance", "key", "list"]
severity: "warning"
solution: "Use unique, stable identifiers from your data as keys. Avoid using Math.random() or Date.now() as keys. If no unique ID exists, generate one when data is created, not during render."
---

Performance issues related to improper use of key props in React lists. Using array indices as keys for dynamic lists can cause unnecessary re-renders and state preservation issues.

## Solution

Use unique, stable identifiers from your data as keys. Avoid using Math.random() or Date.now() as keys. If no unique ID exists, generate one when data is created, not during render.

## Code Example

```javascript
  import { v4 as uuidv4 } from 'uuid';
  
  // BAD: Using index as key for dynamic list
  function BadTodoList({ todos }) {
    return (
      <ul>
        {todos.map((todo, index) => (
          <TodoItem key={index} todo={todo} />
        ))}
      </ul>
    );
  }
  
  // BAD: Using Math.random() as key
  function BadRandomList() {
    const items = ['a', 'b', 'c'];
    return (
      <ul>
        {items.map(item => (
          <li key={Math.random()}>{item}</li>
        ))}
      </ul>
    );
  }
  
  // GOOD: Using unique ID from data
  function GoodTodoList({ todos }) {
    return (
      <ul>
        {todos.map(todo => (
          <TodoItem key={todo.id} todo={todo} />
        ))}
      </ul>
    );
  }
  
  // GOOD: Generate stable IDs when creating data
  function TodoApp() {
    const [todos, setTodos] = useState([]);
    
    const addTodo = (text) => {
      setTodos(prev => [
        ...prev,
        { id: uuidv4(), text, completed: false }
      ]);
    };
    
    return (
      <div>
        <TodoForm onAdd={addTodo} />
        <TodoList todos={todos} />
      </div>
    );
  }
```
