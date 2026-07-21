---
title: "Hilt Testing Error"
description: "Fix Hilt testing configuration and test component errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Hilt tests fail because of missing test components or incorrect configuration

## Common Causes

- @HiltAndroidTest not on test class
- Test modules not overriding production modules
- HiltTestApplication not configured in manifest
- UninstallModules not removing unwanted modules

## Fixes

- Add @HiltAndroidTest to test class
- Use @UninstallModules and @TestInstallIn
- Configure HiltTestApplication in test manifest
- Use @BindValue to provide test doubles

## Code Example

```kotlin
@HiltAndroidTest
@RunWith(AndroidJUnit4::class)
class MyTest {
    @get:Rule
    val hiltRule = HiltAndroidRule(this)

    @BindValue
    val fakeRepository: Repository = FakeRepository()

    @Inject lateinit var viewModel: MyViewModel

    @Before
    fun setup() {
        hiltRule.inject()
    }

    @Test
    fun testSomething() {
        // Test with injected ViewModel using FakeRepository
    }
}

// Custom test module:
@Module
@TestInstallIn(components = [SingletonComponent::class], replaces = [NetworkModule::class])
object TestNetworkModule {
    @Provides fun provideApi(): ApiService = FakeApiService()
}
```

# @HiltAndroidTest enables Hilt for testing
# @TestInstallIn replaces production modules
# @BindValue provides test doubles inline
