---
title: "[Solution] MyBatis Dynamic SQL Error Fix"
description: "Fix MyBatis dynamic SQL errors. Resolve malformed XML tags, null parameter issues, and foreach collection errors."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["mybatis", "dynamic-sql", "xml", "foreach", "sql"]
weight: 5
---

# MyBatis Dynamic SQL Error Fix

A MyBatis dynamic SQL error occurs when XML-based dynamic SQL tags are malformed, reference non-existent parameters, or have incorrect collection bindings.

## What This Error Means

Common messages:

- `ExecutorException: Dynamic SQL error: <foreach> property not found`
- `BindingException: Parameter 'list' not found. Available parameters are [collection, list]`
- `SQLSyntaxErrorException: ... near 'AND'` (empty dynamic SQL generates bad SQL)

MyBatis processes `<if>`, `<foreach>`, `<choose>`, `<where>`, and `<set>` tags at runtime. Errors occur when the XML is malformed or parameter names do not match the mapper method signature.

## Common Causes

```xml
<!-- Cause 1: Wrong collection name in foreach -->
<select id="findByIds" resultType="User">
    SELECT * FROM users WHERE id IN
    <foreach item="id" collection="ids" open="(" separator="," close=")">
        #{id}
    </foreach>
</select>
<!-- Java: List<User> findByIds(List<Long> ids);  // 'ids' is the param name -->

<!-- Cause 2: Empty list causes SQL syntax error -->
<!-- If ids is empty: SELECT * FROM users WHERE id IN () — invalid SQL -->

<!-- Cause 3: Missing property in if test -->
<if test="name != null AND name != ''">
    AND name = #{name}
</if>
<!-- Should be: name != null and name != '' -->
```

## How to Fix

### Fix 1: Match collection name to parameter name

```xml
<select id="findByIds" resultType="com.example.entity.User">
    SELECT * FROM users WHERE id IN
    <foreach item="id" collection="ids" open="(" separator="," close=")">
        #{id}
    </foreach>
</select>
```

```java
@Mapper
public interface UserMapper {
    List<User> findByIds(@Param("ids") List<Long> ids);
}
```

### Fix 2: Add empty collection guard

```xml
<select id="findByIds" resultType="com.example.entity.User">
    SELECT * FROM users
    <where>
        <if test="ids != null and ids.size() > 0">
            id IN
            <foreach item="id" collection="ids" open="(" separator="," close=")">
                #{id}
            </foreach>
        </if>
    </where>
</select>
```

### Fix 3: Use proper boolean test expressions

```xml
<!-- Wrong -->
<if test="status != null AND active == true">

<!-- Correct -->
<if test="status != null and active == true">

<!-- Or use OGNL syntax -->
<if test="status != null and active">
```

### Fix 4: Handle null parameters with default values

```xml
<where>
    <if test="name != null and name != ''">
        AND name = #{name}
    </if>
    <if test="status != null">
        AND status = #{status}
    </if>
    <if test="offset != null">
        LIMIT #{limit} OFFSET #{offset}
    </if>
</where>
```

### Fix 5: Use choose/when/otherwise for conditional SQL

```xml
<select id="findUsers" resultType="User">
    SELECT * FROM users
    <where>
        <choose>
            <when test="email != null">
                AND email = #{email}
            </when>
            <when test="name != null">
                AND name LIKE CONCAT('%', #{name}, '%')
            </when>
            <otherwise>
                AND active = true
            </otherwise>
        </choose>
    </where>
</select>
```

## Related Errors

- {{< relref "mybatis" >}} — MyBatis general configuration error.
- {{< relref "mybatis-spring" >}} — MyBatis Spring integration error.
