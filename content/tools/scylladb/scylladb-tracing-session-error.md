---
title: "[Solution] ScyllaDB Tracing Error — How to Fix"
description: "Fix ScyllaDB tracing errors when query tracing fails to capture or store trace data correctly"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Tracing Error

Tracing errors occur when ScyllaDB fails to enable, capture, or retrieve query trace data, making it impossible to diagnose slow queries.

## Why It Happens

- Tracing session expired before results were retrieved
- Too many concurrent tracing sessions exhaust memory
- Trace tables are too large and slow to query
- Tracing is disabled at the cluster level
- Coordinator node failed to collect trace events

## Common Error Messages

```
error: tracing session not found, expired
```

```
Tracing: unable to enable tracing, session limit reached
```

```
warning: trace data may be incomplete for this query
```

## How to Fix It

### 1. Enable Tracing for a Query

```cql
TRACING ON;
SELECT * FROM users WHERE id = 1;
-- View trace after query completes
TRACING OFF;
```

### 2. Retrieve Recent Traces

```cql
SELECT * FROM system_traces.sessions ORDER BY start DESC LIMIT 10;
SELECT * FROM system_traces.events WHERE session_id = <uuid>;
```

### 3. Increase Tracing Buffer Size

```yaml
# In scylla.yaml
tracing_page_size: 10000
```

### 4. Use Client-Side Tracing

```python
# Python driver tracing
from cassandra.query import SimpleStatement

statement = SimpleStatement("SELECT * FROM users WHERE id = 1")
rows = session.execute(statement)
print(session.default_fetch_size)
# Check trace via session.trace
```

## Examples

```
cqlsh> TRACING ON;
cqlsh> SELECT * FROM users WHERE id = 1;

Tracing session: abc-123
- coordinator: 10.0.0.1
- duration: 2.5ms
- events: 15
```

## Prevent It

- Use tracing for specific debugging, not always-on
- Clear old trace data periodically
- Increase tracing buffer for complex queries

## Related Pages

- [ScyllaDB Tracing Error](/tools/scylladb/scylladb-tracing-error)
- [ScyllaDB Query Error](/tools/scylladb/scylladb-query-error)
- [ScyllaDB Query Timeout Error](/tools/scylladb/scylladb-query-timeout-error)
