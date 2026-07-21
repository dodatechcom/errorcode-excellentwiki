---
title: "[Solution] Apache Auth Provider Error"
description: "Fix Apache authentication provider errors when mod_auth modules fail to authenticate users."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache Auth Provider Error

Apache fails to authenticate users due to misconfigured authentication provider modules.

```
AH01618: user not found: authorization failure
```

## Common Causes

- AuthProvider module not loaded
- AuthUserFile points to wrong file
- Password file format is incorrect
- Digest authentication requires different hash
- Module order conflicts in authentication stack

## How to Fix

### Verify Module Loading

```bash
apachectl -M | grep auth
# Should show: auth_basic_module, authn_file_module, authz_user_module
```

### Configure Basic Auth

```apache
<Directory "/var/www/protected">
    AuthType Basic
    AuthName "Restricted Area"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>
```

### Create Password File

```bash
# Create new password file
htpasswd -c /etc/apache2/.htpasswd admin

# Add user to existing file
htpasswd /etc/apache2/.htpasswd user1
```

### Fix Digest Auth

```bash
# Use htdigest instead of htpasswd for digest auth
htdigest -c /etc/apache2/.htdigest realm_name username
```

```apache
<Directory "/var/www/digest-protected">
    AuthType Digest
    AuthName "Digest Realm"
    AuthDigestProvider file
    AuthUserFile /etc/apache2/.htdigest
    Require valid-user
</Directory>
```

## Examples

```apache
# Multiple auth providers
<Directory "/var/www/multi-auth">
    AuthType Basic
    AuthName "Multi Auth"
    AuthBasicProvider file ldap
    AuthUserFile /etc/apache2/.htpasswd
    AuthLDAPURL "ldap://ldap.example.com/dc=example,dc=com"
    Require valid-user
</Directory>
```
