---
title: "[Solution] PostgreSQL Connection Refused - Fix pg_hba.conf and Listen Addresses"
description: "Fix PostgreSQL connection refused errors by configuring pg_hba.conf, verifying listen addresses, and checking firewall rules on your server"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Connection Refused

A `connection refused` error in PostgreSQL means the server actively rejected the TCP connection from the client. This is different from an authentication failure -- the server never accepted the connection at all.

## What This Error Means

PostgreSQL maintains a client authentication configuration file (`pg_hba.conf`) that controls which hosts can connect, which databases they can access, and what authentication method they must use. When you see `connection refused`, it typically means either the PostgreSQL server is not listening on the expected address and port, or the `pg_hba.conf` file does not contain a rule that allows your client to connect.

The full error message usually looks like:

```
FATAL: connection to server failed
FATAL: pg_hba.conf rejects connection for host "192.168.1.100", user "myuser", database "mydb", SSL off
```

Or from the client side:

```
psql: error: could not connect to server: Connection refused
Is the server running on host "192.168.1.100" and accepting TCP/IP connections on port 5432?
```

## Why It Happens

- PostgreSQL is not running on the target server
- `postgresql.conf` has `listen_addresses` set to `localhost` only
- `pg_hba.conf` does not contain a matching rule for the client IP, user, or database
- A firewall (iptables, ufw, cloud security group) blocks port 5432
- The PostgreSQL instance is running on a non-standard port and the client is connecting to 5432
- The server is listening on IPv4 but the client connects via IPv6 (or vice versa)

## How to Fix It

### 1. Verify PostgreSQL Is Running

```bash
sudo systemctl status postgresql
# Or check the process
ps aux | grep postgres
```

### 2. Check and Update listen_addresses

```sql
-- In postgresql.conf
listen_addresses = '*'
-- Or for a specific interface
listen_addresses = 'localhost,192.168.1.100'
```

After changing, reload the configuration:

```sql
SELECT pg_reload_conf();
```

### 3. Add a Rule to pg_hba.conf

```bash
# Allow connections from a specific subnet
# TYPE  DATABASE  USER    ADDRESS          METHOD
host    all       all     192.168.1.0/24   md5

# Allow connections from anywhere (use with caution)
host    all       all     0.0.0.0/0        md5
```

Then reload:

```bash
sudo systemctl reload postgresql
```

### 4. Verify the Port

```bash
ss -tlnp | grep 5432
```

If PostgreSQL listens on a different port, connect with `-p`:

```bash
psql -h 192.168.1.100 -p 5433 -U myuser -d mydb
```

### 5. Check Firewall Rules

```bash
# ufw
sudo ufw status | grep 5432

# iptables
sudo iptables -L -n | grep 5432
```

## Common Mistakes

- Editing `pg_hba.conf` but forgetting to reload PostgreSQL afterward
- Adding a rule with the wrong netmask (using `/32` when you need `/24`)
- Restarting PostgreSQL instead of reloading -- restarts cause connection drops for all users
- Assuming `listen_addresses = '*'` is the default -- it is not on most distributions
- Not checking whether the PostgreSQL server is actually running before changing config files

## Related Pages

- [PostgreSQL Role Does Not Exist](/tools/postgresql/pg-role-does-not-exist)
- [PostgreSQL Too Many Connections](/tools/postgresql/pg-connection-limit)
- [PostgreSQL Config Error](/tools/postgresql/pg-config-error)
- [MySQL Connection Refused](/tools/mysql/mysql-connection-refused)
