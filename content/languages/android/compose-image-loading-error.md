---
title: "Compose Image Loading Error"
description: "Fix Jetpack Compose image loading errors with Coil or Glide integration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Images do not load or display correctly in Compose using image loading libraries

## Common Causes

- Coil or Glide Compose dependency not added
- Image URL not valid or not accessible
- Missing placeholder or error state
- Image aspect ratio or size not set correctly

## Fixes

- Add coil-compose or glide-compose dependency
- Verify image URL is accessible
- Use placeholder and error parameters
- Set contentScale for proper sizing

## Code Example

```kotlin
// Coil Compose
implementation("io.coil-kt:coil-compose:2.5.0")

AsyncImage(
    model = ImageRequest.Builder(context)
        .data(user.avatarUrl)
        .crossfade(true)
        .build(),
    contentDescription = user.name,
    placeholder = painterResource(R.drawable.placeholder),
    error = painterResource(R.drawable.error),
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(48.dp)
        .clip(CircleShape)
)
```

# Coil: io.coil-kt:coil-compose
# Glide: com.github.bumptech.glide:compose
# Both provide AsyncImage composable
# Use crossfade for smooth loading
