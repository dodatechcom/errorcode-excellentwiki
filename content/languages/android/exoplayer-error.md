---
title: "ExoPlayer Error"
description: "Fix ExoPlayer (Media3) initialization and playback errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ExoPlayer fails to play media or throws player errors

## Common Causes

- ExoPlayer not properly initialized with context
- MediaItem URI not valid or accessible
- Player not released on Activity/Fragment destruction
- Audio focus not properly managed

## Fixes

- Create ExoPlayer with.Builder(context).build()
- Verify media URI is accessible
- Release player in onRelease lifecycle
- Implement AudioAttributes for audio focus

## Code Example

```kotlin
val player = ExoPlayer.Builder(context).build()
binding.playerView.player = player

val mediaItem = MediaItem.fromUri(mediaUri)
player.setMediaItem(mediaItem)
player.prepare()
player.playWhenReady = true

// Release when done:
override fun onStop() {
    super.onStop()
    player.release()
}
```

# Media3 (formerly ExoPlayer):
# implementation 'androidx.media3:media3-exoplayer:1.2.0'
# Always release player when done
