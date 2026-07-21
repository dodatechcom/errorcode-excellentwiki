---
title: "Network Security Config Error"
description: "Fix Android network security configuration and certificate trust errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App cannot connect to server because of network security configuration issues

## Common Causes

- Certificate not trusted by default system trust store
- Custom CA certificate not configured
- Cleartext HTTP traffic not allowed
- Domain not matching network_security_config entry

## Fixes

- Add domain config with trusted certificates
- Use cleartextTrafficPermitted for HTTP if needed
- Verify domain name matches exactly
- Use debug-config for development certificates

## Code Example

```kotlin
<!-- res/xml/network_security_config.xml -->
<network-security-config>
    <!-- Allow cleartext for dev server -->
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">10.0.2.2</domain>
        <domain includeSubdomains="true">localhost</domain>
    </domain-config>

    <!-- Trust custom CA -->
    <domain-config>
        <domain>api.example.com</domain>
        <trust-anchors>
            <certificates src="@raw/my_ca_cert" />
        </trust-anchors>
    </domain-config>
</network-security-config>
```

<!-- AndroidManifest.xml -->
<application
    android:networkSecurityConfig="@xml/network_security_config"
    ...>
