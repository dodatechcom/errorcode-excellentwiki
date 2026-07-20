---
title: "[Solution] MongoDB Regex Parse Error"
description: "Fix MongoDB regular expression parse errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Regex Parse Error

```
MongoServerError: syntax error in regular expression
```

```
MongoServerError: invalid regex
```

## Common Causes

- The regex pattern contains invalid syntax
- Special characters are not properly escaped
- The regex options are invalid
- The regex is too complex

## How to Fix

### 1. Validate the regex pattern

```javascript
// Correct regex
db.users.find({ name: { $regex: "^John" } })

// Wrong: unescaped special characters
db.users.find({ name: { $regex: "[invalid" } })  // Missing closing bracket
```

### 2. Use $options for case-insensitive matching

```javascript
db.users.find({ name: { $regex: "^john", $options: "i" } })
```

### 3. Escape special characters

```javascript
// Escape dots, asterisks, and other regex special characters
const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
db.users.find({ name: { $regex: escaped } });
```

### 4. Use text search instead of regex when possible

```javascript
// Instead of regex
db.users.find({ name: { $regex: /keyword/i } })

// Use text search
db.users.createIndex({ name: "text" })
db.users.find({ $text: { $search: "keyword" } })
```

## Examples

```bash
# Test regex syntax
mongosh --eval '
  try {
    db.test.find({field: {$regex: "[invalid"}});
  } catch(e) { print("Error:", e.message); }
'

# Test valid regex
mongosh --eval '
  db.test.find({field: {$regex: "^test", $options: "i"}}).toArray();
'
```