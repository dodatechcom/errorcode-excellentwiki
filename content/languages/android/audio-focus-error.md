---
title: "Audio Focus Error"
description: "Fix Android audio focus handling errors for media playback apps"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Media playback does not pause or duck when other apps request audio focus

## Common Causes

- AudioFocusRequest not properly configured
- Focus change listener not implemented
- Audio ducking not configured for music apps
- Focus loss not handled by pausing playback

## Fixes

- Create AudioFocusRequest with proper usage and content type
- Implement OnAudioFocusChangeListener
- Use AUDIOFOCUS_GAIN_TRANSIENT for short interruptions
- Pause playback on permanent focus loss

## Code Example

```kotlin
val audioAttributes = AudioAttributes.Builder()
    .setUsage(AudioAttributes.USAGE_MEDIA)
    .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
    .build()

val focusRequest = AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN)
    .setAudioAttributes(audioAttributes)
    .setOnAudioFocusChangeListener { focusChange ->
        when (focusChange) {
            AudioManager.AUDIOFOCUS_LOSS -> player.pause()
            AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> player.pause()
            AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK ->
                player.volume = 0.2f
            AudioManager.AUDIOFOCUS_GAIN -> player.play()
        }
    }
    .build()

audioManager.requestAudioFocus(focusRequest)
```

# AUDIOFOCUS_GAIN: long focus (music)
# AUDIOFOCUS_GAIN_TRANSIENT: short focus (notification)
# AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK: can lower volume
