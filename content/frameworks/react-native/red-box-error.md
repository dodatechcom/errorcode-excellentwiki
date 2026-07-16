---
title: "Red Box Error - Unable to Resolve Module"
description: "React Native displays a red box error when it cannot resolve a module import during development"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["module", "import", "bundler", "metro"]
weight: 5
---

## What This Error Means

The Red Box error "Unable to resolve module" appears when React Native's Metro bundler cannot find a module that your code is trying to import. This typically happens during development when the module path is incorrect or the module is not installed.

## Common Causes

- Incorrect import path or module name typo
- Module not installed in node_modules
- Missing dependencies that need to be linked
- Metro bundler cache is stale or corrupted

## How to Fix

**Check your import path:**

```javascript
// Wrong - incorrect path
import MyComponent from './Component';

// Correct - verify the file exists at this path
import MyComponent from './components/MyComponent';
```

**Clear Metro cache and restart:**

```bash
npx react-native start --reset-cache
```

**Install missing dependencies:**

```bash
npm install <module-name>
# or
yarn add <module-name>
```

## Examples

```javascript
// This error occurs when:
import { StyleSheet } from 'react-native'; // Module exists

import { SomeNonExistent } from 'missing-module'; // Triggers Red Box
```

## Related Errors

- [Native Module Error]({{< relref "/frameworks/react-native/native-module-error" >}})
