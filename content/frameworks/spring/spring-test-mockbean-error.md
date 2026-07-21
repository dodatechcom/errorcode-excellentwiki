---
title: "[Solution] Spring @MockBean Error"
description: "Fix Spring @MockBean errors when mocked beans are not injected or interfere with other tests."
frameworks: ["spring"]
error-types: ["test-error"]
severities: ["error"]
---

`@MockBean` errors occur when mocked beans are not properly reset between tests, causing test pollution or unexpected behavior.

## Common Causes

- Mock not reset between test methods
- Mock behavior not properly configured
- Mock bean conflicts with real beans
- Test context cached with stale mocks
- Mockito version incompatibility

## How to Fix

### Use @MockBean Correctly

```java
@SpringBootTest
class UserServiceTest {
    @MockBean
    private UserRepository userRepository;

    @Autowired
    private UserService userService;

    @Test
    void testGetUser() {
        User mockUser = new User(1L, "Alice");
        when(userRepository.findById(1L)).thenReturn(Optional.of(mockUser));

        User result = userService.getUser(1L);
        assertEquals("Alice", result.getName());
    }
}
```

### Reset Mocks Between Tests

```java
@BeforeEach
void setUp() {
    reset(userRepository);
}

@Test
void test1() {
    when(userRepository.findById(1L)).thenReturn(Optional.of(new User(1L, "Alice")));
    // ...
}

@Test
void test2() {
    // Previous mock behavior is cleared
    when(userRepository.findById(1L)).thenReturn(Optional.empty());
}
```

### Use @Mock Instead of @MockBean

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    @Test
    void testGetUser() {
        when(userRepository.findById(1L)).thenReturn(Optional.of(new User(1L, "Alice")));
        assertEquals("Alice", userService.getUser(1L).getName());
    }
}
```

## Examples

```java
// Bug -- mock not reset
@MockBean
private UserRepository userRepository;

@Test
void test1() {
    when(userRepository.findById(1L)).thenReturn(Optional.of(new User(1L, "Alice")));
}

@Test
void test2() {
    // Still returns Alice from test1
    // Fix: add @BeforeEach with reset(userRepository)
}
```
