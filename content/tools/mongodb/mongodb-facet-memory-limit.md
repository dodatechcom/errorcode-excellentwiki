---
title: "[Solution] MongoDB $facet Memory Limit Error"
description: "Fix MongoDB $facet aggregation pipeline memory limit errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB $facet Memory Limit Error

The `$facet` stage has a memory limit of 100 MB per sub-pipeline:

```
$facet stage exceeded memory limit of 100 MB
```

## Common Causes

- One or more sub-pipelines produce more than 100 MB of data
- The sub-pipeline uses $group or $sortByCount on a large dataset
- No $limit is applied in sub-pipelines
- The input to $facet is too large

## How to Fix

### 1. Add $limit to each sub-pipeline

```javascript
db.products.aggregate([
  {
    $facet: {
      "topByPrice": [
        { $sort: { price: -1 } },
        { $limit: 10 },
        { $project: { name: 1, price: 1 } }
      ],
      "topByRating": [
        { $sort: { rating: -1 } },
        { $limit: 10 },
        { $project: { name: 1, rating: 1 } }
      ],
      "totalCount": [
        { $count: "count" }
      ]
    }
  }
]);
```

### 2. Reduce input before $facet

```javascript
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $facet: {
    "topPriced": [{ $sort: { price: -1 } }, { $limit: 10 }],
    "avgPrice": [{ $group: { _id: null, avg: { $avg: "$price" } } }]
  }}
]);
```

### 3. Use allowDiskUse

```javascript
db.products.aggregate([
  { $facet: { ... } }
], { allowDiskUse: true });
```

## Examples

```bash
# Demonstrate $facet with limits
mongosh --eval '
  db.products.drop();
  let products = [];
  for (let i = 0; i < 50000; i++) {
    products.push({name:"P"+i, category:["A","B","C"][i%3], price:Math.random()*100, rating:Math.random()*5});
  }
  db.products.insertMany(products);

  let result = db.products.aggregate([
    {$facet:{
      byCategory:[{$group:{_id:"$category",count:{$sum:1}}}],
      priceStats:[{$group:{_id:null,avg:{$avg:"$price"},max:{$max:"$price"}}}],
      topRated:[{$sort:{rating:-1}},{$limit:5},{$project:{name:1,rating:1}}]
    }}
  ]).toArray();
  printjson(result[0]);
'
```