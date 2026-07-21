---
title: "OkHttp DNS Error"
description: "Fix OkHttp DNS resolution errors and custom DNS configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
OkHttp requests fail because DNS resolution fails or returns wrong IP

## Common Causes

- DNS resolution failing on certain networks
- DNS over HTTPS not configured
- Custom DNS resolver returning null
- IPv6 not supported on target network

## Fixes

- Implement custom Dns interface for custom resolution
- Use DnsOverHttps for encrypted DNS
- Provide fallback DNS servers
- Handle DNS failures gracefully with retries

## Code Example

```kotlin
val customDns = object : Dns {
    override fun lookup(hostname: String): List<InetAddress> {
        return try {
            InetAddress.getAllByName(hostname).toList()
        } catch (e: UnknownHostException) {
            // Fallback to Google DNS
            Dns.SYSTEM.lookup(hostname)
        }
    }
}

val client = OkHttpClient.Builder()
    .dns(customDns)
    .build()
```

# For DNS over HTTPS:
val dnsOverHttps = DnsOverHttps.Builder()
    .client(OkHttpClient())
    .url("https://dns.google/dns-query".toHttpUrl())
    .build()
