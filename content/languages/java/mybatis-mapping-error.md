---
title: "[Solution] Java MyBatis mapping error — result mapping or column mismatch"
description: "Fix Java MyBatis mapping error by checking XML mapper, verifying resultType, and handling column mappings. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 115
---

# MyBatis mapping error — result mapping or column mismatch

A MyBatis mapping error occurs when the result mapping between SQL columns and Java object properties fails. This includes missing `resultMap` definitions, incorrect `resultType` references, and column name mismatches.

## Description

MyBatis maps SQL result set columns to Java object fields through `resultMap` or automatic column-to-property mapping. When the mapping configuration is incorrect or incomplete, properties are left null or exceptions are thrown. Common message variants include:

- `Unknown column 'X' in result list`
- `Could not find result map 'X'`
- `Error setting property 'X' of 'Y' with value 'Z'`
- `No suitable driver for column type X`
- `SqlSessionTemplate$SqlSessionInterceptor.invoke: Error querying database`

## Common Causes

```xml
<!-- Cause 1: Missing resultMap for complex queries -->
<mapper namespace="com.example.mapper.UserMapper">
    <select id="findByIdWithOrders" resultType="com.example.model.User">
        SELECT u.id, u.name, o.id as order_id, o.total
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        WHERE u.id = #{id}
        <!-- No resultMap defined for nested collections -->
    </select>
</mapper>
```

```java
// Cause 2: resultType points to wrong class
@Select("SELECT id, name FROM users WHERE id = #{id}")
@Results(id = "userMap", value = {
    @Result(property = "id", column = "id"),
    @Result(property = "name", column = "name")
})
User findById(@Param("id") Long id);  // User class has fields: id, name, email

// Cause 3: Column name doesn't match Java property
// SQL returns: user_name
// Java field: username (not userName)
```

## Solutions

### Fix 1: Define proper resultMap

```xml
<mapper namespace="com.example.mapper.UserMapper">

    <resultMap id="UserResultMap" type="com.example.model.User">
        <id property="id" column="id"/>
        <result property="name" column="user_name"/>
        <result property="email" column="email"/>
        <result property="createdAt" column="created_at"/>
    </resultMap>

    <resultMap id="UserWithOrdersResultMap" type="com.example.model.User" extends="UserResultMap">
        <collection property="orders" ofType="com.example.model.Order">
            <id property="id" column="order_id"/>
            <result property="total" column="order_total"/>
            <result property="createdAt" column="order_created_at"/>
        </collection>
    </resultMap>

    <select id="findById" resultMap="UserResultMap">
        SELECT id, user_name, email, created_at
        FROM users
        WHERE id = #{id}
    </select>

    <select id="findByIdWithOrders" resultMap="UserWithOrdersResultMap">
        SELECT u.id, u.user_name, u.email, u.created_at,
               o.id as order_id, o.total as order_total, o.created_at as order_created_at
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        WHERE u.id = #{id}
    </select>
</mapper>
```

### Fix 2: Use column aliases for matching

```xml
<mapper namespace="com.example.mapper.UserMapper">

    <select id="findAll" resultType="com.example.model.User">
        SELECT
            id,
            user_name AS name,
            email_address AS email,
            created_date AS createdAt
        FROM users
    </select>

    <!-- Or use resultMap with explicit mappings -->
    <resultMap id="UserMap" type="com.example.model.User">
        <id property="id" column="id"/>
        <result property="name" column="user_name"/>
        <result property="email" column="email_address"/>
        <result property="createdAt" column="created_date"/>
    </resultMap>
</mapper>
```

### Fix 3: Use annotation-based mapping

```java
@Mapper
public interface UserMapper {

    @Select("SELECT id, user_name, email FROM users WHERE id = #{id}")
    @Results(id = "userResultMap", value = {
        @Result(property = "id", column = "id"),
        @Result(property = "name", column = "user_name"),
        @Result(property = "email", column = "email")
    })
    User findById(@Param("id") Long id);

    @Select("SELECT * FROM users")
    @ResultMap("userResultMap")  // Reuse the resultMap defined above
    List<User> findAll();

    @Select("SELECT u.id, u.user_name, COUNT(o.id) as order_count " +
            "FROM users u LEFT JOIN orders o ON u.id = o.user_id " +
            "GROUP BY u.id, u.user_name")
    @Results(id = "userWithCountMap", value = {
        @Result(property = "id", column = "id"),
        @Result(property = "name", column = "user_name"),
        @Result(property = "orderCount", column = "order_count")
    })
    List<UserSummary> findUserOrderCounts();
}
```

### Fix 4: Handle type conversions with TypeHandler

```java
public class JsonTypeHandler extends BaseTypeHandler<List<String>> {

    private static final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i,
                                     List<String> parameter, JdbcType jdbcType)
            throws SQLException {
        try {
            ps.setString(i, objectMapper.writeValueAsString(parameter));
        } catch (JsonProcessingException e) {
            throw new SQLException("Failed to serialize list", e);
        }
    }

    @Override
    public List<String> getNullableResult(ResultSet rs, String columnName)
            throws SQLException {
        String json = rs.getString(columnName);
        if (json == null) return Collections.emptyList();
        try {
            return objectMapper.readValue(json, new TypeReference<List<String>>() {});
        } catch (JsonProcessingException e) {
            throw new SQLException("Failed to deserialize list", e);
        }
    }

    // Implement other getNullableResult overloads similarly
}
```

```xml
<resultMap id="ProductResultMap" type="com.example.model.Product">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="tags" column="tags"
            typeHandler="com.example.handler.JsonTypeHandler"/>
</resultMap>
```

### Fix 5: Enable camelCase auto-mapping

```yaml
mybatis:
  configuration:
    map-underscore-to-camel-case: true
    auto-mapping-behavior: full  # Automatically maps all columns
```

```xml
<!-- With auto-mapping enabled, columns map to matching Java properties automatically -->
<mapper namespace="com.example.mapper.UserMapper">
    <select id="findById" resultType="com.example.model.User">
        SELECT id, user_name, email_address, created_at
        FROM users
        WHERE id = #{id}
        <!-- user_name -> userName, email_address -> emailAddress, etc. -->
    </select>
</mapper>
```

## Prevention Checklist

- Define `resultMap` for complex queries with multiple tables or nested objects
- Use column aliases (`AS`) to match Java property names in simple queries
- Enable `map-underscore-to-camel-case` for automatic snake_case to camelCase conversion
- Implement custom `TypeHandler` for non-standard types (JSON, enums, arrays)
- Test queries with realistic data to catch null mappings early
- Use `@Results` / `@ResultMap` annotations for annotation-based mappers

## Related Errors

- [MyBatis SqlSession Error](/languages/java/mybatis-sql-session-error/)
- [MyBatis BindingError](/languages/java/mybatis-binding-error/)
- [MyBatis DynamicError](/languages/java/mybatis-dynamic-error/)
