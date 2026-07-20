---
title: "[Solution] Rails ActionCable — WebSocket, Channel, Auth, PubSub Errors"
description: "Fix Rails ActionCable errors. Handle WebSocket connection, channel streaming, authentication, and pub/sub issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, action_cable, websocket, channel"]
severity: "error"
---

# Rails ActionCable Errors

## Error Message

```
ActionCable::Connection::Authorization::UnauthorizedError
# or
Redis::CannotConnectError: Error connecting to Redis
# or
ActionCable::Connection::Rejected: ...
```

## Common Causes

- Missing or failed authentication in `Connection#identify`
- Redis server not running or unreachable
- Channel not subscribed to the correct stream
- WebSocket connection not properly configured

## Solutions

### Solution 1: Implement Connection Authentication

Authenticate users in the connection class before allowing channels.

```ruby
# app/channels/application_cable/connection.rb
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

### Solution 2: Subscribe to Channel Streams Correctly

Use proper stream names and handle subscription lifecycle.

```ruby
# app/channels/chat_channel.rb
class ChatChannel < ApplicationCable::Channel
  def subscribed
    # Stream from a specific room
    stream_from "chat_#{params[:room_id]}"
  end

  def unsubscribed
    # Cleanup when channel is unsubscribed
  end

  def speak(data)
    ActionCable.server.broadcast(
      "chat_#{params[:room_id]}",
      { message: data["message"], user: current_user.name }
    )
  end
end
```

### Solution 3: Configure ActionCable for Production

Set up Redis and adapter configuration properly.

```ruby
# config/cable.yml
development:
  adapter: redis
  url: redis://localhost:6379/1

production:
  adapter: redis
  url: <%= ENV.fetch("REDIS_URL") { "redis://localhost:6379/1" } %>
  channel_prefix: myapp_production

# config/environments/production.rb
config.action_cable.url = "wss://example.com/cable"
config.action_cable.allowed_request_origins = ["https://example.com"]
```

### Solution 4: Handle ActionCable Broadcasts

Broadcast updates efficiently with proper serialization.

```ruby
# Broadcasting from anywhere
ActionCable.server.broadcast("chat_1", {
  message: "Hello",
  timestamp: Time.current.iso8601
})

# Broadcasting from a model callback
class Message < ApplicationRecord
  after_create_commit do
    ActionCable.server.broadcast(
      "chat_#{room_id}",
      { id: id, content: content, user: user.name }
    )
  end
end
```

## Prevention Tips

- Always implement `identify` and `find_verified_user` in Connection
- Use Redis for ActionCable in production (not async adapter)
- Set `allowed_request_origins` in production for security
- Test channels with `ActionCable::Channel::TestCase`

## Related Errors

- [Redis::CannotConnectError]({{< relref "/languages/ruby/rails-redis-error" >}})
- [ActionController::InvalidAuthenticityToken]({{< relref "/languages/ruby/rails-csrf-error" >}})
- [WebSocket Error]({{< relref "/languages/ruby/rails-controller-error" >}})
