---
title: "[Solution] React useContext Not Found Error"
description: "Error when useContext is called without a matching Provider."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when useContext is called without a matching Provider.

## Common Causes

Using useContext without a Provider.

## How to Fix

Wrap component in the corresponding Provider.

## Example

```jsx
<ThemeContext.Provider value="dark"><ThemedButton /></ThemeContext.Provider>
```
