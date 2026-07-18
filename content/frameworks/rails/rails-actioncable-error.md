---
title: "[Solution] Rails ActionCable Error — How to Fix"
description: "Fix Rails ActionCable errors. Resolve WebSocket connection failures, channel subscription issues, and broadcasting problems."
frameworks: ["rails"]
error-types: ["websocket-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails ActionCable error occurs when WebSocket connections fail, channel subscriptions are rejected, or broadcasts do not reach subscribers.

## Why It Happens

ActionCable errors happen due to Redis configuration issues, incorrect channel definitions, authentication failures, or connection timeout problems.

## Common Error Messages

```
ActionCable::Connection::Authorization::UnauthorizedError: Not authenticated
```

```
Redis::CannotConnectError: Error connecting to Redis
```

```
ActionCable::Channel::Rejected: Unable to subscribe
```

```
WebSocket connection failed
```

## How to Fix It

### 1. Configure ActionCable Adapter

Set up Redis as the adapter.

```yaml
# config/cable.yml
production:
  adapter: redis
  url: <%= ENV.fetch('REDIS_URL') { 'redis://localhost:6379/1' } %>
  channel_prefix: myapp_production
```

### 2. Authenticate WebSocket Connections

Implement connection authentication.

```ruby
module ApplicationCable
  class Connection < ActionCable::Connection::Base
    identified_by :current_user

    def connect
      self.current_user = find_verified_user
    end

    private
    def find_verified_user
      if verified_user = User.find_by(id: cookies.encrypted[:user_id])
        verified_user
      else
        reject_unauthorized_connection
      end
    end
  end
end
```

### 3. Define Channel Subscriptions

Create channels with proper logic.

```ruby
class ChatChannel < ApplicationCable::Channel
  def subscribed
    stream_from "chat_#{params[:room_id]}"
  end

  def unsubscribed
  end

  def speak(data)
    broadcast_to("chat_#{params[:room_id]}", message: data['message'])
  end
end
```

### 4. Handle Connection Failures

Add reconnection logic on the client.

```javascript
consumer.subscriptions.create('ChatChannel', {
  connected() { console.log('Connected') },
  disconnected() { console.log('Disconnected, reconnecting...') },
  received(data) { console.log('Received:', data) }
})
```

## Common Scenarios

**Scenario 1: WebSocket fails in production.**
Ensure Redis is running and REDIS_URL is set.

**Scenario 2: Channel subscription rejected.**
Check stream_from matches client subscription.

**Scenario 3: Broadcasts not reaching subscribers.**
Verify Redis adapter is configured.

## Prevent It

1. **Monitor connections.**
Track connected clients.

2. **Handle Redis failures gracefully.**
Use fallback behavior.

3. **Test WebSocket connections.**
Use ActionCable test helpers.

