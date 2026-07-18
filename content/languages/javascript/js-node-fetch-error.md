---
title: "Solved JavaScript node-fetch Error — How to Fix"
date: 2026-03-20T14:30:00+00:00
description: "Learn how to resolve JavaScript node-fetch HTTP request, redirect, and streaming errors."
categories: ["javascript"]
keywords: ["node-fetch error", "node fetch", "fetch api", "http request", "node-fetch timeout"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

node-fetch errors occur when the lightweight fetch API implementation encounters network issues, timeout problems, or response handling failures. node-fetch has different behavior from browser fetch in several key areas.

Common causes include:
- Request timeout before response completes
- Redirect limit exceeded
- Response body not properly consumed
- SSL certificate verification failures
- Large response bodies causing memory issues

## Common Error Messages

```
FetchError: network timeout at https://api.example.com
```

```
FetchError: request to https://api.example.com failed, reason: connect ECONNREFUSED
```

```
TypeError: Cannot read property 'json' of undefined
```

## How to Fix It

### 1. Configure node-fetch Properly

Set up fetch with proper options.

```javascript
import fetch from "node-fetch";

// Basic configuration
const response = await fetch("https://api.example.com/data", {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${token}`
  },
  timeout: 10000,
  redirect: "follow",
  compress: true
});

// Handle response
if (!response.ok) {
  throw new Error(`HTTP error! status: ${response.status}`);
}

const data = await response.json();
```

### 2. Handle Different Response Types

Process various response formats properly.

```javascript
import fetch from "node-fetch";

// JSON response
async function getJson(url) {
  const response = await fetch(url);
  
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  
  return response.json();
}

// Text response
async function getText(url) {
  const response = await fetch(url);
  return response.text();
}

// Stream large files
async function downloadFile(url, outputPath) {
  const { createWriteStream } = require("fs");
  const { pipeline } = require("stream");
  const { promisify } = require("util");
  
  const pipelineAsync = promisify(pipeline);
  
  const response = await fetch(url);
  const fileStream = createWriteStream(outputPath);
  
  await pipelineAsync(response.body, fileStream);
  return outputPath;
}

// POST with JSON body
async function postData(url, data) {
  const response = await fetch(url, {
    method: "POST",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" }
  });
  
  return response.json();
}
```

### 3. Implement Retry Logic

Add automatic retries for failed requests.

```javascript
import fetch from "node-fetch";

async function fetchWithRetry(url, options = {}, maxRetries = 3) {
  let lastError;
  
  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await fetch(url, {
        ...options,
        timeout: options.timeout || 10000
      });
      
      if (response.ok) {
        return response;
      }
      
      if (response.status >= 500) {
        throw new Error(`Server error: ${response.status}`);
      }
      
      return response;
    } catch (error) {
      lastError = error;
      
      if (i < maxRetries - 1) {
        const delay = Math.pow(2, i) * 1000;
        await new Promise(r => setTimeout(r, delay));
      }
    }
  }
  
  throw lastError;
}

// Usage
const data = await fetchWithRetry("https://api.example.com/data")
  .then(r => r.json());
```

## Common Scenarios

### Scenario 1: Concurrent Requests

Handle multiple parallel requests:

```javascript
import fetch from "node-fetch";

async function fetchMultiple(urls) {
  const promises = urls.map(url => 
    fetch(url)
      .then(r => r.json())
      .catch(error => ({ error: error.message, url }))
  );
  
  return Promise.all(promises);
}

// With concurrency limit
async function fetchWithLimit(urls, limit = 5) {
  const results = [];
  
  for (let i = 0; i < urls.length; i += limit) {
    const batch = urls.slice(i, i + limit);
    const batchResults = await Promise.all(
      batch.map(url => fetch(url).then(r => r.json()))
    );
    results.push(...batchResults);
  }
  
  return results;
}
```

### Scenario 2: File Upload

Upload files with fetch:

```javascript
import fetch from "node-fetch";
import FormData from "form-data";
import fs from "fs";

async function uploadFile(filePath, uploadUrl) {
  const form = new FormData();
  form.append("file", fs.createReadStream(filePath));
  
  const response = await fetch(uploadUrl, {
    method: "POST",
    body: form,
    headers: form.getHeaders()
  });
  
  return response.json();
}
```

## Prevent It

- Always consume response body immediately or pipe to a stream
- Set appropriate timeouts for connect and response
- Use `redirect: "manual"` when you need to handle redirects yourself
- Handle non-2xx responses with `response.ok` check
- Use `AbortController` for request cancellation in modern Node.js