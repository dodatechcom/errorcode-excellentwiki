---
title: "[Solution] JavaScript NotSupportedError — Media Error Fix"
description: "Fix JavaScript NotSupportedError: The media element does not support the loaded source. Check format support, codec availability, and cross-origin policies."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# NotSupportedError — Media Error Fix

A `NotSupportedError` is thrown when a media element (HTML `<audio>` or `<video>`) encounters a source format, codec, or configuration that the browser or environment cannot play. This error surfaces through the media element's `error` event and indicates the media pipeline rejected the resource.

## Description

Common NotSupportedError messages include:

- `NotSupportedError: The media element does not support the loaded source` — the format or codec is not recognized.
- `NotSupportedError: Failed to load because no supported source was found` — no `<source>` element succeeded.
- `NotAllowedError` may also appear if autoplay is blocked, but `NotSupportedError` specifically means the format is unsupported.

## Common Causes

```javascript
// Cause 1: Unsupported media format
const video = document.createElement("video");
video.src = "clip.avi";  // NotSupportedError — browsers don't play AVI natively

// Cause 2: Codec not available on the device
const audio = document.getElementById("player");
audio.src = "music.opus";  // may fail on older Safari versions

// Cause 3: Missing or incorrect MIME type from server
// Server sends Content-Type: application/octet-stream instead of video/mp4

// Cause 4: Encrypted or DRM-protected content without a license
const emeVideo = document.getElementById("drm-video");
emeVideo.src = "encrypted-stream.mpd";  // NotSupportedError if no DRM system
```

## Solutions

### Fix 1: Use widely supported formats with fallbacks

```html
<!-- Provide multiple source formats for cross-browser support -->
<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <source src="video.ogv" type="video/ogg">
  Your browser does not support the video tag.
</video>
```

### Fix 2: Check codec support before playback

```javascript
function canPlay(mediaType, mimeType) {
  const video = document.createElement("video");
  const result = video.canPlayType(mimeType);
  console.log(`${mimeType}: ${result || "not supported"}`);
  return result === "probably" || result === "maybe";
}

canPlay("video", 'video/mp4; codecs="avc1.42E01E, mp4a.40.2"');  // H.264
canPlay("video", 'video/webm; codecs="vp8, vorbis"');            // VP8
canPlay("audio", 'audio/ogg; codecs="vorbis"');                  // Ogg Vorbis
```

### Fix 3: Set correct MIME types on the server

```nginx
# Nginx — ensure correct Content-Type headers
location ~* \.mp4$ {
    add_header Content-Type "video/mp4";
}
location ~* \.webm$ {
    add_header Content-Type "video/webm";
}
```

```javascript
// Verify the response headers in JavaScript
const response = await fetch("video.mp4");
const contentType = response.headers.get("Content-Type");
if (!contentType?.startsWith("video/")) {
  console.warn("Server may be returning incorrect MIME type:", contentType);
}
```

### Fix 4: Handle the error event gracefully

```javascript
const video = document.getElementById("my-video");

video.addEventListener("error", () => {
  const error = video.error;
  switch (error.code) {
    case MediaError.MEDIA_ERR_ABORTED:
      console.error("Playback aborted by user.");
      break;
    case MediaError.MEDIA_ERR_NETWORK:
      console.error("Network error while loading media.");
      break;
    case MediaError.MEDIA_ERR_DECODE:
      console.error("Media decoding error.");
      break;
    case MediaError.MEDIA_ERR_SRC_NOT_SUPPORTED:
      console.error("Format not supported or source missing.");
      // Fallback: show a download link
      video.poster = "fallback.png";
      break;
  }
});
```

## Examples

```javascript
// This triggers NotSupportedError in most browsers
const audio = new Audio("recording.wav");
// WAV may not be supported in all environments; use MP3 or OGG instead

// Detect before attempting playback
if (!audio.canPlayType("audio/wav")) {
  console.error("WAV format is not supported in this browser");
}
```

## Related Errors

- [TypeError]({{< relref "/languages/javascript/typeerror" >}}) — value is not the expected type.
- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — code has invalid syntax.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream has already been destroyed.
