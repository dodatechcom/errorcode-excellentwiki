---
title: "SSL Pinning Error"
description: "Fix SSL certificate pinning errors in Android network security configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App cannot connect to server because SSL pin does not match server certificate

## Common Causes

- Pin hash does not match server certificate
- Backup pin not provided causing lockout
- Pin expiration date passed
- Network security config not applied to domain

## Fixes

- Verify pin hash matches current certificate
- Provide at least two pins for backup
- Set reasonable expiration date
- Ensure domain matches in network_security_config.xml

## Code Example

```kotlin
<!-- res/xml/network_security_config.xml -->
<network-security-config>
    <domain-config>
        <domain includeSubdomains="true">api.example.com</domain>
        <pin-set expiration="2025-12-31">
            <pin digest="SHA-256">3vorylECiaRPkqMn6fC0UB6F...=</pin>
            <pin digest="SHA-256">vZG4sHqPF9CpHlGdL3Pv9M3...=</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

# Get certificate pin:
openssl s_client -connect api.example.com:443 | openssl x509 -pubkey | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64
# Always include backup pin!
