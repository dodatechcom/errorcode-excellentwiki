---
title: "[Solution] Cloudflare Mixed Content with SSL Error — How to Fix"
description: "Fix Cloudflare mixed content errors with SSL. Resolve HTTP resource loading on HTTPS pages, broken styles, and console warnings."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Cloudflare mixed content error occurs when your site loads over HTTPS but some resources (images, scripts, stylesheets, iframes) are still referenced via HTTP. Browsers block these insecure requests, causing broken layouts, missing functionality, and security warnings.

## What This Error Means

When Cloudflare proxies your domain and forces HTTPS, the browser expects all resources to load over HTTPS. If your HTML contains links to `http://` resources, the browser flags them as mixed content. This is a security issue because an attacker could intercept the HTTP requests and modify the content. Browsers either block or warn about mixed content depending on the resource type.

## Why It Happens

- Hardcoded `http://` URLs in HTML, CSS, or JavaScript files
- Content loaded from third-party sources via HTTP
- CMS generates HTTP URLs instead of protocol-relative or HTTPS URLs
- Database contains old HTTP references from before Cloudflare was enabled
- Iframes embedded with HTTP source URLs
- API endpoints referenced with HTTP instead of HTTPS
- CSS files reference `http://` background images or font files
- JavaScript makes AJAX calls to HTTP endpoints
- RSS feeds or XML sitemaps contain HTTP URLs

## Common Error Messages

- `Mixed Content: The page was loaded over HTTPS, but requested an insecure resource`
- `Mixed Content: The page at 'https://example.com' was loaded over HTTPS`
- `ERR_BLOCKED_BY_CLIENT` — Browser blocked the HTTP resource entirely
- `The SSL certificate used to load resources from ... must be trusted`
- `Mixed Content: Automatically upgraded insecure XHR request to HTTPS`

## How to Fix It

### Use Protocol-Relative URLs

```html
<!-- WRONG: Hardcoded HTTP -->
<script src="http://cdn.example.com/script.js"></script>
<link href="http://cdn.example.com/style.css" rel="stylesheet">
<img src="http://example.com/image.png" alt="">
<iframe src="http://example.com/widget"></iframe>

<!-- RIGHT: Protocol-relative -->
<script src="//cdn.example.com/script.js"></script>
<link href="//cdn.example.com/style.css" rel="stylesheet">
<img src="//example.com/image.png" alt="">
<iframe src="//example.com/widget"></iframe>

<!-- BETTER: Explicit HTTPS (recommended) -->
<script src="https://cdn.example.com/script.js"></script>
<link href="https://cdn.example.com/style.css" rel="stylesheet">
<img src="https://example.com/image.png" alt="">
<iframe src="https://example.com/widget"></iframe>
```

### Fix Database Content

```sql
-- Find all HTTP URLs in your database (MySQL)
SELECT * FROM posts WHERE content LIKE '%http://%'
  AND content NOT LIKE '%https://%';

-- Check specific tables for HTTP references
SELECT TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'your_database'
  AND (COLUMN_NAME LIKE '%url%' OR COLUMN_NAME LIKE '%link%');

-- Update them (test first on a staging database)
UPDATE posts
SET content = REPLACE(content, 'http://example.com', 'https://example.com')
WHERE content LIKE '%http://example.com%';

-- Fix image src attributes
UPDATE posts
SET content = REPLACE(content, 'src="http://', 'src="https://')
WHERE content LIKE '%src="http://%';

-- Fix href attributes
UPDATE posts
SET content = REPLACE(content, 'href="http://', 'href="https://')
WHERE content LIKE '%href="http://%';
```

### Enable Cloudflare Always Use HTTPS

```bash
# In Cloudflare Dashboard:
# SSL/TLS > Edge Certificates > Always Use HTTPS > ON

# Or use an API call
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/ZONE_ID/settings/always_use_https" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"value": "on"}'

# Verify the setting
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/settings/always_use_https" \
  -H "Authorization: Bearer YOUR_API_TOKEN" | jq '.result.value'
```

### Use Content-Security-Policy Upgrade Insecure Requests

```nginx
# In your server config or Cloudflare Transform Rules
# This tells the browser to upgrade HTTP requests to HTTPS automatically

# Cloudflare Dashboard: Security > WAF > Custom Rules
# Rule: Upgrade insecure requests
```

```javascript
// Or in your application middleware
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    "upgrade-insecure-requests"
  );
  next();
});
```

### Fix Third-Party Resources

```html
<!-- Check all third-party embeds -->
<!-- Google Fonts — always HTTPS -->
<link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet">

<!-- jQuery — use HTTPS CDN -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>

<!-- Analytics — verify HTTPS version -->
<script src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>

<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
```

### Fix CSS Mixed Content

```css
/* WRONG: HTTP references in CSS */
body {
  background-image: url(http://example.com/background.jpg);
  font-family: 'CustomFont';
  src: url(http://fonts.example.com/custom.woff2);
}

/* RIGHT: Protocol-relative or HTTPS */
body {
  background-image: url(//example.com/background.jpg);
  font-family: 'CustomFont';
  src: url(https://fonts.example.com/custom.woff2);
}

/* BEST: Use absolute HTTPS paths */
body {
  background-image: url(https://example.com/background.jpg);
}
```

### Audit All Mixed Content

```bash
# Use curl to check for HTTP resources in your HTML
curl -s https://your-domain.com | grep -i 'http://' | head -20

# Check specific pages
curl -s https://your-domain.com/page | grep -oi 'src="http://[^"]*"\|href="http://[^"]*"'

# Use a mixed content checker tool
# Visit: https://www.whynopadlock.com/
# Enter your URL and it will scan for mixed content
```

## Common Scenarios

- **WordPress site migration:** After enabling Cloudflare, old theme templates and plugin settings still reference `http://` URLs. The `wp-options` table stores the site URL as HTTP. Plugins like Really Simple SSL can fix this.
- **Third-party widget:** A chat widget, ad script, or analytics tag loaded from an HTTP source breaks the entire page's security context. The browser blocks the resource and shows a mixed content warning.
- **CSS background images:** A stylesheet references `background-image: url(http://...)` which triggers mixed content warnings even though the HTML is clean. These are harder to find because they are in CSS files, not HTML.

## Prevent It

1. Always use `https://` explicitly in all source code rather than protocol-relative `//` URLs
2. Run `mixed-content-checker` scans as part of your CI/CD pipeline before deploying changes
3. Use Cloudflare's Content Security Policy `upgrade-insecure-requests` directive as a safety net to automatically upgrade HTTP requests to HTTPS

## Related Pages

- [Cloudflare SSL Error]({{< relref "/tools/cloudflare/cloudflare-526" >}}) — Invalid SSL certificate
- [Cloudflare 525 Error]({{< relref "/tools/cloudflare/cloudflare-525" >}}) — SSL handshake failed
