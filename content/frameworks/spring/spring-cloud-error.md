---
title: "[Solution] Spring Cloud Service Discovery Error -- How to Fix"
description: "Fix Spring Cloud service discovery errors. Resolve Eureka, Consul, and service registration issues in Spring."
frameworks: ["spring"]
error-types: ["connection-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring Cloud service discovery error occurs when microservices cannot register with or discover other services through the service registry. This breaks inter-service communication in distributed systems.

## Why It Happens

Spring Cloud uses service registries like Eureka, Consul, or Nacos for service discovery. Errors occur when the registry server is not running, when client configuration points to the wrong registry URL, when health checks fail, when network partitions isolate services, or when the registry's heartbeat mechanism loses track of services.

## Common Error Messages

```
com.netflix.discovery.shared.transport.TransportException: Cannot execute request on any known server
```

```
org.springframework.cloud.client.ServiceUnavailableException: No instances available
```

```
com.netflix.discovery.DiscoveryClient: Fetch registry failed
```

```
java.net.ConnectException: Connection refused: connect
```

## How to Fix It

### 1. Configure Service Registration

Set up service registration with Eureka:

```yaml
# application.yml
spring:
  application:
    name: user-service

eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
    fetch-registry: true
    register-with-eureka: true
  instance:
    prefer-ip-address: true
    lease-renewal-interval-in-seconds: 30
    lease-expiration-duration-in-seconds: 90
```

### 2. Set Up Discovery Client

Use the discovery client to find services:

```java
@Service
public class OrderService {

    private final DiscoveryClient discoveryClient;
    private final RestTemplate restTemplate;

    public OrderService(DiscoveryClient discoveryClient, RestTemplate restTemplate) {
        this.discoveryClient = discoveryClient;
        this.restTemplate = restTemplate;
    }

    // Using RestTemplate with Load Balancer
    @Bean
    @LoadBalanced
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }

    public User getUser(Long userId) {
        return restTemplate.getForObject(
            "http://user-service/api/users/{id}", User.class, userId);
    }

    // Using WebClient (reactive)
    public Flux<String> getServiceInstances() {
        return discoveryClient.getServices()
            .flatMapMany(Flux::fromIterable)
            .map(service -> {
                List<ServiceInstance> instances = discoveryClient.getInstances(service);
                return service + " at " + instances.get(0).getUri();
            });
    }
}
```

### 3. Handle Discovery Failures Gracefully

Add fallback mechanisms:

```java
@Service
public class ResilientOrderService {

    private final RestTemplate restTemplate;

    @CircuitBreaker(name = "userService", fallbackMethod = "getUserFallback")
    @Retry(name = "userService")
    public User getUser(Long userId) {
        return restTemplate.getForObject(
            "http://user-service/api/users/{id}", User.class, userId);
    }

    public User getUserFallback(Long userId, Exception e) {
        log.warn("User service unavailable, using fallback: {}", e.getMessage());
        return new User(userId, "Unknown User", "unknown@example.com");
    }
}
```

### 4. Run Service Registry Locally

Start Eureka server:

```java
@SpringBootApplication
@EnableEurekaServer
public class EurekaServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServerApplication.class, args);
    }
}
```

```yaml
# Eureka server config
server:
  port: 8761

eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
  server:
    wait-time-in-ms-when-sync-empty: 0
```

## Common Scenarios

**Scenario 1: Service registers but is not discoverable.**
Check that the service name matches what clients use. Eureka is case-sensitive with service names.

**Scenario 2: Discovery fails in Docker/Kubernetes.**
Use the host's IP instead of `localhost`. Set `eureka.instance.prefer-ip-address=true` and configure the IP address.

**Scenario 3: Service shows as DOWN in registry.**
Verify the `/actuator/health` endpoint is accessible. Eureka uses this for health checks.

## Prevent It

1. **Run Eureka in HA mode** with multiple instances for production.

2. **Use circuit breakers** (Resilience4j) to handle service discovery failures gracefully.

3. **Monitor the Eureka dashboard** to verify all services are registered and healthy.
