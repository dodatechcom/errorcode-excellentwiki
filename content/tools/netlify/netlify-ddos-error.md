---
title: "[Solution] Netlify DDoS Protection False Positive Error — How to Fix"
description: "Fix Netlify DDoS protection false positives. Resolve legitimate traffic being blocked and bot detection configuration issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Netlify DDoS protection false positive error occurs when Netlify's automated traffic protection incorrectly identifies legitimate requests as DDoS attacks and blocks them. This results in 403 Forbidden or rate-limited responses for valid users.

## What This Error Means

Netlify provides built-in DDoS protection and bot detection that analyzes incoming traffic patterns. When the system detects traffic that matches known attack signatures (rapid requests, unusual patterns, suspicious IPs), it blocks or challenges the requests. False positives occur when legitimate traffic triggers these protections.

## Why It Happens

- High-traffic events (product launches, viral content) trigger rate limiting
- Legitimate bots (Googlebot, monitoring services) are blocked by bot detection
- CDN or proxy IPs are flagged as suspicious
- Automated testing or CI/CD pipelines generate high request volumes
- Geographic anomalies (requests from unexpected regions)
- IP addresses on threat intelligence blocklists are shared with legitimate users (CGNAT)
- The traffic pattern resembles a DDoS attack (uniform request distribution)
- Load balancers or health check services make frequent requests

## Common Error Messages

- `403 Forbidden` — Request blocked by DDoS protection
- `Rate limit exceeded` — Too many requests from a single IP
- `Access denied` — Traffic flagged as suspicious
- `Challenge required` — Bot challenge presented to the user

## How to Fix It

### Check Rate Limiting Settings

```bash
# Netlify has built-in rate limiting
# Check your plan's limits:
# Free: 100 bandwidth shares
# Pro: Custom rate limits available

# Via API, check current traffic patterns
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID/analytics" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Whitelist Legitimate Bots

```toml
# netlify.toml — allow specific bots through DDoS protection
[[headers]]
  for = "/*"
  [headers.values]
    X-Robots-Tag = "index, follow"

# Netlify automatically allows known bots:
# - Googlebot
# - Bingbot
# - Facebook External Hit
# - Twitterbot
# For custom bots, use Netlify's IP allowlisting
```

### Configure Bot Detection

```toml
# netlify.toml — relax bot detection for specific paths
[build]
  command = "npm run build"

# For API endpoints that receive automated traffic
[[headers]]
  for = "/api/*"
  [headers.values]
    Cache-Control = "no-cache"
    X-Rate-Limit-Bypass = "ci-cd-pipeline"

# For health check endpoints
[[headers]]
  for = "/health"
  [headers.values]
    Cache-Control = "no-cache, no-store"
```

### Use External CDN for Static Assets

```toml
# netlify.toml — serve static assets from CDN
[[headers]]
  for = "/static/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
    Access-Control-Allow-Origin = "*"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
    Access-Control-Allow-Origin = "*"
```

### Handle High-Traffic Events

```javascript
// Implement client-side retry logic for rate-limited requests
async function fetchWithRetry(url, options = {}, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const response = await fetch(url, options);

      if (response.status === 429) {
        // Rate limited — wait and retry
        const retryAfter = response.headers.get('Retry-After') || 5;
        await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
        continue;
      }

      return response;
    } catch (error) {
      if (i === retries - 1) throw error;
      await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
    }
  }
}

// Use exponential backoff
async function fetchWithBackoff(url, options = {}, maxRetries = 5) {
  for (let i = 0; i < maxRetries; i++) {
    const response = await fetch(url, options);
    if (response.status !== 429) return response;

    const delay = Math.min(1000 * Math.pow(2, i), 30000);
    await new Promise(resolve => setTimeout(resolve, delay));
  }
  throw new Error('Max retries exceeded');
}
```

### Monitor and Alert

```bash
# Set up monitoring for false positives
# Track 403/429 responses in your analytics

# In Netlify Dashboard:
# Analytics > Traffic > Look for spikes in 403/429 responses

# Use Netlify's log drain to monitor blocked requests
netlify logs --follow | grep -E "(403|429)"

# Set up a simple health check
curl -s -o /dev/null -w "%{http_code}" https://your-domain.com/
# Should return 200
# If you get 403/429, traffic may be blocked
```

## Common Scenarios

- **CI/CD pipeline blocked:** A deployment pipeline makes 100+ requests per minute to your Netlify site, triggering rate limiting and blocking all subsequent requests from the same IP range.
- **Monitoring tool flagged:** An uptime monitoring service checks your site every 10 seconds. Netlify's bot detection flags this as a potential DDoS attack and blocks the monitoring IP.
- **Viral content spike:** A blog post goes viral, generating 10,000 requests per minute. Netlify's DDoS protection begins challenging or blocking some legitimate users.

## Prevent It

1. Use Netlify's Analytics dashboard to monitor false positive rates and adjust bot detection settings accordingly
2. Implement exponential backoff and retry logic in client-side code for handling rate-limited responses
3. Contact Netlify support before high-traffic events (product launches, viral campaigns) to request temporary rate limit adjustments

## Related Pages

- [Netlify DDoS Error]({{< relref "/tools/netlify/netlify-ddos-error" >}}) — DDoS protection issues
- [Netlify Headers Error]({{< relref "/tools/netlify/netlify-headers-error" >}}) — Headers configuration issues
