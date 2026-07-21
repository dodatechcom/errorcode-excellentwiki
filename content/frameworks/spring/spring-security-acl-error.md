---
title: "[Solution] Spring Security ACL Error"
description: "Fix Spring Security ACL errors when access control lists fail to authorize resource access."
frameworks: ["spring"]
error-types: ["security-error"]
severities: ["error"]
---

Spring Security ACL errors occur when ACL entries are not properly configured, evaluated, or persisted.

## Common Causes

- ACL database tables not created
- `@PreAuthorize` expressions reference non-existent ACL methods
- Parent ACL not configured correctly
- Object identity not properly registered
- Cache not configured for ACL lookups

## How to Fix

### Configure Spring Security ACL

```sql
CREATE TABLE acl_sid (
    id BIGSERIAL PRIMARY KEY,
    principal BOOLEAN NOT NULL,
    sid VARCHAR(100) NOT NULL,
    UNIQUE(principal, sid)
);

CREATE TABLE acl_class (
    id BIGSERIAL PRIMARY KEY,
    class VARCHAR(100) NOT NULL,
    UNIQUE(class)
);

CREATE TABLE acl_object_identity (
    id BIGSERIAL PRIMARY KEY,
    object_id_class BIGINT NOT NULL REFERENCES acl_class(id),
    object_id_identity BIGINT NOT NULL,
    parent_object BIGINT REFERENCES acl_object_identity(id),
    owner_sid BIGINT NOT NULL REFERENCES acl_sid(id),
    UNIQUE(object_id_class, object_id_identity)
);

CREATE TABLE acl_entry (
    id BIGSERIAL PRIMARY KEY,
    acl_object_identity BIGINT NOT NULL REFERENCES acl_object_identity(id),
    ace_order INT NOT NULL,
    sid BIGINT NOT NULL REFERENCES acl_sid(id),
    mask INT NOT NULL,
    granting BOOLEAN NOT NULL,
    audit_success BOOLEAN NOT NULL DEFAULT FALSE,
    audit_failure BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE(acl_object_identity, ace_order)
);
```

### Use ACL in Service Layer

```java
@Service
public class DocumentService {
    @PreAuthorize("hasPermission(#document, 'READ')")
    public Document getDocument(Document document) {
        return document;
    }

    @PreAuthorize("hasPermission(#document, 'WRITE')")
    public Document updateDocument(Document document, DocumentDto dto) {
        document.setContent(dto.getContent());
        return documentRepository.save(document);
    }
}
```

## Examples

```java
// Bug -- ACL tables missing
// @PreAuthorize("hasPermission(#doc, 'READ')") throws exception

// Fix -- create ACL tables and configure
@EnableMethodSecurity(prePostEnabled = true, securedEnabled = true)
public class SecurityConfig {}
```
