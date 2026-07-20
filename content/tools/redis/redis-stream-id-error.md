---
title: "[Solution] Redis Stream ID Error"
description: "How to fix Redis stream ID errors when working with streams"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Invalid stream ID format (must be `<millisecondsTime>-<sequenceNumber>`)
- ID already exists (duplicate)
- Trying to read from non-existent stream
- XPENDING with wrong stream ID

## Fix

Generate valid ID:

```bash
# Let Redis auto-generate ID
redis-cli XADD mystream * field value

# Use specific valid ID
redis-cli XADD mystream 1234567890-0 field value
```

Read stream:

```bash
redis-cli XREAD COUNT 10 STREAMS mystream 0
```

Check stream info:

```bash
redis-cli XINFO STREAM mystream
```

## Examples

```bash
# Add to stream with auto ID
redis-cli XADD mystream * name "event1" data "payload"

# Read from specific ID
redis-cli XREAD COUNT 5 STREAMS mystream 1234567890-0

# Check stream length
redis-cli XLEN mystream
```
