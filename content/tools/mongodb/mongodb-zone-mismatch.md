---
title: "[Solution] MongoDB Zone Mismatch Error"
description: "Fix MongoDB zone sharding configuration errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Zone Mismatch Error

Zone sharding errors occur when zone ranges do not match the shard key:

```
MongoServerError: zone range does not match the shard key
```

## Common Causes

- The zone range boundaries do not align with the shard key type
- The shard is not assigned to the correct zone
- The zone tag does not exist
- The range is overlapping with another zone

## How to Fix

### 1. Verify zone configuration

```javascript
sh.status()
```

### 2. Add a shard to a zone

```javascript
sh.addShardTag("shard1", "US-EAST")
sh.addShardTag("shard2", "US-WEST")
```

### 3. Define zone ranges

```javascript
sh.updateZoneKeyRange("mydb.users", { region: "east" }, { region: "east;" }, "US-EAST")
```

### 4. Ensure ranges do not overlap

```javascript
// Check existing zone ranges
use config
db.tags.find()
```

## Examples

```bash
# Set up zone sharding
mongosh --eval '
  // Add tags to shards
  sh.addShardTag("shard1", "US-EAST")
  sh.addShardTag("shard2", "US-WEST")

  // Define zone ranges
  sh.updateZoneKeyRange("mydb.users", {zip:{$gte:"01000",$lt:"30000"}}, "US-EAST")
  sh.updateZoneKeyRange("mydb.users", {zip:{$gte:"90000",$lt:"99999"}}, "US-WEST")

  sh.status()
'
```