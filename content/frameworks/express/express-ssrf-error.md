---
title: "[Solution] Express SSRF Error"
description: "Fix Express SSRF errors when server-side requests can be tricked into accessing internal resources."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An SSRF error in Express occurs when a server-side request forgery vulnerability allows attackers to make the server fetch internal or restricted resources by manipulating the URL parameter used in HTTP requests.

## Common Causes

- URL from user input passed directly to `fetch()` or `axios.get()`
- No validation of whether the target URL is internal or external
- Webhook handler fetches the provided URL without restriction
- Image proxy fetches user-supplied image URLs
- DNS rebinding allows internal IP access after initial validation

## How to Fix

1. Validate and restrict URLs before making server-side requests:

```javascript
const { URL } = require('url');
const dns = require('dns').promises;

async function isSafeUrl(targetUrl) {
  const parsed = new URL(targetUrl);

  // Block non-HTTP protocols
  if (!['http:', 'https:'].includes(parsed.protocol)) return false;

  // Block internal IPs
  const hostname = parsed.hostname;
  if (['localhost', '127.0.0.1', '0.0.0.0', '::1'].includes(hostname)) return false;

  // Resolve DNS and check for internal addresses
  const addresses = await dns.resolve4(hostname);
  for (const addr of addresses) {
    if (addr.startsWith('10.') || addr.startsWith('172.') || addr.startsWith('192.168.')) {
      return false;
    }
  }
  return true;
}

app.post('/fetch', async (req, res) => {
  const safe = await isSafeUrl(req.body.url);
  if (!safe) return res.status(400).json({ error: 'URL not allowed' });

  const response = await fetch(req.body.url);
  res.json(await response.json());
});
```

2. Use an allowlist of permitted domains:

```javascript
const allowedDomains = ['api.example.com', 'cdn.example.com'];

app.post('/proxy', async (req, res) => {
  const parsed = new URL(req.body.url);
  if (!allowedDomains.includes(parsed.hostname)) {
    return res.status(403).json({ error: 'Domain not allowed' });
  }
  const response = await fetch(req.body.url);
  res.send(await response.buffer());
});
```

## Examples

```javascript
// Vulnerable: fetches any URL including internal services
app.post('/webhook-test', async (req, res) => {
  const response = await fetch(req.body.callbackUrl);
  res.json({ status: response.status });
});

// Attacker sends: {"callbackUrl": "http://169.254.169.254/latest/meta-data/"}
// Server fetches AWS metadata endpoint
```

```text
Error: connect ECONNREFUSED 127.0.0.1:5432
```
