---
title: "Solved JavaScript browserslist Error — How to Fix"
date: 2026-03-20T18:35:40+00:00
description: "Learn how to resolve JavaScript browserslist browser compatibility configuration errors."
categories: ["javascript"]
keywords: ["browserslist error", "browser compatibility", "browserslist config", "target browsers", "compatibility"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

browserslist errors occur when browser targets are invalid, configuration conflicts, or queries return empty results. The tool specifies browser support targets.

Common causes include:
- Invalid query syntax
- Conflicting configurations
- Empty query results
- Missing configuration file
- Version format errors

## Common Error Messages

```
Error: Unknown browser query `bad browser`
```

```
Browserslist: caniuse-lite is outdated
```

```
Error: No browsers were passed to Browserslist
```

## How to Fix It

### 1. Configure browserslist

Set up browser targets.

```json
// package.json
{
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

```bash
# .browserslistrc
> 0.2%
not dead
not ie 11
not op_mini all
```

### 2. Query Browser Support

Check browser coverage.

```bash
# Check coverage
npx browserslist

# Update caniuse-lite
npx update-browserslist-db@latest
```

### 3. Use with Tools

Integrate with build tools.

```javascript
// babel.config.js
export default {
  presets: [
    ["@babel/preset-env", {
      useBuiltIns: "usage",
      corejs: 3
    }]
  ]
};

// postcss.config.js
export default {
  plugins: {
    "autoprefixer": {}
  }
};
```

## Common Scenarios

### Scenario 1: Modern Browsers

Target modern browsers:

```json
{
  "browserslist": [
    "defaults",
    "not ie 11",
    "not ie_mob 11"
  ]
}
```

### Scenario 2: Legacy Support

Support older browsers:

```json
{
  "browserslist": [
    "> 0.5%",
    "last 2 versions",
    "not dead",
    "not < 0.2%"
  ]
}
```

## Prevent It

- Run `npx update-browserslist-db@latest` regularly
- Use `> 0.2%, not dead` for modern but not cutting-edge
- Don't include `ie 11` unless absolutely necessary
- Check coverage with `npx browserslist`
- Keep caniuse-lite database updated