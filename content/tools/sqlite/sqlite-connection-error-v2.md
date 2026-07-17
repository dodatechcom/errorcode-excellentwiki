---
title: "SQLite - unable to open database file"
description: "SQLite fails to open or create a database file due to file system issues or permission errors"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlite", "connection", "open", "file", "permission", "filesystem"]
weight: 5
---

SQLite "unable to open database file" error occurs when the database engine cannot create, open, or access the database file. Since SQLite is file-based, this error is almost always related to the file system rather than the database itself.

## Common Causes

- Database file path does not exist
- Insufficient file permissions on the database directory
- Read-only filesystem or mount
- File locked by another process
- Disk space exhaustion
- Symlink to a non-existent target

## How to Fix

1. Verify the directory exists and is writable:

```bash
ls -la /path/to/database/
chmod 755 /path/to/database/
```

2. Check file permissions:

```bash
chmod 644 /path/to/database/mydb.sqlite
chown www-data:www-data /path/to/database/mydb.sqlite
```

3. Ensure disk space is available:

```bash
df -h /path/to/database/
```

4. Check for file locks:

```bash
lsof /path/to/database/mydb.sqlite
fuser /path/to/database/mydb.sqlite
```

5. Test SQLite can access the path:

```bash
sqlite3 /path/to/database/mydb.sqlite "SELECT 1;"
```

6. Create the directory if it does not exist:

```bash
mkdir -p /path/to/database/
```

## Examples

```python
import sqlite3
# Error: unable to open database file
conn = sqlite3.connect('/nonexistent/path/mydb.sqlite')

# Fix: ensure path exists
import os
os.makedirs('/path/to/database/', exist_ok=True)
conn = sqlite3.connect('/path/to/database/mydb.sqlite')
```

```javascript
// Node.js better-sqlite3
const Database = require('better-sqlite3');
// Error: unable to open database file
const db = new Database('/locked/path/mydb.sqlite');

// Fix: check permissions first
const db = new Database('./mydb.sqlite');
```

## Related Errors

- [Database locked]({{< relref "/tools/sqlite/sqlite-database-locked" >}})
- [I/O error]({{< relref "/tools/sqlite/sqlite-io-error" >}})
