---
title: "Benchmark Test Error"
description: "Fix Android Benchmark test configuration and execution errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Android Benchmark tests fail to run or produce unreliable results

## Common Causes

- Benchmark not configured with correct dependencies
- Test running on emulator instead of physical device
- Jit warmup iterations too low
- Thermal throttling affecting results

## Fixes

- Add microbenchmark dependency in build.gradle
- Run on physical device for accurate results
- Use default warmup and measurement iterations
- Ensure device is not thermally throttled

## Code Example

```kotlin
dependencies {
    androidTestImplementation 'androidx.benchmark:benchmark-macro-junit4:1.2.0'
}

@RunWith(AndroidJUnit4::class)
class MyBenchmark {
    @get:Rule
    val benchmarkRule = MacroBenchmarkRule()

    @Test
    fun scrollList() {
        benchmarkRule.measureRepeated {
            // Repeat in measureRepeated block
            val context = InstrumentationRegistry.getInstrumentation().targetContext
            val intent = Intent(context, MainActivity::class.java)
            startActivityAndWait(intent)
        }
    }
}
```

# Run benchmarks:
./gradlew :benchmark:connectedBenchmarkAndroidTest
# Use physical device, not emulator
# Keep device cool between runs
