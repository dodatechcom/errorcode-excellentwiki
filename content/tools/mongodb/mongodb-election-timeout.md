---
title: "[Solution] MongoDB Election Timeout Error"
description: "Fix MongoDB replica set election timeout issues"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Election Timeout Error

```
MongoServerError: ELECTION FAILED
```

```
rsMember is in state PRIMARY but heartbeat says DOWN
```

## Common Causes

- Network latency between replica set members exceeds the election timeout
- The `electionTimeoutMillis` is too low
- Members cannot reach each other due to firewall rules
- Clock skew between members
- Too many members are down

## How to Fix

### 1. Increase the election timeout

```javascript
rs.reconfig({
  _id: "rs0",
  settings: {
    electionTimeoutMillis: 30000  // Default is 10000 (10 seconds)
  }
});
```

### 2. Ensure network connectivity between all members

```bash
ping mongo2
ping mongo3
sudo iptables -L -n | grep 27017
```

### 3. Synchronize clocks

```bash
sudo ntpdate pool.ntp.org
# Or use chrony
sudo chronyc makestep
```

## Examples

```bash
# Check election-related settings
mongosh --eval '
  let config = rs.conf();
  print("Election timeout:", config.settings.electionTimeoutMillis, "ms");
  print("Members:", config.members.length);
'

# Update election timeout
mongosh --eval '
  rs.reconfig({
    _id: "rs0",
    settings: { electionTimeoutMillis: 30000 },
    members: rs.conf().members
  });
'
```