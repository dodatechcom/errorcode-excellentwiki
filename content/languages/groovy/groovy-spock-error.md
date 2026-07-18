---
title: "[Solution] Groovy Spock Test Interaction Error"
description: "Fix Groovy Spock test interaction errors. Resolve mocking, stubbing, and test setup issues in Spock framework."
languages: ["groovy"]
error-types: ["test-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Spock test interaction errors occur when test interactions like mocking, stubbing, or verification fail. These errors indicate that the test setup does not match actual code behavior.

## Why It Happens

- Mock method called with unexpected arguments: The actual call does not match the stubbed arguments.
- Interaction verification fails due to call count mismatch: The method was called more or fewer times than expected.
- Stub return type does not match expected type: The return value cannot be coerced to the expected type.
- Test setup order affects interaction recording: Mocks must be configured before the when block.
- Static methods cannot be mocked by default: Spock does not mock static methods without PowerMock.

## How to Fix It

Use proper interaction syntax in Spock:

```groovy
class UserServiceSpec extends Specification {
    def "should call repository"() {
        given:
        def repository = Mock(UserRepository)
        def service = new UserService(repository)
        
        when:
        service.findUser(1)
        
        then:
        1 * repository.findById(1) >> new User(id: 1)
    }
}
```

Handle argument matching correctly:

```groovy
then:
1 * repository.save({ it.name == "Alice" }) >> savedUser
_ * repository.findAll() >> [user1, user2]
```

Use Spy for partial mocking:

```groovy
given:
def service = Spy(UserService)
service.someMethod(_) >> "mocked"

when:
def result = service.complexMethod()

then:
result == "expected"
```

Verify interaction counts:

```groovy
then:
2 * mock.process(_)  // Exactly 2 times
0 * mock.error(_)    // Never called
1..3 * mock.step(_)  // Between 1 and 3 times
```

Use data tables for parameterized tests:

```groovy
def "should validate #input returns #expected"() {
    expect:
    validator.validate(input) == expected
    
    where:
    input   || expected
    "valid" || true
    ""      || false
    null    || false
}
```

## Common Mistakes

- Placing interactions before when block. Interactions belong in then or expect blocks.
- Forgetting that Spock uses groovy.lang.Range for cardinality. Use 1, 2, 1..3 for ranges.
- Not mocking final classes. Use @Spy or PowerMock for final classes.
- Mocking too much instead of focusing on behavior. Mock only what is necessary for the test.
- Not cleaning up mocks between tests. Spock handles this automatically with @Subject.

## Related Pages

- [groovy-closure-error]({{< relref "/languages/groovy/groovy-closureerror-v2" >}}) - closure errors
- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-classcast-error-v2]({{< relref "/languages/groovy/groovy-casterror-v2" >}}) - class cast error
