---
title: "[Solution] Netlify Deploy Notification Error"
description: "Fix Netlify deploy notification errors when email, Slack, or webhook notifications fail."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Netlify Deploy Notification Error

Netlify deploy notifications fail to send via email, Slack, or webhook.

```
Failed to send deploy notification
```

## Common Causes

- Slack webhook URL expired or invalid
- Email notification not configured
- Webhook endpoint unreachable
- Notification settings not saved
- API token expired

## How to Fix

### Configure Slack Notifications

```toml
# netlify.toml
[build]
  command = "npm run build"

# Notifications configured in Netlify Dashboard
# Site settings > Notifications
```

### Update Webhook URL

```bash
# Test webhook endpoint
curl -X POST https://hooks.slack.com/services/YOUR/WEBHOOK/URL \
  -H 'Content-type: application/json' \
  -d '{"text":"Test notification"}'
```

### Check Notification Settings

```bash
# Via Netlify CLI
netlify api getSite --data '{"site_id": "YOUR_SITE_ID"}' | jq '.notifications'
```

### Configure Deploy Notifications in Dashboard

```
1. Go to Site settings > Notifications
2. Add notification channel
3. Select deploy events: Succeeded, Failed, Building
4. Test notification
```

### Disable Problematic Notifications

```toml
# In netlify.toml, no direct notification config
# Use Dashboard to manage notifications
```

## Examples

```toml
# Custom notification via build hooks
[[plugins]]
  package = "netlify-plugin-webhook"
  [plugins.inputs]
    url = "https://hooks.slack.com/services/YOUR/WEBHOOK"
    method = "POST"
    body = '{"text": "Deploy $DEPLOY_URL"}'
```
