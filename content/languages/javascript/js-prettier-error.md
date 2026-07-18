---
title: "Solved JavaScript prettier Error — How to Fix"
date: 2026-03-20T17:05:40+00:00
description: "Learn how to resolve JavaScript Prettier code formatting configuration and parser errors."
categories: ["javascript"]
keywords: ["prettier error", "prettier config", "code formatting", "prettier format", "code style"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Prettier errors occur when configuration conflicts with project settings, parser can't handle file type, or ignore patterns are invalid. Prettier is opinionated but requires correct setup.

Common causes include:
- Conflicting rules between Prettier and ESLint
- Invalid configuration file syntax
- Parser not available for file type
- Ignore patterns blocking expected files
- Options incompatible with each other

## Common Error Messages

```
Error: Couldn't resolve parser "babel"
```

```
Error: Incompatible options: "trailingComma" and "箭头函数"
```

```
Warning: Code style issues detected
```

## How to Fix It

### 1. Configure Prettier

Set up prettier configuration.

```javascript
// .prettierrc.js
export default {
  semi: true,
  singleQuote: true,
  tabWidth: 2,
  useTabs: false,
  trailingComma: "es5",
  printWidth: 80,
  bracketSpacing: true,
  arrowParens: "always",
  endOfLine: "lf",
  plugins: [],
  overrides: [
    {
      files: "*.md",
      options: {
        printWidth: 100
      }
    },
    {
      files: "*.json",
      options: {
        printWidth: 40
      }
    }
  ]
};

// Or JSON format
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "es5"
}
```

### 2. Format Code

Apply formatting.

```bash
# Format single file
npx prettier --write src/index.js

# Format all files
npx prettier --write "src/**/*.{js,jsx,ts,tsx}"

# Check without writing
npx prettier --check "src/**/*.{js,jsx,ts,tsx}"

# Format with specific config
npx prettier --config .prettierrc.js --write src/
```

### 3. Handle Common Issues

Fix formatting problems.

```javascript
// ❌ Wrong - inconsistent quotes
let name = "John";
let email = 'john@example.com';

// ✅ Correct - after prettier
let name = "John";
let email = "john@example.com";

// ❌ Wrong - missing semicolons
const greeting = "hello"

// ✅ Correct - after prettier
const greeting = "hello";

// ❌ Wrong - inconsistent spacing
function add(a,b){
return a+b;
}

// ✅ Correct - after prettier
function add(a, b) {
  return a + b;
}
```

## Common Scenarios

### Scenario 1: Ignore Files

Configure ignore patterns:

```bash
# .prettierignore
dist/
node_modules/
coverage/
*.min.js
package-lock.json
pnpm-lock.yaml
yarn.lock
```

### Scenario 2: VS Code Integration

Setup editor integration:

```json
// .vscode/settings.json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "prettier.requireConfig": true
}
```

## Prevent It

- Use `.prettierrc.js` for JavaScript config or `.prettierrc` for JSON
- Add `.prettierignore` to exclude generated files
- Use `--check` in CI to verify formatting
- Don't mix Prettier and ESLint formatting rules
- Use editor integration for auto-formatting on save