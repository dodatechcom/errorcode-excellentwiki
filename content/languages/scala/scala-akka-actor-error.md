---
title: "[Solution] Scala AkkaActorError - Brief Description"
description: "Fix Akka actor errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1058
---

An Akka actor error occurs when an actor fails to handle a message or crashes.

## Common Causes

- Actor throws exception during handling
- Sending to a dead actor
- Missing pattern match for message type

## How to Fix

Handle all message types:

```scala
class MyActor extends Actor {
  def receive: Receive = {
    case msg: String => handleString(msg)
    case msg: Int => handleInt(msg)
    case msg => unhandled(msg)
  }
}
```

Use supervision:

```scala
class MySupervisor extends Actor {
  override def supervisorStrategy: SupervisorStrategy =
    OneForOneStrategy(maxNrOfRetries = 10) {
      case _: ArithmeticException => Restart
      case _: Exception => Stop
    }
}
```

## Examples

```scala
class PingPong extends Actor {
  def receive: Receive = {
    case "ping" => sender() ! "pong"
    case "stop" => context.stop(self)
  }
}
```

## Related Errors

- [Scala AkkaTimeout](/languages/scala/scala-akka-timeout)
- [Scala AkkaAskError](/languages/scala/scala-akka-ask-error)
