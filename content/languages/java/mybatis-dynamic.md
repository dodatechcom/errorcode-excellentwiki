---
title: "[Solution] BindingException Dynamic SQL — MyBatis Dynamic SQL Fix"
description: "Fix MyBatis BindingException with dynamic SQL. Check XML mapper configuration and dynamic SQL tags."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# BindingException Dynamic SQL — MyBatis Dynamic SQL Fix

A `BindingException` with dynamic SQL occurs when MyBatis cannot find the SQL statement in XML mappers that use dynamic SQL tags like `<if>`, `<choose>`, `<where>`, and `<foreach>`.

## What This Error Means

Common message:

- `Invalid bound statement (not found): com.example.mapper.UserMapper.findUsers`

## Common Causes

```xml
<!-- Cause 1: Wrong tag nesting -->
<mapper namespace="com.example.mapper.UserMapper">
    <select id="findUsers" resultType="User">
        SELECT * FROM users
        <where>
            <if test="name != null">
                AND name = #{name}
            </if>
            <!-- Missing closing </where> -->
```

```xml
<!-- Cause 2: Incorrect test expression -->
<if test="name != null">
    AND name = #{name}
</if>
<!-- Wrong: test="name != 'null'" or test="name == null" -->
```

```xml
<!-- Cause 3: foreach collection name mismatch -->
<select id="findByIds" resultType="User">
    SELECT * FROM users WHERE id IN
    <foreach collection="ids" item="id" open="(" close=")" separator=",">
        #{id}
    </foreach>
</select>
<!-- Wrong: collection="list" when using @Param("ids") -->
```

## How to Fix

### Fix 1: Use correct dynamic SQL tags

```xml
<mapper namespace="com.example.mapper.UserMapper">
    <select id="findUsers" resultType="com.example.model.User">
        SELECT * FROM users
        <where>
            <if test="name != null and name != ''">
                AND name = #{name}
            </if>
            <if test="email != null and email != ''">
                AND email = #{email}
            </if>
        </where>
    </select>
</mapper>
```

### Fix 2: Match collection parameter names

```java
public interface UserMapper {
    List<User> findByIds(@Param("ids") List<Long> ids);
}
```

```xml
<select id="findByIds" resultType="com.example.model.User">
    SELECT * FROM users WHERE id IN
    <foreach collection="ids" item="id" open="(" close=")" separator=",">
        #{id}
    </foreach>
</select>
```

## Related Errors

- {{< relref "mybatis" >}} — BindingException: Invalid bound statement
- {{< relref "mybatis-spring" >}} — SpringBoot MyBatis config
- {{< relref "mybatis-plus" >}} — MyBatis-Plus errors
