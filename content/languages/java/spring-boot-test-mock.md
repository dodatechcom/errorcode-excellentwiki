---
title: "[Solution] NoSuchBeanDefinitionException — Spring Boot @MockBean Fix"
description: "Fix NoSuchBeanDefinitionException when @MockBean is not working in Spring Boot tests. Resolve mock bean injection failures."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# NoSuchBeanDefinitionException — Spring Boot @MockBean Fix

A `NoSuchBeanDefinitionException` in a test context with `@MockBean` means Spring could not inject the mocked bean into the class under test. This happens when the mock is declared in the wrong test class or when the test context is not correctly configured.

## What This Error Means

Common messages:

- `NoSuchBeanDefinitionException: No qualifying bean of type 'UserService' available`
- `NoSuchBeanDefinitionException: No qualifying bean of type 'UserRepository' expected at least 1 bean`
- `Unsatisfied dependency through field 'userService'`

## Common Causes

```java
// Cause 1: @MockBean in a different test class
// TestClassA has @MockBean UserRepository
// TestClassB tries to inject UserRepository without @MockBean

// Cause 2: Wrong import — using Mockito @Mock instead of @MockBean
import org.mockito.Mock; // Wrong! Should be:
// import org.springframework.boot.test.mock.bean.MockBean;

// Cause 3: Test sliced — @WebMvcTest excludes repository layer
@WebMvcTest(UserController.class) // Only loads controller layer
public class UserControllerTest {
    @Autowired
    private UserRepository userRepository; // Not loaded by slice!
}
```

## How to Fix

### Fix 1: Use @MockBean in the correct test class

Declare @MockBean on the same test class that needs the mock, or in a @TestConfiguration that is imported.

```java
@SpringBootTest
class UserServiceTest {

    @MockBean
    private UserRepository userRepository; // Correct!

    @Autowired
    private UserService userService;

    @Test
    void shouldFindUserById() {
        User user = new User(1L, "Alice");
        when(userRepository.findById(1L))
            .thenReturn(Optional.of(user));

        User result = userService.findById(1L);
        assertEquals("Alice", result.getName());
        verify(userRepository).findById(1L);
    }
}
```

### Fix 2: Use @TestConfiguration for shared mock setup

Create a shared test configuration class with @MockBean declarations that can be imported by multiple test classes.

```java
@TestConfiguration
public class MockConfig {

    @MockBean
    public UserRepository userRepository;

    @MockBean
    public EmailService emailService;
}

@SpringBootTest
@Import(MockConfig.class)
class OrderServiceTest {

    @Autowired
    private OrderService orderService;

    @MockBean
    private PaymentGateway paymentGateway; // Additional mock specific to this test
}
```

### Fix 3: Use @WebMvcTest with explicit mock setup

For controller tests, use @WebMvcTest with @MockBean to mock service dependencies while testing the controller layer.

```java
@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void shouldReturnUser() throws Exception {
        User user = new User(1L, "Alice");
        when(userService.findById(1L)).thenReturn(user);

        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.name").value("Alice"));
    }
}
```

## Related Errors

- {{< relref "mockito" >}} — Mockito Misuse Errors
- {{< relref "junit5" >}} — JUnit Platform Launcher Error
