---
title: "[Solution] JavaScript WebRTC Connection Error — How to Fix"
description: "Fix JavaScript WebRTC getUserMedia failures, RTCPeerConnection errors, ICE candidate issues, SDP negotiation problems, and track errors."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 814
---

# JavaScript WebRTC Connection Error

A `DOMException`, `TypeError`, or `RTCError` occurs when WebRTC's `getUserMedia` fails due to permissions, `RTCPeerConnection` cannot negotiate SDP, ICE candidates fail to connect, or media tracks cannot be added or removed.

## Why It Happens

WebRTC errors arise from missing camera/microphone permissions, STUN/TURN server misconfiguration, SDP offer/answer mismatches, ICE connection timeouts, and attempting to add tracks after negotiation is complete.

## Common Error Messages

- `DOMException: Permission denied (getUserMedia)`
- `TypeError: Failed to construct 'RTCPeerConnection': Invalid RTCConfiguration`
- `Error: ICE failed, see about:webrtc for more details`
- `Error: Failed to set remote answer sdp: Called in wrong state`
- `DOMException: Failed to add track - connection already negotiated`

## How to Fix It

### Fix 1: Handle getUserMedia errors

```javascript
// ❌ Wrong - no error handling
// const stream = await navigator.mediaDevices.getUserMedia({ video: true })

// ✅ Correct
async function startCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true
    })
    return stream
  } catch (err) {
    if (err.name === 'NotAllowedError') {
      console.error('Camera permission denied')
      showPermissionPrompt()
    } else if (err.name === 'NotFoundError') {
      console.error('No camera found')
    } else {
      console.error('getUserMedia error:', err)
    }
  }
}
```

### Fix 2: Configure ICE servers properly

```javascript
// ❌ Wrong - missing STUN/TURN servers
// const pc = new RTCPeerConnection()

// ✅ Correct
const configuration = {
  iceServers: [
    { urls: 'stun:stun.l.google.com:19302' },
    {
      urls: 'turn:turn.example.com:3478',
      username: 'user',
      credential: 'pass'
    }
  ],
  iceCandidatePoolSize: 10
}

const pc = new RTCPeerConnection(configuration)
```

### Fix 3: SDP negotiation sequence

```javascript
// ❌ Wrong - setting answer before offer
// ✅ Correct signaling flow

async function createOffer() {
  const pc = new RTCPeerConnection(config)
  const offer = await pc.createOffer()
  await pc.setLocalDescription(offer)
  // Send offer to remote peer via signaling server
  signaling.send({ type: 'offer', sdp: offer })
}

async function handleOffer(offer) {
  const pc = new RTCPeerConnection(config)
  await pc.setRemoteDescription(new RTCSessionDescription(offer))
  const answer = await pc.createAnswer()
  await pc.setLocalDescription(answer)
  // Send answer back
  signaling.send({ type: 'answer', sdp: answer })
}
```

### Fix 4: Handle ICE connection state

```javascript
pc.oniceconnectionstatechange = () => {
  console.log('ICE state:', pc.iceConnectionState)

  if (pc.iceConnectionState === 'failed') {
    // ❌ Connection failed
    // ✅ Correct - restart ICE
    pc.restartIce()
  } else if (pc.iceConnectionState === 'disconnected') {
    // Temporary network issue - wait before reconnecting
    setTimeout(() => {
      if (pc.iceConnectionState === 'disconnected') {
        pc.restartIce()
      }
    }, 3000)
  }
}
```

## Examples

Full peer connection setup with error handling:

```javascript
async function setupPeerConnection(localStream) {
  const pc = new RTCPeerConnection({
    iceServers: [{ urls: 'stun:stun.l.google.com:19302' }]
  })

  // Add tracks
  localStream.getTracks().forEach(track => {
    if (pc.addTrack) {
      pc.addTrack(track, localStream)
    }
  })

  // Handle incoming tracks
  pc.ontrack = (event) => {
    remoteVideo.srcObject = event.streams[0]
  }

  // Handle connection state
  pc.onconnectionstatechange = () => {
    if (pc.connectionState === 'failed') {
      pc.close()
      // Create new connection
      setupPeerConnection(localStream)
    }
  }

  return pc
}
```

## Related Errors

- [WebSocket Error](/languages/javascript/websocket-error)
- [WebSocket Close Codes](/languages/javascript/websocket-close-codes)
- [JavaScript Media Error](/languages/javascript/enomediaerror)
