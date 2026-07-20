---
title: "[Solution] Java NoSuchElementException — No More Elements Fix"
description: "Fix Java NoSuchElementException by checking hasNext() before next(), using Optional for findFirst(), and handling empty collections."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# NoSuchElementException — No More Elements Fix

A `NoSuchElementException` is thrown when an attempt is made to access an element that does not exist in an iterator, enumeration, tokenizer, or scanner. This is a subclass of `NoSuchElementException` extending `RuntimeException`.

## Description

The exception is part of Java's `java.util` package and is thrown by several classes that provide sequential access to elements. The message is typically `"NoSuch element"` or `"No line found"`, depending on the source. The class hierarchy is `RuntimeException → NoSuchElementException`.

## Common Causes

```java
// Cause 1: Calling Iterator.next() without checking hasNext()
List<String> list = Arrays.asList("a", "b");
Iterator<String> it = list.iterator();
it.next(); // "a"
it.next(); // "b"
it.next(); // NoSuchElementException — no more elements

// Cause 2: Calling Enumeration.nextElement() past the end
Vector<String> vector = new Vector<>(Arrays.asList("x", "y"));
Enumeration<String> en = vector.elements();
en.nextElement(); // "x"
en.nextElement(); // "y"
en.nextElement(); // NoSuchElementException

// Cause 3: StringTokenizer with no tokens
StringTokenizer st = new StringTokenizer("");
st.nextToken(); // NoSuchElementException — empty string

// Cause 4: Scanner.nextLine() with no more input
Scanner scanner = new Scanner(new StringReader(""));
scanner.nextLine(); // NoSuchElementException — no line

// Cause 5: Calling getFirst() or getLast() on empty deque
Deque<String> deque = new ArrayDeque<>();
deque.getFirst(); // NoSuchElementException
```

## Solutions

### Fix 1: Check hasNext() Before next()

```java
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    String element = it.next();
    // process element
}
```

### Fix 2: Use Optional for findFirst()

```java
Optional<String> first = list.stream()
    .filter(s -> s.startsWith("a"))
    .findFirst();

first.ifPresent(System.out::println);
// or
String value = first.orElse("default");
```

### Fix 3: Handle Empty Collections

```java
if (!list.isEmpty()) {
    String first = list.get(0);
    // process first element
} else {
    // handle empty case
}
```

### Fix 4: Use peek() Instead of next() for Inspection

```java
Deque<String> stack = new ArrayDeque<>(Arrays.asList("a", "b"));
Optional<String> top = Optional.ofNullable(stack.peek());
top.ifPresent(System.out::println);
```

### Fix 5: Guard Scanner Input

```java
Scanner scanner = new Scanner(System.in);
if (scanner.hasNextLine()) {
    String line = scanner.nextLine();
    // process line
} else {
    // no input available
}
```

## Prevention Checklist

- Always check `hasNext()` before calling `next()` on iterators and enumerations
- Use `Optional` return types instead of throwing exceptions for missing elements
- Validate collection size before accessing elements by index
- Use `peek()` methods for inspection without removal
- Check `Scanner.hasNext()` / `hasNextLine()` before reading

## Related Errors

- [IllegalStateException]({{< relref "/languages/java/illegalstateexception" >}}) — iterator or scanner in invalid state
- [UnsupportedOperationException]({{< relref "/languages/java/unsupportedoperationexception" >}}) — operation not supported on collection
- [EmptyStackException]({{< relref "/languages/java/emptystackexception" >}}) — stack is empty during pop/peek
