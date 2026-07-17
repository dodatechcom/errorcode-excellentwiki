---
title: "[Solution] Cloudflare 522 Connection Timed Out Error — Fix Origin Timeout"
description: "Fix Cloudflare 522 connection timed out errors. Resolve origin server connection failures and timeout issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 2
---

A Cloudflare 522 error means Cloudflare could not establish a TCP connection to your origin server within the allowed time. Unlike a 502 error where the server responds with an invalid answer, here the server does not respond at all.

## What This Error Means

The 522 error appears when the TCP handshake between Cloudflare and your origin server times out. Cloudflare waits up to 30 seconds for a connection, then returns this error if no response is received.

## Why It Happens

- The origin server is offline or has crashed
- A firewall is blocking Cloudflare IP addresses
- The origin server is overloaded and not accepting new connections
- DNS points to an incorrect IP address
- The server's port 80/443 is not listening
- Network routing issues between Cloudflare and the origin
- The origin server has too many active connections (backlog full)

## How to Fix It

### Test Origin Connectivity

```bash
# Check if origin responds on port 80
curl -v http://your-origin-ip.com --connect-timeout 10

# Check port 443 for HTTPS
curl -v https://your-domain.com --connect-timeout 10

# Test with telnet
telnet your-origin-ip.com 80
```

### Verify DNS Configuration

```bash
# Check what IP your domain points to
dig your-domain.com +short

# Compare with your origin server IP
curl ifconfig.me
```

### Check Firewall Rules

```bash
# Check iptables on origin
sudo iptables -L -n | grep -E "(80|443)"

# Check if Cloudflare IPs are allowed
sudo iptables -A INPUT -p tcp -s 173.245.48.0/20 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 103.21.244.0/22 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 103.22.200.0/22 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 103.31.4.0/22 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 141.101.64.0/18 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 108.162.192.0/18 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 190.93.240.0/20 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 188.114.96.0/20 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 197.234.240.0/22 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 198.41.128.0/17 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 162.158.0.0/15 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 104.16.0.0/13 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 104.24.0.0/14 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 172.64.0.0/13 --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 131.0.72.0/22 --dport 80 -j ACCEPT
```

### Check Server Resources

```bash
# Check available memory
free -m

# Check CPU load
uptime

# Check open file descriptors
cat /proc/sys/fs/file-nr

# Check listening ports
ss -tlnp | grep -E "(80|443)"
```

### Increase Connection Limits

```bash
# Linux kernel tuning
echo 65535 > /proc/sys/net/core/somaxconn
echo 65535 > /proc/sys/net/ipv4/ip_local_port_range
```

## Common Mistakes

- Assuming the issue is with Cloudflare without testing the origin
- Not checking firewall rules after server migration
- Forgetting that Cloudflare only connects on ports 80 and 443
- Not monitoring server resource usage proactively

## Related Pages

- [Cloudflare 502 Error]({{< relref "/tools/cloudflare/cloudflare-502" >}}) — Bad Gateway
- [Cloudflare 524 Error]({{< relref "/tools/cloudflare/cloudflare-524" >}}) — A timeout occurred
