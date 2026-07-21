---
title: "[Solution] Spring Liquibase Checksum Error"
description: "Fix Spring Liquibase checksum errors when changeset validation fails after modifications."
frameworks: ["spring"]
error-types: ["database-error"]
severities: ["error"]
---

Liquibase checksum errors occur when an executed changeset is modified, causing the stored checksum to not match.

## Common Causes

- Changeset modified after execution
- Manual changes to `DATABASECHANGELOG` table
- Database-specific formatting differences
- Encoding differences between environments
- Changeset ID and author combination not unique

## How to Fix

### Never Modify Executed Changesets

```xml
<!-- Wrong -- modifying executed changeset -->
<changeSet id="1" author="dev">
    <!-- This was already executed -->
    <modifyDataType tableName="users" columnName="name" newDataType="VARCHAR(200)"/>
</changeSet>

<!-- Correct -- create new changeset -->
<changeSet id="2" author="dev">
    <modifyDataType tableName="users" columnName="name" newDataType="VARCHAR(200)"/>
</changeSet>
```

### Clear Checksums (Development Only)

```bash
# Clear all checksums
liquibase clearCheckSums

# Or in application
spring:
  liquibase:
    clear-checksums: true
```

### Repair Liquibase State

```java
@Configuration
public class LiquibaseConfig {
    @Bean
    public SpringLiquibase liquibase(DataSource dataSource) {
        SpringLiquibase liquibase = new SpringLiquibase();
        liquibase.setDataSource(dataSource);
        liquibase.setChangeLog("classpath:db/changelog/db.changelog-master.xml");
        liquibase.setClearCheckSums(true);  // Use carefully
        return liquibase;
    }
}
```

## Examples

```xml
<!-- Bug -- changeset already in DATABASECHANGELOG -->
<changeSet id="create-users" author="dev">
    <!-- Modified after execution causes checksum error -->
</changeSet>

<!-- Fix -- new changeset -->
<changeSet id="modify-users-name" author="dev">
    <modifyDataType tableName="users" columnName="name" newDataType="VARCHAR(200)"/>
</changeSet>
```

Check current checksums: `SELECT * FROM DATABASECHANGELOG;`
