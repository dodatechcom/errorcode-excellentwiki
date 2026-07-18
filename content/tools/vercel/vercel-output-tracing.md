---
title: "[Solution] Vercel Output Tracing Error — Fix File Tracing Failed"
description: "Fix Vercel output tracing errors when the build system cannot detect required files. Configure file tracing includes and excludes for serverless functions."
tools: ["vercel"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

A Vercel output tracing error occurs when the build system cannot find or trace all files required by serverless functions. The deployment fails because essential files are missing.

## What This Error Means

Vercel traces your code to find all required files (node_modules, static assets, configs). When tracing fails:

```
Error: Failed to trace output files for serverless function api/users
Missing: /var/task/node_modules/some-dep/package.json
```

## Why It Happens

- A dynamic require or import cannot be statically analyzed
- A dependency is installed but not detected by the tracing algorithm
- Monorepo dependencies are hoisted outside the function root
- Native modules or binaries are not part of the traced output
- Symlinks confuse the file tracing algorithm
- The `.vercel/output` directory has incomplete build artifacts

## How to Fix It

### Use Explicit Includes in vercel.json

```json
{
  "functions": {
    "api/**/*.js": {
      "includeFiles": "node_modules/**"
    }
  }
}
```

### Include Specific Directories

```json
{
  "functions": {
    "api/**/*.js": {
      "includeFiles": "public/**"
    }
  }
}
```

### Avoid Dynamic Requires

```javascript
// Avoid this (cannot be traced):
const moduleName = getModuleName();
const mod = require(moduleName);

// Use this instead:
const { feature1, feature2 } = {
  feature1: require('./features/feature1'),
  feature2: require('./features/feature2'),
};
const mod = features[getModuleName()];
```

### Configure Monorepo Dependencies

```json
{
  "functions": {
    "api/**/*.js": {
      "includeFiles": "../../packages/**"
    }
  }
}
```

### Force Include All Node Modules

```json
{
  "functions": {
    "api/**/*.js": {
      "includeFiles": "**"
    }
  }
}
```

### Check the Trace Output

```bash
vercel build --debug | grep "tracing"
```

## Common Mistakes

- Using dynamic requires with computed paths that cannot be statically traced
- Not configuring `includeFiles` for functions that use monorepo shared packages
- Assuming all devDependencies are available in production (only dependencies are included)
- Ignoring the trace output and deploying broken functions

## Related Pages

- [Vercel Build Error]({{< relref "/tools/vercel/vercel-build-error" >}}) -- Build failures
- [Vercel Missing Function Error]({{< relref "/tools/vercel/vercel-missing-function" >}}) -- Function not found
- [Vercel Serverless Error]({{< relref "/tools/vercel/vercel-serverless-error" >}}) -- Serverless issues
