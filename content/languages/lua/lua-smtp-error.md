---
title: "[Solution] Lua Smtp Error"
description: "Fix Lua SMTP email sending errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

SMTP errors occur when sending emails fails.

## Common Causes

- Connection refused
- Authentication failed
- Invalid recipient
- Message format error

## How to Fix

### 1. Handle SMTP connection

```lua
local smtp = require("socket.smtp")
local msg = smtp.message{
  from = "sender@example.com",
  to = "recipient@example.com",
  subject = "Test",
  body = "Hello"
}
```

### 2. Set timeout

```lua
local smtp = require("socket.smtp")
local msg = smtp.message{
  ...
  server = "smtp.example.com",
  port = 587,
  timeout = 30
}
```

## Examples

```lua
-- Send email safely
local function sendEmail(from, to, subject, body)
  local smtp = require("socket.smtp")
  
  local msg, err = smtp.message{
    from = from,
    to = to,
    subject = subject,
    body = body
  }
  
  if not msg then
    return nil, err
  end
  
  local ok, err = smtp.send(msg)
  return ok, err
end
```

## Related Errors

- [Socket error](/languages/lua/lua-socket-error)
- [Connection error](/languages/lua/lua-connection-error)
- [Runtime error](/languages/lua/lua-runtime-error)
