---
title: "[Solution] Cloudflare 502 Bad Gateway Error — Origin Server Issue"
description: "Fix Cloudflare 502 Bad Gateway errors. Resolve origin server communication failures and gateway timeout issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
---

A Cloudflare 502 Bad Gateway error occurs when Cloudflare cannot connect to or receive a valid response from your origin server. Cloudflare acts as a reverse proxy, and when the origin is unreachable or returns an invalid response, this error appears.

## What This Error Means

The 502 error means Cloudflare successfully reached your server, but the server returned an invalid, incomplete, or unexpected response. This is different from a 522 error where the connection itself fails.

Common 502 variations:

- **502 Bad Gateway** — Origin returned an invalid response
- **502 Ray ID** — Unique identifier for debugging (shown on error page)
- **Cloudflare 502 from nginx** — Origin nginx is misconfigured

## Why It Happens

- The origin web server is overloaded or crashed
- Application code is throwing unhandled exceptions
- The origin server is restarting or shutting down
- Reverse proxy on the origin (nginx/Apache) is misconfigured
- Firewall rules on the origin are blocking Cloudflare IPs
- The application is using incompatible protocols
- PHP-FPM or application process pools have exhausted

## How to Fix It

### Check Origin Server Status

```bash
# Test origin directly (bypass Cloudflare)
curl -I http://your-origin-ip.com

# Check if the server is responding
telnet your-origin-ip.com 80
```

### Verify Origin Web Server

```bash
# For nginx
sudo systemctl status nginx
sudo nginx -t

# For Apache
sudo systemctl status apache2
sudo apachectl configtest
```

### Check Application Process

```bash
# Check if PHP-FPM is running
sudo systemctl status php8.1-fpm

# Check if your Node.js app is running
pm2 status

# View application logs
tail -f /var/log/nginx/error.log
```

### Whitelist Cloudflare IPs

```bash
# Allow all Cloudflare IP ranges on origin
# Get current list: https://www.cloudflare.com/ips/

# iptables example
for ip in 173.245.48.0/20 103.21.244.0/22 103.22.200.0/22; do
  iptables -A INPUT -p tcp -s $ip --dport 80 -j ACCEPT
done
```

### Increase Timeouts

```nginx
# nginx config on origin
proxy_connect_timeout 60s;
proxy_send_timeout 60s;
proxy_read_timeout 60s;
```

## Common Mistakes

- Only checking Cloudflare without testing the origin directly
- Not monitoring origin server resource usage
- Forgetting to update Cloudflare IP whitelist after changes
- Deploying code changes without graceful restarts
- Not setting up health checks on the origin server

## Related Pages

- [Cloudflare 522 Error]({{< relref "/tools/cloudflare/cloudflare-522" >}}) — Connection timed out
- [Cloudflare 524 Error]({{< relref "/tools/cloudflare/cloudflare-524" >}}) — A timeout occurred
