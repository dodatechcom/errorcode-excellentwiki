---
title: "[Solution] Apache mod_unique_id Error"
description: "Fix Apache mod_unique_id errors when unique request IDs cannot be generated."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache mod_unique_id Error

Apache mod_unique_id fails to generate unique request identifiers.

```
AH00598: mod_unique_id: unable to generate unique id
```

## Common Causes

- Server environment variables not sufficient for ID generation
- Running in a container with limited environment
- Multi-process concurrency race condition
- Missing HostnameLookups configuration
- Insufficient entropy on the system

## How to Fix

### Enable HostnameLookups

```apache
HostnameLookups On
```

### Check Unique ID Configuration

```apache
# Ensure SERVER_NAME is set
ServerName example.com

# Use UniqueIDFormat if available
UniqueIDFormat "%{reqenv:REMOTE_ADDR}_%{reqenv:REMOTE_PORT}_%t"
```

### Fix Container Issues

```bash
# Ensure hostname is set in container
docker run -h webserver.example.com myapp

# Or set in Dockerfile
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
```

### Alternative ID Generation

```apache
# Use mod_headers to set custom ID
<IfModule mod_headers.c>
    RequestHeader set X-Request-ID "%{UNIQUE_ID}e"
</IfModule>
```

### Verify Entropy

```bash
# Check system entropy
cat /proc/sys/kernel/random/entropy_avail
# Should be above 200
```

## Examples

```apache
# Custom unique ID format
<IfModule mod_unique_id.c>
    UniqueIDFormat "%{reqenv:HOSTNAME}_%{reqenv:REMOTE_ADDR}_%{time:sec}"
</IfModule>
```

```bash
# Install haveged for more entropy
apt install haveged
systemctl enable haveged
```
