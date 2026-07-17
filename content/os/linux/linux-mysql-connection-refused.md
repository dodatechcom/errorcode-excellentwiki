---
title: "[Solution] Linux MySQL Can't Connect to Local Server"
description: "Fix Linux MySQL 'Can't connect to local server' errors. Resolve MySQL connection refused, socket issues, and server startup failures."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["mysql", "connection-refused", "socket", "database", "server"]
weight: 5
---

# Linux: MySQL — Can't connect to local server

The `Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock'` error means the MySQL client cannot connect to the MySQL server via the Unix socket file. This happens when the MySQL server is not running, the socket file does not exist, or the client is looking in the wrong location.

## What This Error Means

MySQL clients connect to the server either via a Unix socket (default for localhost) or TCP. The socket path is usually `/var/run/mysqld/mysqld.sock`. When MySQL server is not running, the socket file is not created, and any client connection attempt fails. If the socket exists but the server is not listening, the connection also fails.

## Common Causes

- MySQL server is not running or crashed
- Socket file missing or in a different location
- MySQL server failed to start due to configuration error
- Disk space full preventing socket creation
- Another process using the socket file path
- Incorrect `socket` directive in `my.cnf`
- AppArmor or SELinux blocking socket access

## How to Fix

### 1. Check MySQL Server Status

```bash
# Check if MySQL is running
sudo systemctl status mysql
# or
sudo systemctl status mysqld

# Check if the socket file exists
ls -la /var/run/mysqld/mysqld.sock
```

### 2. Start MySQL Server

```bash
# Start MySQL
sudo systemctl start mysql
# or
sudo systemctl start mysqld

# Enable on boot
sudo systemctl enable mysql

# Check logs if it fails to start
sudo journalctl -u mysql -n 50 --no-pager
```

### 3. Check MySQL Error Log

```bash
# Default log locations
sudo tail -50 /var/log/mysql/error.log
sudo tail -50 /var/log/mysqld.log

# Common errors:
# "Can't open/create test table" — disk full or permissions
# "InnoDB: Unable to lock ./ibdata1" — another instance running
# "Fatal error: Can't open and lock privilege tables" — table corruption
```

### 4. Fix Socket Path Mismatch

```bash
# Check where MySQL expects the socket
mysql --help | grep socket
# or
sudo grep socket /etc/mysql/my.cnf

# Ensure client and server use the same socket path
# In /etc/mysql/my.cnf:
# [mysqld]
# socket = /var/run/mysqld/mysqld.sock
# [client]
# socket = /var/run/mysqld/mysqld.sock

# Create the directory if missing
sudo mkdir -p /var/run/mysqld
sudo chown mysql:mysql /var/run/mysqld
```

### 5. Fix Permissions

```bash
# Check MySQL data directory permissions
ls -la /var/lib/mysql/

# Fix ownership
sudo chown -R mysql:mysql /var/lib/mysql
sudo chown -R mysql:mysql /var/run/mysqld

# Fix socket permissions
sudo chmod 755 /var/run/mysqld
```

### 6. Initialize MySQL if Needed

```bash
# If MySQL data directory is missing or corrupted
sudo mysqld --initialize --user=mysql

# For MariaDB
sudo mysql_install_db --user=mysql --datadir=/var/lib/mysql
```

### 7. Connect via TCP Instead

```bash
# Force TCP connection (bypass socket)
mysql -h 127.0.0.1 -P 3306 -u root -p

# Check if MySQL is listening on TCP
sudo ss -tlnp | grep 3306
```

## Examples

```bash
$ mysql -u root -p
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)

$ ls -la /var/run/mysqld/mysqld.sock
ls: cannot access '/var/run/mysqld/mysqld.sock': No such file or directory

$ sudo systemctl status mysql
● mysql.service - MySQL Community Server
     Active: inactive (dead)

$ sudo systemctl start mysql
$ ls -la /var/run/mysqld/mysqld.sock
srwxrwxrwx 1 mysql mysql 0 /var/run/mysqld/mysqld.sock

$ mysql -u root -p
Welcome to the MySQL monitor.
```

## Related Errors

- [MySQL deadlock]({{< relref "/os/linux/linux-mysql-deadlock" >}}) — Deadlock errors
- [PostgreSQL connection refused]({{< relref "/os/linux/linux-postgres-connection-refused" >}}) — PostgreSQL connection issues
- [nginx 502 bad gateway]({{< relref "/os/linux/linux-nginx-502-upstream" >}}) — Backend connection failures
