---
title: "[Solution] PostgreSQL Extension Installation Failed Error — How to Fix"
description: "Fix PostgreSQL extension installation failures by checking compatibility, installing build dependencies, verifying permissions, and resolving version conflicts"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# PostgreSQL Extension Installation Failed Error

This error means the `CREATE EXTENSION` command failed because the extension files are missing, incompatible, or the required shared libraries cannot be loaded. Extensions must be installed at the OS level before they can be activated in a database.

## Why It Happens

- The extension package is not installed on the server OS
- The extension version is incompatible with the PostgreSQL server version
- The `shared_preload_libraries` setting is missing for extensions that require it
- The PostgreSQL development headers were not installed during compilation
- The extension SQL files are in the wrong directory
- The user executing `CREATE EXTENSION` lacks superuser privileges
- A required C library or dependency is missing from the system

## Common Error Messages

```
ERROR: could not open extension control file "/usr/share/postgresql/14/extension/postgis.control": No such file or directory
```

```
ERROR: extension "pg_stat_statements" must be loaded via shared_preload_libraries
```

```
ERROR: function pg_stat_statements_reset() does not exist
HINT: No function matches the given name and argument types.
```

## How to Fix It

### 1. Install the Extension Package

```bash
# Debian/Ubuntu
sudo apt install postgresql-14-postgis-3

# RHEL/CentOS/Fedora
sudo dnf install postgis25_14

# For pg_stat_statements
sudo apt install postgresql-14-stat-statistics
```

### 2. Verify Available Extensions

```sql
-- List all extensions available in the share directory
SELECT * FROM pg_available_extensions
ORDER BY name;

-- Check if a specific extension is available
SELECT * FROM pg_available_extensions
WHERE name = 'postgis';
```

### 3. Add to shared_preload_libraries

```sql
-- Some extensions must be preloaded before CREATE EXTENSION
-- In postgresql.conf:
shared_preload_libraries = 'pg_stat_statements, auto_explain'

-- Restart PostgreSQL
sudo systemctl restart postgresql
```

### 4. Grant Superuser for Installation

```sql
-- CREATE EXTENSION requires superuser
GRANT postgres TO myuser;

-- Or run as superuser
SET ROLE postgres;
CREATE EXTENSION IF NOT EXISTS postgis;
RESET ROLE;
```

### 5. Verify Installation Path

```bash
# Find the PostgreSQL share directory
pg_config --sharedir

# List installed extensions
ls $(pg_config --sharedir)/extension/

# Check for the specific extension
ls $(pg_config --sharedir)/extension/postgis*
```

### 6. Fix Missing Dependencies

```bash
# Check required shared libraries
ldd /usr/lib/postgresql/14/lib/postgis-3.so

# Install missing system libraries
sudo apt install libgdal-dev libgeos-dev libproj-dev

# Update library cache
sudo ldconfig
```

## Common Scenarios

- **PostGIS on a fresh install**: The PostgreSQL server was installed but `postgresql-14-postgis-3` was not. Install the package and then run `CREATE EXTENSION postgis;`.
- **pg_stat_statements after upgrade**: Upgraded from PostgreSQL 12 to 14 but did not reinstall extensions. Reinstall all extension packages for the new version.
- **Docker image missing extensions**: The base PostgreSQL Docker image does not include third-party extensions. Create a custom Dockerfile that installs the required packages.

## Prevent It

- Document all required extensions in the database setup playbook
- Test extension installation in staging before deploying to production
- Use infrastructure-as-code to ensure extension packages are installed automatically

## Related Pages

- [PostgreSQL Ambiguous Column](/tools/postgresql/pg-ambiguous-column)
- [PostgreSQL Duplicate Table](/tools/postgresql/pg-duplicate-table)
- [MySQL Syntax Error](/tools/mysql/mysql-syntax-error)
