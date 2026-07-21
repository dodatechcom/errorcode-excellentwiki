---
title: "Julia Task Deadlock Error in Async Code"
description: "Fix Julia Task deadlock errors when async tasks block waiting for each other creating circular dependencies."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Task deadlocks occur when two or more async tasks are each waiting for the other to complete, preventing any progress. This is common with channels and shared resources.

## Common Causes

- Two tasks waiting on each other's channels
- fetch() on task that waits on current task
- Lock ordering violations between tasks
- All tasks blocked on full channels with no consumer
- Timer or sleep in task preventing progress

## How to Fix

```julia
# WRONG: Deadlock between two tasks
ch1 = Channel{Int}(1)
ch2 = Channel{Int}(1)

@async begin
    put!(ch1, 1)  # fills ch1
    val = take!(ch2)  # waits for ch2 -- blocked!
end

@async begin
    put!(ch2, 2)  # fills ch2
    val = take!(ch1)  # waits for ch1 -- blocked!
end
# DEADLOCK: both full, both waiting
```

```julia
# CORRECT: Use unbuffered channels or async put/take
ch1 = Channel{Int}(0)  # unbuffered
ch2 = Channel{Int}(0)

@async put!(ch1, 1)
@async begin
    val = take!(ch1)
    put!(ch2, 2)
end
@async take!(ch2)
```

## Examples

```julia
# Example 1: Producer-consumer without deadlock
buffer = Channel{Int}(10)

@async begin
    for i in 1:100
        put!(buffer, i)
    end
    close(buffer)
end

for item in buffer
    println(item)
end

# Example 2: Safe task coordination
condition = Condition()

@async begin
    sleep(1)
    notify(condition)
end

wait(condition)  # waits for notify

# Example 3: Avoid deadlock with select
using Base.Threads
ch1 = Channel{Int}(1)
ch2 = Channel{Int}(1)
t = @async while true
    result = wait(ch1, ch2)  # wait on either
    println("Got: ", result)
end
```

## Related Errors

- [Channel error](julia-channel-error) -- channel operation issues
- [Deadlock error](julia-deadlock-error) -- lock deadlocks
