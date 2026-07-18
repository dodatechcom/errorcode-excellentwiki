---
title: "Solved JavaScript Bun Error — How to Fix"
date: 2026-03-20T12:45:15+00:00
description: "Learn how to resolve JavaScript Bun runtime errors, bundler issues, and compatibility problems."
categories: ["javascript"]
keywords: ["bun error", "bun runtime", "bun bundler", "bun install", "bun compatibility"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Bun errors occur when the JavaScript runtime encounters incompatibilities with Node.js APIs, bundler configuration issues, or module resolution differences. Bun aims for Node.js compatibility but has some behavioral differences.

Common causes include:
- Using Node.js-specific APIs not yet implemented in Bun
- Package with native addons not compiled for Bun's runtime
- Module resolution differences between Bun and Node.js
- Test runner assertions not matching Jest behavior
- WebSocket or server API implementation differences

## Common Error Messages

```
error: Cannot find module '...'
```

```
ReferenceError: Buffer is not defined
```

```
Error: bun: not implemented: crypto.createCipher
```

## How to Fix It

### 1. Use Bun-Compatible APIs

Replace Node.js-specific code with Bun-compatible alternatives.

```javascript
// ❌ Node.js specific
import { readFileSync } from 'fs';
import { join } from 'path';
const config = JSON.parse(readFileSync(join(__dirname, 'config.json')));

// ✅ Bun compatible
import { readFileSync } from 'bun:fs';
const config = JSON.parse(readFileSync('./config.json'));

// Or use import for JSON
import config from './config.json' with { type: 'json' };

// Process API
const port = process.env.PORT || 3000;

// Bun-specific features
import { $ } from 'bun';

// Execute shell commands
const result = await $`ls -la`.text();
console.log(result);
```

### 2. Configure Bun for Your Project

Set up proper Bun configuration.

```json
// package.json
{
  "name": "my-app",
  "scripts": {
    "dev": "bun run --watch src/index.ts",
    "build": "bun build src/index.ts --outdir ./dist",
    "start": "bun run dist/index.js",
    "test": "bun test"
  },
  "dependencies": {
    "hono": "^4.0.0"
  },
  "devDependencies": {
    "@types/bun": "^1.0.0",
    "typescript": "^5.3.0"
  }
}

// tsconfig.json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "types": ["bun-types"],
    "strict": true,
    "skipLibCheck": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### 3. Handle Testing with Bun

Use Bun's built-in test runner.

```typescript
// src/utils.test.ts
import { describe, expect, test } from "bun:test";
import { calculateTotal, formatCurrency } from "./utils";

describe("calculateTotal", () => {
  test("should sum array of numbers", () => {
    expect(calculateTotal([1, 2, 3])).toBe(6);
  });

  test("should handle empty array", () => {
    expect(calculateTotal([])).toBe(0);
  });

  test("should handle negative numbers", () => {
    expect(calculateTotal([1, -2, 3])).toBe(2);
  });
});

describe("formatCurrency", () => {
  test("should format USD correctly", () => {
    expect(formatCurrency(1234.56, "USD")).toBe("$1,234.56");
  });

  test("should format EUR correctly", () => {
    expect(formatCurrency(1234.56, "EUR")).toBe("€1,234.56");
  });
});

// Async tests
describe("async operations", () => {
  test("should fetch data", async () => {
    const data = await fetchData();
    expect(data).toBeDefined();
    expect(data.length).toBeGreaterThan(0);
  });
});
```

```bash
# Run tests
bun test

# Run specific test file
bun test src/utils.test.ts

# Watch mode
bun test --watch

# Coverage
bun test --coverage
```

## Common Scenarios

### Scenario 1: HTTP Server with Bun

Create high-performance HTTP server:

```typescript
// src/server.ts
import { serve } from "bun";

const port = process.env.PORT || 3000;

serve({
  port,
  fetch(req) {
    const url = new URL(req.url);
    
    if (url.pathname === "/") {
      return new Response("Hello World!");
    }
    
    if (url.pathname === "/json") {
      return Response.json({ message: "JSON response" });
    }
    
    if (url.pathname === "/stream") {
      const stream = new ReadableStream({
        start(controller) {
          let count = 0;
          const interval = setInterval(() => {
            controller.enqueue(`data: ${count++}\n\n`);
            if (count > 10) {
              clearInterval(interval);
              controller.close();
            }
          }, 1000);
        }
      });
      
      return new Response(stream, {
        headers: { "Content-Type": "text/event-stream" }
      });
    }
    
    return new Response("Not Found", { status: 404 });
  }
});

console.log(`Server running at http://localhost:${port}`);
```

### Scenario 2: Bun with File I/O

Efficient file operations:

```typescript
import { write, read, file } from "bun";

// Write file
await write("output.txt", "Hello World");

// Read file
const content = await read("output.txt");

// Stream large files
const fileHandle = await file("large-file.csv").stream();
for await (const chunk of fileHandle) {
  processChunk(chunk);
}

// Watch file changes
import { watch } from "fs";
watch("./src", { recursive: true }, (event, filename) => {
  console.log(`File changed: ${filename}`);
});
```

## Prevent It

- Use `bun:test` instead of `jest` for native Bun testing
- Check Bun compatibility at https://bun.sh/docs/runtime/nodejs-apis
- Use `bun build` for faster builds instead of webpack/esbuild
- Set `"types": ["bun-types"]` in tsconfig.json for type safety
- Run `bun --version` to verify latest Bun installation