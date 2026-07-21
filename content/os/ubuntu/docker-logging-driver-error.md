---
title: "Docker Logging Driver Error"
description: "Docker container logging fails or logs not captured"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Logging Driver Error

Docker container logging fails or logs not captured

## Common Causes

- Logging driver not available (json-file, syslog, journald)
- Log file permissions prevent writing
- Max-size or max-file limits reached
- Remote logging server unreachable

## How to Fix

1. Check logging driver: `docker inspect <container> | grep LogConfig`
2. View logs: `docker logs <container>`
3. Configure logging: `--log-driver=syslog --log-opt syslog-address=udp://...`
4. Check disk: `docker system df`

## Examples

```bash
# Check container logging config
docker inspect mycontainer | grep -A5 LogConfig

# View container logs
docker logs --tail 100 mycontainer

# Set logging options
docker run --log-driver=json-file --log-opt max-size=10m --log-opt max-file=3 myimage
```
