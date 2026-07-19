---
title: "[Solution] ERR_UNKNOWN_FILE_EXTENSION — Unknown File Extension Error Fix"
description: "Fix ERR_UNKNOWN_FILE_EXTENSION when Node.js encounters an unrecognized file type."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_UNKNOWN_FILE_EXTENSION

```bash
# Error when running TypeScript directly
node script.ts  # ERR_UNKNOWN_FILE_EXTENSION .ts

# Fix — use tsx or ts-node
npx tsx script.ts
npx ts-node script.ts
```

Or register a loader:

```bash
node --loader ts-node/esm script.ts
```
