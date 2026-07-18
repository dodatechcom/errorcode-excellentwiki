---
title: "[Solution] Cloudflare 1000 Error — DNS Points to Prohibited IP"
description: "Fix Cloudflare Error 1000 when DNS resolves to a restricted IP address. Update DNS records to point to the correct origin server IP and check proxy settings."
tools: ["cloudflare"]
error-types: ["dns-error"]
severities: ["error"]
weight: 5
---

Cloudflare Error 1000 occurs when DNS points to an IP address that Cloudflare is prohibited from proxying. Cloudflare blocks traffic to certain IP ranges to prevent abuse.

## What This Error Means

Cloudflare refuses to proxy traffic to the DNS target because the IP address is in a restricted range. This includes private IPs, reserved IPs, and known bad actor addresses.

## Why It Happens

- DNS points to a private IP (10.x.x.x, 172.16-31.x.x, 192.168.x.x)
- DNS points to localhost (127.0.0.1 or ::1)
- DNS points to a Cloudflare IP address (creating a loop)
- DNS points to a known malicious or abuse IP
- The A or AAAA record was accidentally set to an internal or test IP
- The IP address was recently used for abuse and is blocked by Cloudflare

## How to Fix It

### Check the Current DNS Resolution

```bash
dig your-domain.com A +short
dig your-domain.com AAAA +short
```

### Update to the Correct Origin IP

In the Cloudflare dashboard, update the DNS A or AAAA record to point to your real origin server IP:

```
Type: A
Name: @
Content: <your-origin-server-public-ip>
Proxy status: Proxied
```

### Check for Private IPs

Ensure the IP is not any of these ranges:

- 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 (private)
- 127.0.0.0/8 (localhost)
- 169.254.0.0/16 (link-local)
- 100.64.0.0/10 (CGNAT)

### Use a Public Origin Server

Your origin must have a public, routable IP address. Use `curl ifconfig.me` on your server to find its public IP.

### Check for Proxy Loops

Ensure your DNS does not point to any Cloudflare IP. Use `dig cloudflare.com` for reference ranges.

## Common Mistakes

- Pointing DNS to a private IP when developing locally and forgetting to change it for production
- Using a Cloudflare IP as the origin (creates a proxy loop)
- Not checking whether the IP is in a reserved range before adding the record
- Pointing DNS to a load balancer internal IP instead of its public IP

## Related Pages

- [Cloudflare DNS Error]({{< relref "/tools/cloudflare/cloudflare-dns-error" >}}) -- DNS configuration issues
- [Cloudflare 1016 Error]({{< relref "/tools/cloudflare/cloudflare-1016" >}}) -- Origin DNS error
- [Cloudflare 1020 Error]({{< relref "/tools/cloudflare/cloudflare-1020" >}}) -- Access denied
