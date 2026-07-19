---
title: "[Solution] Hibernate LazyInitializationException — Collection Not Initialized"
description: "Fix org.hibernate.LazyInitializationException could not initialize proxy. Initialize Hibernate collections properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# LazyInitializationException — Could Not Initialize Proxy (Collection)

A `LazyInitializationException` with message `could not initialize proxy - no Session` occurs when code tries to access a lazily loaded collection that has not been initialized, outside the Hibernate Session that loaded the owning entity.

## What This Error Means

Hibernate lazily loads collections to avoid loading unnecessary data. A lazy collection is represented by a proxy that requires an open Session to fetch data. Once the Session is closed, accessing the uninitialized collection fails because Hibernate has no connection to the database.

## Common Causes

```java
// Cause 1: Accessing lazy collection in DTO/converter
@Entity
public class Department {
    @OneToMany(fetch = FetchType.LAZY, mappedBy = "department")
    private List<Employee> employees;
}

// In service — Session closes after transaction
@Transactional
public Department getDepartment(Long id) {
    return departmentRepository.findById(id).orElseThrow();
    // Session closes here
}

// In controller — accessing lazy collection
@GetMapping("/departments/{id}/employees")
public List<Employee> getEmployees(@PathVariable Long id) {
    Department dept = departmentService.getDepartment(id);
    return dept.getEmployees();  // LazyInitializationException!
}

// Cause 2: Jackson serialization triggering lazy load
@RestController
public class DepartmentController {
    @GetMapping("/departments/{id}")
    public Department getDepartment(@PathVariable Long id) {
        return departmentRepository.findById(id).orElseThrow();
        // Jackson tries to serialize employees — triggers lazy load
    }
}
```

## How to Fix

### Fix 1: Use JOIN FETCH in query

```java
@Query("SELECT d FROM Department d JOIN FETCH d.employees WHERE d.id = :id")
Department findByIdWithEmployees(@Param("id") Long id);
```

### Fix 2: Use @EntityGraph for specific fetch plans

```java
@EntityGraph(attributePaths = {"employees", "employees.skills"})
@Query("SELECT d FROM Department d WHERE d.id = :id")
Department findByIdWithDetails(@Param("id") Long id);
```

### Fix 3: Initialize collection within transaction

```java
@Service
public class DepartmentService {
    @Transactional
    public Department getDepartmentWithEmployees(Long id) {
        Department dept = departmentRepository.findById(id).orElseThrow();
        Hibernate.initialize(dept.getEmployees());  // Forces initialization
        return dept;
    }
}
```

### Fix 4: Use @BatchSize to prevent N+1 without full join

```java
@Entity
public class Department {
    @OneToMany(fetch = FetchType.LAZY, mappedBy = "department")
    @BatchSize(size = 20)
    private List<Employee> employees;
}
```

### Fix 5: Disable lazy loading in serialization (Jackson)

```java
@Entity
public class Department {
    @OneToMany(fetch = FetchType.LAZY, mappedBy = "department")
    @JsonIgnore
    private List<Employee> employees;  // Won't trigger lazy load during serialization
}
```

## Prevention Tips

- Use `JOIN FETCH` or `@EntityGraph` for all queries that need related collections.
- Disable Jackson lazy loading with `@JsonIgnore` or `spring.jackson.serialization.fail-on-empty-beans=false`.
- Keep transactions open until all lazy data is accessed (Open Session in View pattern with caution).
- Consider `@EntityGraph` as the preferred approach over `JOIN FETCH` for complex fetch plans.

## Related Errors

- {{< relref "hibernate-lazy" >}} — LazyInitializationException general
- {{< relref "hibernate-proxy-init" >}} — Proxy initialization failed
- {{< relref "hibernate-unknown-entity" >}} — Unknown entity mapping
