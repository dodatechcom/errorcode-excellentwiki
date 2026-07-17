---
title: "[Solution] BindingException — Invalid Bound Statement Fix"
description: "Fix MyBatis BindingException: Invalid bound statement when mapper XML is not found or namespace mismatches."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["mybatis", "sql", "mapper", "binding-exception", "xml"]
weight: 5
---

# BindingException — Invalid Bound Statement Fix

A `BindingException: Invalid bound statement` occurs when MyBatis cannot find the SQL statement mapped to a Java method. This usually means the mapper XML file is not loaded, the namespace is wrong, or the method name does not match.

## What This Error Means

Common message:

- `org.apache.ibatis.binding.BindingException: Invalid bound statement (not found): com.example.mapper.UserMapper.findById`

## Common Causes

```xml
<!-- Cause 1: Mapper XML not in classpath -->
<!-- resources/mapper/UserMapper.xml exists but not in the right location -->

<!-- Cause 2: Namespace mismatch in XML -->
<mapper namespace="com.example.mapper.UserMapper">
<!-- But Java interface is: com.example.dao.UserMapper -->

<!-- Cause 3: Method name mismatch -->
<select id="getUserById">
<!-- Java: User findById(Long id); -->
```

## How to Fix

### Fix 1: Configure mapper XML location

```properties
mybatis.mapper-locations=classpath*:mapper/**/*.xml
```

### Fix 2: Ensure namespace matches

```xml
<mapper namespace="com.example.mapper.UserMapper">
    <select id="findById" resultType="com.example.model.User">
        SELECT * FROM users WHERE id = #{id}
    </select>
</mapper>
```

### Fix 3: Add @Mapper annotation or scan

```java
@Mapper
public interface UserMapper {
    User findById(@Param("id") Long id);
}
```

```java
@SpringBootApplication
@MapperScan("com.example.mapper")
public class Application { }
```

## Related Errors

- {{< relref "mybatis-spring" >}} — SpringBoot MyBatis config issues
- {{< relref "mybatis-dynamic" >}} — Dynamic SQL binding errors
- {{< relref "mybatis-plus" >}} — MyBatis-Plus specific errors
