---
title: "[Solution] Deprecated Function Migration: XMLHttpRequest to fetch API"
description: "Migrate from deprecated XMLHttpRequest to the modern fetch API in JavaScript for HTTP requests."
deprecated_function: "XMLHttpRequest"
replacement_function: "fetch()"
languages: ["javascript"]
deprecated_since: "ES6/2015+"
---

# [Solution] Deprecated Function Migration: XMLHttpRequest to fetch API

The `XMLHttpRequest` has been deprecated in favor of `fetch()`.

## Migration Guide

XMLHttpRequest is verbose and uses callbacks. The fetch API is Promise-based, cleaner, and the modern standard for HTTP requests.

## Before (Deprecated)

```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.example.com/data");
xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var data = JSON.parse(xhr.responseText);
        console.log(data);
    }
};
xhr.send();
```

## After (Modern)

```javascript
async function getData() {
    try {
        const response = await fetch("https://api.example.com/data");
        if (!response.ok) throw new Error(response.statusText);
        const data = await response.json();
        console.log(data);
    } catch (err) {
        console.error("Error:", err);
    }
}
```

## Key Differences

- fetch returns a Promise with Response object
- Use response.json() to parse JSON
- Use response.ok to check status
- AbortController for timeouts
