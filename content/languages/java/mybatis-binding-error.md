---
title: "[Solution] MyBatis Invalid Bound Statement Fix"
description: "Fix MyBatis invalid bound statement not found. Verify mapper XML namespace, statement IDs, and SqlSession configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# MyBatis Invalid Bound Statement Fix

An `InvalidBindingException: Invalid bound statement (not found)` is thrown when MyBatis cannot find the SQL statement mapped to a mapper method call.

## What This Error Means

Common messages:

- `org.apache.ibatis.binding.InvalidBindingException: Invalid bound statement (not found): com.example.mapper.UserMapper.findById`
- `BindingException: Invalid bound statement (not found)`

MyBatis looked up the SQL statement by its mapper interface's fully qualified name and method name but found no matching XML statement or annotation.

## Common Causes

```java
// Cause 1: XML mapper file not loaded
// UserMapper.xml exists but not on classpath or not scanned

// Cause 2: Namespace mismatch
// XML: <mapper namespace="com.example.mapper.UserMapper">
// Java: public interface UserMapper { ... }
// If package path differs, binding fails

// Cause 3: Statement ID typo
// XML: <select id="findUserById">
// Java: List<User> findById(Long id);  // Method name differs from XML id

// Cause 4: Mapper XML not registered with Spring
// Missing @MapperScan or @Mapper annotation
```

## How to Fix

### Fix 1: Ensure mapper XML is on classpath

```xml
<!-- src/main/resources/mapper/UserMapper.xml -->
<mapper namespace="com.example.mapper.UserMapper">
    <select id="findById" resultType="com.example.entity.User">
        SELECT * FROM users WHERE id = #{id}
    </select>
</mapper>
```

```yaml
# application.yml
mybatis:
  mapper-locations: classpath:mapper/*.xml
```

### Fix 2: Match namespace and method names exactly

```xml
<!-- Namespace must match fully qualified interface name -->
<mapper namespace="com.example.mapper.UserMapper">
    <!-- Statement ID must match method name in interface -->
    <select id="findById" resultType="com.example.entity.User">
        SELECT * FROM users WHERE id = #{id}
    </select>
</mapper>
```

### Fix 3: Configure mapper scanning

```java
@SpringBootApplication
@MapperScan("com.example.mapper")
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Fix 4: Use annotations as alternative

```java
@Mapper
public interface UserMapper {
    @Select("SELECT * FROM users WHERE id = #{id}")
    User findById(@Param("id") Long id);
}
```

### Fix 5: Verify mapper-locations path

```yaml
# Correct
mybatis:
  mapper-locations: classpath*:mapper/**/*.xml

# Also correct
mybatis:
  mapper-locations: classpath:mapper/*.xml
```

## Related Errors

- {{< relref "mybatis" >}} — General MyBatis configuration error.
- {{< relref "mybatis-dynamic" >}} — MyBatis dynamic SQL error.
