---
title: "Solved JavaScript react-hook Error — How to Fix"
date: 2026-03-20T16:15:55+00:00
description: "Learn how to resolve JavaScript custom React hooks and React hooks rules violations."
categories: ["javascript"]
keywords: ["react hooks error", "hooks rules", "useeffect error", "custom hooks", "react hook violation"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

React hooks errors occur when hooks are called conditionally, inside loops, or outside React components. React maintains a call order that must be consistent between renders.

Common causes include:
- Hook called inside conditional statement
- Hook called inside loop or nested function
- Hook called in non-component function
- Missing dependency in useEffect array
- Cleanup function not returned properly

## Common Error Messages

```
Error: Invalid hook call. Hooks can only be called inside of the body of a function component
```

```
Error: React Hook "useEffect" has a missing dependency
```

```
Warning: React has detected a change in the order of Hooks
```

## How to Fix It

### 1. Follow Hooks Rules

Always call hooks at the top level.

```jsx
// ❌ Wrong - conditional hook
function BadComponent({ showDetails }) {
  if (showDetails) {
    const [details, setDetails] = useState(null); // Error!
  }
  return <div>...</div>;
}

// ✅ Correct - hooks at top level
function GoodComponent({ showDetails }) {
  const [details, setDetails] = useState(null);
  
  useEffect(() => {
    if (showDetails) {
      fetchDetails().then(setDetails);
    }
  }, [showDetails]);
  
  return showDetails && details ? <div>{details}</div> : null;
}

// ❌ Wrong - hook in callback
function BadComponent() {
  const handleClick = () => {
    const [count, setCount] = useState(0); // Error!
  };
  return <button onClick={handleClick}>Click</button>;
}
```

### 2. Create Custom Hooks

Extract logic into reusable hooks.

```jsx
import { useState, useEffect, useCallback } from "react";

// Custom hook for API calls
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    let cancelled = false;
    
    async function fetchData() {
      try {
        const response = await fetch(url);
        const json = await response.json();
        
        if (!cancelled) {
          setData(json);
          setLoading(false);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err);
          setLoading(false);
        }
      }
    }
    
    fetchData();
    
    return () => {
      cancelled = true;
    };
  }, [url]);
  
  return { data, loading, error };
}

// Custom hook for localStorage
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });
  
  const setValue = useCallback((value) => {
    setStoredValue((prev) => {
      const newValue = value instanceof Function ? value(prev) : value;
      window.localStorage.setItem(key, JSON.stringify(newValue));
      return newValue;
    });
  }, [key]);
  
  return [storedValue, setValue];
}

// Usage
function UserProfile() {
  const { data: user, loading, error } = useFetch("/api/user");
  const [theme, setTheme] = useLocalStorage("theme", "light");
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return (
    <div data-theme={theme}>
      <h1>{user.name}</h1>
      <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
        Toggle Theme
      </button>
    </div>
  );
}
```

### 3. Handle Dependencies Correctly

Manage useEffect dependencies.

```jsx
// ❌ Wrong - missing dependency
function BadComponent({ userId }) {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, []); // Missing userId dependency!
}

// ✅ Correct - proper dependencies
function GoodComponent({ userId }) {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]); // userId in dependency array
}

// ✅ Correct - effect that doesn't need dependencies
function GoodComponent2() {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]); // Only runs when count changes
}

// ✅ Correct - cleanup function
function GoodComponent3() {
  useEffect(() => {
    const interval = setInterval(() => {
      console.log("tick");
    }, 1000);
    
    return () => clearInterval(interval); // Cleanup
  }, []);
}
```

## Common Scenarios

### Scenario 1: Debounced Input

Create debounce hook:

```jsx
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => clearTimeout(timer);
  }, [value, delay]);
  
  return debouncedValue;
}

function SearchInput() {
  const [query, setQuery] = useState("");
  const debouncedQuery = useDebounce(query, 300);
  
  useEffect(() => {
    if (debouncedQuery) {
      searchAPI(debouncedQuery);
    }
  }, [debouncedQuery]);
  
  return (
    <input
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Search..."
    />
  );
}
```

### Scenario 2: Window Size Hook

Track window dimensions:

```jsx
function useWindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });
  
  useEffect(() => {
    let timeoutId;
    
    const handleResize = () => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        setSize({
          width: window.innerWidth,
          height: window.innerHeight
        });
      }, 100);
    };
    
    window.addEventListener("resize", handleResize);
    
    return () => {
      clearTimeout(timeoutId);
      window.removeEventListener("resize", handleResize);
    };
  }, []);
  
  return size;
}
```

## Prevent It

- Never call hooks inside conditions, loops, or nested functions
- Only call hooks from React components or custom hooks
- Include all dependencies in useEffect dependency array
- Use `useCallback` and `useMemo` for expensive computations
- Always return cleanup functions for subscriptions and timers