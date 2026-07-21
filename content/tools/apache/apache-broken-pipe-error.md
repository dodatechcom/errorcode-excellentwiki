---
title: "[Solution] Apache Broken Pipe Error"
description: "Fix Apache broken pipe errors when client disconnects during response transmission."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Apache Broken Pipe Error

Apache encounters a broken pipe when the client disconnects before the response is fully sent.

```
AH01084: failed to read from client connection
AH01110: request failed: error reading from remote stream
```

## Common Causes

- Client timeout exceeded
- Large file downloads interrupted
- Browser navigated away before response completed
- Network connection lost during transfer
- KeepAlive timeout too short

## How to Fix

### Increase Timeouts

```apache
# Increase keepalive and IO timeouts
Timeout 300
KeepAliveTimeout 5

# For proxy scenarios
ProxyTimeout 300
```

### Handle Broken Pipes Gracefully

```apache
# Reduce logging for broken pipes
LogLevel warn

# Use ErrorLogFormat for better diagnostics
ErrorLogFormat "[%{u}t] [%{a} %A:%p] %M"
```

### Adjust Buffer Settings

```apache
# Increase output buffer
BufferSize 65536

# For mod_deflate
DeflateBufferSize 65536
```

### Disable Logging for Expected Disconnects

```apache
# Filter out common broken pipe messages
SetEnvIf Request_Method "HEAD" nolog
CustomLog /var/log/apache2/access.log combined env=!nolog
```

## Examples

```apache
# Configure timeouts per directory
<Directory "/var/www/downloads">
    Timeout 600
    KeepAliveTimeout 10
</Directory>
```
