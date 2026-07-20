---
title: "[Solution] MySQL Packet too large error"
description: "Fix MySQL 'Packet too large' error. Resolve max_allowed_packet size issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Packet too large error

ERROR 1153 (08S01): Got a packet bigger than 'max_allowed_packet' bytes

This error occurs when a query or result set exceeds the max_allowed_packet setting.

## How to Fix

### Check MySQL Status

```bash
sudo systemctl status mysql
mysqladmin ping
```

### Check Error Log

```bash
sudo tail -100 /var/log/mysql/error.log
```

### Verify Configuration

```bash
mysql --help
sudo mysql -e "SHOW VARIABLES LIKE '%timeout%';"
```

## Related Errors

- [MySQL Connection Refused]({{< relref "/tools/mysql/mysql-connection-refused" >}}) — connection refused
- [MySQL Gone Away]({{< relref "/tools/mysql/mysql-gone-away" >}}) — connection lost
