---
title: "[Solution] Apache Kafka ACL Error"
description: "Fix Apache Kafka acl errors. Learn why this happens and how to resolve it quickly."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Apache Kafka ACL Error

Kafka ACL errors occur when access control lists are misconfigured, denying legitimate access.

## Why This Happens

- ACL not found
- Permission denied
- ACL format invalid
- Resource not found

## Common Error Messages

- `acl_not_found`
- `acl_permission_denied`
- `acl_format_error`
- `acl_resource_error`

## How to Fix It

### Solution 1: List ACLs

View existing ACLs:

```bash
kafka-acls.sh --bootstrap-server localhost:9092 --list
```

### Solution 2: Create ACLs

Add ACLs:

```bash
kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:alice --operation Read --topic mytopic
```

### Solution 3: Remove ACLs

Remove ACLs:

```bash
kafka-acls.sh --bootstrap-server localhost:9092 --remove --allow-principal User:alice --operation Read --topic mytopic
```


## Common Scenarios

- **Permission denied:** Check if ACLs are configured correctly.
- **ACL not found:** Verify the ACL exists.

## Prevent It

- Use appropriate ACLs
- Test access
- Monitor ACL changes
