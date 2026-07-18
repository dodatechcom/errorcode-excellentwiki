---
title: "[Solution] Cloudflare 1016 Error — Origin DNS Error"
description: "Fix Cloudflare Error 1016 when DNS resolution for the origin server fails. Correct DNS records and verify origin server accessibility through Cloudflare."
tools: ["cloudflare"]
error-types: ["dns-error"]
severities: ["error"]
weight: 5
---

Cloudflare Error 1016 occurs when Cloudflare cannot resolve the origin server's hostname to an IP address. The origin DNS lookup fails, preventing Cloudflare from forwarding requests.

## What This Error Means

When Cloudflare proxies traffic, it resolves your origin server's hostname. If that DNS lookup fails, Cloudflare returns a 1016 error to the visitor.

## Why It Happens

- The origin server hostname in the Cloudflare dashboard DNS record does not resolve
- The origin CNAME record points to a hostname that no longer exists
- The external DNS provider for the origin hostname is down or misconfigured
- The origin domain has expired or the DNS zone was deleted
- The DNS record uses a CNAME to a domain with no A or AAAA record

## How to Fix It

### Test Origin DNS Resolution

```bash
dig your-origin-hostname.com A +short
dig your-origin-hostname.com AAAA +short
```

### Check the Cloudflare DNS Record

Verify the DNS record in Cloudflare for your domain points to a resolvable origin.

### Use an IP Directly

Instead of a CNAME to an origin hostname, use an A or AAAA record with the origin IP:

```
Type: A
Name: origin
Content: 203.0.113.10
```

### Check DNS Propagation

```bash
dig @1.1.1.1 your-origin-hostname.com
dig @8.8.8.8 your-origin-hostname.com
```

### Verify Origin Server Status

```bash
curl -H "Host: your-domain.com" http://<origin-ip>
```

### Fix CNAME Chain

Ensure the entire CNAME chain resolves. Each step in the chain must have a valid DNS record.

## Common Mistakes

- Using a CNAME to an origin that itself uses a CNAME to a non-existent host
- Not testing origin DNS resolution from outside the hosting network
- Assuming Cloudflare resolves DNS the same way as local tools
- Forgetting to update origin DNS after migrating hosting providers

## Related Pages

- [Cloudflare 1000 Error]({{< relref "/tools/cloudflare/cloudflare-1000" >}}) -- Prohibited IP
- [Cloudflare DNS Error]({{< relref "/tools/cloudflare/cloudflare-dns-error" >}}) -- DNS configuration
- [Cloudflare 522 Error]({{< relref "/tools/cloudflare/cloudflare-522" >}}) -- Connection timeout
