---
title: "[Solution] React Fragment Key Prop Error"
description: "Error when passing key prop to shorthand fragment."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when passing key prop to shorthand fragment.

## Common Causes

Using key with shorthand fragment.

## How to Fix

Use explicit Fragment component.

## Example

```jsx
import { Fragment } from 'react';
items.map(i => <Fragment key={i.id}><div /></Fragment>)
```
