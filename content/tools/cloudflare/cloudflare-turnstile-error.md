---
title: "[Solution] Cloudflare Turnstile CAPTCHA Verification Failed Error — How to Fix"
description: "Fix Cloudflare Turnstile CAPTCHA verification failures. Resolve token validation errors, CSP issues, and invisible CAPTCHA problems."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Cloudflare Turnstile CAPTCHA verification failed error occurs when the Turnstile widget generates a token but the server-side verification rejects it. This blocks form submissions and prevents user actions on your site.

## What This Error Means

Turnstile is Cloudflare's invisible CAPTCHA alternative that provides bot protection without user interaction. After a user completes the widget challenge (invisible or visible), a token is generated and must be verified server-side via Cloudflare's siteverify endpoint. If the token is invalid, expired, or the verification API call fails, the action is denied.

## Why It Happens

- The site key or secret key is incorrect or mismatched between client and server
- The token was already used (tokens are single-use)
- The token expired (valid for approximately 300 seconds)
- The server-side verification endpoint is misconfigured or unreachable
- The Turnstile widget failed to load due to Content Security Policy restrictions
- Bot detection mode is too aggressive for your traffic pattern
- The `cf-turnstile-response` field name is missing from the form
- The verification API call timed out or returned a non-200 status
- The Turnstile script was blocked by an ad blocker or browser extension

## Common Error Messages

- `Invalid token` — The token failed server-side validation
- `Token already used` — The token was submitted more than once
- `Token expired` — The token is older than 300 seconds
- `Missing sitekey or response` — Form submission is missing the Turnstile fields
- `Invalid input: sitekey` — The sitekey parameter is malformed
- `Unsupported adapter` — The Turnstile script could not initialize

## How to Fix It

### Verify Keys Match

```javascript
// The site key in your HTML and the secret key in your server must belong to the same widget

// HTML (client-side) — uses the SITE key
<div class="cf-turnstile" data-sitekey="YOUR_SITE_KEY"></div>

// Server-side verification — uses the SECRET key
const TURNSTILE_SECRET = 'YOUR_SECRET_KEY';

async function verifyTurnstile(token) {
  const response = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: `secret=${TURNSTILE_SECRET}&response=${token}`,
  });

  const result = await response.json();
  return result.success;
}
```

### Handle Token Expiration

```javascript
// Add timestamp tracking on the client side
let turnstileToken = null;
let tokenTimestamp = 0;

// Callback when Turnstile widget generates a token
function onTurnstileSuccess(token) {
  turnstileToken = token;
  tokenTimestamp = Date.now();
}

// Before submitting the form, check if token is still valid
function handleSubmit(e) {
  e.preventDefault();

  const tokenAge = Date.now() - tokenTimestamp;
  if (tokenAge > 240000) { // 4 minutes, less than the 5-minute expiry
    // Token is about to expire, request a new one
    turnstile.reset();
    return;
  }

  // Submit with the token
  document.getElementById('turnstile-response').value = turnstileToken;
  e.target.submit();
}
```

### Fix Server-Side Verification

```javascript
// Express.js verification middleware
const TURNSTILE_SECRET = process.env.TURNSTILE_SECRET;

async function verifyTurnstileMiddleware(req, res, next) {
  const token = req.body['cf-turnstile-response'];

  if (!token) {
    return res.status(403).json({ error: 'Turnstile token missing' });
  }

  try {
    const response = await fetch(
      'https://challenges.cloudflare.com/turnstile/v0/siteverify',
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `secret=${TURNSTILE_SECRET}&response=${token}&remoteip=${req.ip}`,
      }
    );

    const result = await response.json();

    if (!result.success) {
      console.error('Turnstile verification failed:', result['error-codes']);
      return res.status(403).json({ error: 'CAPTCHA verification failed' });
    }

    next();
  } catch (err) {
    console.error('Turnstile API error:', err);
    return res.status(500).json({ error: 'CAPTCHA service unavailable' });
  }
}

app.post('/submit', verifyTurnstileMiddleware, handleSubmit);
```

### Fix CSP for Turnstile

```javascript
// Add Cloudflare Turnstile domains to your Content Security Policy
const csp = [
  "default-src 'self'",
  "script-src 'self' https://challenges.cloudflare.com",
  "frame-src https://challenges.cloudflare.com",
  "connect-src 'self' https://challenges.cloudflare.com",
].join('; ');

res.setHeader('Content-Security-Policy', csp);
```

### Handle Ad Blocker Fallback

```javascript
// Check if Turnstile loaded successfully
function checkTurnstileAvailable() {
  return new Promise((resolve) => {
    // Check if the Turnstile global is available
    if (typeof window.turnstile !== 'undefined') {
      resolve(true);
      return;
    }

    // If not loaded after 3 seconds, it may be blocked
    setTimeout(() => {
      resolve(typeof window.turnstile !== 'undefined');
    }, 3000);
  });
}

// Fallback for when Turnstile is blocked
async function submitForm() {
  const turnstileAvailable = await checkTurnstileAvailable();

  if (turnstileAvailable) {
    // Use Turnstile
    const token = turnstile.getResponse();
    await submitWithTurnstile(token);
  } else {
    // Fallback to alternative verification (e.g., honeypot)
    await submitWithHoneypot();
  }
}
```

## Common Scenarios

- **Form submits but verification always fails:** The site key in the HTML was copied from one project but the secret key is from a different Turnstile widget in the Cloudflare dashboard.
- **Token expired before submit:** A long form takes users several minutes to complete. By the time they submit, the Turnstile token has expired.
- **CSP blocks Turnstile:** A strict Content-Security-Policy blocks the Turnstile script from loading, so the widget never generates a token.

## Prevent It

1. Always verify the Turnstile token server-side and handle the `error-codes` response to distinguish between expired, invalid, and missing tokens
2. Include the `cf-turnstile-response` field name exactly as Turnstile expects in your form, and do not modify it with JavaScript
3. Set your CSP headers to allow `challenges.cloudflare.com` before enabling Turnstile on your domain

## Related Pages

- [Cloudflare WAF Blocked]({{< relref "/tools/cloudflare/cloudflare-waf-blocked" >}}) — WAF blocking requests
- [Cloudflare 1020 Error]({{< relref "/tools/cloudflare/cloudflare-1020" >}}) — Access denied
