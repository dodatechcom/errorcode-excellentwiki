---
title: "[Solution] Java SqlSession Error — MyBatis session or mapper error"
description: "Fix Java SqlSession Error by checking mapper configuration, verifying SQL, and handling session lifecycle. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 114
---

# SqlSession Error — MyBatis session or mapper error

A SqlSession error in MyBatis occurs when the SQL session cannot execute a query, the mapper is not properly configured, or the session lifecycle is mismanaged. This covers mapper binding failures, SQL execution errors, and session creation issues.

## Description

MyBatis uses `SqlSession` to execute SQL statements through mapper interfaces or XML definitions. Errors occur when the session is not configured correctly, the mapper is missing, or the SQL is malformed. Common message variants include:

- `org.apache.ibatis.exceptions.PersistenceException: Error getting a new connection`
- `org.apache.ibatis.binding.BindingException: Invalid bound statement (not found)`
- `org.apache.ibatis.executor.ExecutorException: A query was run and no Query Handler was registered`
- `SqlSession was already closed`
- `Error flushing statements. Cause: org.apache.ibatis.executor.ExecutorException`

## Common Causes

```java
// Cause 1: Mapper interface not registered
@Mapper
public interface UserMapper {
    User findById(Long id);  // No corresponding XML or annotation
}

// Missing @MapperScan or @Mapper on interface
@SpringBootApplication
@MapperScan("com.example.mapper")  // This is required
public class Application {}

// Cause 2: XML mapper path not configured
mybatis:
  mapper-locations: classpath:mapper/*.xml  // Wrong path

// Cause 3: SQL session used outside transaction
@Service
public class UserService {
    private final UserMapper userMapper;

    public User getUser(Long id) {
        // No @Transactional — session may not be available
        return userMapper.findById(id);
    }
}

// Cause 4: Multiple SqlSession instances not closed
SqlSession session1 = sqlSessionFactory.openSession();
SqlSession session2 = sqlSessionFactory.openSession();
// If one fails, the other may be left open
```

## Solutions

### Fix 1: Configure mapper scanning correctly

```java
@SpringBootApplication
@MapperScan("com.example.mapper")
public class MyBatisApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyBatisApplication.class, args);
    }
}

// Or annotate each mapper with @Mapper
@Mapper
public interface UserMapper {
    User findById(@Param("id") Long id);
    List<User> findAll();
    int insert(@Param("user") User user);
    int update(@Param("user") User user);
    int deleteById(@Param("id") Long id);
}
```

### Fix 2: Set up XML mapper correctly

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.mapper.UserMapper">

    <resultMap id="UserResultMap" type="com.example.model.User">
        <id property="id" column="id"/>
        <result property="name" column="user_name"/>
        <result property="email" column="email"/>
    </resultMap>

    <select id="findById" resultMap="UserResultMap">
        SELECT id, user_name, email
        FROM users
        WHERE id = #{id}
    </select>

    <insert id="insert" useGeneratedKeys="true" keyProperty="user.id">
        INSERT INTO users (user_name, email)
        VALUES (#{user.name}, #{user.email})
    </insert>

</mapper>
```

### Fix 3: Add @Transactional to service methods

```java
@Service
public class UserService {

    private final UserMapper userMapper;

    public UserService(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    @Transactional(readOnly = true)
    public User findById(Long id) {
        return userMapper.findById(id);
    }

    @Transactional
    public int insert(User user) {
        return userMapper.insert(user);
    }

    @Transactional
    public int update(User user) {
        return userMapper.update(user);
    }
}
```

### Fix 4: Configure MyBatis in application.yml

```yaml
mybatis:
  mapper-locations: classpath:mapper/**/*.xml
  type-aliases-package: com.example.model
  configuration:
    map-underscore-to-camel-case: true
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
    default-statement-timeout: 30

spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: postgres
    password: secret
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
```

### Fix 5: Use SqlSessionFactory correctly

```java
@Configuration
public class MyBatisConfig {

    @Bean
    public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception {
        SqlSessionFactoryBean factory = new SqlSessionFactoryBean();
        factory.setDataSource(dataSource);
        factory.setMapperLocations(
            new PathMatchingResourcePatternResolver()
                .getResources("classpath:mapper/**/*.xml"));
        factory.setTypeAliasesPackage("com.example.model");

        org.apache.ibatis.session.Configuration config = new org.apache.ibatis.session.Configuration();
        config.setMapUnderscoreToCamelCase(true);
        factory.setConfiguration(config);

        return factory.getObject();
    }
}
```

## Prevention Checklist

- Annotate mapper interfaces with `@Mapper` or use `@MapperScan` on a configuration class
- Ensure XML mapper files are in `mapper-locations` path and have correct `namespace`
- Add `@Transactional` to service methods that use mappers
- Configure `map-underscore-to-camel-case` for automatic column-to-field mapping
- Verify mapper method names and parameter types match XML SQL statements
- Test mapper queries independently to isolate SQL issues

## Related Errors

- [MyBatis Mapping Error](/languages/java/mybatis-mapping-error/)
- [MyBatis BindingError](/languages/java/mybatis-binding-error/)
- [MyBatis SpringError](/languages/java/mybatis-spring/)
