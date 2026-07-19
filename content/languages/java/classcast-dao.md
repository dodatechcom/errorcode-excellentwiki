---
title: "[Solution] Java ClassCastException — casting between DAO types or JPA EntityManager types"
description: "Fix Java ClassCastException when casting between dao types or jpa entitymanager types with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassCastException — casting between DAO types or JPA EntityManager types

A `ClassCastException` occurs when EntityManager em = emf.createEntityManager();
Session s = (Session) em;  // ClassCastException if not Hibernate.

## Common Causes

```java
EntityManager em = emf.createEntityManager();
Session s = (Session) em;  // ClassCastException if not Hibernate
```

## Solutions

```java
// Fix: use unwrap
Session s = em.unwrap(Session.class);

// Fix: instanceof check
if (em instanceof HibernateEntityManager hem) { Session s = hem.getSession(); }
```

## Prevention Checklist

- Use JPA unwrap() instead of casting.
- Define repos with specific entity types.
- Test type compatibility.

## Related Errors

ClassCastException, PersistenceException
