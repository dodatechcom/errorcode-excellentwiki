---
title: "[Solution] Playwright: Browser Page Crash Fix"
description: "Fix Playwright browser page crash errors. Handle OOM kills, renderer crashes, and connection resets during test execution."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["playwright", "browser", "testing", "crash", "automation"]
weight: 5
---

# Playwright: Browser Page Crash

This error occurs when a Playwright browser page or context crashes during execution. The renderer process is killed (often due to out-of-memory) or the browser connection is lost.

## What This Error Means

Common error messages:

- `Error: Page crashed`
- `Error: Target page, context or browser has been closed`
- `browserContext.newPage: Target crashed`
- `Connection closed while reading from the socket`
- `Error: Protocol error (Target.closeTarget): Target closed`

A page crash means the browser's rendering process terminated unexpectedly. Playwright detects this and throws the error, closing any references to the page.

## Common Causes

```javascript
// Cause 1: Out of memory from large DOM
await page.goto('https://example.com/huge-table'); // 500k DOM nodes

// Cause 2: Too many open pages/contexts
for (let i = 0; i < 200; i++) {
  await browser.newPage(); // memory pressure

// Cause 3: GPU rendering failure in headless mode
await chromium.launch({ headless: false, args: ['--no-sandbox'] });

// Cause 4: Page triggers native crash (e.g., WebAssembly OOM)
await page.evaluate(() => {
  const memory = new WebAssembly.Memory({ initial: 10000 });
});

// Cause 5: Browser binary crash or version mismatch
```

## How to Fix

### Fix 1: Limit page resources

```javascript
const context = await browser.newContext({
  viewport: { width: 1280, height: 720 },
});

const page = await context.newPage();

// Block heavy resources
await page.route('**/*.{png,jpg,jpeg,gif,svg,mp4}', route => route.abort());
await page.route('**/analytics.js', route => route.abort());
```

### Fix 2: Close pages when done

```javascript
for (const url of urls) {
  const page = await context.newPage();
  await page.goto(url);
  const data = await page.evaluate(() => document.title);
  await page.close(); // free memory
}
```

### Fix 3: Use separate contexts per test

```javascript
test('page test', async ({ browser }) => {
  const context = await browser.newContext();
  const page = await context.newPage();
  // ... test
  await context.close(); // fully cleanup
});
```

### Fix 4: Add browser restart on crash

```javascript
let browser;
let page;

async function setup() {
  browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  page = await context.newPage();

  page.on('crash', async () => {
    console.error('Page crashed, restarting browser');
    await browser.close();
    await setup();
  });
}
```

### Fix 5: Use chromium flags for stability

```javascript
const browser = await chromium.launch({
  args: [
    '--no-sandbox',
    '--disable-gpu',
    '--disable-dev-shm-usage',
    '--disable-extensions',
    '--single-process',
  ],
});
```

## Examples

```
Error: Page crashed
    at Page._onTargetCrashed (node_modules/playwright-core/lib/server/page.js:...)
    at Target._onCrashed (node_modules/playwright-core/lib/server/frames.js:...)
```

```javascript
// Fix: use test fixtures for proper cleanup
const { test, expect } = require('@playwright/test');

test.afterEach(async ({ page }) => {
  // Ensure page is closed even if test fails
  if (!page.isClosed()) {
    await page.close();
  }
});
```

## Related Errors

- [Playwright Error]({{< relref "/languages/javascript/playwright-error" >}}) — basic Playwright error
- [Puppeteer Error V2]({{< relref "/languages/javascript/puppeteer-error-v2" >}}) — navigation timeout
- [Jest Error V2]({{< relref "/languages/javascript/jest-error-v2" >}}) — test assertion failed
