---
title: "Skeleton Loading Error"
description: "Fix Compose skeleton loading and shimmer placeholder screen errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Skeleton loading placeholders do not match content layout or shimmer not working

## Common Causes

- Skeleton items not matching actual item dimensions
- Shimmer animation not visible
- Skeleton not showing during loading
- Skeleton layout not responsive to screen size

## Fixes

- Match skeleton item dimensions to real items
- Use shimmer modifier for loading effect
- Show skeleton during loading state
- Use fillMaxWidth for responsive skeleton

## Code Example

```kotlin
@Composable
fun ItemListSkeleton(count: Int = 5) {
    Column(modifier = Modifier.padding(16.dp)) {
        repeat(count) {
            ItemSkeleton()
            Spacer(modifier = Modifier.height(8.dp))
        }
    }
}

@Composable
fun ItemSkeleton() {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .shimmer()  // Custom shimmer modifier
            .padding(8.dp)
    ) {
        Box(
            modifier = Modifier
                .size(48.dp)
                .clip(RoundedCornerShape(8.dp))
                .background(Color.LightGray)
        )
        Spacer(modifier = Modifier.width(12.dp))
        Column {
            Box(
                modifier = Modifier
                    .fillMaxWidth(0.7f)
                    .height(16.dp)
                    .clip(RoundedCornerShape(4.dp))
                    .background(Color.LightGray)
            )
            Spacer(modifier = Modifier.height(8.dp))
            Box(
                modifier = Modifier
                    .fillMaxWidth(0.5f)
                    .height(12.dp)
                    .clip(RoundedCornerShape(4.dp))
                    .background(Color.LightGray)
            )
        }
    }
}
```

# Match skeleton to real item dimensions
# Use shimmer for loading animation
# Show skeleton during loading state
# Responsive to screen size
