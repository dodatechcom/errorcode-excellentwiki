---
title: "[Solution] TimescaleDB Install Error — How to Fix"
description: "Fix TimescaleDB installation errors by resolving package dependency failures, fixing shared library issues, and handling PostgreSQL version mismatches"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Install Error

TimescaleDB install errors occur when installing TimescaleDB via package manager, source compilation, or Docker fails due to dependency, version, or configuration issues.

## Why It Happens

- Package repository is not configured for the OS or PostgreSQL version
- PostgreSQL development headers are not installed
- Shared library paths are not correctly configured
- Docker image version does not match the PostgreSQL version
- The install script fails due to network issues
- SELinux or AppArmor blocks the library loading

## Common Error Messages

```
ERROR: could not find timescaledb.so
```

```
ERROR: timescaledb version mismatch
```

```
ERROR: package dependency resolution failed
```

```
FATAL: could not load library "timescaledb.so"
```

## How to Fix It

### 1. Install via Package Manager

```bash
# For Ubuntu/Debian
sudo add-apt-repository ppa:timescale/timescaledb-2-pg14
sudo apt-get update
sudo apt-get install timescaledb-2-postgresql-14

# For RHEL/CentOS
sudo yum install -y timescaledb_2-postgresql-14

# Configure shared_preload_libraries
echo "shared_preload_libraries = 'timescaledb'" | \
  sudo tee -a /etc/postgresql/*/main/postgresql.conf
```

### 2. Fix Library Path Issues

```bash
# Check library installation
find / -name "timescaledb.so" 2>/dev/null

# Verify PostgreSQL can find the library
ls /usr/lib/postgresql/*/lib/timescaledb*

# Update ldconfig
sudo ldconfig

# Check library path in PostgreSQL
SHOW shared_preload_libraries;
```

### 3. Fix Docker Installation

```bash
# Use official TimescaleDB Docker image
docker run -d \
  --name timescaledb \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=password \
  timescale/timescaledb:latest-pg14

# Or add extension to existing PostgreSQL
docker run -d \
  --name timescaledb \
  -v /var/lib/postgresql/data:/var/lib/postgresql/data \
  -p 5432:5432 \
  timescale/timescaledb:latest-pg14
```

### 4. Fix SELinux Issues

```bash
# Check SELinux status
getenforce

# Temporarily set to permissive
sudo setenforce 0

# Or create a policy module
sudo ausearch -c 'timescaledb' --raw | audit2allow -M timescaledb
sudo semodule -i timescaledb.pp
```

## Common Scenarios

- **Extension fails to load after install**: Ensure shared_preload_libraries includes timescaledb and restart PostgreSQL.
- **Version mismatch error**: Install the correct TimescaleDB version for your PostgreSQL version.
- **Docker container fails to start**: Check that the PostgreSQL data directory is properly mounted.

## Prevent It

- Use the official TimescaleDB package repository for your OS
- Match TimescaleDB version to PostgreSQL version
- Test the installation in a staging environment

## Related Pages

- [TimescaleDB Extension Error](/tools/timescaledb/timescale-extension-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Upgrade Error](/tools/timescaledb/timescale-upgrade-error)
