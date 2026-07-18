---
title: "Solved JavaScript socket.io Error — How to Fix"
date: 2026-03-20T16:45:00+00:00
description: "Learn how to resolve JavaScript Socket.IO real-time connection and event handling errors."
categories: ["javascript"]
keywords: ["socket.io error", "websocket error", "real-time connection", "socket event", "socket.io client"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Socket.IO errors occur when WebSocket connections fail, events aren't properly registered, or CORS configuration blocks connections. The library provides fallback mechanisms but requires proper setup.

Common causes include:
- CORS not configured for WebSocket
- Event listeners not registered before connection
- Server not running or unreachable
- Namespace/room configuration issues
- Transport upgrade failures

## Common Error Messages

```
Error: xhr poll error
```

```
Error: WebSocket connection to 'ws://...' failed
```

```
Error: illegal "callback" argument
```

## How to Fix It

### 1. Configure Socket.IO Server

Set up server with proper options.

```javascript
import { Server } from "socket.io";

const io = new Server(server, {
  cors: {
    origin: process.env.CLIENT_URL,
    methods: ["GET", "POST"],
    credentials: true
  },
  pingTimeout: 60000,
  pingInterval: 25000,
  transports: ["websocket", "polling"],
  allowUpgrades: true
});

// Connection handler
io.on("connection", (socket) => {
  console.log("User connected:", socket.id);
  
  // Join room
  socket.on("join-room", (roomId) => {
    socket.join(roomId);
    console.log(`User ${socket.id} joined room ${roomId}`);
  });
  
  // Handle messages
  socket.on("send-message", (data) => {
    io.to(data.roomId).emit("new-message", {
      message: data.message,
      sender: socket.id,
      timestamp: Date.now()
    });
  });
  
  // Disconnect handler
  socket.on("disconnect", (reason) => {
    console.log("User disconnected:", socket.id, reason);
  });
});
```

### 2. Configure Socket.IO Client

Set up client with reconnection.

```javascript
import { io } from "socket.io-client";

const socket = io(process.env.SERVER_URL, {
  auth: {
    token: localStorage.getItem("token")
  },
  reconnection: true,
  reconnectionAttempts: 5,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
  timeout: 20000,
  transports: ["websocket", "polling"]
});

// Connection events
socket.on("connect", () => {
  console.log("Connected:", socket.id);
});

socket.on("connect_error", (error) => {
  console.error("Connection error:", error.message);
});

socket.on("disconnect", (reason) => {
  console.log("Disconnected:", reason);
  
  if (reason === "io server disconnect") {
    socket.connect(); // Reconnect manually
  }
});

// Reconnection events
socket.io.on("reconnect_attempt", (attempt) => {
  console.log("Reconnect attempt:", attempt);
});

socket.io.on("reconnect", (attempt) => {
  console.log("Reconnected after", attempt, "attempts");
});

// Join room and listen
socket.emit("join-room", "room-123");

socket.on("new-message", (data) => {
  console.log("Message received:", data);
});
```

### 3. Handle Namespaces and Rooms

Organize connections.

```javascript
import { Server } from "socket.io";

// Namespaces
const chatNamespace = io.of("/chat");
const notificationNamespace = io.of("/notifications");

chatNamespace.on("connection", (socket) => {
  console.log("Chat connected:", socket.id);
  
  socket.on("join-conversation", (conversationId) => {
    socket.join(`conversation:${conversationId}`);
  });
  
  socket.on("send-message", (data) => {
    chatNamespace
      .to(`conversation:${data.conversationId}`)
      .emit("new-message", data);
  });
});

notificationNamespace.on("connection", (socket) => {
  console.log("Notification connected:", socket.id);
});

// Room management
io.on("connection", (socket) => {
  socket.on("subscribe", (room) => {
    socket.join(room);
    socket.to(room).emit("user-joined", { userId: socket.userId });
  });
  
  socket.on("unsubscribe", (room) => {
    socket.leave(room);
    socket.to(room).emit("user-left", { userId: socket.userId });
  });
  
  socket.on("disconnecting", () => {
    socket.rooms.forEach((room) => {
      socket.to(room).emit("user-left", { userId: socket.userId });
    });
  });
});
```

## Common Scenarios

### Scenario 1: Chat Application

Build real-time chat:

```javascript
// Server
io.on("connection", (socket) => {
  socket.on("join-chat", async (chatId) => {
    socket.join(`chat:${chatId}`);
    
    const messages = await getMessages(chatId);
    socket.emit("message-history", messages);
  });
  
  socket.on("send-message", async (data) => {
    const message = await saveMessage(data);
    
    io.to(`chat:${data.chatId}`).emit("new-message", {
      ...message,
      sender: {
        id: socket.userId,
        name: socket.userName
      }
    });
  });
  
  socket.on("typing-start", (chatId) => {
    socket.to(`chat:${chatId}`).emit("user-typing", {
      userId: socket.userId,
      chatId
    });
  });
  
  socket.on("typing-stop", (chatId) => {
    socket.to(`chat:${chatId}`).emit("user-stopped-typing", {
      userId: socket.userId,
      chatId
    });
  });
});
```

### Scenario 2: Real-time Notifications

Push notifications to users:

```javascript
// Server
function notifyUser(userId, notification) {
  io.to(`user:${userId}`).emit("notification", notification);
}

io.on("connection", (socket) => {
  const userId = socket.handshake.auth.userId;
  socket.join(`user:${userId}`);
  
  socket.on("mark-read", async (notificationId) => {
    await markNotificationRead(notificationId);
  });
});

// Client
socket.on("notification", (data) => {
  showToast(data.title, data.message);
  updateNotificationBadge();
});
```

## Prevent It

- Configure CORS with specific origin (not `*`)
- Register event listeners before connecting
- Use `transports: ["websocket"]` for production
- Implement reconnection logic with backoff
- Handle `connect_error` and `disconnect` events