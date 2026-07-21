---
title: "[Solution] Spring Test Context or Mock Error -- How to Fix"
description: "Fix Spring test errors. Resolve test context, mock configuration, and test slicing issues in Spring."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring test context or mock error occurs when the Spring test context fails to load, when mocks are not properly configured, or when test slices don't include the necessary components. Testing in Spring requires careful context management.

## Why It Happens

Spring tests create an application context that is cached between tests. Errors occur when test configurations conflict, when `@MockBean` replaces beans that other tests depend on, when test profiles don't match expected configurations, when `@DataJpaTest` doesn't include required services, or when test context IDs collide.

## Common Error Messages

```
org.springframework.test.context.TestContextLoaderNotFoundException
```

```
org.springframework.beans.factory.NoSuchBeanDefinitionException: No qualifying bean
```

```
org.springframework.context.ApplicationContextException: Failed to load ApplicationContext
```

```
java.lang.IllegalStateException: Cached ApplicationContext has been closed
```

## How to Fix It

### 1. Use Correct Test Slices

Choose the right test annotation:

```java
// Unit test -- only loads controllers, skips services/repos
@WebMvcTest(UserController.class)
class UserControllerTest {

    @MockBean
    private UserService userService;  // Mock the service

    @Autowired
    private MockMvc mockMvc;

    @Test
    void shouldReturnUser() throws Exception {
        when(userService.findById(1L)).thenReturn(Optional.of(new User("test@example.com")));

        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.email").value("test@example.com"));
    }
}

// Repository test -- loads repos, uses embedded DB
@DataJpaTest
class UserRepositoryTest {

    @Autowired
    private TestEntityManager entityManager;

    @Autowired
    private UserRepository userRepository;

    @Test
    void shouldFindByEmail() {
        User user = new User("test@example.com", "Test User");
        entityManager.persistAndFlush(user);

        Optional<User> found = userRepository.findByEmail("test@example.com");
        assertThat(found).isPresent();
        assertThat(found.get().getName()).isEqualTo("Test User");
    }
}

// Full integration test
@SpringBootTest
class UserServiceIntegrationTest {

    @Autowired
    private UserService userService;

    @Test
    void shouldCreateUser() {
        User user = userService.createUser(new User("test@example.com"));
        assertThat(user.getId()).isNotNull();
    }
}
```

### 2. Configure Mocks Properly

Use `@MockBean` and `@SpyBean` correctly:

```java
@SpringBootTest
class OrderServiceTest {

    @MockBean
    private PaymentGateway paymentGateway;  // Replaces the real bean

    @SpyBean
    private EmailService emailService;  // Wraps the real bean

    @Autowired
    private OrderService orderService;

    @Test
    void shouldCreateOrder() {
        when(paymentGateway.charge(any())).thenReturn(PaymentResult.success());

        Order order = orderService.createOrder(new CreateOrderRequest());

        assertThat(order.getStatus()).isEqualTo(OrderStatus.CONFIRMED);
        verify(paymentGateway).charge(any());
        verify(emailService).sendConfirmation(any());  // Real method called
    }
}
```

### 3. Isolate Test Contexts

Prevent context pollution between tests:

```java
// Use different context configuration IDs
@SpringBootTest(classes = {TestConfig1.class})
@ActiveProfiles("test")
class FirstTest { }

@SpringBootTest(classes = {TestConfig2.class})
@ActiveProfiles("test")
class SecondTest { }

// Or use @TestConfiguration for test-specific beans
@SpringBootTest
@TestConfiguration
class TestConfig {
    @Bean
    @Primary
    public ExternalService mockExternalService() {
        return mock(ExternalService.class);
    }
}
```

### 4. Test REST Controllers with MockMvc

Test controllers without starting the full server:

```java
@WebMvcTest(UserController.class)
class UserControllerMockMvcTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void shouldCreateUser() throws Exception {
        when(userService.create(any())).thenReturn(new User(1L, "test@example.com"));

        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"email\":\"test@example.com\",\"name\":\"Test\"}"))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.id").value(1));
    }

    @Test
    void shouldReturn404WhenUserNotFound() throws Exception {
        when(userService.findById(999L)).thenReturn(Optional.empty());

        mockMvc.perform(get("/api/users/999"))
            .andExpect(status().isNotFound());
    }
}
```

## Common Scenarios

**Scenario 1: `@WebMvcTest` doesn't load my service.**
`@WebMvcTest` only loads web-layer components. Use `@MockBean` for services or use `@SpringBootTest` for full context.

**Scenario 2: Test context conflicts between test classes.**
Different `@SpringBootTest` classes may create conflicting contexts. Use `@ContextConfiguration` to share contexts or `@TestConfiguration` for test-specific beans.

**Scenario 3: Database not reset between tests.**
Use `@Transactional` on test methods to automatically rollback after each test, or use `@DirtiesContext` to force context reload.

## Prevent It

1. **Use test slices** (`@WebMvcTest`, `@DataJpaTest`) instead of `@SpringBootTest` when possible for faster tests.

2. **Use `@MockBean` only when necessary.** Prefer constructor injection and manual mocking for better test isolation.

3. **Run tests with `--info` flag** to see context loading details when tests fail mysteriously.
