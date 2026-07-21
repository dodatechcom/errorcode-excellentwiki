---
title: "[Solution] Spring MockMvc Error"
description: "Fix Spring MockMvc errors when integration tests fail to simulate HTTP requests correctly."
frameworks: ["spring"]
error-types: ["test-error"]
severities: ["error"]
---

MockMvc errors occur when the test server is not properly initialized, security is not configured for tests, or request builders are incorrect.

## Common Causes

- `@WebMvcTest` missing controller class argument
- Security not configured for test context
- `@MockBean` not provided for dependencies
- Request content type not specified
- Response body not properly parsed

## How to Fix

### Configure MockMvc

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void testGetUser() throws Exception {
        when(userService.getUser(1L)).thenReturn(new User(1L, "Alice"));

        mockMvc.perform(get("/api/users/1")
                .accept(MediaType.APPLICATION_JSON))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.name").value("Alice"));
    }
}
```

### Test POST Requests

```java
@Test
void testCreateUser() throws Exception {
    CreateUserRequest request = new CreateUserRequest("Alice", "alice@example.com");
    User created = new User(1L, "Alice", "alice@example.com");
    when(userService.createUser(any())).thenReturn(created);

    mockMvc.perform(post("/api/users")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
        .andExpect(status().isCreated())
        .andExpect(jsonPath("$.name").value("Alice"));
}
```

### Handle Security in Tests

```java
@WebMvcTest(UserController.class)
@AutoConfigureMockMvc(addFilters = false)  // Disable security filters
class UserControllerTest {
    // Tests run without security
}
```

## Examples

```java
// Bug -- missing controller class
@WebMvcTest  // Loads all controllers
class Test {
    @Autowired
    private MockMvc mockMvc;
}

// Fix -- specify controller
@WebMvcTest(UserController.class)
class Test {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;
}
```
