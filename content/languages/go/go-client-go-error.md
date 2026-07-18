---
title: "[Solution] Go client-go Error — How to Fix"
description: "Fix Go client-go errors. Handle Kubernetes client configuration, dynamic clients, informers, and watches."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go client-go Error

Fix Go client-go errors. Handle Kubernetes client configuration, dynamic clients, informers, and watches.

## Why It Happens

- Client cannot connect to cluster because of invalid kubeconfig
- Informer does not start because the cache is not synced
- Dynamic client fails because of wrong API version or kind
- Watch channel is not properly handled causing missed events

## Common Error Messages

```
client-go: unable to load kubeconfig
```
```
client-go: cache not synced
```
```
client-go: no matches for kind
```
```
client-go: watch channel closed
```

## How to Fix It

### Solution 1: Create clientset

```go
config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
if err != nil { config, err = rest.InClusterConfig() }
if err != nil { log.Fatal(err) }

clientset, err := kubernetes.NewForConfig(config)
```

### Solution 2: Use dynamic client

```go
dynamicClient, err := dynamic.NewForConfig(config)
// List resources
list, err := dynamicClient.Resource(schema.GroupVersionResource{
    Group:    "apps",
    Version:  "v1",
    Resource: "deployments",
}).Namespace("default").List(ctx, metav1.ListOptions{})
```

### Solution 3: Use informers

```go
factory := informers.NewSharedInformerFactory(clientset, 30*time.Second)
deployInformer := factory.Apps().V1().Deployments().Informer()

stopCh := make(chan struct{})
defer close(stopCh)
factory.Start(stopCh)
factory.WaitForCacheSync(stopCh)

for _, d := range factory.Apps().V1().Deployments().Lister().Deployments("default") {
    fmt.Println(d.Name)
}
```

### Solution 4: Handle watch

```go
watcher, err := clientset.CoreV1().Pods("").Watch(ctx, metav1.ListOptions{})
for event := range watcher.ResultChan() {
    pod := event.Object.(*corev1.Pod)
    switch event.Type {
    case watch.Added: fmt.Println("Added:", pod.Name)
    case watch.Modified: fmt.Println("Modified:", pod.Name)
    case watch.Deleted: fmt.Println("Deleted:", pod.Name)
    }
}
```

## Common Scenarios

- client-go cannot connect because kubeconfig is invalid
- Informer does not return results because cache is not synced
- Watch events are missed because the channel is not read fast enough

## Prevent It

- Use rest.InClusterConfig() for in-cluster and clientcmd for local development
- Always call WaitForCacheSync before reading from informers
- ['Use watch bookmarks to handle reconnection', '```go\nlistOpts := metav1.ListOptions{ResourceVersion: "0"}\nwatcher, _ := clientset.CoreV1().Pods("").Watch(ctx, listOpts)\n```']
