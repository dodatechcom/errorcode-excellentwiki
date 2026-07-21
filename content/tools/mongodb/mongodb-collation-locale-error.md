---
title: "[Solution] MongoDB Collation Locale Not Found Error"
description: "Fix MongoDB collation locale not found error when text comparison rules reference an unsupported locale"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Collation Locale Not Found Error

The specified collation locale is not available in the MongoDB installation. Collation-dependent operations fail because the ICU library does not support the requested locale.

## Common Causes

- Locale string is misspelled or uses incorrect format
- MongoDB was built without ICU support
- Locale is not installed on the operating system
- Using a locale version that was removed in a MongoDB upgrade
- Case-insensitive collation with unsupported locale

## How to Fix

### Check Available Locales

```javascript
db.adminCommand({ connectionStatus: 1 })

// Test a locale
db.test.createCollection('test')
db.test.insertOne({ text: 'test' })
db.test.find({ text: 'test' }).collation({ locale: 'en' })
```

### Use Standard Locale Codes

```javascript
// Common valid locales
db.collection('products').createIndex(
  { name: 1 },
  { collation: { locale: 'en', strength: 2 } }  // case-insensitive
)

// Other valid locales
{ locale: 'fr' }     // French
{ locale: 'de' }     // German
{ locale: 'ja' }     // Japanese
{ locale: 'zh' }     // Chinese
{ locale: 'es' }     // Spanish
```

### Use Simple Comparison as Fallback

```javascript
// Instead of locale-specific comparison
db.collection('users').find({
  name: { $regex: /^john$/i }  // case-insensitive regex
})

// Or normalize data before storage
await db.collection('users').updateMany({}, [
  { $set: { nameLower: { $toLower: '$name' } } }
])
db.collection('users').createIndex({ nameLower: 1 })
```

### Verify ICU Installation

```bash
# Check if MongoDB has ICU support
mongod --version
# Look for "with ICU" in the build info

# On Ubuntu, install ICU if missing
sudo apt-get install libicu-dev
```

## Examples

```
MongoServerError: locale not supported: "en_US.UTF-8"
  Valid format: "en" or "en-US"

MongoServerError: collation not supported:
  "simple" is not a valid locale string
```

## Related Errors

- [MongoDB Collation Error]({{< relref "/tools/mongodb/mongodb-collation-error" >}}) -- collation issues
- [MongoDB Text Index Error]({{< relref "/tools/mongodb/mongodb-text-index-error" >}}) -- text search issues
- [MongoDB Index Error]({{< relref "/tools/mongodb/mongodb-index-error" >}}) -- index issues
