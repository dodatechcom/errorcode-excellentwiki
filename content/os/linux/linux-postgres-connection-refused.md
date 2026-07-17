---
title: "[Solution] Linux PostgreSQL Connection Refused"
description: "Fix Linux PostgreSQL 'connection refused' errors. Resolve PostgreSQL server connection issues, pg_hba.conf problems, and port conflicts."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: PostgreSQL — connection refused

The `FATAL: could not connect to server: Connection refused` error means the PostgreSQL client cannot establish a TCP connection to the server. The server is either not running, not listening on the expected port/IP, or a firewall is blocking the connection.

## What This Error Means

PostgreSQL server (`postmaster` or `postgres`) listens on a TCP port (default 5432) and optionally on a Unix socket. A connection refused error means the TCP connection to the specified host and port was actively rejected — either the server is not running on that port, or the port is closed by a firewall. This is different from `no pg_hba.conf entry` which means the server is running but rejected the authentication.

## Common Causes

- PostgreSQL server is not running
- Server not listening on the expected IP/port
- `postgresql.conf` has `listen_addresses` restricted
- Firewall blocking port 5432
- `pg_hba.conf` not configured for the client IP
- Server crashed and not restarted
- Port conflict with another service

## How to Fix

### 1. Check PostgreSQL Server Status

```bash
# Check if PostgreSQL is running
sudo systemctl status postgresql

# Check the process
sudo pg_lsclusters

# Check listening ports
sudo ss -tlnp | grep 5432
```

### 2. Start PostgreSQL

```bash
# Start PostgreSQL
sudo systemctl start postgresql

# Enable on boot
sudo systemctl enable postgresql

# Check logs
sudo journalctl -u postgresql -n 50 --no-pager
sudo tail -50 /var/log/postgresql/postgresql-*-main.log
```

### 3. Fix listen_addresses

```bash
# Check current setting
sudo grep listen_addresses /etc/postgresql/*/main/postgresql.conf

# Edit to listen on all interfaces
sudo nano /etc/postgresql/15/main/postgresql.conf

# Change:
# listen_addresses = 'localhost'
# To:
# listen_addresses = '*'

# Restart PostgreSQL
sudo systemctl restart postgresql
```

### 4. Fix pg_hba.conf

```bash
# Allow remote connections
sudo nano /etc/postgresql/15/main/pg_hba.conf

# Add line for specific IP:
# host    all    all    192.168.1.0/24    scram-sha-256

# Or allow all (less secure):
# host    all    all    0.0.0.0/0        scram-sha-256

# Restart PostgreSQL
sudo systemctl restart postgresql
```

### 5. Fix Firewall Rules

```bash
# Check if firewall blocks 5432
sudo firewall-cmd --list-ports
sudo iptables -L -n | grep 5432

# Open the port
sudo firewall-cmd --permanent --add-port=5432/tcp
sudo firewall-cmd --reload
```

### 6. Test the Connection

```bash
# Test locally
psql -h localhost -U postgres -c "SELECT version();"

# Test via TCP
psql -h 127.0.0.1 -p 5432 -U postgres

# Test from remote
psql -h <server-ip> -p 5432 -U myuser -d mydb
```

### 7. Check Port Conflicts

```bash
# Verify port 5432 is used by PostgreSQL
sudo ss -tlnp | grep 5432

# If another process is using the port
sudo lsof -i :5432

# Change PostgreSQL port in postgresql.conf
# port = 5433
```

## Examples

```bash
$ psql -h 192.168.1.100 -U myuser mydb
psql: error: connection to server at "192.168.1.100", port 5432 failed:
Connection refused (0x0000274D/10061)
    Is the server running on that host and accepting TCP/IP connections?

$ sudo systemctl status postgresql
● postgresql.service - PostgreSQL Cluster 15-main
     Active: inactive (dead)

$ sudo systemctl start postgresql
$ sudo ss -tlnp | grep 5432
LISTEN  0  128  0.0.0.0:5432  0.0.0.0:*  users:(("postgres",pid=1234))

$ psql -h 192.168.1.100 -U myuser mydb
psql (15.3)
Type "help" for help.
mydb=>
```

## Related Errors

- [PostgreSQL role error]({{< relref "/os/linux/linux-postgres-role-error" >}}) — Role not found
- [MySQL connection refused]({{< relref "/os/linux/linux-mysql-connection-refused" >}}) — MySQL connection issues
- [Redis OOM]({{< relref "/os/linux/linux-redis-oom" >}}) — Redis memory errors
