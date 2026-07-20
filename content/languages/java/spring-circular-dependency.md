---
title: "[Solution] Java CircularDependencyException — Spring beans depend on each other"
description: "Fix Java CircularDependencyException by using @Lazy injection, redesigning beans, or switching to setter injection. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 103
---

# CircularDependencyException — Spring beans depend on each other

A `CircularDependencyException` is thrown when two or more Spring beans have a circular dependency chain, meaning each bean requires the other to be constructed before it can be created. Spring cannot resolve this for constructor-injected singletons.

## Description

Spring creates singleton beans eagerly during context initialization. When Bean A requires Bean B and Bean B requires Bean A through constructor injection, the container enters an infinite loop. Spring detects this and throws an exception. Common message variants include:

- `Requested bean is a singleton in circular reference`
- `The dependencies of some of the beans in the application context form a cycle`
- `BeanCreationException: Circular reference`
- `unresolvable circular reference`

## Common Causes

```java
// Cause 1: Constructor injection cycle
@Service
public class OrderService {
    private final PaymentService paymentService;
    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }
}

@Service
public class PaymentService {
    private final OrderService orderService;
    public PaymentService(OrderService orderService) {
        this.orderService = orderService;
    }
}

// Cause 2: Three-bean cycle
@Service public class ServiceA { @Autowired private ServiceB b; }
@Service public class ServiceB { @Autowired private ServiceC c; }
@Service public class ServiceC { @Autowired private ServiceA a; }

// Cause 3: Configuration bean referencing another config bean
@Configuration
public class DataSourceConfig {
    @Autowired private CacheConfig cacheConfig;
}
@Configuration
public class CacheConfig {
    @Autowired private DataSourceConfig dataSourceConfig;
}
```

## Solutions

### Fix 1: Use @Lazy to defer initialization

```java
@Service
public class OrderService {
    private final PaymentService paymentService;

    public OrderService(@Lazy PaymentService paymentService) {
        this.paymentService = paymentService;
    }
}

// The proxy is injected immediately; the real bean is resolved on first use
@Service
public class PaymentService {
    private final OrderService orderService;

    public PaymentService(@Lazy OrderService orderService) {
        this.orderService = orderService;
    }
}
```

### Fix 2: Switch to setter or field injection for one side

```java
@Service
public class OrderService {
    private PaymentService paymentService;

    @Autowired
    public void setPaymentService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }
}

@Service
public class PaymentService {
    private final OrderService orderService;

    public PaymentService(OrderService orderService) {
        this.orderService = orderService;
    }
}
```

### Fix 3: Extract shared logic to a third bean

```java
// Before: OrderService <-> PaymentService cycle
// After: Both depend on TransactionLogger (no cycle)

@Service
public class TransactionLogger {
    public void logTransaction(Long orderId, double amount) {
        // Shared logic extracted from both services
    }
}

@Service
public class OrderService {
    private final TransactionLogger logger;
    public OrderService(TransactionLogger logger) { this.logger = logger; }
}

@Service
public class PaymentService {
    private final TransactionLogger logger;
    public PaymentService(TransactionLogger logger) { this.logger = logger; }
}
```

### Fix 4: Use ApplicationContext lookup as last resort

```java
@Service
public class OrderService {
    private final ApplicationContext context;
    private PaymentService paymentService;

    public OrderService(ApplicationContext context) {
        this.context = context;
    }

    @PostConstruct
    public void init() {
        this.paymentService = context.getBean(PaymentService.class);
    }
}

@Service
public class PaymentService {
    private final OrderService orderService;
    public PaymentService(OrderService orderService) {
        this.orderService = orderService;
    }
}
```

### Fix 5: Use @DependsSibling (Spring Framework 6.1+)

```java
@Service
@DependsOn("paymentService")
public class OrderService {
    // Explicitly declares the creation order
}
```

## Prevention Checklist

- Favor constructor injection and design beans to avoid mutual dependencies
- Use `@Lazy` when a circular reference is genuinely needed
- Extract shared logic into a dedicated service to break cycles
- Review domain design — circular dependencies often indicate a design smell
- Use setter injection selectively to break cycles while keeping constructor injection for other dependencies
- Enable `spring.main.allow-circular-references=true` only as a temporary workaround during migration

## Related Errors

- [BeanCreationException](/languages/java/spring-bean-creation-failed/)
- [NoSuchBeanDefinitionException](/languages/java/spring-no-bean-found/)
- [StackOverflowError](/languages/java/stackoverflowerror/)
