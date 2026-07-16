---
title: "[Solution] React useContext Must Be Used Within a Provider — Context Error Fix"
description: "Fix React 'useContext must be used within a Provider' error. Understand context scope, provider nesting, and how to handle missing providers."
languages: ["javascript"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["react", "context", "useContext", "provider", "context-error"]
weight: 5
---

# React: useContext Must Be Used Within a Provider

This error occurs when you call `useContext(SomeContext)` in a component that is not rendered within the corresponding `<SomeContext.Provider>`. React requires that context consumers are descendants of their matching provider in the component tree.

## Common Causes

- **Provider missing in component tree** — the component using the context is not wrapped by its Provider
- **Provider at wrong level** — Provider wraps the wrong branch of the component tree
- **Context created but never provided** — `createContext()` is called but no Provider is rendered
- **Component rendered outside the app tree** — testing or portal rendering without providers

## How to Fix

```jsx
// Cause 1: Using context without Provider
import { createContext, useContext } from "react";

const ThemeContext = createContext(null);

function ThemedButton() {
  const theme = useContext(ThemeContext);  // Error if no Provider above
  return <button className={theme}>Click</button>;
}

// Fix: wrap consumers in Provider
function App() {
  return (
    <ThemeContext.Provider value="dark">
      <ThemedButton />
    </ThemeContext.Provider>
  );
}

// Cause 2: Provider at wrong level
function WrongLayout() {
  return (
    <ThemeContext.Provider value="dark">
      <Header />
    </ThemeContext.Provider>
  );
  // Footer uses ThemeContext but is OUTSIDE the Provider
}

// Fix: ensure Provider wraps all consumers
function CorrectLayout() {
  return (
    <ThemeContext.Provider value="dark">
      <Header />
      <Main />
      <Footer />
    </ThemeContext.Provider>
  );
}
```

```jsx
// Provide a default value that indicates "no provider"
const ThemeContext = createContext("light");  // default value

// Or use undefined to detect missing provider
const ThemeContext = createContext(undefined);

function useTheme() {
  const theme = useContext(ThemeContext);
  if (theme === undefined) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return theme;
}

function ThemedButton() {
  const theme = useTheme();  // throws descriptive error if no provider
  return <button className={theme}>Click</button>;
}
```

```jsx
// Nested providers pattern
function App() {
  const [theme, setTheme] = useState("light");
  const [user, setUser] = useState(null);

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <UserContext.Provider value={{ user, setUser }}>
        <Layout />
      </UserContext.Provider>
    </ThemeContext.Provider>
  );
}
```

## Example: Full Provider Setup

```jsx
import { createContext, useContext, useState } from "react";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = (credentials) => {
    // login logic
    setUser({ name: "Alice" });
  };

  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
}

// Usage
function App() {
  return (
    <AuthProvider>
      <Dashboard />
    </AuthProvider>
  );
}

function Dashboard() {
  const { user, logout } = useAuth();
  return (
    <div>
      <h1>Welcome, {user?.name}</h1>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
```

## Related Errors

- [React Hooks Violation]({{< relref "/languages/javascript/react-hooks" >}}) — hooks called outside components
- [React State Update on Unmounted]({{< relref "/languages/javascript/react-state-update" >}}) — state updates after unmount
- [React Lazy Error]({{< relref "/languages/javascript/react-lazy-error" >}}) — React.lazy type mismatch
