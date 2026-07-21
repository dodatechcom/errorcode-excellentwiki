---
title: "[Solution] MongoDB Validate Command Failed Error"
description: "Fix MongoDB validate command failed error when collection validation detects corruption or structural issues"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Validate Command Failed Error

The validate command detects data corruption, invalid BSON, or structural problems within a collection. Validation failure indicates the collection needs repair or recovery.

## Common Causes

- Disk corruption from hardware failure or unclean shutdown
- WiredTiger metadata inconsistency
- Power loss during a write operation caused partial document corruption
- Bad data was written due to a driver bug
- WiredTiger checkpoint was incomplete or corrupted

## How to Fix

### Run Validation with Full Detail

```javascript
const result = await db.runCommand({
  validate: 'orders',
  full: true,      // check all documents
  metadataCheck: true  // validate metadata
});

console.log('Valid:', result.valid);
console.log('Errors:', result.errors);
console.log('Warnings:', result.warnings);
```

### Repair Corrupted Collection

```javascript
// Attempt repair by re-inserting data
const tempName = 'orders_repair_' + Date.now();
db.createCollection(tempName);

// Copy valid documents
await db.orders.aggregate([
  { $match: {} },
  { $out: tempName }
]).toArray();

// Drop corrupted and rename
db.orders.drop();
db[tempName].renameCollection('orders');
```

### Check WiredTiger Integrity

```javascript
// Check for WiredTiger-level corruption
db.serverStatus().wiredTiger

// Look for these indicators:
// - "btree: corrupted" entries
// - "block manager: free space" inconsistencies
// - checkpoint failure counts
```

### Restore from Backup

```bash
# If validation finds unrecoverable corruption
# 1. Stop mongod
# 2. Restore from the latest backup
mongorestore --archive=/backup/latest.archive --nsInclude='mydb.orders'

# 3. Replay oplog from backup time to current time
mongorestore --archive=/backup/oplog.archive --oplogReplay
```

### Run offline Repair (Last Resort)

```bash
mongod --repair --dbpath /data/db --repairpath /data/db_repair
# Then swap directories and restart
```

## Examples

```
MongoServerError: Failed to validate collection "orders":
  BSON type 0x03 is not a valid BSON type at offset 128

MongoServerError: Collection validation found 3 corrupted documents
  in "orders". Total documents checked: 1500000. Valid: 1499997.
```

## Related Errors

- [MongoDB Write Error]({{< relref "/tools/mongodb/mongodb-write-error" >}}) -- write failures
- [MongoDB Invalid BSON]({{< relref "/tools/mongodb/mongodb-invalid-bson" >}}) -- BSON issues
- [MongoDB No Free Disk Space]({{< relref "/tools/mongodb/mongodb-no-free-disk-space" >}}) -- disk issues
