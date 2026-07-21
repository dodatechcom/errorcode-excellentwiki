---
title: "[Solution] Deprecated Function Migration: asyncio.get_event_loop() to asyncio.run()"
description: "Migrate from deprecated asyncio.get_event_loop() to asyncio.run()."
deprecated_function: "loop = asyncio.get_event_loop(); loop.run_until_complete(coro)"
replacement_function: "asyncio.run(coro)"
languages: ["python"]
deprecated_since: "Python 3.7+"
---

# [Solution] Deprecated Function Migration: asyncio.get_event_loop() to asyncio.run()

The `loop = asyncio.get_event_loop(); loop.run_until_complete(coro)` has been deprecated in favor of `asyncio.run(coro)`.

## Migration Guide

asyncio.run() manages the event loop.

## Before (Deprecated)

```python
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

## After (Modern)

```python
asyncio.run(main())
```

## Key Differences

- asyncio.run() manages the event loop
