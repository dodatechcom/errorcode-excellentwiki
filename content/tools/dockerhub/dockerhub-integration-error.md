---
title: "[Solution] Docker Hub Integration Error"
description: "Fix Docker Hub integration errors. Learn why this happens and how to resolve it quickly."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Hub Integration Error

Docker Hub integration errors occur when connecting to GitHub, Bitbucket, or other services fails.

## Why This Happens

- Integration not connected
- OAuth failed
- Webhook not delivering
- Build not triggered

## Common Error Messages

- `integration_not_connected_error`
- `integration_oauth_error`
- `integration_webhook_error`
- `integration_build_error`

## How to Fix It

### Solution 1: Check integration

Verify integration status in Docker Hub settings.

### Solution 2: Reconnect integration

Reconnect the service integration.

### Solution 3: Fix webhook

Check webhook configuration and delivery.


## Common Scenarios

- **Integration not connected:** Reconnect the integration.
- **OAuth failed:** Re-authenticate with the service.

## Prevent It

- Test integrations regularly
- Monitor build status
- Keep integrations updated
