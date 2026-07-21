---
title: "[Solution] Apache mod_security Error"
description: "Fix Apache mod_security WAF errors when rules block legitimate requests or cause 500 errors."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache mod_security Error

Apache mod_security blocks legitimate requests or returns internal server errors.

```
ModSecurity: Access denied with code 501
[client 1.2.3.4] ModSecurity: Rule processing failed
```

## Common Causes

- Default rules too aggressive
- False positives on POST requests
- Request body exceeds SecRequestBodyLimit
- Rule IDs conflicting
- Log file permissions wrong

## How to Fix

### Disable Specific Rules

```apache
<IfModule mod_security2.c>
    # Disable a specific rule by ID
    SecRuleRemoveById 211020

    # Disable rules by tag
    SecRuleRemoveByTag "paranoid"
</IfModule>
```

### Increase Body Size Limit

```apache
SecRequestBodyLimit 52428800
SecRequestBodyNoFilesLimit 131072
SecRequestBodyLimitAction Reject
```

### Create Custom Rule Exceptions

```apache
<IfModule mod_security2.c>
    # Allow specific path
    <Location "/api/upload">
        SecRuleRemoveById 200002
        SecRuleRemoveById 200003
    </Location>
</IfModule>
```

### Fix Log Permissions

```bash
touch /var/log/modsecurity/modsec_audit.log
chown www-data:www-data /var/log/modsecurity/modsec_audit.log
chmod 644 /var/log/modsecurity/modsec_audit.log
```

### Check OWASP Rule Set Version

```bash
# Verify CRS version
cat /etc/modsecurity/crs/crs-setup.conf | grep CRSVersion
```

## Examples

```apache
# Full mod_security configuration
<IfModule mod_security2.c>
    SecRuleEngine On
    SecRequestBodyAccess On
    SecResponseBodyAccess Off
    SecRequestBodyLimit 52428800
    SecRequestBodyNoFilesLimit 131072
    SecAuditLog /var/log/modsecurity/modsec_audit.log
    SecDebugLog /var/log/modsecurity/debug.log

    # Exempt API upload endpoint
    <Location "/api/files">
        SecRuleRemoveById 200002
    </Location>
</IfModule>
```
