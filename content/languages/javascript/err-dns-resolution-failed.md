---
title: "[Solution] Node.js ERR_DNS_RESOLUTION_FAILED — DNS Resolution Failed Fix"
description: "Fix Node.js ERR_DNS_RESOLUTION_FAILED when a domain name cannot be resolved to an IP address. Check DNS configuration and network connectivity."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_DNS_RESOLUTION_FAILED — DNS Resolution Failed Fix

The `ERR_DNS_RESOLUTION_FAILED` error occurs when Node.js cannot resolve a domain name to an IP address using the DNS system. This prevents establishing any network connection to the target host.

## Description

Common ERR_DNS_RESOLUTION_FAILED messages include:

- `getaddrinfo ENOTFOUND example.com` — domain does not exist or cannot be resolved.
- `getaddrinfo failed` — DNS lookup failed for the given hostname.
- `EAI_AGAIN: DNS lookup timed out` — DNS query timed out.

## Common Causes

```javascript
const dns = require("node:dns");
const https = require("node:https");

// Cause 1: Domain does not exist
https.get("https://nonexistent-domain-12345.com", (res) => {
  // ERR_DNS_RESOLUTION_FAILED
});

// Cause 2: DNS server is unreachable
// Network configuration prevents DNS queries

// Cause 3: Typo in domain name
https.get("https://exmple.com", (res) => {
  // ERR_DNS_RESOLUTION_FAILED — typo in domain
});

// Cause 4: DNS cache issues
// Stale DNS entries causing resolution failure
```

## Solutions

### Fix 1: Validate domain names before requests

```javascript
const dns = require("node:dns");
const { promisify } = require("node:util");

const resolve = promisify(dns.resolve);

async function isValidDomain(domain) {
  try {
    await resolve(domain);
    return true;
  } catch {
    return false;
  }
}

// Check before making HTTP request
if (await isValidDomain("example.com")) {
  https.get("https://example.com", (res) => {
    // Connection will succeed
  });
}
```

### Fix 2: Use custom DNS servers

```javascript
const dns = require("node:dns");

// Use Google's public DNS servers
dns.setServers(["8.8.8.8", "8.8.4.4", "1.1.1.1"]);

// Or Cloudflare's DNS
dns.setServers(["1.1.1.1", "1.0.0.1"]);

dns.lookup("example.com", (err, address) => {
  if (err) {
    console.error("DNS resolution failed:", err.message);
    return;
  }
  console.log("Resolved to:", address);
});
```

### Fix 3: Implement DNS caching

```javascript
const dns = require("node:dns");

const cache = new Map();
const CACHE_TTL = 300000; // 5 minutes

function cachedLookup(hostname) {
  const cached = cache.get(hostname);
  if (cached && Date.now() - cached.timestamp < CACHE_TTL) {
    return Promise.resolve(cached.address);
  }

  return new Promise((resolve, reject) => {
    dns.lookup(hostname, (err, address) => {
      if (err) {
        reject(err);
        return;
      }
      cache.set(hostname, { address, timestamp: Date.now() });
      resolve(address);
    });
  });
}
```

### Fix 4: Handle DNS errors gracefully

```javascript
const https = require("node:https");

function fetchWithDNSHandling(url) {
  return new Promise((resolve, reject) => {
    const req = https.get(url, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => resolve(data));
    });

    req.on("error", (err) => {
      if (err.code === "ENOTFOUND" || err.code === "ERR_DNS_RESOLUTION_FAILED") {
        reject(new Error(`DNS resolution failed for ${url}: ${err.message}`));
      } else {
        reject(err);
      }
    });

    req.end();
  });
}
```

## Examples

```javascript
const dns = require("node:dns");

// ERR_DNS_RESOLUTION_FAILED for non-existent domain
dns.lookup("this-domain-does-not-exist-12345.com", (err, address) => {
  if (err) {
    console.error("Code:", err.code); // ENOTFOUND
    console.error("Message:", err.message);
  }
});
```

## Related Errors

- [ERR_CONNECTION_REFUSED]({{< relref "/languages/javascript/err-connection-refused" >}}) — server refused connection.
- [ERR_CERT_HAS_EXPIRED]({{< relref "/languages/javascript/err-certificate-has-expired" >}}) — certificate expired.
- [ERR_SOCKET_TIMEOUT]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket timed out.
- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection was reset.
