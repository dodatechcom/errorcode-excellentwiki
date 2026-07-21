---
title: "InfluxDB User Error"
description: "User management failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Cannot create, modify, or authenticate users.

## Common Causes
- Duplicate username
- Password policy violation
- User locked out

## How to Fix
```bash
# List users
influx user list --org myorg

# Create user
influx user create --name myuser --password mypassword --org myorg
```

## Examples
```bash
# Reset password
influx user reset-password --id <user-id> --password newpassword
# Delete user
influx user delete --id <user-id>
```

