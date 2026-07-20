---
title: "[Solution] Java method does not override or implement a method from a supertype — Fix @Override"
description: "Fix Java compiler error 'method does not override or implement a method from a supertype' by verifying method signature, spelling, return type, and parameters. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 414
---

# Java Compiler Error: method does not override or implement a method from a supertype

This compile-time error occurs when a method annotated with `@Override` doesn't actually override a method from the superclass or implement a method from an interface. The `@Override` annotation is a compile-time check that ensures your method signature matches a supertype method exactly.

## Error Message

```
error: method does not override or implement a method from a supertype
    @Override
    ^
```

Other variants:

```
error: method does not override a method from its superclass
error: method does not implement a method from an interface
```

## Common Causes

### Cause 1: Typo in Method Name

```java
class Dog extends Animal {
    @Override
    public void Speack() { // ERROR: typo — should be "speak"
        System.out.println("Woof");
    }
}
```

### Cause 2: Wrong Parameter Types

```java
class MyList extends ArrayList<String> {
    @Override
    public boolean add(String item) { // OK — matches ArrayList.add(E)
    }

    @Override
    public boolean addAll(Collection<Integer> items) { // ERROR: wrong type parameter
    }
}
```

### Cause 3: Wrong Return Type

```java
class MyService implements Comparable<MyService> {
    @Override
    public int compareTo(MyService other) { // OK
        return 0;
    }
}

class MyComparable implements Comparable<String> {
    @Override
    public Integer compareTo(String other) { // ERROR: return type must be int
        return 0;
    }
}
```

### Cause 4: Missing @Override on Interface Method

```java
interface Greeter {
    void greet();
}

class FriendlyGreeter implements Greeter {
    public void greet() { // OK even without @Override, but @Override is recommended
        System.out.println("Hello!");
    }

    @Override
    public void SayHello() { // ERROR: method not in interface
        System.out.println("Hi!");
    }
}
```

### Cause 5: Static Method Hiding Confused with Overriding

```java
class Parent {
    public static void doSomething() { }
}

class Child extends Parent {
    @Override
    public static void doSomething() { } // ERROR: static methods cannot be overridden
}
```

### Cause 6: Private Method in Parent

```java
class Parent {
    private void helper() { }
}

class Child extends Parent {
    @Override
    void helper() { } // ERROR: cannot override private method
}
```

## Solutions

### Fix 1: Verify Method Signature

Ensure the method name, parameter types, and return type exactly match the supertype method.

```java
class Dog extends Animal {
    @Override
    public void speak() { // exact match with Animal.speak()
        System.out.println("Woof");
    }
}
```

### Fix 2: Check Spelling Carefully

```java
class Dog extends Animal {
    @Override
    public void speak() { // fixed typo: "Speack" -> "speak"
        System.out.println("Woof");
    }
}
```

### Fix 3: Match Return Type Exactly

```java
class MyComparable implements Comparable<String> {
    @Override
    public int compareTo(String other) { // return type must be int, not Integer
        return 0;
    }
}
```

### Fix 4: Remove @Override if Not Overriding

If the method isn't overriding anything, remove the annotation.

```java
class MyService {
    // No @Override — this is a new method, not an override
    public void customMethod() { }
}
```

### Fix 5: Use @Override for All Overrides

Always use `@Override` when overriding methods — it catches errors at compile time.

```java
class Dog extends Animal {
    @Override
    public void speak() {
        System.out.println("Woof");
    }

    @Override
    public String toString() {
        return "Dog";
    }
}
```

### Fix 6: Check Interface Method Signatures

When implementing an interface, verify all abstract methods and their signatures.

```java
interface Repository<T> {
    T findById(long id);
    List<T> findAll();
    void save(T entity);
}

class UserRepository implements Repository<User> {
    @Override
    public User findById(long id) { } // OK

    @Override
    public List<User> findAll() { } // OK

    @Override
    public void save(User entity) { } // OK
}
```

## Prevention Checklist

- Always use `@Override` when overriding methods — it's your safety net
- Verify the exact method signature (name, parameter types, return type) before adding `@Override`
- Use your IDE's "Override Methods" feature to generate method stubs automatically
- Check for typos in method names — they're the most common cause
- Remember that `@Override` doesn't work on static methods or private methods
- When implementing interfaces, implement all abstract methods with correct signatures

## Related Errors

- [cannot find symbol: method (method-not-found)](/languages/java/method-not-found)
- [X is abstract; cannot be instantiated (abstract-method)](/languages/java/abstract-method)
- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
