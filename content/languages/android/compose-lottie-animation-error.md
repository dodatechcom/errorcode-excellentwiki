---
title: "Lottie Animation Error"
description: "Fix Lottie animation integration and playback errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Lottie animation does not play or displays incorrectly in Compose

## Common Causes

- LottieCompositionSpec not loading animation file
- Animation not playing automatically
- Animation speed or repeat mode incorrect
- Lottie library not added to dependencies

## Fixes

- Use LottieCompositionSpec for animation loading
- Set autoPlay = true for immediate play
- Configure speed and repeatMode parameters
- Add compose-lottie dependency

## Code Example

```kotlin
dependencies {
    implementation "com.airbnb.android:lottie-compose:6.3.0"
}

@Composable
fun LottieAnimation() {
    val composition by rememberLottieComposition(
        LottieCompositionSpec.RawRes(R.raw.animation)
    )
    val progress by animateLottieCompositionAsState(
        composition,
        iterations = LottieConstants.IterateForever,
        speed = 1.0f
    )
    LottieAnimation(
        composition = composition,
        progress = { progress },
        modifier = Modifier.size(200.dp)
    )
}
```

# rememberLottieComposition: load animation
# animateLottieCompositionAsState: control playback
# iterations: how many times to play
# speed: playback speed multiplier
