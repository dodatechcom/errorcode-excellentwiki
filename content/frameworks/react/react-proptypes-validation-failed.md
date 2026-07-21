---
title: "[Solution] React PropTypes Validation Failed"
description: "Warning when prop types don't match."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning when prop types don't match.

## Common Causes

Wrong types passed.

## How to Fix

Fix parent to pass correct types.

## Example

```javascript
B.propTypes = { label: PropTypes.string.isRequired };
```
