---
title: "[Solution] Heroku Log Drain Error - Fix Log Drain Connection Failed"
description: "Fix Heroku log drain connection failures. Resolve drain URL, SSL, and network issues for Heroku log aggregation."
tools: ["heroku"]
error-types: ["log-drain"]
severities: ["warning"]
weight: 5
---

This error means your Heroku log drain cannot connect to the external logging endpoint. The drain URL may be wrong, the endpoint may be down, or SSL verification is failing.

## What This Error Means

When a log drain cannot establish a connection, you see:

```
L10 - Drain error: could not connect to drain
# or
app[router]: error connecting to drain
```

Log drains forward your app's logs to external services like Papertrail, Logentries, or a custom endpoint. When the connection fails, logs are buffered locally but not sent.

## Why It Happens

- The drain URL is incorrect or has been changed
- The logging service endpoint is down or unreachable
- SSL certificate verification is failing
- The drain token or authentication is invalid
- Network firewalls block outbound connections from Heroku dynos
- The logging service has rate limits that are being exceeded
- The drain was added to a different app than intended

## How to Fix It

### Check current drains

```bash
heroku drains -a my-app
```

List all configured drains and their status.

### Update the drain URL

```bash
heroku drains:replace old-drain-url new-drain-url -a my-app
```

### Verify the drain endpoint is reachable

```bash
curl -I https://logs.papertrailapp.com:12345
```

Check that the endpoint responds and the SSL certificate is valid.

### Add a new drain

```bash
heroku drains:add syslog+tls://logs.papertrailapp.com:12345 -a my-app
```

### Check drain status

```bash
heroku drains:info -a my-app
```

This shows the drain URL, token, and recent delivery status.

### Verify SSL certificate

```bash
openssl s_client -connect logs.example.com:514 -showcerts
```

Expired or self-signed certificates cause drain failures.

### Check for rate limiting

```bash
heroku logs -a my-app | grep "drain"
```

Frequent drain errors may indicate the endpoint is overwhelmed.

### Use Heroku Log Drains for syslog

```bash
heroku drains:add syslog+tls://logs.example.com:514 --app my-app --token MY_TOKEN
```

Include the token for authenticated drains.

## Common Mistakes

- Not including the correct port in the drain URL
- Forgetting that Heroku requires TLS for syslog drains
- Not checking if the logging service is down before troubleshooting Heroku
- Using HTTP instead of HTTPS for the drain endpoint
- Not rotating drain tokens when they are compromised

## Related Pages

- [Heroku Deploy Error]({{< relref "/tools/heroku/heroku-deploy-error" >}}) -- deployment issues
- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) -- configuration problems
- [Heroku API Error]({{< relref "/tools/heroku/heroku-api-error" >}}) -- API failures
