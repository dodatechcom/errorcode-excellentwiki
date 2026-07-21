---
title: "Android Test Mock Error"
description: "Fix Android test mocking errors with Mockito or Mockk in unit tests"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Mocked objects return null or wrong values in Android unit tests

## Common Causes

- Mock not properly initialized
- Mockk annotation not applied
- Final class not mockable with standard Mockito
- Coroutine test dispatcher not set up

## Fixes

- Use @MockkBean or @Mock annotation
- Use mockk for Kotlin classes (handles final)
- Use MockK for coroutine mocking
- Set TestCoroutineDispatcher in setup

## Code Example

```kotlin
@RunWith(MockitoJUnitRunner::class)
class MyViewModelTest {
    @Mock
    lateinit var repository: Repository

    @Before
    fun setup() {
        MockitoAnnotations.openMocks(this)
    }

    @Test
    fun `test load data success`() = runTest {
        whenever(repository.getData()).thenReturn(listOf(item))
        val viewModel = MyViewModel(repository)
        viewModel.loadData()
        assertEquals(UiState.Success(listOf(item)), viewModel.uiState.value)
    }
}
```

# Use MockK for Kotlin final classes
# Use runTest for coroutine tests
# Use TestCoroutineDispatcher for timing control
