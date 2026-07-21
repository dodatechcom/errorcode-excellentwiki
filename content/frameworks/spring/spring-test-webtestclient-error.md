---
title: "[Solution] Spring WebTestClient Error"
description: "Fix Spring WebTestClient errors when integration tests fail to connect or return unexpected responses."
frameworks: ["spring"]
error-types: ["test-error"]
severities: ["error"]
---

WebTestClient errors occur when the test client is not properly configured, cannot connect to the server, or assertions fail.

## Common Causes

- Test server not started
- WebTestClient not configured with correct base URL
- MockMvc not properly integrated
- Request body not properly serialized
- Response assertions do not match actual response

## How to Fix

### Configure WebTestClient for Integration Tests

```java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class UserControllerTest {
    @Autowired
    private WebTestClient webTestClient;

    @Test
    void testGetUser() {
        webTestClient.get()
            .uri("/api/users/{id}", 1)
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus().isOk()
            .expectBody()
            .jsonPath("$.name").isEqualTo("Alice");
    }
}
```

### Use MockMvc for Unit Tests

```java
@WebMvcTest(UserController.class)
class UserControllerMockTest {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void testGetUser() throws Exception {
        when(userService.getUser(1L)).thenReturn(new User(1L, "Alice"));

        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.name").value("Alice"));
    }
}
```

### Test POST Requests

```java
@Test
void testCreateUser() {
    CreateUserRequest request = new CreateUserRequest("Alice", "alice@example.com");

    webTestClient.post()
        .uri("/api/users")
        .contentType(MediaType.APPLICATION_JSON)
        .bodyValue(request)
        .exchange()
        .expectStatus().isCreated()
        .expectBody()
        .jsonPath("$.name").isEqualTo("Alice");
}
```

## Examples

```java
// Bug -- no @SpringBootTest
class UserControllerTest {
    @Autowired
    private WebTestClient webTestClient;  // NullPointerException

}

// Fix -- add annotation
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class UserControllerTest {
    @Autowired
    private WebTestClient webTestClient;  // Works

    @Test
    void test() {
        webTestClient.get().uri("/api/health").exchange()
            .expectStatus().isOk();
    }
}
```
