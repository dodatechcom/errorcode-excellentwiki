---
title: "[Solution] JavaScript Biome Linter Error — How to Fix"
description: "Fix JavaScript Biome linter configuration errors, lint rule conflicts, formatter discrepancies, and migration failures from ESLint."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 815
---

# JavaScript Biome Linter Error

A `BiomeError`, `DiagnosticError`, or `ConfigurationError` occurs when `biome.json` is misconfigured, lint rules conflict with each other, formatting rules produce unexpected output, or migrating from ESLint leaves stale configuration.

## Why It Happens

Biome errors arise from invalid `biome.json` syntax, incompatible rule configurations in the `linter` and `formatter` sections, missing or incorrect `include`/`ignore` patterns, version mismatches in the Biome binary, and leftover ESLint config files that cause confusion.

## Common Error Messages

- `Error: Could not find biome.json in project root`
- `Error: Configuration file is not valid JSON`
- `Error: Rule "noUnusedVariables" is not configured correctly`
- `Error: Formatter and linter have conflicting settings for "indentStyle"`
- `Error: Migration failed: ESLint config not found or empty`

## How to Fix It

### Fix 1: Create valid biome.json

```json
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
  "organizeImports": {
    "enabled": true
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "correctness": {
        "noUnusedVariables": "error"
      }
    }
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  }
}
```

### Fix 2: Resolve conflicting settings

```json
{
  "formatter": {
    "indentStyle": "space",
    "indentWidth": 2
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single",
      "trailingCommas": "all",
      "semicolons": "always"
    }
  }
}
```

```javascript
// ❌ Wrong - mixed quotes in file
// const name = "hello"
// const greeting = 'world'

// ✅ Correct - consistent with biome config
const name = 'hello'
const greeting = 'world'
```

### Fix 3: Use ignore patterns

```json
{
  "files": {
    "include": ["src/**/*.js", "src/**/*.ts"],
    "ignore": ["dist/**", "node_modules/**", "coverage/**"]
  },
  "linter": {
    "enabled": true,
    "rules": {
      "correctness": {
        "noUnusedVariables": "error"
      }
    },
    "ignore": ["**/*.test.js", "**/*.spec.js"]
  }
}
```

### Fix 4: Migrate from ESLint

```bash
# ❌ Wrong - keeping both eslintrc and biome.json
# ✅ Correct - run migration and remove ESLint

# Run migration to convert ESLint config
npx @biomejs/biome migrate eslint

# Remove ESLint after verifying
rm .eslintrc.json .eslintignore

# Format and lint with Biome
npx @biomejs/biome check --apply .
```

## Examples

Full Biome configuration for TypeScript project:

```json
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
  "organizeImports": { "enabled": true },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "correctness": {
        "noUnusedVariables": "error",
        "noUnusedImports": "error"
      },
      "style": {
        "noNonNullAssertion": "off"
      },
      "complexity": {
        "noBannedTypes": "warn"
      }
    }
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single",
      "semicolons": "asNeeded",
      "trailingComma": "all"
    }
  },
  "files": {
    "ignore": ["dist", "node_modules", "*.config.js"]
  }
}
```

## Related Errors

- [ESLint Error](/languages/javascript/eslint-error)
- [Prettier Error](/languages/javascript/prettier-error)
- [JavaScript SWC Error](/languages/javascript/js-swc-error)
