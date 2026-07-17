---
title: "[Solution] Node.js ERR_UNSUPPORTED_ESM_URL_SCHEME — ESM URL Scheme Fix"
description: "Fix Node.js ERR_UNSUPPORTED_ESM_URL schemes by handling protocol imports, converting data URLs, or configuring import maps for unsupported schemes."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_UNSUPPORTED_ESM_URL_SCHEME — ESM URL Scheme Fix

The `ERR_UNSUPPORTED_ESM_URL_SCHEME` error occurs when an ESM `import` statement uses a URL scheme that Node.js does not support for module resolution. Node.js supports `file:`, `data:`, and `node:` schemes — other protocols like `http:`, `https:`, or custom schemes are not natively supported without a loader.

## Description

Common ERR_UNSUPPORTED_ESM_URL_SCHEME messages include:

- `ERR_UNSUPPORTED_ESM_URL_SCHEME: Only file and data URLs are supported by the default ESM loader` — using `http:` or `https:` imports.
- `ERR_UNSUPPORTED_ESM_URL_SCHEME: Unsupported URL scheme "custom"` — custom protocol in import.

## Common Causes

```javascript
// Cause 1: Importing via HTTP URL
import { helper } from "https://example.com/utils.js";  // ERR_UNSUPPORTED_ESM_URL_SCHEME

// Cause 2: Importing with a custom protocol
import { data } from "myprotocol://resource";  // ERR_UNSUPPORTED_ESM_URL_SCHEME

// Cause 3: Importing from non-file data URLs with unsupported types
import "data:text/javascript,export default 42";  // works, but some variations fail

// Cause 4: Import map or path resolving to an unsupported scheme
// importMap in package.json pointing to https://
```

## Solutions

### Fix 1: Download the module locally instead of importing from HTTP

```bash
# Download the file locally
curl -o utils.js https://example.com/utils.js

# Or use npm to install it
npm install https://example.com/package.tgz
```

```javascript
// Correct: import from the local copy
import { helper } from "./utils.js";
```

### Fix 2: Use data: URL imports for inline modules

```javascript
// data: URLs are supported for simple inline modules
import "data:text/javascript,export default function greet() { return 'hi'; }";
```

### Fix 3: Use a custom loader for HTTP imports

```javascript
// http-loader.mjs
import { get } from "https";
import { fileURLToPath } from "url";

export async function resolve(specifier, context, nextResolve) {
  if (specifier.startsWith("https://")) {
    return {
      url: specifier,
      shortCircuit: true,
    };
  }
  return nextResolve(specifier, context);
}

export async function load(url, context, nextLoad) {
  if (url.startsWith("https://")) {
    const data = await fetchHttps(url);
    return {
      format: "module",
      shortCircuit: true,
      source: data,
    };
  }
  return nextLoad(url, context);
}

function fetchHttps(url) {
  return new Promise((resolve, reject) => {
    get(url, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => resolve(data));
    }).on("error", reject);
  });
}
```

```bash
node --import ./http-loader.mjs src/index.js
```

### Fix 4: Use import maps (Node.js 18.19+ / 20.6+)

```json
{
  "imports": {
    "my-lib": "https://cdn.example.com/my-lib/index.js"
  }
}
```

```bash
# Load the import map
node --import ./http-loader.mjs --experimental-import-map src/index.js
```

## Examples

```javascript
// This triggers ERR_UNSUPPORTED_ESM_URL_SCHEME
import { parse } from "https://deno.land/std/flags/mod.ts";

// Workaround: install the package via npm
// npm install parse-url
import { parse } from "parse-url";
```

## Related Errors

- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err_module_not_found" >}}) — ESM import resolution failed.
- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err_require_esm" >}}) — cannot require an ES module.
- [ERR_UNKNOWN_FILE_EXTENSION]({{< relref "/languages/javascript/err_unknown_file_extension" >}}) — unknown file extension.
- [MODULE_NOT_FOUND]({{< relref "/languages/javascript/modulenotfounderror" >}}) — CommonJS module not found.
