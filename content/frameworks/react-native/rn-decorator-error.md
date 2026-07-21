---
title: "[Solution] React Native Decorator/ES Legacy Support Error"
description: "react-native Metro bundler throws Babel transform error for experimental legacy decorator syntax used in JavaScript or TypeScript React Native projects"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The decorator error occurs when TypeScript or JavaScript files use legacy decorator syntax that the Babel presets in React Native's Metro config cannot parse. React Native 0.72+ uses the TypeScript parser directly, which expects the TC39 stage-3 decorator proposal.

## Common Causes

- Project uses @decorator syntax without enabling the Babel plugin
- TypeScript experimentalDecorators enabled without matching Babel plugin
- React Native version does not ship the default decorator plugin
- Metro config override removes the default Babel presets
- mix of legacy and TC39 decorator syntax in the same file

## How to Fix

1. Install the Babel decorator plugin:

```bash
npm install --save-dev @babel/plugin-proposal-decorators
```

2. Update babel.config.js:

```javascript
module.exports = {
  presets: ['module:@react-native/babel-preset'],
  plugins: [
    ['@babel/plugin-proposal-decorators', { legacy: true }],
  ],
};
```

3. For TypeScript projects using legacy decorators:

```json
// tsconfig.json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "useDefineForClassFields": true
  }
}
```

## Examples

```javascript
// Error: Support for the legacy experimental decorators syntax in TypeScript was removed in Metro
// Fix: add Babel plugin
// babel.config.js
plugins: [
  ['@babel/plugin-proposal-decorators', { legacy: false, version: '2022-03' }]
```

## Related Errors

- [Transform Error]({{< relref "/frameworks/react-native/rn-transform-error" >}})
- [TypeScript Error]({{< relref "/frameworks/react-native/rn-typescript-error" >}})
