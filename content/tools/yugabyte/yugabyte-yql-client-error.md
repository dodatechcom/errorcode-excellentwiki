---
title: "YugabyteDB YQL Client Error"
description: "YQL client connection error"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
YQL client cannot connect to YugabyteDB.

## Common Causes
- YQL port not reachable
- Authentication failure
- Network firewall blocking

## How to Fix
```bash
# Check YQL port
nc -zv localhost 9042

# Test connection
ycqlsh localhost 9042
```

## Examples
```bash
# Check YQL listener
netstat -tlnp | grep 9042
# Test YQL connection
ycqlsh -e "DESCRIBE CLUSTER;"
```

