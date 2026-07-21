---
title: "[Solution] Spring Jackson Serialization Error"
description: "Fix Spring Jackson serialization errors when JSON responses fail to serialize or deserialize objects."
frameworks: ["spring"]
error-types: ["serialization-error"]
severities: ["error"]
---

Jackson errors occur when objects contain fields that cannot be serialized, have circular references, or use unsupported data types.

## Common Causes

- Circular references between objects
- Custom types not registered with Jackson
- `@JsonIgnore` missing on sensitive fields
- Date format not configured
- Null values not handled properly

## How to Fix

### Configure Jackson ObjectMapper

```java
@Configuration
public class JacksonConfig {
    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());
        mapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);
        mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
        return mapper;
    }
}
```

### Handle Circular References

```java
@Entity
public class User {
    @OneToMany(mappedBy = "user")
    @JsonManagedReference
    private List<Post> posts;
}

@Entity
public class Post {
    @ManyToOne
    @JsonBackReference
    private User user;
}
```

### Use DTOs to Avoid Issues

```java
public class UserResponse {
    private Long id;
    private String name;
    private String email;

    public static UserResponse fromEntity(User user) {
        UserResponse response = new UserResponse();
        response.id = user.getId();
        response.name = user.getName();
        response.email = user.getEmail();
        return response;
    }
}
```

### Configure Date Format

```java
@Configuration
public class JacksonConfig {
    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.setDateFormat(new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"));
        mapper.registerModule(new JavaTimeModule());
        return mapper;
    }
}
```

## Examples

```java
// Bug -- circular reference
@Entity
public class User {
    @OneToMany(mappedBy = "user")
    private List<Post> posts;  // Infinite loop
}

// Fix -- use DTO
public class UserDto {
    private Long id;
    private String name;

    public static UserDto from(User user) {
        UserDto dto = new UserDto();
        dto.id = user.getId();
        dto.name = user.getName();
        return dto;
    }
}
```
