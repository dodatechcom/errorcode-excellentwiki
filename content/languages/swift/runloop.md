---
title: "[Solution] Swift Error — RunLoop Error"
description: "Fix Swift RunLoop errors. Learn about RunLoop observer issues, timer invalidation, and common RunLoop-related crashes and bugs."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runloop", "timer", "observer", "main-thread", "modes"]
weight: 5
---

# RunLoop Error

RunLoop errors occur when observers, timers, or sources are used incorrectly with the RunLoop. Common issues include accessing invalidated timers, RunLoop observer crashes, and mode-specific scheduling problems.

## Description

The RunLoop is an event processing loop that manages input sources, timers, and observers on a thread. Errors occur when objects interact with the RunLoop after being deallocated, when timers are invalidated but still referenced, or when scheduling in the wrong RunLoop mode.

Common patterns:

- **Invalidated timer access** — using a timer after `invalidate()`.
- **RunLoop observer crash** — accessing deallocated observer.
- **Mode mismatch** — scheduling in default mode but running in tracking mode.
- **Timer retain cycle** — timer strongly retaining its target.

## Common Causes

```swift
// Cause 1: Accessing invalidated timer
var timer: Timer?
timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
    print("tick")
}
timer?.invalidate()
timer?.fire() // May crash or behave unexpectedly

// Cause 2: Timer retain cycle
class ViewController: UIViewController {
    var timer: Timer?
    func startTimer() {
        timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
            self.updateUI() // Strong reference to self
        }
    }
}

// Cause 3: Timer in wrong RunLoop mode
let timer = Timer(timeInterval: 1.0, repeats: true) { _ in
    print("tick")
}
RunLoop.main.add(timer, forMode: .default)
// Timer won't fire during scrolling (tracking mode)

// Cause 4: Observer on wrong thread
let observer = CFRunLoopObserverCreateWithHandler(nil, CFRunLoopActivity.allActivities.rawValue, true, 0) { observer, activity in
    print(activity)
}
CFRunLoopAddObserver(CFRunLoopGetMain(), observer, .commonModes)
```

## How to Fix

### Fix 1: Invalidate timers properly

```swift
class ViewController: UIViewController {
    var timer: Timer?

    func startTimer() {
        timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { [weak self] _ in
            self?.updateUI()
        }
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        timer?.invalidate()
        timer = nil
    }
}
```

### Fix 2: Use weak self in timer closures

```swift
// Wrong
timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
    self.doSomething() // Retain cycle
}

// Correct
timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { [weak self] _ in
    self?.doSomething()
}
```

### Fix 3: Schedule timer in common modes

```swift
let timer = Timer(timeInterval: 1.0, repeats: true) { _ in
    print("tick even during scrolling")
}
RunLoop.main.add(timer, forMode: .common) // Fires in all modes
```

### Fix 4: Check RunLoop mode before processing

```swift
let observer = CFRunLoopObserverCreateWithHandler(nil, CFRunLoopActivity.beforeSources.rawValue, true, 0) { _, activity in
    guard CFRunLoopGetCurrent() == CFRunLoopGetMain() else { return }
    // Process on main RunLoop only
}
CFRunLoopAddObserver(CFRunLoopGetMain(), observer, CFRunLoopMode.defaultMode.rawValue)
```

## Examples

```swift
// Example 1: Timer fired after deallocation
class Task {
    var timer: Timer?
    func start() {
        timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { [weak self] _ in
            guard let self = self else {
                self?.timer?.invalidate() // Wrong: can't access self
                return
            }
            self.process()
        }
    }
}

// Example 2: Observer leak
class Monitor {
    var observer: CFRunLoopObserver?
    func start() {
        observer = CFRunLoopObserverCreateWithHandler(nil, CFRunLoopActivity.allActivities.rawValue, true, 0) { _, _ in
            print("activity")
        }
        CFRunLoopAddObserver(CFRunLoopGetMain(), observer, CFRunLoopMode.commonModes)
    }
    // Never removed observer — leaks
}
```

## Related Errors

- [Thread Sanitizer Error]({{< relref "/languages/swift/thread-sanitizer" >}}) — data race with RunLoop.
- [EXC_BAD_ACCESS]({{< relref "/languages/swift/memory-access" >}}) — accessing deallocated RunLoop objects.
- [Stack Overflow]({{< relref "/languages/swift/stack-overflow" >}}) — recursive RunLoop callbacks.
