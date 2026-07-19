---
title: "React state management anti-patterns"
description: "Common state management anti-patterns in React applications. This includes overcomplicating state, duplicating state, putting derived state in state, or storing props in state unnecessarily."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "state", "anti-pattern", "architecture"]
severity: "warning"
solution: "Keep state minimal and derived. Don't put computed values in state. Derive values during render instead of storing them. Use state lifting judiciously. Consider state machines for complex state logic."
---

Common state management anti-patterns in React applications. This includes overcomplicating state, duplicating state, putting derived state in state, or storing props in state unnecessarily.

## Solution

Keep state minimal and derived. Don't put computed values in state. Derive values during render instead of storing them. Use state lifting judiciously. Consider state machines for complex state logic.

## Code Example

```javascript
  import { useState, useMemo } from 'react';
  
  // BAD: Duplicating state
  function BadForm() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [fullName, setFullName] = useState(''); // Duplicated!
    
    const handleFirstChange = (e) => {
      setFirstName(e.target.value);
      setFullName(`${e.target.value} ${lastName}`); // Maintain duplicate
    };
    
    return <input value={firstName} onChange={handleFirstChange} />;
  }
  
  // GOOD: Derive values during render
  function GoodForm() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    
    // Derived value, not state
    const fullName = `${firstName} ${lastName}`;
    
    return (
      <div>
        <input 
          value={firstName} 
          onChange={e => setFirstName(e.target.value)} 
        />
        <input 
          value={lastName} 
          onChange={e => setLastName(e.target.value)} 
        />
        <p>Full name: {fullName}</p>
      </div>
    );
  }
  
  // BAD: Storing props in state
  function BadPropsInState({ items }) {
    const [localItems, setLocalItems] = useState(items); // Unnecessary copy
    
    return (
      <ul>
        {localItems.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    );
  }
  
  // GOOD: Use props directly
  function GoodPropsUsage({ items }) {
    return (
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    );
  }
  
  // GOOD: Use state machines for complex state
  const STATES = {
    IDLE: 'idle',
    LOADING: 'loading',
    SUCCESS: 'success',
    ERROR: 'error'
  };
  
  function useAsyncOperation() {
    const [state, setState] = useState({
      status: STATES.IDLE,
      data: null,
      error: null
    });
    
    const execute = async (asyncFn) => {
      setState({ status: STATES.LOADING, data: null, error: null });
      try {
        const data = await asyncFn();
        setState({ status: STATES.SUCCESS, data, error: null });
      } catch (error) {
        setState({ status: STATES.ERROR, data: null, error });
      }
    };
    
    return { ...state, execute };
  }
```
