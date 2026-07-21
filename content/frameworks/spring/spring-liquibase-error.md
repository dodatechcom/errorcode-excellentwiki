---
title: "[Solution] spring Liquibase Error"
description: "Liquibase changeset failing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Liquibase changeset failing.

## Common Causes

Wrong changeset.

## How to Fix

Check changeset.

## Example

```xml
<changeSet id="1" author="dev">
  <createTable tableName="users">
    <column name="id" type="BIGINT"/>
  </createTable>
</changeSet>
```
