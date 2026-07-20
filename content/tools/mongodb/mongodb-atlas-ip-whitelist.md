---
title: "[Solution] MongoDB Atlas IP Whitelist Error"
description: "Fix MongoDB Atlas IP whitelist connection errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Atlas IP Whitelist Error

```
MongoServerError: Cannot connect to MongoDB Atlas
```

```
IP address is not whitelisted in the Atlas IP whitelist
```

## Common Causes

- The client IP address is not in the Atlas whitelist
- The IP address changed (dynamic IP)
- The Atlas project has no IP whitelist entries
- The whitelist entry is incorrect (wrong IP or CIDR)

## How to Fix

### 1. Add the client IP to the Atlas whitelist

1. Go to Atlas dashboard -> Network Access
2. Click "Add IP Address"
3. Enter the client IP or select "Allow Access from Anywhere" (0.0.0.0/0) for development

### 2. Use the Atlas API to add IPs

```bash
curl --user "publicKey:privateKey" \
  --data '{"ipAddress":"203.0.113.50","comment":"Office IP"}' \
  --header "Content-Type: application/json" \
  https://cloud.mongodb.com/api/atlas/v1.0/groups/<projectId>/whitelist
```

### 3. Check current whitelist

```bash
curl --user "publicKey:privateKey" \
  https://cloud.mongodb.com/api/atlas/v1.0/groups/<projectId>/whitelist
```

### 4. Use VPC peering for private connectivity

For production, use VPC peering instead of IP whitelisting.

## Examples

```bash
# Get current IP
curl https://api.ipify.org

# Add current IP to Atlas whitelist
curl --user "publicKey:privateKey" \
  --data "{\"ipAddress\":\"$(curl -s https://api.ipify.org)\",\"comment\":\"Current IP\"}" \
  --header "Content-Type: application/json" \
  https://cloud.mongodb.com/api/atlas/v1.0/groups/<projectId>/whitelist
```