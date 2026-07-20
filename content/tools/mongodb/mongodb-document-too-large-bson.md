---
title: "[Solution] MongoDB Document Too Large BSON Error"
description: "Fix document too large error exceeding BSON size limit"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Document Too Large (BSON) Error

When a document exceeds the maximum BSON document size (16 MB):

```
MongoServerError: Object too large (2147483648 bytes), max size: 16777216
```

```
BSONError: BSONObj size: 2147483648 is invalid. Size must be between 0 and 1679360057
```

## Common Causes

- Storing large binary data (images, files) directly in the document
- Accumulation of array elements pushing the document over 16 MB
- An update operator (`$set`) accidentally sets a value to a very large object
- GridFS was not used for file storage
- Logging or debug fields containing excessive data

## How to Fix

### 1. Use GridFS for large files

```javascript
const { GridFSBucket } = require('mongodb');
const bucket = new GridFSBucket(db);

// Upload
const uploadStream = bucket.openUploadStream('largefile.bin');
fs.createReadStream('largefile.bin').pipe(uploadStream);

// Download
const downloadStream = bucket.openDownloadStreamByName('largefile.bin');
downloadStream.pipe(fs.createWriteStream('output.bin'));
```

### 2. Break large arrays into subdocuments or separate collections

```javascript
// Instead of storing all comments in one document
// collection: posts (has post metadata)
// collection: comments (references post _id)
```

### 3. Validate document size before insert

```javascript
function checkDocSize(doc) {
  const size = BSON.serialize(doc).byteLength;
  if (size > 16 * 1024 * 1024) {
    throw new Error(`Document too large: ${size} bytes (max: 16MB)`);
  }
  return true;
}
```

### 4. Use compression to reduce size

```javascript
await db.collection('logs').insertOne({
  data: compressData(largeObject)  // Use zlib or similar
});
```

## Examples

```bash
# Check the size of a document
mongosh --eval '
  let doc = db.mycol.findOne();
  printjson(BSON.serialize(doc).byteLength);
'

# Check current collection storage stats
mongosh --eval "db.mycol.stats()"

# Convert a document to GridFS using mongofiles
mongofiles --db=mydb put largefile.bin

# Check maximum BSON object size
mongosh --eval "db.runCommand({getParameter:1, maxBsonObjectSize:1})"
```