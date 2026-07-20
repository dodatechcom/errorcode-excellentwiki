---
title: "[Solution] MongoDB Text Index Error"
description: "Fix MongoDB full text index creation and query errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Text Index Error

Text index operations can fail with several errors:

```
MongoServerError: bad query: Bad Value ... text index
```

```
MongoServerError: Only non-compound, non-array, non-geo fields can have a TTL index
```

## Common Causes

- Only one text index is allowed per collection
- The text index field is too large
- Text search is combined with an unsupported aggregation stage
- The search language is not supported
- Duplicate text index names
- The query uses a text index with an incompatible sort

## How to Fix

### 1. Only create one text index per collection

```javascript
// If you need to search multiple fields, combine them into one text index
db.articles.createIndex({ title: "text", content: "text", tags: "text" });

// Drop an existing text index before creating a new one
db.articles.dropIndex("title_text");
```

### 2. Use weights to prioritize fields

```javascript
db.articles.createIndex(
  { title: "text", content: "text" },
  { weights: { title: 10, content: 5 } }
);
```

### 3. Use language-specific text indexes

```javascript
db.articles.createIndex(
  { title: "text", content: "text" },
  { default_language: "english", language_override: "lang" }
);
```

### 4. Combine text search with aggregation correctly

```javascript
db.articles.aggregate([
  { $match: { $text: { $search: "mongodb" } } },
  { $project: { title: 1, score: { $meta: "textScore" } } },
  { $sort: { score: { $meta: "textScore" } } }
]);
```

## Examples

```bash
# Create a comprehensive text index
mongosh --eval '
  db.articles.drop();
  db.articles.createIndex({title:"text", content:"text", tags:"text"}, {weights:{title:10,content:5,tags:1}});
  db.articles.insertMany([
    {title:"MongoDB Guide", content:"Learn MongoDB basics", tags:["database","nosql"]},
    {title:"Advanced Queries", content:"Complex MongoDB queries", tags:["database","queries"]}
  ]);
  printjson(db.articles.find({$text:{$search:"MongoDB queries"}}).toArray());
'
```