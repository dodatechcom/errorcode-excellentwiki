---
title: "Compose Video Player Error"
description: "Fix Compose video player integration with ExoPlayer or Media3 errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Video player does not display or play correctly in Compose

## Common Causes

- PlayerView not properly embedded in Compose
- Video surface not rendering
- Player not released on composable disposal
- Media item not loading

## Fixes

- Use AndroidView to embed PlayerView
- Configure PlayerView with correct surface type
- Release player in DisposableEffect onDispose
- Set MediaItem before prepare

## Code Example

```kotlin
@Composable
fun VideoPlayer(mediaUrl: String) {
    val context = LocalContext.current
    val player = remember { ExoPlayer.Builder(context).build() }

    DisposableEffect(mediaUrl) {
        player.setMediaItem(MediaItem.fromUri(mediaUrl))
        player.prepare()
        player.playWhenReady = true

        onDispose {
            player.release()
        }
    }

    AndroidView(
        factory = { ctx ->
            PlayerView(ctx).apply {
                this.player = player
                useController = true
            }
        },
        modifier = Modifier.fillMaxWidth().aspectRatio(16f / 9f)
    )
}
```

# AndroidView for PlayerView in Compose
# DisposableEffect for player lifecycle
# Always release() player in onDispose
# aspectRatio for video dimensions
