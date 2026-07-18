---
title: "[Solution] MySQL Can't Connect to Server - Fix Connection Refused Errors"
description: "Fix MySQL can't connect to server errors by checking mysqld status, verify bind-address config, and open firewall ports for remote access"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Can't Connect to Server

This error means the MySQL client cannot establish a TCP connection to the MySQL server. The server may not be running, may not be listening on the expected address, or a firewall is blocking the connection.

## What This Error Means

MySQL returns this error when the client fails to connect:

```
ERROR 2003 (HY000): Can't connect to MySQL server on '192.168.1.100' (111)
```

The error code 111 is the operating system error for "Connection refused." A different error appears when the server is reachable but the port is wrong:

```
ERROR 2003 (HY000): Can't connect to MySQL server on '192.168.1.100' (113)
```

Error 113 means "No route to host," which typically indicates a firewall issue.

## Why It Happens

- The MySQL server process (`mysqld`) is not running
- `bind-address` in `my.cnf` is set to `127.0.0.1` only
- The MySQL server is listening on a non-standard port
- A firewall blocks port 3306
- SELinux or AppArmor prevents MySQL from binding to the port
- The MySQL server is configured to use a socket only, not TCP

## How to Fix It

### 1. Verify MySQL Is Running

```bash
sudo systemctl status mysql
# Or on older systems
sudo systemctl status mysqld

# Check the process
ps aux | grep mysql
```

### 2. Check and Update bind-address

```bash
# In my.cnf (usually /etc/mysql/my.cnf or /etc/my.cnf)
[mysqld]
bind-address = 0.0.0.0
```

Then restart MySQL:

```bash
sudo systemctl restart mysql
```

### 3. Verify the Listening Port

```bash
# Check what port MySQL is listening on
ss -tlnp | grep mysql

# Or
netstat -tlnp | grep mysql
```

### 4. Check Firewall Rules

```bash
# ufw
sudo ufw allow 3306/tcp

# firewalld
sudo firewall-cmd --add-port=3306/tcp --permanent
sudo firewall-cmd --reload

# iptables
sudo iptables -A INPUT -p tcp --dport 3306 -j ACCEPT
```

### 5. Test the Connection

```bash
# Test from the server itself
mysql -u root -p -h 127.0.0.1

# Test from a remote host
mysql -u myuser -p -h 192.168.1.100 -P 3306
```

## Common Mistakes

- Not restarting MySQL after changing `bind-address` -- the change only takes effect on restart
- Editing the wrong `my.cnf` file when multiple MySQL configurations exist
- Assuming MySQL listens on TCP by default -- some installations configure socket-only mode
- Not checking SELinux or AppArmor when the port is open but connections are refused
- Testing connectivity with `ping` instead of `telnet` or `nc` -- ping uses ICMP, not TCP

## Related Pages

- [MySQL Access Denied](/tools/mysql/mysql-access-denied)
- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)
- [MySQL SSL Error](/tools/mysql/mysql-ssl-error)
- [PostgreSQL Connection Refused](/tools/postgresql/pg-connection-refused)
