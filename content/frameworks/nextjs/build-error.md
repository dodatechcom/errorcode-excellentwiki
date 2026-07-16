---
title: "Build error: Failed to compile"
description: "Next.js raises this build error when the application code contains syntax errors, import issues, or configuration problems that prevent compilation."
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["build", "compilation", "webpack", "next-config"]
weight: 5
---

This error occurs during `next build` (or in development mode) when Next.js cannot compile your application. The build log will include the specific compilation error above the general "Failed to compile" message.

## Common Causes

- Syntax error or invalid JSX in a page or component
- Importing a file or package that does not exist or is not installed
- Using CommonJS `require()` in a file that expects ESM imports (or vice versa)
- Invalid `next.config.js` / `next.config.mjs` configuration

## How to Fix

Read the full error message above "Failed to compile" — it will point to the exact file and line number. Common fixes:

```bash
# Reinstall node_modules if the error is about missing packages
rm -rf node_modules && npm install

# Check for syntax errors manually
npx tsc --noEmit        # TypeScript projects
npx next lint           # Lint issues
```

If the issue is a config problem, validate your configuration:

```js
// next.config.mjs
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};
export default nextConfig;
```

## Example

```bash
$ npm run build
> Build error occurred
Error: Failed to compile

./pages/about.tsx
Syntax error: Unexpected token

> 5 | export default function About() {
> 6 |   return <div>Hello<"div>;   // malformed JSX
```

## Related Errors

- [Text content did not match (Hydration failed)]({{< relref "/frameworks/nextjs/hydration-error" >}})
