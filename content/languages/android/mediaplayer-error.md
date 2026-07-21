---
title: "MediaPlayer Error"
description: "Fix Android MediaPlayer initialization and playback errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
MediaPlayer fails to initialize, play audio, or recover from errors

## Common Causes

- MediaPlayer not initialized before play
- Audio file not found or inaccessible
- MediaPlayer not released causing resource leak
- Wrong thread for MediaPlayer operations

## Fixes

- Initialize MediaPlayer in onPrepared callback
- Verify audio resource exists and is accessible
- Always call release() in onDestroy
- Use main thread for MediaPlayer operations

## Code Example

```kotlin
val mediaPlayer = MediaPlayer()
mediaPlayer.apply {
    setDataSource(context, audioUri)
    setOnPreparedListener { start() }
    prepareAsync()
}
// In onDestroy:
mediaPlayer.release()
```

# Lifecycle: setDataSource -> prepare -> start
# Always release() in onDestroy or onStop
# Use prepareAsync for network streams
