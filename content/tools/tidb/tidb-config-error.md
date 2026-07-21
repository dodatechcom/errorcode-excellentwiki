---
title: "[Solution] TiDB Configuration Error — How to Fix"
description: "Fix TiDB configuration errors by resolving gflag conflicts, correcting toml syntax, and validating component configuration parameters"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Configuration Error

TiDB configuration errors occur when startup parameters, gflags, or toml configuration files contain invalid values, missing sections, or incompatible settings.

## Why It Happens

- Invalid gflag value passed at startup
- Missing required configuration section in toml file
- Duplicate configuration keys
- Type mismatch between config value and expected format
- Deprecated option used in newer TiDB version
- Circular dependency between configuration settings

## Common Error Messages

```
ERROR: unknown flag: --invalid-flag
```

```
FATAL: invalid config: unknown option 'unknown_key'
```

```
ERROR: flag 'store' expects a value
```

```
FATAL: parse config error near [tikv] section
```

## How to Fix It

### 1. Validate Configuration File

```bash
# Check toml syntax
python3 -c "
import toml
with open('tidb.toml') as f:
    toml.load(f)
print('Config is valid')
"

# Check TiDB config with flag help
tidb-server --help | grep store

# Dry run configuration
tidb-server --config-check --config=tidb.toml
```

### 2. Fix Common gflag Issues

```bash
# Correct flag format
tidb-server --store=tikv --path=pd1:2379,pd2:2379,pd3:2379

# Use config file instead of flags
tidb-server --config=tidb.toml

# Check for deprecated flags
grep -E "deprecated|removed" tidb.toml
```

### 3. Fix toml Configuration

```ini
# tidb.toml - correct structure
[tidb]
# Port for MySQL protocol
port = 4000
# Status port for monitoring
status-port = 10080

[tikv]
# TiKV client timeout
timeout = "3s"

[pd]
# PD endpoints
endpoints = ["pd1:2379", "pd2:2379", "pd3:2379"]
```

### 4. Recover from Bad Configuration

```bash
# Start with minimal flags
tidb-server --store=tikv --path=pd:2379 --config=minimal.toml

# Use default config to generate reference
tidb-server --print-default-config > tidb-default.toml

# Compare with current config
diff tidb-default.toml tidb.toml
```

## Common Scenarios

- **TiDB will not start after config change**: Use `--config-check` flag to validate before restarting.
- **Unknown option error after upgrade**: Check the changelog for deprecated or renamed options.
- **Connection refused after port change**: Ensure all clients use the new port.

## Prevent It

- Always validate config with `--config-check` before restarting
- Use `--print-default-config` as a reference for valid options
- Keep configuration versioned and reviewed before deployment

## Related Pages

- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
- [TiDB TiFlash Config Error](/tools/tidb/tidb-tiflash-config-error)
