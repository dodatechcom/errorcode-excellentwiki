---
title: "[Solution] MongoDB replSetReconfig Not Safe"
description: "Fix MongoDB replica set reconfiguration safety issues"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB replSetReconfig Not Safe Error

```
MongoServerError: Reconfig would remove a voting member that has data
```

```
MongoServerError: only one voting member at a time may be removed
```

## Common Causes

- Attempting to remove a member with votes and data simultaneously
- Removing too many voting members at once
- The new configuration would leave less than 3 voting members
- Changing the `_id` of an existing member

## How to Fix

### 1. Use { force: true } cautiously

```javascript
// Safe reconfiguration (requires majority)
rs.reconfig(newConfig);

// Force reconfiguration (only from one member, bypasses checks)
rs.reconfig(newConfig, { force: true });
```

### 2. Remove members one at a time

```javascript
rs.remove("mongo4:27017");
// Wait for stability, then remove another if needed
rs.remove("mongo5:27017");
```

### 3. Verify the new config is valid before applying

```javascript
const config = rs.conf();
config.members = config.members.filter(m => m.host !== "mongo4:27017");
rs.reconfig(config);
```

## Examples

```bash
# View current configuration
mongosh --eval "printjson(rs.conf())"

# Safely add a member
mongosh --eval '
  let config = rs.conf();
  config.members.push({_id:3, host:"mongo4:27017", priority:0.5});
  rs.reconfig(config);
'
```