---
title: "[Solution] Cloudflare Turnstile CAPTCHA Not Verifying Error — Fix Bot Challenge"
description: "Fix Cloudflare Turnstile CAPTCHA not verifying. Resolve Turnstile token validation failures and challenge bypass issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 12
---

A Cloudflare Turnstile CAPTCHA not verifying error occurs when the Turnstile widget on your site fails to issue or validate a token. Visitors see a spinning challenge that never completes, or the token verification fails on your backend.

## What This Error Means

Turnstile is Cloudflare's CAPTCHA replacement that verifies visitors are human without showing a visual puzzle. When it fails, the widget either stays in a loading state indefinitely or returns an invalid token to your server for verification.

## Why It Happens

- The Turnstile site key or secret key is incorrect
- JavaScript is blocked in the visitor's browser
- The Turnstile script is not loaded or is blocked by extensions
- The token has expired (tokens are valid for 300 seconds)
- The secret key is exposed in client-side code
- The verification endpoint is misconfigured
- Content Security Policy headers block the Turnstile script

## How to Fix It

### Verify Site Key and Secret Key

```bash
# In Cloudflare Dashboard:
# Turnstile > Sites
# Copy the correct site key and secret key

# Site key starts with: 0x...
# Secret key starts with: 0x...
```

### Load Turnstile Script Correctly

```html
<!-- Add before closing body tag -->
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>

<!-- Add the widget -->
<div class="cf-turnstile" data-sitekey="YOUR_SITE_KEY"></div>

<!-- Get the token on form submit -->
<form action="/verify" method="POST">
  <div class="cf-turnstile" data-sitekey="YOUR_SITE_KEY"></div>
  <button type="submit">Submit</button>
</form>
```

### Verify Token on Backend

```python
import requests

def verify_turnstile(token, remote_ip):
    secret_key = os.environ['TURNSTILE_SECRET_KEY']

    response = requests.post(
        'https://challenges.cloudflare.com/turnstile/v0/siteverify',
        data={
            'secret': secret_key,
            'response': token,
            'remoteip': remote_ip,
        }
    )

    result = response.json()
    return result.get('success', False)
```

### Node.js Verification

```javascript
const fetch = require('node-fetch');

async function verifyTurnstile(token, ip) {
  const response = await fetch(
    'https://challenges.cloudflare.com/turnstile/v0/siteverify',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        secret: process.env.TURNSTILE_SECRET_KEY,
        response: token,
        remoteip: ip,
      }),
    }
  );

  const result = await response.json();
  return result.success;
}

// In your route handler
app.post('/verify', async (req, res) => {
  const token = req.body['cf-turnstile-response'];
  const ip = req.ip;

  if (await verifyTurnstile(token, ip)) {
    res.json({ success: true });
  } else {
    res.status(403).json({ error: 'CAPTCHA verification failed' });
  }
});
```

### Fix Content Security Policy

```nginx
# Add Turnstile domains to CSP header
# nginx configuration
add_header Content-Security-Policy "
  script-src 'self' https://challenges.cloudflare.com;
  frame-src https://challenges.cloudflare.com;
";
```

### Handle Expired Tokens

```javascript
// Tokens expire after 300 seconds
// Re-request token if form is open too long
let turnstileToken = null;
let tokenTimestamp = null;

function onTurnstileSuccess(token) {
  turnstileToken = token;
  tokenTimestamp = Date.now();
}

function isTokenValid() {
  if (!turnstileToken) return false;
  return Date.now() - tokenTimestamp < 300000; // 5 minutes
}

// Refresh token if needed
function refreshToken() {
  turnstile.reset(); // Reset the widget
}
```

## Common Mistakes

- Using the site key as the secret key (they are different)
- Exposing the secret key in client-side JavaScript
- Not verifying the token on the server side
- Not handling token expiration for long forms
- Blocking the Turnstile script domain in CSP headers

## Related Pages

- [Cloudflare 1020 Error]({{< relref "/tools/cloudflare/cloudflare-1020" >}}) — Access Denied
- [Cloudflare DNS Error]({{< relref "/tools/cloudflare/cloudflare-dns-error" >}}) — DNS resolution failed
