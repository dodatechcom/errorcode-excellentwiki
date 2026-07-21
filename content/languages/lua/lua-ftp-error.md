---
title: "[Solution] Lua Ftp Error"
description: "Fix Lua FTP connection errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

FTP errors occur when FTP operations fail.

## Common Causes

- Connection refused
- Authentication failed
- File not found
- Passive mode error

## How to Fix

### 1. Handle FTP connection

```lua
local ftp = require("socket.ftp")
local conn, err = ftp.open(host, user, pass)
if not conn then
  print("FTP error:", err)
end
```

### 2. Set timeout

```lua
local ftp = require("socket.ftp")
local conn = ftp.open(host, user, pass)
conn:settimeout(30)
```

## Examples

```lua
-- Safe FTP download
local function ftpDownload(host, user, pass, remotePath, localPath)
  local ftp = require("socket.ftp")
  
  local conn, err = ftp.open(host, user, pass)
  if not conn then
    return nil, err
  end
  
  conn:settimeout(60)
  
  local ok, err = conn:get(remotePath, localPath)
  conn:close()
  
  return ok, err
end
```

## Related Errors

- [Socket error](/languages/lua/lua-socket-error)
- [Connection error](/languages/lua/lua-connection-error)
- [Runtime error](/languages/lua/lua-runtime-error)
