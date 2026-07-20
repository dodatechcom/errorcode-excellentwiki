---
title: "[Solution] Jenkins Login Failed"
description: "Fix Jenkins login failed errors. Resolve authentication and login issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Login Failed

Login failures occur when Jenkins cannot authenticate the user.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Security Realm
# Verify LDAP/AD settings
```

### Reset Admin Password

```bash
# Edit $JENKINS_HOME/users/admin/config.xml
# Remove <passwordHash> line, restart Jenkins, set new password
```
