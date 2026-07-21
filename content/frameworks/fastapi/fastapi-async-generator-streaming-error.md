---
title: "[Solution] FastAPI Async Generator Streaming Error"
description: "Fix FastAPI async generator streaming errors when async generators fail to yield data in StreamingResponse."
frameworks: ["fastapi"]
error-types: ["streaming-error"]
severities: ["error"]
---

When using an async generator with `StreamingResponse` in FastAPI, errors occur if the generator raises an exception or the client disconnects mid-stream.

## Common Causes

- Async generator raises an exception during iteration
- Client disconnects while the generator is still producing data
- Generator yields non-string or non-bytes data
- Event loop is blocked by a synchronous operation in the generator
- Generator has an infinite loop without a break condition

## How to Fix

### Wrap Generator Logic in Try/Except

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def data_generator():
    try:
        for i in range(100):
            yield f"data: {i}\n\n"
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Client disconnected")
    except Exception as e:
        print(f"Generator error: {e}")

@app.get("/stream")
async def stream():
    return StreamingResponse(data_generator(), media_type="text/event-stream")
```

### Yield Bytes or Strings

```python
async def bytes_generator():
    with open("large_file.bin", "rb") as f:
        while chunk := f.read(8192):
            yield chunk
```

## Examples

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def broken_stream():
    while True:
        yield 123  # Bug -- yields int instead of str
        await asyncio.sleep(1)

async def working_stream():
    while True:
        yield f"data: {time.time()}\n\n"
        await asyncio.sleep(1)
```
