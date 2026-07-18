---
title: "Solved JavaScript Socket.IO Client Error — How to Fix"
date: 2026-03-20T14:15:10+00:00
description: "Learn how to resolve JavaScript Socket.IO client connection, reconnection, and authentication errors."
categories: ["javascript"]
keywords: ["socket.io client", "socket client error", "websocket client", "socket reconnection", "socket auth"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Socket.IO client errors occur when the WebSocket connection fails to establish, authenticate, or maintain stable communication. Client-side issues often involve CORS, token management, and network interruptions.

Common causes include:
- CORS configuration blocking client connections
- Authentication token expired or invalid
- Network interruptions causing disconnections
- Transport fallback issues between WebSocket and polling
- Memory leaks from uncleared event listeners

## Common Error Messages

```
Error: connect ECONNREFUSED
```

```
Error: websocket connection failed
```

```
Error: unauthorized
```

## How to Fix It

### 1. Configure Socket.IO Client

Set up client with proper connection options.

```javascript
import { io } from "socket.io-client";

const socket = io("https://api.example.com", {
  auth: {
    token: getAuthToken()
  },
  transports: ["websocket", "polling"],
  upgrade: true,
  rememberUpgrade: true,
  reconnection: true,
  reconnectionAttempts: 10,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 30000,
  timeout: 20000,
  autoConnect: true
});

// Connection events
socket.on("connect", () => {
  console.log("Connected:", socket.id);
  updateConnectionStatus("connected");
});

socket.on("disconnect", (reason) => {
  console.log("Disconnected:", reason);
  updateConnectionStatus("disconnected");
  
  if (reason === "io server disconnect") {
    socket.connect();
  }
});

socket.on("connect_error", (err) => {
  console.error("Connection error:", err.message);
  
  if (err.message === "unauthorized") {
    refreshToken();
  }
});

socket.on("reconnect", (attempt) => {
  console.log("Reconnected after", attempt, "attempts");
});

socket.on("reconnect_attempt", (attempt) => {
  console.log("Reconnect attempt:", attempt);
});
```

### 2. Handle Authentication

Implement proper token refresh and authentication.

```javascript
class SocketManager {
  constructor(url) {
    this.url = url;
    this.socket = null;
    this.token = null;
  }
  
  connect(token) {
    this.token = token;
    
    this.socket = io(this.url, {
      auth: { token },
      transports: ["websocket"]
    });
    
    this.setupEventHandlers();
    return this.socket;
  }
  
  setupEventHandlers() {
    this.socket.on("connect_error", (err) => {
      if (err.message === "token_expired") {
        this.refreshAndReconnect();
      }
    });
    
    this.socket.on("disconnect", (reason) => {
      if (reason === "io server disconnect") {
        this.refreshAndReconnect();
      }
    });
  }
  
  async refreshAndReconnect() {
    try {
      const newToken = await this.fetchNewToken();
      this.token = newToken;
      this.socket.auth.token = newToken;
      this.socket.connect();
    } catch (error) {
      console.error("Failed to refresh token:", error);
    }
  }
  
  async fetchNewToken() {
    const response = await fetch("/auth/refresh", {
      method: "POST",
      credentials: "include"
    });
    const data = await response.json();
    return data.accessToken;
  }
  
  disconnect() {
    if (this.socket) {
      this.socket.disconnect();
    }
  }
}
```

### 3. Manage Event Listeners

Properly add and remove listeners to prevent memory leaks.

```javascript
class ChatClient {
  constructor(socket) {
    this.socket = socket;
    this.handlers = new Map();
  }
  
  on(event, handler) {
    this.socket.on(event, handler);
    this.handlers.set(event, handler);
  }
  
  off(event) {
    const handler = this.handlers.get(event);
    if (handler) {
      this.socket.off(event, handler);
      this.handlers.delete(event);
    }
  }
  
  removeAll() {
    this.handlers.forEach((handler, event) => {
      this.socket.off(event, handler);
    });
    this.handlers.clear();
  }
  
  disconnect() {
    this.removeAll();
    this.socket.disconnect();
  }
}

// Usage
const chatClient = new ChatClient(socket);

chatClient.on("message", (data) => {
  console.log("Received:", data);
});

// Cleanup when component unmounts
function cleanup() {
  chatClient.disconnect();
}
```

## Common Scenarios

### Scenario 1: React Component Integration

Integrate Socket.IO with React:

```javascript
import { useEffect, useRef, useState } from "react";
import { io } from "socket.io-client";

function useSocket(url) {
  const socketRef = useRef(null);
  const [isConnected, setIsConnected] = useState(false);
  
  useEffect(() => {
    socketRef.current = io(url, {
      auth: { token: getAuthToken() },
      transports: ["websocket"]
    });
    
    socketRef.current.on("connect", () => {
      setIsConnected(true);
    });
    
    socketRef.current.on("disconnect", () => {
      setIsConnected(false);
    });
    
    return () => {
      socketRef.current?.disconnect();
    };
  }, [url]);
  
  return { socket: socketRef.current, isConnected };
}

function ChatRoom() {
  const { socket, isConnected } = useSocket("https://api.example.com");
  const [messages, setMessages] = useState([]);
  
  useEffect(() => {
    if (!socket) return;
    
    const handleMessage = (msg) => {
      setMessages(prev => [...prev, msg]);
    };
    
    socket.on("message", handleMessage);
    
    return () => {
      socket.off("message", handleMessage);
    };
  }, [socket]);
  
  return (
    <div>
      <p>Status: {isConnected ? "Connected" : "Disconnected"}</p>
      <ul>
        {messages.map((msg, i) => (
          <li key={i}>{msg.text}</li>
        ))}
      </ul>
    </div>
  );
}
```

## Prevent It

- Handle `connect_error` events to manage authentication failures
- Use `reconnectionDelayMax` to cap exponential backoff
- Remove event listeners when components unmount
- Use `rememberUpgrade: true` for faster subsequent connections
- Monitor connection state with `socket.connected` property