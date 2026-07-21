---
title: "Room In-Memory Test Error"
description: "Fix Room in-memory database configuration for Android unit tests"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room tests fail because database is not properly configured for testing

## Common Causes

- Using production database in tests
- In-memory database not properly closed
- Migration tests not using MigrationTestHelper
- Test running on wrong dispatcher

## Fixes

- Use Room.inMemoryDatabaseBuilder for tests
- Close database in @After
- Use MigrationTestHelper for migration tests
- Use runTest for coroutine DAO methods

## Code Example

```kotlin
@RunWith(AndroidJUnit4::class)
class UserDaoTest {
    private lateinit var db: AppDatabase
    private lateinit var dao: UserDao

    @Before
    fun setup() {
        db = Room.inMemoryDatabaseBuilder(
            ApplicationProvider.getApplicationContext(),
            AppDatabase::class.java
        ).build()
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
        val result = dao.getUserById(1)
        assertNotNull(result)
        assertEquals("Test", result?.name)
    }
}
```

# In-memory database is fastest for testing
# Always close database in @After
# Use runTest for suspend DAO methods
