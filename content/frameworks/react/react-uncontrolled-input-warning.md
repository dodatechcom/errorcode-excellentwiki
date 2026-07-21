---
title: "[Solution] React Uncontrolled Input Warning"
description: "Issues with uncontrolled inputs."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Issues with uncontrolled inputs.

## Common Causes

defaultValue without onChange.

## How to Fix

Use controlled inputs.

## Example

```jsx
const [v, setV] = useState('');
<input value={v} onChange={e => setV(e.target.value)} />
```
