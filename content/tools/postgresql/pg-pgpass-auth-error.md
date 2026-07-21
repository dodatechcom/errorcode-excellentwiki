---
title: "[Solution] PostgreSQL pg_pass File Authentication Error"
description: "Fix PostgreSQL pgpass file authentication errors. Resolve connection failures when using password file."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL pg_pass File Authentication Error

ERROR: password authentication failed for user / pgpass file not used

This error occurs when the pgpass file is present but not being read due to incorrect permissions, format, or file location.

## Common Causes

- pgpass file permissions are too open (must be 0600)
- Incorrect hostname, port, or database name in the pgpass entry
- PGPASSFILE environment variable pointing to wrong location
- Password does not match what is stored in pgpass

## How to Fix

1. Set correct permissions on the pgpass file:

```bash
chmod 0600 ~/.pgpass
ls -la ~/.pgpass
```

2. Verify the pgpass file format -- each line must match:

```
hostname:port:database:username:password
```

3. Set the PGPASSFILE environment variable:

```bash
export PGPASSFILE="/home/user/.pgpass"
```

4. Test the connection:

```bash
psql -h dbhost -p 5432 -U myuser -d mydb
```

## Examples

```bash
# Example pgpass file entries
echo "localhost:5432:appdb:appuser:s3cur3p@ss" > ~/.pgpass
echo "replica.db.local:5432:repldb:repluser:r3plp@ss" >> ~/.pgpass

# Verify permissions
stat -c "%a %U" ~/.pgpass
```
