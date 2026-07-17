---
title: "Oracle - ORA-12541: TNS no listener"
description: "Oracle client cannot connect because the TNS listener is not running on the database server"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "tns", "listener", "connection", "ora-12541", "network"]
weight: 5
---

ORA-12541: TNS no listener occurs when the Oracle client cannot connect to the database because the TNS listener process is not running on the server or is not accessible on the configured port.

## Common Causes

- TNS listener service stopped or crashed
- Listener listening on wrong port or interface
- Firewall blocking port 1521
- Incorrect tnsnames.ora entry
- Oracle home not properly configured

## How to Fix

1. Check listener status:

```bash
lsnrctl status
```

2. Start the listener:

```bash
lsnrctl start
```

3. Verify listener configuration:

```bash
cat $ORACLE_HOME/network/admin/listener.ora
```

4. Test connectivity with tnsping:

```bash
tnsping your_database_host:1521
```

5. Fix tnsnames.ora entry:

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

6. Check firewall:

```bash
telnet dbhost.example.com 1521
sudo ufw allow 1521/tcp
```

## Examples

```bash
$ sqlplus user/password@mydb
ERROR: ORA-12541: TNS:no listener

$ lsnrctl status
LSNRCTL for Linux: Version 19.0.0.0.0
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=0.0.0.0)(PORT=1521))
TNS-12541: TNS:no listener
```

## Related Errors

- [Auth error]({{< relref "/tools/oracle/oracle-auth-error" >}})
- [Permission error]({{< relref "/tools/oracle/oracle-permission-error" >}})
