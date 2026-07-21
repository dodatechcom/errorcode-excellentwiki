---
title: "[Solution] Groovy Testing Error"
description: "Spock framework testing errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Testing Error

Spock framework testing errors.

### Common Causes
Wrong specification; missing @Subject

### How to Fix
```groovy
import spock.lang.Specification
class MySpec extends Specification {
    def "should add numbers"() {
        expect:
        1 + 1 == 2
    }
}
```

### Examples
```groovy
def "should parse JSON"() {
    given:
    def json = '{"name": "test"}'
    
    when:
    def result = new JsonSlurper().parseText(json)
    
    then:
    result.name == 'test'
}
```
