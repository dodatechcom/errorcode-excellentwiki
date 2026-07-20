---
title: "[Solution] Java NoSuchElementException — Scanner Input Fix"
description: "Fix Java NoSuchElementException from Scanner.hasNext() by checking hasNext() before next(), handling end-of-input, and using try-catch for input parsing."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# NoSuchElementException — Scanner Input Fix

A `NoSuchElementException` from `Scanner` is thrown when `next()`, `nextLine()`, `nextInt()`, or similar methods are called after the input is exhausted — `hasNext()` returned `false` but the code called `next()` anyway.

## Description

The `Scanner` class reads tokens from an input source. When all input has been consumed, `hasNext()` returns `false`. Calling `next()` or any `nextXxx()` method after this point throws `NoSuchElementException`. This commonly happens when reading from files, System.in, or strings without checking for end-of-input.

Message variants:

- `java.util.NoSuchElementException: No line found`
- `java.util.NoSuchElementException: Next int: <no value>`
- `java.util.NoSuchElementException`
- `java.util.InputMismatchException` (related — wrong token type)

## Common Causes

```java
// Cause 1: Calling next() without checking hasNext()
Scanner scanner = new Scanner("a b c");
while (scanner.hasNext()) {
    String token = scanner.next();
}
scanner.next();  // NoSuchElementException — input exhausted

// Cause 2: Reading past end of file
Scanner fileScanner = new Scanner(new File("data.txt"));
while (fileScanner.hasNextLine()) {
    String line = fileScanner.nextLine();
}
fileScanner.nextLine();  // NoSuchElementException

// Cause 3: Wrong delimiter causes unexpected token count
Scanner scanner = new Scanner("one,two,three");
scanner.useDelimiter(",");
while (scanner.hasNext()) {
    System.out.println(scanner.next());
}
scanner.next();  // NoSuchElementException

// Cause 4: Reading from empty System.in
Scanner scanner = new Scanner(System.in);
String input = scanner.nextLine();  // blocks or throws if stdin closed

// Cause 5: Using nextInt() when token is not an integer
Scanner scanner = new Scanner("abc");
int value = scanner.nextInt();  // InputMismatchException (related)
```

## Solutions

### Fix 1: Always check hasNext() before next()

```java
Scanner scanner = new Scanner(input);
while (scanner.hasNextLine()) {
    String line = scanner.nextLine();
    process(line);
}
// Don't call scanner.nextLine() here — input is exhausted
```

### Fix 2: Handle end-of-input with try-catch

```java
import java.util.NoSuchElementException;
import java.util.Scanner;

public class SafeInputReader {
    public static String readToken(Scanner scanner) {
        try {
            if (scanner.hasNext()) {
                return scanner.next();
            }
        } catch (NoSuchElementException e) {
            System.err.println("Input exhausted: " + e.getMessage());
        }
        return null;
    }

    public static int readInt(Scanner scanner) {
        try {
            if (scanner.hasNextInt()) {
                return scanner.nextInt();
            } else {
                System.err.println("Not an integer: "
                    + (scanner.hasNext() ? scanner.next() : "<empty>"));
            }
        } catch (NoSuchElementException e) {
            System.err.println("No more input available");
        }
        return -1;  // default value
    }
}
```

### Fix 3: Use hasNext() with specific type check

```java
Scanner scanner = new Scanner(input);
while (true) {
    if (scanner.hasNextInt()) {
        int value = scanner.nextInt();
        System.out.println("Integer: " + value);
    } else if (scanner.hasNextDouble()) {
        double value = scanner.nextDouble();
        System.out.println("Double: " + value);
    } else if (scanner.hasNextLine()) {
        String line = scanner.nextLine();
        System.out.println("Line: " + line);
    } else {
        break;  // no more input
    }
}
```

### Fix 4: Read all lines safely from a file

```java
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public static List<String> readAllLines(String filePath) throws Exception {
    List<String> lines = new ArrayList<>();
    try (Scanner scanner = new Scanner(new File(filePath))) {
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine());
        }
    }
    return lines;
}
```

### Fix 5: Use BufferedReader for line-by-line input (preferred over Scanner)

```java
import java.io.BufferedReader;
import java.io.FileReader;

// BufferedReader avoids Scanner's NoSuchElementException entirely
try (BufferedReader reader = new BufferedReader(new FileReader("data.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        process(line);
    }
    // null check is built-in — no exception on end-of-input
}
```

## Prevention Checklist

- Always call `hasNext()` or `hasNextXxx()` before `next()` or `nextXxx()`.
- Use try-catch around `Scanner` operations in production code.
- Prefer `BufferedReader` over `Scanner` for file reading — it uses null checks instead of exceptions.
- Verify the input source is not empty before creating a `Scanner`.
- Close `Scanner` in a try-with-resources block.
- Use `hasNextLine()` as the loop condition for line-by-line reading.

## Related Errors

- [InputMismatchException](../reached-eof-while-parsing) — wrong token type for Scanner
- [NoSuchElementException](../nosuchelementexception) — general no such element
- [IllegalStateException](../ise-iterator) — Scanner already closed
