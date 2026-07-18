---
title: "Solved JavaScript puppeteer Error — How to Fix"
date: 2026-03-20T15:20:45+00:00
description: "Learn how to resolve JavaScript Puppeteer headless browser automation and navigation errors."
categories: ["javascript"]
keywords: ["puppeteer error", "headless browser", "puppeteer navigation", "browser automation", "puppeteer timeout"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Puppeteer errors occur when the headless Chrome/Chromium browser encounters navigation timeouts, selector not found issues, or resource loading failures. The browser automation framework requires careful handling of async operations.

Common causes include:
- Page navigation timeout
- Element selector not found in DOM
- Browser context closed unexpectedly
- Memory leak from unclosed pages
- Navigation blocked by security headers

## Common Error Messages

```
TimeoutError: Navigation timeout of 30000 ms exceeded
```

```
Error: Execution context was destroyed
```

```
Error: Protocol error (Page.navigate): Target closed
```

## How to Fix It

### 1. Configure Puppeteer Browser

Set up browser with appropriate options.

```javascript
import puppeteer from "puppeteer";

// Launch browser
const browser = await puppeteer.launch({
  headless: "new", // Use new headless mode
  args: [
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--window-size=1920,1080"
  ],
  defaultViewport: {
    width: 1920,
    height: 1080
  }
});

// Create new page
const page = await browser.newPage();

// Set user agent
await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64)...");

// Enable request interception
await page.setRequestInterception(true);
page.on("request", (req) => {
  if (req.resourceType() === "image") {
    req.abort(); // Block images
  } else {
    req.continue();
  }
});
```

### 2. Handle Navigation and Selection

Navigate pages and select elements safely.

```javascript
// Navigate with timeout
await page.goto("https://example.com", {
  waitUntil: "networkidle2", // Wait for network to be idle
  timeout: 60000
});

// Wait for element before interacting
await page.waitForSelector("#login-form", { timeout: 10000 });

// Type in input
await page.type("#email", "user@example.com");
await page.type("#password", "securePassword123");

// Click button
await page.click("#submit-btn");

// Wait for navigation after click
await Promise.all([
  page.waitForNavigation({ waitUntil: "networkidle0" }),
  page.click("#submit-btn")
]);

// Extract data
const title = await page.title();
const content = await page.$eval("h1", (el) => el.textContent);
```

### 3. Handle Errors and Cleanup

Implement proper error handling.

```javascript
async function scrapeWithRetry(url, maxRetries = 3) {
  let browser;
  
  try {
    browser = await puppeteer.launch({ headless: "new" });
    
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
      try {
        const page = await browser.newPage();
        
        // Set timeout
        page.setDefaultTimeout(30000);
        page.setDefaultNavigationTimeout(60000);
        
        await page.goto(url, { waitUntil: "domcontentloaded" });
        
        // Wait for content
        await page.waitForSelector(".content", { timeout: 10000 });
        
        const data = await page.evaluate(() => {
          return {
            title: document.title,
            paragraphs: Array.from(document.querySelectorAll("p"))
              .map(p => p.textContent.trim())
          };
        });
        
        await page.close();
        return data;
        
      } catch (error) {
        console.error(`Attempt ${attempt} failed:`, error.message);
        
        if (attempt === maxRetries) throw error;
        
        // Wait before retry
        await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
      }
    }
  } finally {
    if (browser) await browser.close();
  }
}
```

## Common Scenarios

### Scenario 1: Screenshot Capture

Take screenshots of pages:

```javascript
async function captureScreenshot(url, outputPath) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto(url, { waitUntil: "networkidle2" });
  
  // Full page screenshot
  await page.screenshot({
    path: outputPath,
    fullPage: true,
    type: "png"
  });
  
  // Or element screenshot
  const element = await page.$(".main-content");
  if (element) {
    await element.screenshot({ path: "element.png" });
  }
  
  await browser.close();
}
```

### Scenario 2: PDF Generation

Generate PDF from web pages:

```javascript
async function generatePDF(url, outputPath) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  await page.goto(url, { waitUntil: "networkidle2" });
  
  await page.pdf({
    path: outputPath,
    format: "A4",
    printBackground: true,
    margin: {
      top: "20mm",
      right: "20mm",
      bottom: "20mm",
      left: "20mm"
    }
  });
  
  await browser.close();
}
```

## Prevent It

- Always close browser instances in `finally` blocks
- Use `waitUntil: "networkidle2"` for dynamic content
- Set appropriate timeouts for navigation and element selection
- Handle browser context closure gracefully
- Use `page.setRequestInterception()` to block unnecessary resources