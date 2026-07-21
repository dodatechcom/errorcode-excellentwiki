---
title: "UI Automator Test Error"
description: "Fix UI Automator test errors for cross-app UI testing in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
UI Automator tests fail to interact with system UI or other apps

## Common Causes

- Device context not properly obtained
- UiDevice not initialized in test
- Package name incorrect for target app
- Selector not finding expected UI element

## Fixes

- Initialize UiDevice in @Before setup
- Use correct package name for target app
- Use UiSelector or BySelector to find elements
- Add delay or wait for idle before assertions

## Code Example

```kotlin
@RunWith(AndroidJUnit4::class)
class UiAutomatorTest {
    private lateinit var device: UiDevice

    @Before
    fun setUp() {
        device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
        device.pressHome()
    }

    @Test
    fun testOpenApp() {
        // Find and launch app
        val app = device.findObject(By.text("My App"))
        app?.click()

        // Wait for app to load
        device.wait(Until.hasObject(By.pkg("com.example.app")), 5000)

        // Find element and interact
        val button = device.findObject(By.res("com.example.app", "button"))
        button?.click()
    }
}
```

# UI Automator for cross-app testing
# Espresso for within-app testing
# Use device.wait() for async operations
