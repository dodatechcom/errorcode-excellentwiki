---
title: "[Solution] JavaScript NotAllowedError — Permission Not Allowed Fix"
description: "Fix JavaScript NotAllowedError when a browser or Node.js operation is denied. Check permissions, user gestures, and security policies."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["notallowederror", "permission", "denied", "security", "autoplay", "clipboard"]
weight: 5
---

# NotAllowedError — Permission Not Allowed Fix

A `NotAllowedError` indicates that the requested operation is not permitted by the browser's security model or the system's permission policy. This commonly occurs with autoplay media, clipboard access, notification requests, and fullscreen API calls that lack a user gesture.

## Description

Common NotAllowedError messages include:

- `NotAllowedError: play() failed because the user didn't interact with the document first` — autoplay blocked.
- `NotAllowedError: Clipboard read was denied` — no clipboard permission.
- `NotAllowedError: The request is not allowed by the user agent or the platform` — general permission denial.

## Common Causes

```javascript
// Cause 1: Autoplay without user interaction
const video = document.getElementById("promo-video");
video.play();  // NotAllowedError: play() failed — no user gesture

// Cause 2: Clipboard access without user gesture
await navigator.clipboard.readText();  // NotAllowedError if no click/keypress

// Cause 3: Notification.requestPermission() called on page load
Notification.requestPermission();  // blocked without user gesture in some browsers

// Cause 4: Fullscreen request without user gesture
document.documentElement.requestFullscreen();  // NotAllowedError if called on load
```

## Solutions

### Fix 1: Trigger media playback on user interaction

```javascript
const video = document.getElementById("promo-video");

// Option A: Mute and play on load, unmute on user interaction
video.muted = true;
video.play().catch(() => {});

video.addEventListener("click", () => {
  video.muted = false;
  video.play();
});

// Option B: Play on the first user gesture
document.addEventListener("click", async () => {
  if (video.paused) {
    await video.play();
  }
}, { once: true });
```

### Fix 2: Request clipboard access within user gesture handlers

```javascript
document.getElementById("copy-btn").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText("Hello, World!");
    console.log("Text copied to clipboard");
  } catch (err) {
    if (err.name === "NotAllowedError") {
      console.error("Clipboard permission denied by user");
    } else {
      throw err;
    }
  }
});
```

### Fix 3: Request notifications after user consent

```javascript
document.getElementById("enable-notifications").addEventListener("click", async () => {
  const permission = await Notification.requestPermission();

  if (permission === "granted") {
    new Notification("Notifications enabled!");
  } else if (permission === "denied") {
    console.warn("User denied notification permission");
  }
});
```

### Fix 4: Request fullscreen on user gesture

```javascript
document.getElementById("fullscreen-btn").addEventListener("click", async () => {
  try {
    await document.documentElement.requestFullscreen();
  } catch (err) {
    if (err.name === "NotAllowedError") {
      console.error("Fullscreen requires a user gesture (click/tap/keypress)");
    } else {
      throw err;
    }
  }
});
```

## Examples

```javascript
// NotAllowedError with Pointer Lock API
canvas.addEventListener("click", async () => {
  try {
    await canvas.requestPointerLock();
  } catch (err) {
    if (err.name === "NotAllowedError") {
      console.error("Pointer lock denied — user may need to grant permission");
    }
  }
});

// NotAllowedError with Payment Request API
const paymentRequest = new PaymentRequest(supportedMethods, paymentDetails);
try {
  const response = await paymentRequest.show();
} catch (err) {
  if (err.name === "NotAllowedError") {
    console.error("Payment request was cancelled or blocked");
  }
}
```

## Related Errors

- [AbortError]({{< relref "/languages/javascript/aborterror" >}}) — operation was intentionally cancelled.
- [NotFoundError]({{< relref "/languages/javascript/notfounderror" >}}) — resource could not be located.
- [InvalidStateError]({{< relref "/languages/javascript/invalidstateerror" >}}) — object is not in the required state.
