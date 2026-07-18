---
title: "Solved JavaScript eslint Error — How to Fix"
date: 2026-03-20T17:00:30+00:00
description: "Learn how to resolve JavaScript ESLint linting configuration and rule errors."
categories: ["javascript"]
keywords: ["eslint error", "eslint config", "linting error", "eslint rules", "code quality"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

ESLint errors occur when code violates configured rules, configuration files have syntax errors, or plugins conflict. The linter enforces code style but requires proper setup.

Common causes include:
- Invalid configuration file syntax
- Missing plugin or parser
- Conflicting rule configurations
- Extending nonexistent configs
- Rule options malformed

## Common Error Messages

```
Error: .eslintrc.js:5:1 - Parsing error: Unexpected token
```

```
Error: Cannot find module 'eslint-plugin-react'
```

```
Error: Definition for rule 'react/prop-types' was not found
```

## How to Fix It

### 1. Configure ESLint

Set up ESLint configuration.

```javascript
// eslint.config.js (flat config)
import js from "@eslint/js";
import react from "eslint-plugin-react";
import tsParser from "@typescript-eslint/parser";

export default [
  js.configs.recommended,
  {
    files: ["**/*.{js,jsx,ts,tsx}"],
    plugins: {
      react
    },
    languageOptions: {
      parser: tsParser,
      ecmaVersion: "latest",
      sourceType: "module",
      parserOptions: {
        ecmaFeatures: {
          jsx: true
        }
      }
    },
    rules: {
      "no-unused-vars": "warn",
      "no-console": "warn",
      "prefer-const": "error",
      "react/prop-types": "off",
      "react/react-in-jsx-scope": "off"
    },
    settings: {
      react: {
        version: "detect"
      }
    }
  },
  {
    ignores: ["dist/", "node_modules/"]
  }
];
```

### 2. Fix Common Issues

Resolve linting errors.

```javascript
// ❌ Wrong - unused variable
function Component({ data, onAction }) {
  return <div>{data}</div>;
}

// ✅ Correct - prefix unused with underscore
function Component({ data, onAction: _onAction }) {
  return <div>{data}</div>;
}

// ❌ Wrong - console.log in production
function fetchData() {
  console.log("Fetching...");
  return api.get("/data");
}

// ✅ Correct - use conditional or remove
function fetchData() {
  if (process.env.NODE_ENV === "development") {
    console.log("Fetching...");
  }
  return api.get("/data");
}

// ❌ Wrong - let when should be const
let name = "John";

// ✅ Correct - use const for non-reassigned
const name = "John";
```

### 3. Add Overrides

Configure file-specific rules.

```javascript
export default [
  {
    files: ["**/*.{js,jsx,ts,tsx}"],
    rules: {
      "no-console": "warn"
    }
  },
  {
    files: ["**/*.test.{js,jsx,ts,tsx}"],
    rules: {
      "no-console": "off",
      "@typescript-eslint/no-explicit-any": "off"
    }
  },
  {
    files: ["**/scripts/**/*.{js,ts}"],
    rules: {
      "no-console": "off"
    }
  }
];
```

## Common Scenarios

### Scenario 1: TypeScript ESLint

Configure for TypeScript:

```javascript
import tsPlugin from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";

export default [
  {
    files: ["**/*.{ts,tsx}"],
    plugins: {
      "@typescript-eslint": tsPlugin
    },
    languageOptions: {
      parser: tsParser
    },
    rules: {
      "@typescript-eslint/no-unused-vars": "warn",
      "@typescript-eslint/explicit-function-return-type": "off",
      "@typescript-eslint/no-explicit-any": "warn"
    }
  }
];
```

### Scenario 2: Prettier Integration

Use with Prettier:

```javascript
import prettierConfig from "eslint-config-prettier";

export default [
  prettierConfig, // Disables conflicting rules
  {
    rules: {
      // Prettier handles formatting
      "indent": "off",
      "quotes": "off",
      "semi": "off"
    }
  }
];
```

## Prevent It

- Use `eslint.config.js` (flat config) for new projects
- Run `npx eslint --fix` to auto-fix issues
- Add `@typescript-eslint` for TypeScript projects
- Use `eslint-config-prettier` to avoid formatting conflicts
- Create `.eslintignore` to skip generated files