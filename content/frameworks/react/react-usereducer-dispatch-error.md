---
title: "[Solution] React useReducer Dispatch Error"
description: "Error when useReducer dispatch is called with incorrect action."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when useReducer dispatch is called with incorrect action.

## Common Causes

Dispatching actions without type property.

## How to Fix

Ensure every action has a valid type.

## Example

```javascript
dispatch({ type: 'INCREMENT' });
```
