---
title: "Solved JavaScript Cheerio Error — How to Fix"
date: 2026-03-20T13:50:00+00:00
description: "Learn how to resolve JavaScript Cheerio HTML parsing, selector, and scraping errors."
categories: ["javascript"]
keywords: ["cheerio error", "cheerio parsing", "html scraping", "cheerio selector", "web scraping"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Cheerio errors occur when the jQuery-like HTML parser encounters malformed HTML, invalid selectors, or encoding issues. Web scraping often encounters non-standard HTML that requires careful handling.

Common causes include:
- Malformed HTML causing parsing failures
- CSS selector syntax errors
- Character encoding mismatches
- Dynamic content not present in static HTML
- Selectors matching no elements

## Common Error Messages

```
Error: Parse Error: < tag at position X
```

```
TypeError: Cannot read property 'children' of undefined
```

```
Error: Selector not valid
```

## How to Fix It

### 1. Configure Cheerio Properly

Set up Cheerio with appropriate options.

```javascript
import * as cheerio from "cheerio";

// Basic loading
const $ = cheerio.load(html, {
  xml: false,
  decodeEntities: true,
  lowerCaseTags: false,
  lowerCaseAttributeNames: false,
  recognizeSelfClosing: true
});

// Load with custom parser options
const $ = cheerio.load(html, {
  xmlMode: false,
  withDomLvl1: true,
  withStartIndices: false,
  withEndIndices: false
});

// Handle encoding
function loadWithEncoding(buffer, encoding = "utf-8") {
  const html = buffer.toString(encoding);
  return cheerio.load(html);
}
```

### 2. Use Robust Selectors

Write resilient CSS selectors for scraping.

```javascript
// ❌ Fragile selector - breaks with layout changes
const price = $(".product-price > span.value").text();

// ✅ Robust selectors with fallbacks
const price = 
  $(".product-price .value").first().text() ||
  $(".price").text() ||
  $('[data-price]').attr("data-price") ||
  "N/A";

// Extract structured data
function extractProductData($) {
  const products = [];
  
  $(".product-item").each((i, el) => {
    const $el = $(el);
    
    const product = {
      name: $el.find(".product-title, h2, h3").first().text().trim(),
      price: parseFloat(
        $el.find(".price, .product-price")
          .first()
          .text()
          .replace(/[^0-9.]/g, "")
      ) || null,
      image: $el.find("img").first().attr("src"),
      url: $el.find("a").first().attr("href")
    };
    
    if (product.name) {
      products.push(product);
    }
  });
  
  return products;
}

// Handle nested structures
function extractTableData($) {
  const data = [];
  
  $("table tbody tr").each((i, row) => {
    const rowData = {};
    
    $(row).find("td").each((j, cell) => {
      const header = $("table thead th").eq(j).text().trim();
      rowData[header] = $(cell).text().trim();
    });
    
    data.push(rowData);
  });
  
  return data;
}
```

### 3. Handle Dynamic Content

Work with pages that require JavaScript rendering.

```javascript
import * as cheerio from "cheerio";
import axios from "axios";

// Handle JavaScript-rendered content
async function scrapeWithRetry(url, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await axios.get(url, {
        timeout: 10000,
        headers: {
          "User-Agent": "Mozilla/5.0 (compatible; scraper/1.0)",
          "Accept": "text/html,application/xhtml+xml"
        }
      });
      
      const $ = cheerio.load(response.data);
      return extractData($);
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}

// Extract all links
function extractLinks($, baseUrl) {
  const links = [];
  
  $("a[href]").each((i, el) => {
    const href = $(el).attr("href");
    const text = $(el).text().trim();
    
    if (href && !href.startsWith("#") && !href.startsWith("javascript:")) {
      try {
        const absoluteUrl = new URL(href, baseUrl).href;
        links.push({ text, url: absoluteUrl });
      } catch (e) {
        // Invalid URL
      }
    }
  });
  
  return links;
}
```

## Common Scenarios

### Scenario 1: Product Scraping

Extract product data from e-commerce sites:

```javascript
import * as cheerio from "cheerio";
import axios from "axios";

async function scrapeProducts(url) {
  const { data } = await axios.get(url);
  const $ = cheerio.load(data);
  
  const products = [];
  
  $(".product-card, .product-item, [data-product-id]").each((i, el) => {
    const $el = $(el);
    
    products.push({
      id: $el.attr("data-product-id") || $el.find("[data-id]").attr("data-id"),
      name: $el.find(".product-name, .title, h2, h3").first().text().trim(),
      price: parseFloat(
        $el.find(".price, .current-price, [data-price]")
          .first()
          .text()
          .replace(/[^0-9.]/g, "")
      ),
      rating: parseFloat($el.find(".rating, .stars").attr("data-rating")) || null,
      imageUrl: $el.find("img").first().attr("src"),
      inStock: !$el.find(".out-of-stock, .sold-out").length
    });
  });
  
  return products.filter(p => p.name && p.price);
}
```

### Scenario 2: HTML Cleaning

Clean and transform HTML content:

```javascript
import * as cheerio from "cheerio";

function cleanHtml(html, options = {}) {
  const $ = cheerio.load(html, { decodeEntities: true });
  
  // Remove scripts and styles
  $("script, style, noscript, iframe").remove();
  
  // Remove comments
  $("*").contents().each(function() {
    if (this.type === "comment") {
      $(this).remove();
    }
  });
  
  // Clean attributes (keep only safe ones)
  const safeAttrs = ["href", "src", "alt", "title", "class", "id"];
  $("*").each(function() {
    const el = $(this);
    Object.keys(el.attr() || {}).forEach(attr => {
      if (!safeAttrs.includes(attr)) {
        el.removeAttr(attr);
      }
    });
  });
  
  // Clean classes
  if (options.removeClasses) {
    $("[class]").removeAttr("class");
  }
  
  return $.html();
}
```

## Prevent It

- Always check if selectors return elements before accessing properties
- Use `.first()` or `.eq(0)` to avoid ambiguity with multiple matches
- Implement retry logic for network requests during scraping
- Handle character encoding explicitly with `decodeEntities: true`
- Cache fetched HTML to avoid repeated requests during development