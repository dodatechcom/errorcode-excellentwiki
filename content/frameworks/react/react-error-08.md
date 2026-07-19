---
title: "Ref forwarding errors in React components"
description: "React error that occurs when trying to pass refs to function components without using forwardRef. Function components cannot receive refs directly and need forwardRef to expose the ref to parent components."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "refs", "forwardref", "components"]
severity: "error"
solution: "Use forwardRef to wrap components that need to receive refs from parents. Alternatively, use useImperativeHandle to customize the ref value. For simpler cases, consider using ref callback props instead of forwardRef."
---

React error that occurs when trying to pass refs to function components without using forwardRef. Function components cannot receive refs directly and need forwardRef to expose the ref to parent components.

## Solution

Use forwardRef to wrap components that need to receive refs from parents. Alternatively, use useImperativeHandle to customize the ref value. For simpler cases, consider using ref callback props instead of forwardRef.

## Code Example

```javascript
  import { forwardRef, useRef, useImperativeHandle } from 'react';
  
  // BAD: Function component cannot receive ref
  function BadInput({ value, onChange }) {
    return <input value={value} onChange={onChange} />;
  }
  
  function Parent() {
    const inputRef = useRef(null);
    return <BadInput ref={inputRef} />; // Error!
  }
  
  // GOOD: Use forwardRef
  const GoodInput = forwardRef(({ value, onChange }, ref) => {
    return <input ref={ref} value={value} onChange={onChange} />;
  });
  
  function Parent() {
    const inputRef = useRef(null);
    
    const focusInput = () => {
      inputRef.current?.focus();
    };
    
    return (
      <div>
        <GoodInput ref={inputRef} />
        <button onClick={focusInput}>Focus</button>
      </div>
    );
  }
  
  // GOOD: Using useImperativeHandle
  const CustomInput = forwardRef(({ value, onChange }, ref) => {
    const inputRef = useRef(null);
    
    useImperativeHandle(ref, () => ({
      focus: () => inputRef.current?.focus(),
      clear: () => inputRef.current?.select()
    }));
    
    return <input ref={inputRef} value={value} onChange={onChange} />;
  });
```
