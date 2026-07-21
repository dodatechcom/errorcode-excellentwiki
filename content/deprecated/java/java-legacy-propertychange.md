---
title: "[Solution] Deprecated Function Migration: PropertyChangeSupport to reactive streams"
description: "Migrate from deprecated PropertyChangeSupport to reactive patterns."
deprecated_function: "PropertyChangeSupport"
replacement_function: "RxJava / Flow"
languages: ["java"]
deprecated_since: "Java 9+"
---

# [Solution] Deprecated Function Migration: PropertyChangeSupport to reactive streams

The `PropertyChangeSupport` has been deprecated in favor of `RxJava / Flow`.

## Migration Guide

Reactive streams provide better composition

PropertyChangeSupport is verbose. Reactive streams provide better composition and backpressure.

## Before (Deprecated)

```java
PropertyChangeSupport pcs = new PropertyChangeSupport(this);
pcs.addPropertyChangeListener(evt -> {
    System.out.println(evt.getProperty() + " changed");
});
pcs.firePropertyChange("value", oldValue, newValue);
```

## After (Modern)

```java
// Using Flow (Java 9+)
Flow.Subscriber<String> subscriber = new Flow.Subscriber<>() {
    public void onSubscribe(Flow.Subscription s) { s.request(Long.MAX_VALUE); }
    public void onNext(String item) { System.out.println(item); }
    public void onError(Throwable t) { t.printStackTrace(); }
    public void onComplete() { }
};

// Or use RxJava/Project Reactor
Observable.of("a", "b", "c")
    .subscribe(System.out::println);
```

## Key Differences

- Reactive streams provide composition
- Backpressure support
- Better error handling
- Multiple subscriber support
