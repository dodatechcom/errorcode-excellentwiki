---
title: "[Solution] MongoDB Feature Compatibility Version Error"
description: "Fix MongoDB feature compatibility version errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Feature Compatibility Version Error

```
MongoServerError: The featureCompatibilityVersion must be set to 4.4 or earlier
```

```
featureCompatibilityVersion is not compatible with this server version
```

## Common Causes

- The FCV was not updated after a MongoDB upgrade
- The FCV is set to a version newer than the server supports
- Mixed-version replica set members

## How to Fix

### 1. Check the current FCV

```javascript
db.adminCommand({ getParameter: 1, featureCompatibilityVersion: 1 })
```

### 2. Update the FCV after upgrade

```javascript
// After upgrading all members to 5.0
db.adminCommand({ setFeatureCompatibilityVersion: "5.0" })
```

### 3. Downgrade FCV before rolling back

```javascript
// Before downgrading, ensure all members support the target version
db.adminCommand({ setFeatureCompatibilityVersion: "4.4" })
```

### 4. Verify all members are on the same version

```javascript
db.adminCommand({ buildInfo: 1 }).version
```

## Examples

```bash
# Check current FCV
mongosh --eval "db.adminCommand({getParameter:1, featureCompatibilityVersion:1})"

# Update FCV
mongosh --eval "db.adminCommand({setFeatureCompatibilityVersion:'5.0'})"

# Check server version
mongosh --eval "db.adminCommand({buildInfo:1}).version"
```