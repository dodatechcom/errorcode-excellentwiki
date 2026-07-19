---
title: "[Solution] ERR_HTTP2_PUSH_DISABLED — Server Push Not Supported Fix"
description: "Fix ERR_HTTP2_PUSH_DISABLED when trying to use HTTP/2 Server Push on a connection where it's disabled."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_HTTP2_PUSH Disabled

Server Push was disabled by the client or server configuration.

## Fix

Don't rely on server push — preload resources via Link headers instead:

```http
Link: </style.css>; rel=preload; as=style
Link: </script.js>; rel=preload; as=script
```
