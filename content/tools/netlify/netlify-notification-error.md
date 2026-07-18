---
title: "[Solution] Netlify Notification Error — Fix Notification Webhook Failed"
description: "Fix Netlify notification errors when deploy notifications fail to send. Resolve webhook configuration, Slack integration, and email notification issues."
tools: ["netlify"]
error-types: ["notification-error"]
severities: ["warning"]
weight: 5
---

A Netlify notification error occurs when deploy notifications fail to send via webhook, Slack, email, or other channels. The notification is triggered but the delivery fails.

## What This Error Means

Netlify sends notifications on deploy success, failure, or other events. When notifications fail:

```
Error: Failed to send deploy notification
Webhook POST to https://hooks.slack.com/services/... returned 404
```

## Why It Happens

- The webhook URL is incorrect or expired
- The Slack webhook URL has been revoked
- The email server configuration is invalid
- The notification service is rate-limiting requests
- The payload format does not match the receiver's expectations
- The notification endpoint returns an error (404, 500, timeout)
- The notification context variables are not properly configured
- The secret token for HMAC-signed webhooks does not match

## How to Fix It

### Check Webhook URL

```toml
[[notification]]
  from = "Slack"
  type = "webhook"
  url = "https://hooks.slack.com/services/T00/B00/xxx"
  event = "deploy_succeeded"
```

### Test the Webhook Manually

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"text": "Test notification from Netlify"}' \
  https://hooks.slack.com/services/T00/B00/xxx
```

### Check Failed Notification Logs

Netlify Dashboard > Site > Deploys > Notifications > View Logs.

### Verify Event Type

```toml
[[notification]]
  from = "Slack"
  type = "slack"
  event = "deploy_failed"
  # Valid events: deploy_succeeded, deploy_failed, deploy_locked, deploy_unlocked
```

### Update the Webhook URL

If the URL has changed, update it in the dashboard or netlify.toml.

### Configure Email Notifications

```toml
[[notification]]
  from = "Email"
  type = "email"
  to = "team@example.com"
  event = "deploy_failed"
```

### Add HMAC Verification

```toml
[[notification]]
  from = "Custom Webhook"
  type = "webhook"
  url = "https://api.example.com/netlify-hook"
  event = "deploy_succeeded"
  secret = "your-secret-token"
```

## Common Mistakes

- Using an expired or revoked Slack webhook URL
- Not selecting the correct event type for the notification
- Forgetting to test webhooks after changing the receiving service
- Using HTTP instead of HTTPS for webhook endpoints

## Related Pages

- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) -- Deploy failures
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
- [Netlify Plugin Error]({{< relref "/tools/netlify/netlify-plugin-error" >}}) -- Plugin issues
