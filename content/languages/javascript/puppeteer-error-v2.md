---
title: "[Solution] Puppeteer: Navigation Timeout Fix"
description: "Fix Puppeteer navigation timeout errors. Handle slow page loads, infinite redirects, and timeout configuration."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Puppeteer: Navigation Timeout

This error occurs when Puppeteer's `page.goto()` or other navigation methods exceed the configured timeout waiting for the page to finish loading.

## What This Error Means

Common error messages:

- `TimeoutError: Navigation timeout of 30000 ms exceeded`
- `TimeoutError: waiting for page to load failed: timeout 30000ms exceeded`
- `net::ERR_TIMED_OUT`
- `TimeoutError: Navigation failed to complete`

Puppeteer waits for the page to reach a stable loading state (usually `load` event). If the page takes too long due to slow network, large resources, or infinite loops, the timeout fires.

## Common Causes

```javascript
// Cause 1: Default 30s timeout too short for heavy pages
await page.goto('https://heavy-dashboard.example.com');

// Cause 2: Page loads resources from slow CDN
await page.goto('https://example.com'); // waits for all scripts

// Cause 3: Infinite redirect loop
await page.goto('https://redirect-chain.example.com');

// Cause 4: Page never fires load event (infinite loading)
await page.goto('https://streaming.example.com');

// Cause 5: Network issue or DNS resolution slow
await page.goto('https://slow-api.example.com');
```

## How to Fix

### Fix 1: Increase timeout

```javascript
await page.goto('https://example.com', {
  timeout: 60000, // 60 seconds
});
```

### Fix 2: Wait for a different lifecycle event

```javascript
// Don't wait for full load — just DOM ready
await page.goto('https://example.com', {
  waitUntil: 'domcontentloaded',
});

// Or just wait for initial response
await page.goto('https://example.com', {
  waitUntil: 'networkidle0', // no network activity for 500ms
});
```

### Fix 3: Use navigation timeout separately from operation timeout

```javascript
page.setDefaultNavigationTimeout(120000);
page.setDefaultTimeout(30000);

await page.goto('https://example.com');
```

### Fix 4: Skip navigation errors for non-critical pages

```javascript
try {
  await page.goto('https://analytics.example.com/track', {
    waitUntil: 'domcontentloaded',
    timeout: 10000,
  });
} catch (err) {
  console.warn('Analytics page timed out, continuing');
}
```

### Fix 5: Use response timeout instead of navigation timeout

```javascript
const response = await page.goto('https://example.com', {
  waitUntil: 'response',
  timeout: 60000,
});

if (response.status() >= 400) {
  console.error('Page returned error:', response.status());
}
```

## Examples

```
TimeoutError: Navigation timeout of 30000 ms exceeded
    at LifecycleWatcher._timeoutTimer (node_modules/puppeteer/lib/cjs/...)
```

```javascript
// Fix: wrap with retry
async function navigateWithRetry(page, url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      await page.goto(url, {
        timeout: 30000,
        waitUntil: 'domcontentloaded',
      });
      return;
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 2000));
    }
  }
}
```

## Related Errors

- [Puppeteer Error]({{< relref "/languages/javascript/puppeteer-error" >}}) — basic Puppeteer error
- [Playwright Error V2]({{< relref "/languages/javascript/playwright-error-v2" >}}) — browser page crash
- [ETIMEDOUT]({{< relref "/languages/javascript/etimedout" >}}) — connection timed out
