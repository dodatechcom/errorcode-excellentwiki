---
title: "[Solution] ScyllaDB Role Permission Error — How to Fix"
description: "Fix ScyllaDB role permission errors when users cannot perform operations due to insufficient grants"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Role Permission Error

Role permission errors occur when a database role lacks the necessary permissions to perform the requested operation on a keyspace, table, or function.

## Why It Happens

- Role was created without LOGIN or SUPERUSER attributes
- GRANT statement was not executed for the required resource
- Role permissions were revoked accidentally
- Custom role hierarchy is missing required parent roles
- Authorization is enabled but role has no permissions

## Common Error Messages

```
Unauthorized: Error from server: code=2100 [Unauthorized] User has no permission
```

```
InvalidRequest: Role app_user does not have permission on keyspace mykeyspace
```

```
error: permission denied for table users
```

## How to Fix It

### 1. Check Current Permissions

```cql
LIST ALL PERMISSIONS OF app_user;
LIST ROLES OF app_user;
```

### 2. Grant Required Permissions

```cql
GRANT ALL ON KEYSPACE mykeyspace TO app_user;
GRANT SELECT, INSERT, UPDATE ON TABLE mykeyspace.users TO app_user;
GRANT CREATE ON KEYSPACE mykeyspace TO app_user;
```

### 3. Create Role with Proper Permissions

```cql
CREATE ROLE app_user WITH PASSWORD = 'secure_pwd' AND LOGIN = true;
GRANT ALL ON KEYSPACE mykeyspace TO app_user;
```

### 4. Revoke Permissions (If Needed)

```cql
REVOKE DELETE ON TABLE mykeyspace.users FROM app_user;
REVOKE ALL ON KEYSPACE mykeyspace FROM old_user;
```

## Examples

```
cqlsh> LIST ALL PERMISSIONS OF app_user;
role      | resource        | permission
----------+-----------------+------------
app_user  | keyspace mykeyspace | SELECT
app_user  | keyspace mykeyspace | INSERT
```

## Prevent It

- Use least-privilege principle for role creation
- Document role permissions and review regularly
- Use role hierarchies to manage complex permission sets

## Related Pages

- [ScyllaDB Permission Denied](/tools/scylladb/scylladb-permission-denied)
- [ScyllaDB Role Not Found](/tools/scylladb/scylladb-role-not-found)
- [ScyllaDB Auth Error](/tools/scylladb/scylladb-auth-error)
