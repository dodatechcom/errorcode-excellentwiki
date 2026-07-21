---
title: "Navigation Graph Error"
description: "Fix Android Navigation graph configuration and XML errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Navigation graph has errors preventing navigation between destinations

## Common Causes

- Start destination not set in nav graph
- Destination ID not found in navigation
- Action ID mismatch between destinations
- Nav graph not included in host fragment

## Fixes

- Set app:startDestination on navigation root
- Verify destination IDs match navigation calls
- Use consistent action IDs between screens
- Add NavHostFragment with graph reference

## Code Example

```kotlin
<!-- nav_graph.xml -->
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/nav_graph"
    app:startDestination="@id/homeFragment">

    <fragment
        android:id="@+id/homeFragment"
        android:name="com.example.HomeFragment"
        android:label="Home">
        <action
            android:id="@+id/action_home_to_detail"
            app:destination="@id/detailFragment" />
    </fragment>

    <fragment
        android:id="@+id/detailFragment"
        android:name="com.example.DetailFragment"
        android:label="Detail" />
</navigation>
```

<!-- Activity layout with NavHostFragment -->
<androidx.fragment.app.FragmentContainerView
    android:id="@+id/nav_host_fragment"
    android:name="androidx.navigation.fragment.NavHostFragment"
    app:navGraph="@navigation/nav_graph"
    app:defaultNavHost="true" />
