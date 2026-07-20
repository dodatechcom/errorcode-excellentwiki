---
title: "[Solution] SwiftUI Dependency Injection Error"
description: "Fix SwiftUI dependency injection errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 115
---

SwiftUI dependency injection errors occur when services aren't properly provided through the environment, circular dependencies arise, or dependencies aren't available in previews.

## Common Causes

```swift
// Circular dependency
class ServiceA {
    let serviceB: ServiceB
    init(serviceB: ServiceB) { self.serviceB = serviceB }
}

class ServiceB {
    let serviceA: ServiceA // Circular!
    init(serviceA: ServiceA) { self.serviceA = serviceA }
}

// Missing environment injection in preview
struct MyView: View {
    @Environment(Service.self) var service
}
```

## How to Fix

**1. Use environment for dependency injection**

```swift
struct AppView: View {
    @State var service = APIService()
    
    var body: some View {
        ContentView()
            .environment(service)
    }
}

struct ContentView: View {
    @Environment(APIService.self) var api
    
    var body: some View {
        Button("Fetch") {
            Task { try await api.fetchData() }
        }
    }
}
```

**2. Create protocol-based dependencies**

```swift
protocol DataService {
    func fetch() async throws -> [Item]
}

@Observable
class LiveDataService: DataService {
    func fetch() async throws -> [Item] {
        // Real implementation
    }
}

// Preview with mock
struct PreviewDataService: DataService {
    func fetch() async throws -> [Item] {
        [.mock]
    }
}
```

**3. Break circular dependencies**

```swift
protocol ServiceAProtocol: AnyObject {}
protocol ServiceBProtocol: AnyObject {}

class ServiceA: ServiceAProtocol {
    weak var serviceB: ServiceBProtocol?
}

class ServiceB: ServiceBProtocol {
    weak var serviceA: ServiceAProtocol?
}
```

**4. Environment key pattern**

```swift
struct APIClientKey: EnvironmentKey {
    static let defaultValue: APIClient = LiveAPIClient()
}

extension EnvironmentValues {
    var apiClient: APIClient {
        get { self[APIClientKey.self] }
        set { self[APIClientKey.self] = newValue }
    }
}
```

**5. Preview providers**

```swift
#Preview {
    ContentView()
        .environment(APIClient.preview)
        .environment(CacheService.preview)
}
```

## Examples

Complete DI setup:
```swift
@Observable
class AppDependencies {
    let api: APIClient
    let cache: CacheService
    let analytics: AnalyticsService
    
    init(
        api: APIClient = LiveAPIClient(),
        cache: CacheService = LiveCacheService(),
        analytics: AnalyticsService = LiveAnalyticsService()
    ) {
        self.api = api
        self.cache = cache
        self.analytics = analytics
    }
}
```

## Related Errors

- [Environment Error](/languages/swift/swiftui-environment-error)
- [Observable Error](/languages/swift/swiftui-observable-error)
- [MainActor Error](/languages/swift/swift-mainactor-error)
