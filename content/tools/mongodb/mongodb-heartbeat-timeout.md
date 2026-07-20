---
title: "[Solution] MongoDB Heartbeat Timeout Error"
description: "Fix MongoDB replica set heartbeat timeout issues"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Heartbeat Timeout Error

```
heartbeat to mongo2:27017 timed out
```

```
MongoServerError: Heartbeat to mongo3:27017 failed
```

## Common Causes

- Network latency between members is too high
- The member is overloaded and cannot respond to heartbeats
- Firewall or network device is dropping heartbeat packets
- The member is performing a long-running operation
- DNS resolution is slow

## How to Fix

### 1. Increase heartbeat intervals

```javascript
rs.reconfig({
  _id: "rs0",
  settings: {
    heartbeatPeriodMillis: 5000,
    electionTimeoutMillis: 30000
  }
});
```

### 2. Optimize network between members

```bash
ping -c 10 mongo2
ping -c 10 mongo3
mtr mongo2
```

### 3. Reduce load on heartbeat targets

```bash
ssh mongo2 "iostat -x 1 5"
ssh mongo2 "top -bn1 | head -20"
```

### 4. Verify firewall rules

```bash
sudo iptables -L -n
```

## Examples

```bash
# Check heartbeat status
mongosh --eval '
  rs.status().members.forEach(m => {
    let lastHB = m.lastHeartbeat ? new Date() - m.lastHeartbeat : "N/A";
    print(m.name, "lastHeartbeat:", lastHB, "ms ago");
  });
'
```