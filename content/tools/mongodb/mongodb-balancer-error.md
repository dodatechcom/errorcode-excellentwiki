---
title: "[Solution] MongoDB Balancer Error"
description: "Fix MongoDB balancer errors in sharded cluster"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Balancer Error

```
Balancer failed to run
```

```
MongoServerError: balancer did not start
```

## Common Causes

- The balancer is not enabled
- The config servers are not accessible
- Chunk migration failed and the balancer stopped
- The balancer lock is stale

## How to Fix

### 1. Check balancer status

```javascript
sh.getBalancerState()
sh.isBalancerRunning()
```

### 2. Enable the balancer

```javascript
sh.startBalancer()
```

### 3. Check the balancer lock

```javascript
use config
db.locks.find({ _id: "balancer" })
```

### 4. Disable and re-enable the balancer

```javascript
sh.stopBalancer()
// Wait a few seconds
sh.startBalancer()
```

## Examples

```bash
# Check balancer status
mongosh --eval '
  print("Balancer state:", sh.getBalancerState());
  print("Running:", sh.isBalancerRunning());
'

# Start the balancer
mongosh --eval 'sh.startBalancer()'

# Check chunk distribution
mongosh --eval 'sh.status({showBalancer: true})'
```