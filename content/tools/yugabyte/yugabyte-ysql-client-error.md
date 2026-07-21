---
title: "[Solution] YugabyteDB YSQL Client Error — How to Fix"
description: "Fix YugabyteDB YSQL client errors by resolving connection failures, fixing client configuration, and handling YSQL protocol issues"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB YSQL Client Error

YugabyteDB YSQL client errors occur when client applications fail to connect, authenticate, or communicate via the YSQL (PostgreSQL-compatible) interface.

## Why It Happens

- Client connects to wrong port (5433 is default for YSQL)
- Authentication credentials are incorrect
- pg_hba.conf does not allow the client connection
- Client driver version is incompatible
- SSL/TLS is required but not configured on the client
- Connection pooler intercepts the connection

## Common Error Messages

```
FATAL: password authentication failed
```

```
FATAL: pg_hba.conf rejects connection
```

```
ERROR: connection refused on port 5433
```

```
FATAL: database does not exist
```

## How to Fix It

### 1. Check YSQL Connectivity

```bash
# Test connection with psql
psql -h yugabyte -p 5433 -U yugabyte -d yugabyte

# Check YSQL proxy status
curl http://yugabyte:9000/varz | grep ysql

# Check if YSQL proxy is running
netstat -tlnp | grep 5433
```

### 2. Fix Authentication

```bash
# Check pg_hba.conf
cat /opt/yugabyte/conf/master/pg_hba.conf

# Add client access
# host all all 0.0.0.0/0 md5
```

```sql
-- Reset password
ALTER USER yugabyte PASSWORD 'new_password';

-- Create new user
CREATE USER app_user WITH PASSWORD 'secure_password';
GRANT ALL ON DATABASE mydb TO app_user;
```

### 3. Fix Client Configuration

```python
# Python psycopg2 connection
import psycopg2

conn = psycopg2.connect(
    host='yugabyte',
    port=5433,
    dbname='mydb',
    user='yugabyte',
    password='password'
)
```

### 4. Fix SSL Configuration

```bash
# Connect with SSL
psql "sslmode=require host=yugabyte port=5433 dbname=mydb user=yugabyte"

# Check SSL status
openssl s_client -connect yugabyte:5433
```

## Common Scenarios

- **Connection refused**: Ensure YSQL proxy is running on port 5433.
- **Authentication failed**: Check pg_hba.conf and user credentials.
- **SSL required**: Configure SSL certificates on the client.

## Prevent It

- Use the correct port (5433) for YSQL connections
- Configure authentication before exposing the cluster
- Test client connectivity before deploying applications

## Related Pages

- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB Auth Error](/tools/yugabyte/yugabyte-auth-error)
- [YugabyteDB SSL Error](/tools/yugabyte/yugabyte-ssl-error)
