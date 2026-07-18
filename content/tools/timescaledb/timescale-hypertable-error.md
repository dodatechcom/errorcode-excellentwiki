---
title: "[Solution] TimescaleDB Hypertable Error — How to Fix"
description: "Fix TimescaleDB hypertable errors by resolving creation failures, fixing dimension configuration, and correcting chunk time interval settings"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Hypertable Error

TimescaleDB hypertable errors occur when creating or managing hypertables, which are time-partitioned tables that automatically split data into chunks for optimal performance.

## Why It Happens

- Time column is not in the primary key
- Chunk time interval is too small or too large
- Hypertable already exists when creating without IF NOT EXISTS
- Partitioning column type is not supported
- Conflicts with existing indexes or constraints
- PostgreSQL version is incompatible with TimescaleDB

## Common Error Messages

```
ERROR: could not convert integer to dimension type
```

```
ERROR: hypertable already exists
```

```
ERROR: cannot create hypertable with the time column not in the primary key
```

```
ERROR: invalid chunk_time_interval value
```

## How to Fix It

### 1. Create Hypertable Correctly

```sql
-- Create a basic hypertable
CREATE TABLE sensor_data (
  time TIMESTAMPTZ NOT NULL,
  sensor_id INTEGER NOT NULL,
  temperature DOUBLE PRECISION,
  humidity DOUBLE PRECISION
);

SELECT create_hypertable('sensor_data', 'time');

-- With custom chunk interval (1 day)
SELECT create_hypertable('sensor_data', 'time',
  chunk_time_interval => INTERVAL '1 day');
```

### 2. Fix Primary Key Issues

```sql
-- The time column must be part of the primary key
-- WRONG: time not in primary key
CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  time TIMESTAMPTZ NOT NULL,
  data TEXT
);

-- CORRECT: include time in primary key
CREATE TABLE events (
  id SERIAL,
  time TIMESTAMPTZ NOT NULL,
  data TEXT,
  PRIMARY KEY (time, id)
);

SELECT create_hypertable('events', 'time');
```

### 3. Convert Existing Table to Hypertable

```sql
-- Check if table can be converted
SELECT * FROM timescaledb_information.hypertables;

-- Convert table to hypertable
SELECT create_hypertable('existing_table', 'created_at',
  if_not_exists => TRUE,
  migrate_data => TRUE);

-- Check migration progress
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'convert_to_hypertable';
```

### 4. Adjust Chunk Time Interval

```sql
-- Change chunk interval after creation
SELECT set_chunk_time_interval('sensor_data', INTERVAL '7 days');

-- Check current chunk interval
SELECT * FROM timescaledb_information.hypertables
WHERE hypertable_name = 'sensor_data';

-- Recommended intervals based on data rate:
-- High volume (>1M rows/min): 1 hour
-- Medium volume: 1 day
-- Low volume: 7 days
```

## Common Scenarios

- **Cannot create hypertable on existing table**: Use `migrate_data => TRUE` to convert.
- **Chunks are too small**: Increase `chunk_time_interval` to reduce chunk count.
- **Hypertable has too many chunks**: Reduce chunk interval or compress old chunks.

## Prevent It

- Design schema with time column as part of primary key from the start
- Choose chunk interval based on data ingestion rate
- Monitor chunk count with `timescaledb_information.chunks`

## Related Pages

- [TimescaleDB Chunk Error](/tools/timescaledb/timescale-chunk-error)
- [TimescaleDB Compression Error](/tools/timescaledb/timescale-compression-error)
- [TimescaleDB Partition Error](/tools/timescaledb/timescale-partition-error)
