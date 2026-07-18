---
title: "Fix Vitess Move Tables Error — How to Fix"
description: "Resolve Vitess move tables errors by checking workflow and tablet state"
tools: ["vitess"]
error-types: ["vitess-move-tables-error"]
severities: ["warning"]
weight: 15
comments:
  - "Check workflow status"
  - "Verify tablet types"
---

# Vitess Move Tables Error — How to Fix

## Why It Happens

Move tables errors occur when Vitess cannot migrate tables between keyspaces due to workflow issues, tablet availability problems, or schema mismatches.

## Common Error Messages

- `move tables error: source keyspace not found`
- `move tables error: target keyspace not found`
- `move tables error: table already exists in target`
- `move tables error: workflow failed`

## How to Fix It

### 1. Check move tables workflow

Verify the workflow status:

```bash
# List workflows
vtctldclient list_workflows --server localhost:15999

# Get workflow details
vtctldclient get_workflow --server localhost:15999 <workflow_name>
```

### 2. Verify source and target

Check both keyspaces exist:

```bash
# List keyspaces
vtctldclient list_keyspaces --server localhost:15999

# Verify source keyspace
vtctldclient get_keyspace --server localhost:15999 <source_keyspace>

# Verify target keyspace
vtctldclient get_keyspace --server localhost:15999 <target_keyspace>
```

### 3. Check tablet availability

Ensure RDONLY tablets are available:

```bash
# List tablets by type
vtctldclient list-tablets --server localhost:15999 | grep RDONLY

# If no RDONLY tablets, create one
vtctldclient backup --server localhost:15999 <tablet-alias>
```

### 4. Restart workflow

If workflow is stuck:

```bash
# Cancel workflow
vtctldclient workflow --server localhost:15999 <workflow_name> cancel

# Restart workflow
vtctldclient workflow --server localhost:15999 moveTables --target-keyspace <target> --tables <tables>
```

## Common Scenarios

**Scenario 1: Table already exists in target**

If table exists in target keyspace:

```bash
# Check table in target
vtctldclient get_schema --server localhost:15999 <target_keyspace> | grep <table>

# If exists, either drop it or skip the table
```

**Scenario 2: Source tablet not available**

If source tablets are not healthy:

```bash
# Check source tablet health
vtctldclient list-tablets --server localhost:15999 | grep <source_keyspace>

# Wait for tablets to be healthy
```

## Prevent It

1. Test move tables in staging first
2. Ensure sufficient tablet capacity
3. Monitor workflow progress

## Related Pages

- [Vitess Workflow Error](vitess-workflow-error)
- [Vitess Keyspace Error](vitess-keyspace-error)
- [Vitess Tablet Error](vitess-tablet-error)
