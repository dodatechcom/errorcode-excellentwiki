---
title: "OkHttp WebSocket Error"
description: "Fix OkHttp WebSocket connection and message handling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
OkHttp WebSocket connection fails or messages are not received correctly

## Common Causes

- WebSocket listener not properly implemented
- Connection URL does not use ws:// or wss:// scheme
- Text or binary message type mismatch
- WebSocket not closed properly on disconnect

## Fixes

- Implement WebSocketListener with all callback methods
- Use wss:// for secure WebSocket connections
- Use send() with correct message type
- Close WebSocket with proper close code and reason

## Code Example

```kotlin
val request = Request.Builder()
    .url("wss://echo.websocket.org")
    .build()

val webSocket = client.newWebSocket(request, object : WebSocketListener() {
    override fun onOpen(webSocket: WebSocket, response: Response) {
        webSocket.send("Hello Server!")
    }

    override fun onMessage(webSocket: WebSocket, text: String) {
        Log.d("WS", "Received: $text")
    }

    override fun onClosing(webSocket: WebSocket, code: Int, reason: String) {
        webSocket.close(1000, null)
    }

    override fun onFailure(webSocket: WebSocket, t: Throwable, response: Response?) {
        Log.e("WS", "Error: ${t.message}")
    }
})
```

# Send messages:
webSocket.send("text message")
webSocket.send(ByteString.of(0x01, 0x02))

# Close:
webSocket.close(1000, "Goodbye")
