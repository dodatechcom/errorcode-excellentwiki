---
title: "Room Testing Error"
description: "Fix Room database unit testing errors with in-memory database configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room tests fail because of database initialization or migration test issues

## Common Causes

- Using real database instead of in-memory for tests
- Migration test not using Helper
- Test running on main thread instead of test dispatcher
- TypeConverters not available in test environment

## Fixes

- Use Room.inMemoryDatabaseBuilder for tests
- Use MigrationTestHelper for migration tests
- Run database operations on test dispatcher
- Provide TypeConverters in test configuration

## Code Example

```kotlin
@Before
fun setup() {
    val context = ApplicationProvider.getApplicationContext<Context>()
    db = Room.inMemoryDatabaseBuilder(context, AppDatabase::class.java)
        .build()
    dao = db.userDao()
}

@After
fun teardown() {
    db.close()
}

@Test
fun insertAndGetUser() = runTest {
    val user = User(name = "Test", email = "test@example.com")
    dao.insertUser(user)
    val retrieved = dao.getUser(1)
    assertEquals("Test", retrieved?.name)
}
```

# Use @RunWith(AndroidJUnit4::class) for instrumented tests
# Use Robolectric for local unit tests with Room
