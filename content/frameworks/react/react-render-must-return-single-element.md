---
title: "[Solution] React Render Must Return Single Element"
description: "Error when render returns multiple root elements."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when render returns multiple root elements.

## Common Causes

Adjacent elements without wrapper.

## How to Fix

Wrap in Fragment or parent.

## Example

```jsx
return (<><h1>Title</h1><p>Content</p></>);
```
