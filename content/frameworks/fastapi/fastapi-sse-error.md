---
title: "[Solution] FastAPI SSE Error"
description: "Fix FastAPI Server-Sent Events errors when streaming event data disconnects or events are not received."
frameworks: ["fastapi"]
error-types: ["streaming-error"]
severities: ["error"]
---

Server-Sent Events (SSE) in FastAPI fail when the streaming response is not properly configured or when the client connection drops.

## Common Causes

- Response does not use `StreamingResponse` with `text/event-stream` content type
- Generator function yields malformed SSE data without proper newlines
- Client or proxy closes the connection due to timeout settings
- Nginx buffers SSE responses instead of streaming them
- Async generator not yielding events fast enough

## How to Fix

### Create Proper SSE Endpoint

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def event_generator():
    counter = 0
    while True:
        yield f"data: {counter}\n\n"
        counter += 1
        await asyncio.sleep(1)

@app.get("/stream")
async def stream_events():
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
```

### Configure Nginx for SSE

```nginx
location /stream {
    proxy_pass http://backend;
    proxy_set_header Connection '';
    proxy_http_version 1.1;
    proxy_buffering off;
    proxy_cache off;
    chunked_transfer_encoding off;
    timeout 86400s;
}
```

## Examples

Each event line must end with `\n\n` (double newline). Missing the double newline causes the client to buffer events indefinitely.
