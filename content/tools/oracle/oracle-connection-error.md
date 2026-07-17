---
title: "Oracle Connection Error"
description: "Oracle client cannot establish a connection to the database."
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "connection", "tns", "listener", "network"]
weight: 5
---

# Oracle Connection Error

An Oracle connection error occurs when the Oracle client cannot connect to the database server. This is typically caused by TNS configuration issues or network problems.

## Common Causes

- TNS listener not running on server
- Incorrect TNS entry in tnsnames.ora
- Network connectivity issues
- Firewall blocking listener port

## How to Fix

### Check TNS Listener

```bash
lsnrctl status
```

### Verify TNS Configuration

```bash
cat $ORACLE_HOME/network/admin/tnsnames.ora
```

### Test Connectivity

```bash
tnsping your_database_host:1521
```

### Fix TNS Entry

```
# tnsnames.ora
MYDB =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = dbhost.example.com)(PORT = 1521))
    (CONNECT_DATA =
      (SERVICE_NAME = mydb)
    )
  )
```

### Test Connection with SQLPlus

```bash
sqlplus user/password@mydb
```

### Check Firewall

```bash
telnet dbhost.example.com 1521
```

## Examples

```bash
sqlplus user/password@mydb
ERROR: ORA-12541: TNS:no listener
```

## Related Errors

- [Auth Error]({{< relref "/tools/oracle/auth-error" >}}) — authentication failure
- [Permission Error]({{< relref "/tools/oracle/permission-error" >}}) — permission denied
