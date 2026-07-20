---
title: "[Solution] Scala SupervisorStrategyError - Brief Description"
description: "Fix Akka SupervisorStrategy errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1061
---

A SupervisorStrategy error occurs when actors fail repeatedly beyond restart limits.

## Common Causes

- Max retries exceeded
- Wrong strategy for failure type
- Restart loops between actors

## How to Fix

Choose the right strategy:

```scala
override def supervisorStrategy = OneForOneStrategy(maxNrOfRetries = 10) {
  case _: ArithmeticException => Restart
  case _: IllegalArgumentException => Stop
  case _: Exception => Escalate
}
```

Use AllForOne:

```scala
override def supervisorStrategy = AllForOneStrategy(maxNrOfRetries = 5) {
  case _: DatabaseException => Restart
}
```

## Examples

```scala
class ResilientWorker extends Actor {
  override def supervisorStrategy = OneForOneStrategy() {
    case _: Exception => Restart
  }
  def receive: Receive = { case work => doWork(work) }
}
```

## Related Errors

- [Scala AkkaActorError](/languages/scala/scala-akka-actor-error)
- [Scala AkkaTimeout](/languages/scala/scala-akka-timeout)
