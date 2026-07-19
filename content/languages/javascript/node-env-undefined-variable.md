---
title: "[Solution] Node.js process.env Undefined — Environment Variable Not Set"
description: "Fix errors when process.env variables are undefined. Use defaults and validate environment configuration."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# process.env Undefined Variables

```javascript
// BUG — will be undefined if not set
const dbUrl = process.env.DATABASE_URL; // undefined

// Fix — use default value
const dbUrl = process.env.DATABASE_URL || 'localhost:5432';

// Better — fail fast
const dbUrl = process.env.DATABASE_URL;
if (!dbUrl) {
  throw new Error('DATABASE_URL environment variable is required');
}
```
