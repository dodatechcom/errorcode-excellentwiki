---
title: "[Solution] Cloudflare Argo Tunnel Connection Lost Error — How to Fix"
description: "Fix Cloudflare Argo Tunnel connection lost errors. Resolve tunnel drops, reconnection failures, and cloudflared daemon issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Cloudflare Argo Tunnel connection lost error occurs when the `cloudflared` daemon loses its connection to Cloudflare's edge network, making your origin server unreachable through the tunnel. This results in 502 or 503 errors for your domain.

## What This Error Means

Argo Tunnels (now called Cloudflare Tunnels) create a persistent outbound connection from your origin server to Cloudflare's edge. When this connection drops, Cloudflare cannot reach your origin, and requests fail. Unlike traditional DNS routing, tunnels do not require inbound ports to be open on your server. The tunnel maintains four concurrent connections to Cloudflare for redundancy.

## Why It Happens

- The `cloudflared` process crashed or was restarted
- Network connectivity between your server and Cloudflare was interrupted
- The tunnel token expired or was revoked
- The origin server is unreachable locally (service is down)
- DNS resolution inside the tunnel environment failed
- The server ran out of memory and the OOM killer stopped `cloudflared`
- A firewall rule on your network blocks outbound HTTPS connections
- The tunnel configuration file is corrupted
- Multiple `cloudflared` instances are competing for the same tunnel

## Common Error Messages

- `Connection lost` — The tunnel connection was unexpectedly terminated
- `Failed to connect to Cloudflare edge` — Outbound connection to Cloudflare blocked
- `Tunnel token invalid` — The authentication token is expired or revoked
- `No such host` — DNS resolution failed within the tunnel environment
- `WebSocket upgrade failed` — The tunnel WebSocket connection could not be established
- `Connection refused` — Local origin service is not running

## How to Fix It

### Check Tunnel Status

```bash
# Check if cloudflared is running
systemctl status cloudflared

# Check cloudflared logs
journalctl -u cloudflared -f --since "1 hour ago"

# For Docker-based tunnels
docker logs cloudflared --tail 100

# Check tunnel health via API
curl -X GET "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/tunnels/TUNNEL_ID/health" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Check active connections
curl -X GET "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/tunnels/TUNNEL_ID/connections" \
  -H "Authorization: Bearer YOUR_API_TOKEN" | jq '.result'
```

### Restart the Tunnel Service

```bash
# Systemd restart
sudo systemctl restart cloudflared

# Docker restart
docker restart cloudflared

# Verify it reconnected
journalctl -u cloudflared -f --since "1 minute ago"

# You should see:
# "Connection registered" connIndex=0
# "Connection registered" connIndex=1
# "Connection registered" connIndex=2
# "Connection registered" connIndex=3
```

### Verify Network Connectivity

```bash
# Test outbound HTTPS to Cloudflare
curl -v https://argotunnel.com --connect-timeout 10

# Check DNS resolution
nslookup your-tunnel-domain.cfargotunnel.com

# Check if port 7844 is reachable (cloudflared WebSocket)
nc -zv region1.v2.argotunnel.com 7844

# Test from within the tunnel config context
cloudflared tunnel --url http://localhost:8080 --no-autoupdate
```

### Fix Memory Issues

```bash
# Check cloudflared memory usage
ps aux | grep cloudflared

# If memory usage is high, check for leaks in logs
journalctl -u cloudflared | grep -i "memory\|oom\|killed"

# Set memory limits in systemd
sudo systemctl edit cloudflared
# Add:
# [Service]
# MemoryMax=512M
# Restart=always
# RestartSec=5
```

### Recreate the Tunnel

```bash
# Delete old tunnel
cloudflared tunnel delete old-tunnel-name

# Create new tunnel
cloudflared tunnel create new-tunnel-name

# Update DNS records
cloudflared tunnel route dns new-tunnel-name your-domain.com

# Start the new tunnel
cloudflared tunnel run new-tunnel-name

# Or recreate from the dashboard
# Cloudflare Dashboard > Zero Trust > Networks > Tunnels
```

### Configure Automatic Recovery

```bash
# /etc/systemd/system/cloudflared.service
[Unit]
Description=Cloudflare Tunnel
After=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/cloudflared tunnel run --token YOUR_TUNNEL_TOKEN
Restart=always
RestartSec=5
MemoryMax=512M
StartLimitBurst=5
StartLimitIntervalSec=60

[Install]
WantedBy=multi-user.target

# Enable and start
sudo systemctl daemon-reload
sudo systemctl enable cloudflared
sudo systemctl start cloudflared
```

### Monitor Tunnel Health

```bash
# Set up a health check script
#!/bin/bash
TUNNEL_STATUS=$(curl -s "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/tunnels/TUNNEL_ID/health" \
  -H "Authorization: Bearer YOUR_API_TOKEN" | jq -r '.result')

if [ "$TUNNEL_STATUS" != "healthy" ]; then
  echo "Tunnel is unhealthy, restarting..."
  sudo systemctl restart cloudflared
fi

# Add to cron for regular checks
# */5 * * * * /path/to/check-tunnel.sh >> /var/log/tunnel-health.log 2>&1
```

## Common Scenarios

- **Server reboot:** The server was rebooted and `cloudflared` did not start automatically because it was not configured as a systemd service.
- **Credential rotation:** The tunnel credentials file was deleted or the tunnel was recreated in the dashboard without updating the local configuration.
- **Resource exhaustion:** The origin server ran out of file descriptors or memory, causing the `cloudflared` process to be killed by the OOM killer.

## Prevent It

1. Configure `cloudflared` as a systemd service with `Restart=always` and `RestartSec=5` for automatic recovery
2. Monitor tunnel health via the Cloudflare API and set up alerts for tunnel disconnections
3. Allocate dedicated memory limits for `cloudflared` and monitor usage with Prometheus or Datadog

## Related Pages

- [Cloudflare 522 Error]({{< relref "/tools/cloudflare/cloudflare-522" >}}) — Origin connection timeout
- [Cloudflare 502 Error]({{< relref "/tools/cloudflare/cloudflare-502" >}}) — Bad gateway
