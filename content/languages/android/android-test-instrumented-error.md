---
title: "Instrumented Test Error"
description: "Fix Android instrumented test configuration and execution errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Instrumented tests fail to run or produce incorrect results on device

## Common Causes

- Test class not annotated with @RunWith(AndroidJUnit4::class)
- Test APK not properly configured
- Device not connected or emulator not running
- Test runner not specified in build.gradle

## Fixes

- Add @RunWith(AndroidJUnit4::class) annotation
- Verify androidTestImplementation dependencies
- Check device connectivity with adb devices
- Configure testInstrumentationRunner in build.gradle

## Code Example

```kotlin
@RunWith(AndroidJUnit4::class)
class MyInstrumentedTest {
    @Test
    fun testAppLaunches() {
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("com.example.app", appContext.packageName)
    }
}

// build.gradle:
android {
    defaultConfig {
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
}

dependencies {
    androidTestImplementation 'androidx.test.ext:junit:1.1.5'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.5.1'
}
```

# Run instrumented tests:
./gradlew connectedDebugAndroidTest
# Or in Android Studio: Run > Edit Configurations > Android Instrumented Test
