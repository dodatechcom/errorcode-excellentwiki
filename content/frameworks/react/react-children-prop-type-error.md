---
title: "[Solution] React Children Prop Type Error"
description: "Error when children type mismatches."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when children type mismatches.

## Common Causes

Wrong types as children.

## How to Fix

Use PropTypes to validate.

## Example

```javascript
C.propTypes = { children: PropTypes.node.isRequired };
```
