---
title: "[Solution] ScyllaDB Tracing Error — How to Fix"
description: "Fix ScyllaDB tracing errors by enabling query tracing, resolving tracing session failures, and analyzing trace output for slow queries"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Tracing Error

ScyllaDB tracing errors occur when query tracing fails to capture or return trace data. Tracing is essential for debugging slow queries and understanding query execution.

## Why It Happens

- Tracing is not enabled on the session or query
- Trace session buffer is full
- Tracing output exceeds the response size limit
- Trace data has been purged due to TTL expiration
- Too many concurrent traces overwhelm the system
- Tracing level is set too low for useful output

## Common Error Messages

```
TraceError: Tracing session not found
```

```
InvalidRequest: Tracing is not enabled
```

```
TraceError: Trace buffer full
```

```
TraceNotFound: Trace data has expired
```

## How to Fix It

### 1. Enable Query Tracing

```cql
-- Enable tracing for a session
TRACING ON;

-- Execute query
SELECT * FROM users WHERE id = '1';

-- Trace output shows:
-- Activity | Timestamp | Source | Source elapsed | Client
-- ...
```

```python
# Enable tracing in Python driver
from cassandra.query import SimpleStatement

statement = SimpleStatement("SELECT * FROM users WHERE id = '1'")
result = session.execute(statement)

# Access trace events
for event in result.get_query_trace().events:
    print(f"{event.source} - {event.description}")
```

### 2. Use Tracing to Debug Slow Queries

```cql
-- Enable tracing
TRACING ON;

-- Run the slow query
SELECT * FROM events WHERE event_type = 'login' AND event_date > '2024-01-01';

-- Check trace output for:
-- 1. Coordinator processing time
-- 2. Per-replica response time
-- 3. Message sending/receiving time
-- 4. Read repair time

TRACING OFF;
```

### 3. Query Trace Data Directly

```cql
-- Trace sessions are stored in system_traces
SELECT * FROM system_traces.sessions
WHERE client = '127.0.0.1'
AND started_at > '2024-01-01'
LIMIT 10;

-- Get detailed events for a session
SELECT * FROM system_traces.events
WHERE session_id = <uuid>
ORDER BY source, activity;
```

### 4. Configure Tracing Level

```cql
-- Set tracing level (NONE, QUERY, FULL)
TRACING ON;

-- For driver-level tracing
from cassandra.query import SimpleStatement
statement = SimpleStatement(
    "SELECT * FROM users",
    trace_level=TraceLevel.REQUEST
)
```

```bash
# Check tracing configuration
nodetool describecluster | grep -i trace

# Purge old trace data
TRUNCATE system_traces.sessions;
TRUNCATE system_traces.events;
```

## Common Scenarios

- **Tracing output is empty**: Ensure tracing is enabled before running the query.
- **Trace session not found**: Tracing data may have expired; increase TTL or check immediately.
- **Tracing slows performance**: Use tracing only for debugging; disable in production.

## Prevent It

- Enable tracing only when debugging specific queries
- Store important trace data before it expires
- Use application-level tracing for production monitoring

## Related Pages

- [ScyllaDB Query Error](/tools/scylladb/scylladb-query-error)
- [ScyllaDB Monitoring Error](/tools/scylladb/scylladb-monitoring-error)
- [ScyllaDB Timeout Error](/tools/scylladb/scylladb-timeout-error)
