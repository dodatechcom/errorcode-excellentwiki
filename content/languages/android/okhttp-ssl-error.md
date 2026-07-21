---
title: "OkHttp SSL Error"
description: "Fix OkHttp SSL certificate and TLS handshake errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
OkHttp requests fail with SSL certificate or TLS handshake exceptions

## Common Causes

- Server certificate not trusted by Android
- SSL pinning configuration incorrect
- Certificate expired or hostname mismatch
- Self-signed certificate not accepted

## Fixes

- Add network security config for custom trust anchors
- Configure certificate pinning correctly
- Use NetworkSecurityConfig for debug builds
- Never disable SSL verification in production

## Code Example

```kotlin
<!-- res/xml/network_security_config.xml -->
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config>
        <domain includeSubdomains="true">api.example.com</domain>
        <pin-set expiration="2025-12-31">
            <pin digest="SHA-256">base64EncodedPin==</pin>
            <pin digest="SHA-256">backupPinBase64==</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

<!-- AndroidManifest.xml -->
<application
    android:networkSecurityConfig="@xml/network_security_config"
    ...>
