---
title: "[Solution] SpringBoot MyBatis Configuration Fix — Mapper Config Fix"
description: "Fix Spring Boot MyBatis configuration issues. Configure mapper scanning, XML locations, and type aliases properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["mybatis", "spring-boot", "configuration", "mapper", "auto-configuration"]
weight: 5
---

# SpringBoot MyBatis Configuration Fix — Mapper Config Fix

MyBatis Spring Boot configuration issues occur when the auto-configuration cannot properly set up MyBatis mappers, SQL sessions, or data sources. This can prevent the application from starting.

## What This Error Means

Common messages:

- `No qualifying bean of type 'SqlSessionFactory'`
- `Property 'mapperLocations' was specified but matching resources are not found`
- `Consider defining a bean of type 'UserMapper' in your configuration`

## Common Causes

```properties
# Cause 1: Wrong mapper-locations path
mybatis.mapper-locations=classpath:mapper/*.xml
# But XML files are in resources/mybatis/mapper/
```

## How to Fix

### Fix 1: Configure mybatis in application.yml

```yaml
mybatis:
  mapper-locations: classpath*:mapper/**/*.xml
  type-aliases-package: com.example.model
  configuration:
    map-underscore-to-camel-case: true
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
```

### Fix 2: Add @MapperScan

```java
@SpringBootApplication
@MapperScan("com.example.mapper")
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Fix 3: Configure SqlSessionFactory manually

```java
@Configuration
@MapperScan("com.example.mapper")
public class MyBatisConfig {

    @Bean
    public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception {
        SqlSessionFactoryBean factory = new SqlSessionFactoryBean();
        factory.setDataSource(dataSource);
        factory.setMapperLocations(
            new PathMatchingResourcePatternResolver()
                .getResources("classpath*:mapper/**/*.xml"));
        return factory.getObject();
    }
}
```

## Related Errors

- {{< relref "mybatis" >}} — BindingException: Invalid bound statement
- {{< relref "mybatis-dynamic" >}} — Dynamic SQL binding errors
- {{< relref "spring-bean" >}} — NoSuchBeanDefinitionException
