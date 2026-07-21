---
title: "[Solution] React Unexpected Token in JSX"
description: "Unexpected token errors appear when expressions inside JSX are malformed."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Unexpected token errors appear when expressions inside JSX are malformed.

## Common Causes

Expression syntax issues inside JSX curly braces.

## How to Fix

Ensure expressions use correct JS syntax inside curly braces.

## Example

```jsx
<div>{items.map(item => <span key={item.id}>{item.name}</span>)}</div>
```
