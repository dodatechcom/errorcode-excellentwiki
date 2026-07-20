---
title: "[Solution] Scala AkkaTellError - Brief Description"
description: "Fix Akka tell pattern errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1060
---

An Akka tell error occurs when sending to a dead or unavailable actor.

## Common Causes

- Sending to a dead actorRef
- Message type not matchable
- Sending null messages

## How to Fix

Check validity:

```scala
if (actorRef != context.system.deadLetters) {
  actorRef ! "message"
}
```

Handle dead letters:

```scala
context.system.eventStream.registerListener(self)
def receive: Receive = {
  case DeadLetter(msg, sender, recipient) =>
    println(s"Dead letter: $msg from $sender to $recipient")
}
```

## Examples

```scala
class MyActor extends Actor {
  def receive: Receive = {
    case "ping" => sender() ! "pong"
    case msg => println(s"Received: $msg")
  }
}
```

## Related Errors

- [Scala AkkaActorError](/languages/scala/scala-akka-actor-error)
- [Scala AkkaAskError](/languages/scala/scala-akka-ask-error)
