---
title: "[Solution] Heroku R14 Memory Quota Exceeded Error — Fix Memory Issues"
description: "Fix Heroku R14 memory quota exceeded errors. Resolve memory leaks, dyno memory limits, and R14 error codes."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A Heroku R14 memory quota exceeded error occurs when your dyno uses more memory than its plan allows. Heroku monitors memory usage and terminates dynos that exceed their quota.

## What This Error Means

```
R14 - Memory quota exceeded
Process running user=app pid=1234 rss=512000 vsz=1048576
```

The dyno's memory usage (RSS) exceeded the plan's quota:

- **Free/Eco**: 512MB
- **Basic**: 512MB
- **Standard-1X**: 512MB
- **Standard-2X**: 1GB
- **Performance-M**: 2.5GB
- **Performance-L**: 14GB

## Why It Happens

- Memory leak in application code
- Large objects loaded into memory
- Unbounded database queries returning too many rows
- Child processes consuming additional memory
- Caching too much data in-memory
- Multiple processes exceeding combined quota

## How to Fix It

### Monitor Memory Usage

```bash
# Check current memory usage
heroku ps

# View memory stats
heroku metrics:memory

# Check for R14 errors
heroku logs --tail | grep "R14"
```

### Fix Memory Leaks

```javascript
// Common leak: storing data in module scope
// WRONG
const cache = {};
app.get('/data', (req, res) => {
  cache[req.query.key] = fetchData(); // Grows forever
});

// RIGHT: Use LRU cache with limits
const LRU = require('lru-cache');
const cache = new LRU({ max: 500, maxAge: 1000 * 60 * 5 });
```

### Use Streaming

```javascript
// Instead of loading entire file into memory
const fs = require('fs');

// WRONG: Loads entire file
const data = fs.readFileSync('large-file.csv', 'utf8');

// RIGHT: Stream the file
const stream = fs.createReadStream('large-file.csv');
stream.pipe(res);
```

### Optimize Database Queries

```sql
-- Add limits to queries
SELECT * FROM orders WHERE created_at > '2024-01-01' LIMIT 100;

-- Use pagination
SELECT * FROM orders ORDER BY id LIMIT 50 OFFSET 0;
```

### Upgrade Dyno Type

```bash
# Check available dyno types
heroku ps:type

# Upgrade to handle more memory
heroku ps:type standard-2x

# Check after upgrade
heroku ps
```

### Add Swap Space

```bash
# Heroku adds swap automatically but with limits
# Check swap usage
heroku logs | grep "swap"

# Better to fix the root cause than rely on swap
```

### Profile Memory

```bash
# For Node.js
heroku config:set NODE_OPTIONS="--max-old-space-size=400"

# Use memory profiling tools
heroku config:set NODE_ENV=development
```

## Common Mistakes

- Ignoring R14 errors hoping they go away
- Not monitoring memory usage regularly
- Using global variables to cache data indefinitely
- Not setting NODE_OPTIONS to limit heap size
- Upgrading dyno size without fixing the underlying leak

## Related Pages

- [Heroku Dyno Error]({{< relref "/tools/heroku/heroku-dyno-error" >}}) — R14 Memory quota exceeded
- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) — Config var not set
