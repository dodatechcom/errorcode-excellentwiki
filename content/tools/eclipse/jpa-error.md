---
title: "[Solution] Eclipse JPA tools error"
description: "JPA/Hibernate tools error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "jpa", "hibernate", "persistence", "orm"]
severity: "error"
---

# JPA tools error

## Error Message

```
javax.persistence.PersistenceException: Exception [EclipseLink-28018] (Eclipse Persistence Services): org.eclipse.persistence.exceptions.EntityManagerSetupException. Deployment name 'myPersistenceUnit' failed to set datasource.
```

## Common Causes

- The persistence unit configuration in `persistence.xml` references a datasource or JDBC URL that is unreachable.
- The JPA entity classes contain annotation errors that prevent the EntityManager from being created.
- The Hibernate/EclipseLink DDL generation is configured incorrectly for the target database.

## Solutions

### Solution 1: Validate Persistence Unit Configuration

Open **Window > Preferences > JPA > Connection** and verify the database connection settings. Then open `persistence.xml` and ensure the `jdbc-url`, `username`, and `password` properties are correct. Use the **JPA > Validate** menu to check for annotation errors in entity classes.

```java
<!-- persistence.xml - Correct datasource configuration -->
<persistence-unit name="myPersistenceUnit">
    <properties>
        <property name="javax.persistence.jdbc.driver" value="com.mysql.cj.jdbc.Driver"/>
        <property name="javax.persistence.jdbc.url" value="jdbc:mysql://localhost:3306/mydb"/>
        <property name="javax.persistence.jdbc.user" value="root"/>
        <property name="javax.persistence.jdbc.password" value="password"/>
    </properties>
</persistence-unit>
```

### Solution 2: Enable DDL Auto-Generation

In the JPA project properties (**Project > Properties > JPA > Connection**), enable automatic schema generation so Eclipse can validate entity mappings against the database schema at startup. Use the Hibernate console view to test queries.

```bash
# hibernate.cfg.xml - Enable schema validation
<property name="hibernate.hbm2ddl.auto">validate</property>
<property name="hibernate.show_sql">true</property>
<property name="hibernate.format_sql">true</property>
```

## Prevention Tips

- Use the **JPA Diagram Editor** to visually validate entity relationships.
- Enable SQL logging in your JPA provider configuration to debug connection issues.
- Keep the Hibernate Tools plugin updated to avoid compatibility issues with newer JPA versions.

## Related Errors

- [database-error]({{< relref "/tools/eclipse/database-error" >}})
- [build-path-error]({{< relref "/tools/eclipse/build-path-error" >}})
- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
