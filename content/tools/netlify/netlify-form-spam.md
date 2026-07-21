---
title: "[Solution] Netlify Form Spam Error"
description: "Fix Netlify form spam errors when form submissions receive spam or bot-generated entries."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Netlify Form Spam Error

Netlify forms receive spam submissions or bot-generated entries.

```
Spam submissions detected in form: contact
```

## Common Causes

- No CAPTCHA protection on forms
- Honeypot field missing or not configured
- Akismet spam filtering not enabled
- Form is publicly accessible without verification
- Bot submitting form programmatically

## How to Fix

### Add Honeypot Field

```html
<form name="contact" netlify>
  <p hidden>
    <label>Don't fill this out: <input name="bot-field" /></label>
  </p>
  <input type="text" name="name" />
  <input type="email" name="email" />
  <textarea name="message"></textarea>
  <button type="submit">Send</button>
</form>
```

### Add CAPTCHA

```html
<form name="contact" netlify data-netlify-recaptcha="true">
  <input type="text" name="name" />
  <input type="email" name="email" />
  <textarea name="message"></textarea>
  <div data-netlify-recaptcha="true"></div>
  <button type="submit">Send</button>
</form>
```

### Enable Akismet

```
1. Go to Site settings > Forms
2. Enable Akismet spam filtering
3. Provide Akismet API key if required
```

### Block Spam IPs via Edge Functions

```javascript
// netlify/edge-functions/block-spam.js
export default async (request, context) => {
  const ip = context.ip;
  const blockedIPs = ["1.2.3.4", "5.6.7.8"];
  
  if (blockedIPs.includes(ip)) {
    return new Response("Blocked", { status: 403 });
  }
};

export const config = { path: "/api/contact" };
```

## Examples

```html
<!-- Complete spam-protected form -->
<form name="contact" method="POST" data-netlify="true" data-netlify-recaptcha="true">
  <input type="hidden" name="form-name" value="contact" />
  <p hidden>
    <label>Leave empty: <input name="bot-field" /></label>
  </p>
  <input type="text" name="name" required />
  <input type="email" name="email" required />
  <textarea name="message" required></textarea>
  <div data-netlify-recaptcha="true"></div>
  <button type="submit">Send</button>
</form>
```
