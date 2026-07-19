---
title: "React prop drilling issues"
description: "Issues related to prop drilling in React applications where props are passed through multiple layers of components that don't use them, leading to unnecessary re-renders and complex component hierarchies."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "prop-drilling", "architecture", "state"]
severity: "warning"
solution: "Use React Context for truly global state. Split state into separate contexts. Use state management libraries like Zustand or Redux for complex state. Move state closer to where it's needed."
---

Issues related to prop drilling in React applications where props are passed through multiple layers of components that don't use them, leading to unnecessary re-renders and complex component hierarchies.

## Solution

Use React Context for truly global state. Split state into separate contexts. Use state management libraries like Zustand or Redux for complex state. Move state closer to where it's needed.

## Code Example

```javascript
  import { createContext, useContext, useState } from 'react';
  
  // BAD: Deep prop drilling
  function App() {
    const [user, setUser] = useState(null);
    const [theme, setTheme] = useState('light');
    
    return (
      <Layout user={user} theme={theme}>
        <Header user={user} theme={theme}>
          <Navigation user={user} />
        </Header>
      </Layout>
    );
  }
  
  // GOOD: Using Context for global state
  const AuthContext = createContext(null);
  const ThemeContext = createContext('light');
  
  function App() {
    return (
      <AuthProvider>
        <ThemeProvider>
          <Layout>
            <Header>
              <Navigation />
            </Header>
          </Layout>
        </ThemeProvider>
      </AuthProvider>
    );
  }
  
  function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    
    return (
      <AuthContext.Provider value={{ user, setUser }}>
        {children}
      </AuthContext.Provider>
    );
  }
  
  function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');
    
    return (
      <ThemeContext.Provider value={{ theme, setTheme }}>
        {children}
      </ThemeContext.Provider>
    );
  }
  
  // GOOD: Move state closer to usage
  function CommentBox() {
    // State only where needed
    const [text, setText] = useState('');
    
    return (
      <div>
        <textarea value={text} onChange={e => setText(e.target.value)} />
        <SubmitButton disabled={!text} />
      </div>
    );
  }
```
