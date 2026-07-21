---
title: "[Solution] Netlify Form ReCAPTCHA Error"
description: "Fix Netlify form reCAPTCHA errors. Resolve issues when CAPTCHA verification fails."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Form ReCAPTCHA Error

Fix Netlify form reCAPTCHA errors. Resolve issues when CAPTCHA verification fails.

## Common Causes

- ReCAPTCHA site key is not configured correctly in the form settings
- ReCAPTCHA score threshold is too high rejecting valid submissions
- ReCAPTCHA script is blocked by the Content Security Policy headers
- Form submission does not include the reCAPTCHA response token

## How to Fix

### Check Configuration

Review your configuration files for incorrect settings.

```json
{
  "setting": "correct-value",
  "enabled": true
}
```

### Verify File Paths

Ensure all file paths in your configuration are correct and files exist on disk.

### Clear Cache and Restart

Delete cached data and restart the development server.

```bash
# Clear cache
rm -rf node_modules/.cache
# Restart server
npm run dev
```

### Update Dependencies

Ensure all packages are up to date and compatible.

```bash
npm update
npm audit fix
```

## Examples

```json
{
  "fix": "applied",
  "setting": "value"
}
```
