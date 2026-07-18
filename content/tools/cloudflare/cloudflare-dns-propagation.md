---
title: "[Solution] Cloudflare DNS Propagation Delay or Failure Error — How to Fix"
description: "Fix Cloudflare DNS propagation delays or failures. Resolve stuck DNS updates, nameserver issues, and stale resolver cache across regions."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Cloudflare DNS propagation delay or failure occurs when DNS record changes do not propagate across the global DNS system within the expected timeframe, or fail to propagate entirely. This affects site availability for users in certain regions who still receive old DNS responses.

## What This Error Means

DNS propagation is the process by which DNS resolvers worldwide update their cached records based on TTL values. When you change a DNS record in Cloudflare, the change must propagate to thousands of recursive resolvers globally. With Cloudflare, you might change a record in your dashboard but find that some users still resolve the old IP address. In severe cases, propagation may appear stuck entirely or some resolvers never pick up the new records.

## Why It Happens

- TTL values on existing records are high (e.g., 86400 seconds = 24 hours)
- Your registrar has not updated the nameservers to Cloudflare
- An upstream DNS resolver is caching stale records aggressively
- The DNS record type is invalid or misconfigured
- You changed nameservers but the registrar-side propagation is incomplete
- The local ISP DNS resolver has not flushed its cache yet
- The DNS record has conflicting data between Cloudflare and the origin
- You have DNSSEC enabled at the registrar but the DS records are incorrect
- A CDN or proxy is caching old DNS responses beyond the TTL

## Common Error Messages

- `DNS_PROBE_FINISHED_NXDOMAIN` — The domain could not be resolved by any DNS server
- `SERVFAIL` — The nameserver returned a general failure response
- `DNS resolution timed out` — Cloudflare could not resolve the record within the timeout window
- `No DNS records found for this domain` — Records are missing or have not propagated
- `REFUSED` — The DNS server refused to answer the query
- `NXDOMAIN` — The domain name does not exist in DNS

## How to Fix It

### Check Current Propagation Status

```bash
# Check Cloudflare DNS directly (bypassing local cache)
dig @1.1.1.1 your-domain.com +short

# Check against Google DNS
dig @8.8.8.8 your-domain.com +short

# Check against Quad9 DNS
dig @9.9.9.9 your-domain.com +short

# Check against your origin IP for comparison
dig @your-origin-nameserver your-domain.com +short

# Full propagation check with TTL
dig your-domain.com +noall +answer

# Check specific record types
dig your-domain.com A +short
dig your-domain.com CNAME +short
dig your-domain.com MX +short
dig your-domain.com TXT +short

# Check from a third-party propagation checker
# Visit: https://dnschecker.org or https://whatsmydns.net
# Enter your domain and select the record type
```

### Lower TTL Before Making Changes

```bash
# Before making a big DNS change, lower TTL 24-48 hours ahead
# In Cloudflare Dashboard: DNS > Records > Edit > TTL > 300 (5 min)

# Or use the Cloudflare API to lower TTL
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records/RECORD_ID" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"ttl": 300}'

# After the change has propagated (wait for old TTL to expire), raise TTL back
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records/RECORD_ID" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"ttl": 3600}'
```

### Verify Nameserver Configuration

```bash
# Check if Cloudflare nameservers are set at the registrar
dig your-domain.com NS +short

# Expected output should be Cloudflare nameservers like:
# ns1.cloudflare.com.
# ns2.cloudflare.com.

# If you see your old nameservers, update them at your registrar
# This is the most common cause of DNS propagation failure

# Check NS records at the TLD nameservers
dig your-domain.com NS +trace

# The trace will show the delegation chain from root -> TLD -> your domain
```

### Force Propagation with API

```bash
# Purge Cloudflare cache to ensure DNS records are fresh
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything": true}'

# Verify the zone is active in Cloudflare
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID" \
  -H "Authorization: Bearer YOUR_API_TOKEN" | jq '.result.status'

# Expected: "active"
# If "pending", nameserver change is still propagating
```

### Flush Local DNS Cache

```bash
# Linux (systemd-resolved)
sudo systemd-resolve --flush-caches
sudo systemd-resolve --statistics | grep -i cache

# macOS
sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder

# Windows
ipconfig /flushdns

# Verify flush worked
nslookup your-domain.com 8.8.8.8

# Chrome internal DNS flush
# Navigate to: chrome://net-internals/#dns
# Click "Clear host cache"
```

### Fix DNSSEC Issues

```bash
# Check if DNSSEC is properly configured
dig your-domain.com DNSKEY +short

# Verify DS records at the registrar
dig your-domain.com DS +short

# If DNSSEC is causing issues, you may need to:
# 1. Disable DNSSEC at the registrar, OR
# 2. Update DS records to match Cloudflare's DNSSEC keys

# Check Cloudflare DNSSEC status in Dashboard:
# DNS > Settings > DNSSEC
```

### Use Cloudflare API for DNS Record Management

```bash
# Create a new DNS record with proper TTL
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "type": "A",
    "name": "example.com",
    "content": "192.0.2.1",
    "ttl": 300,
    "proxied": true
  }'

# List all DNS records to verify
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records" \
  -H "Authorization: Bearer YOUR_API_TOKEN" | jq '.result[] | {type, name, content, ttl}'
```

## Common Scenarios

- **After nameserver migration:** Registrar takes 24-48 hours to propagate NS changes. During this window, some resolvers see the old NS records and return stale data. This is the most common DNS propagation issue.
- **TTL mismatch:** Old records had a 24-hour TTL. Even after Cloudflare propagates, resolvers hold the stale value until TTL expires. Users near ISP resolvers with aggressive caching may see old records for up to 48 hours.
- **Partial propagation:** Cloudflare has propagated globally, but your local ISP resolver cached the old record and ignores the new TTL. The resolver may also be ignoring TTL values entirely (some ISPs do this).

## Prevent It

1. Lower TTL to 300 seconds at least 48 hours before any planned DNS migration or major record change
2. Always verify propagation from multiple DNS resolvers (1.1.1.1, 8.8.8.8, 9.9.9.9) after making changes
3. Use Cloudflare's API health checks to monitor DNS resolution from multiple locations and alert on propagation delays

## Related Pages

- [Cloudflare DNS Error]({{< relref "/tools/cloudflare/cloudflare-dns-error" >}}) — DNS resolution failure
- [Cloudflare 522 Error]({{< relref "/tools/cloudflare/cloudflare-522" >}}) — Connection timed out
