---
title: "Compose XML Interop Error"
description: "Fix Compose and XML view interoperability errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose and XML views do not interoperate correctly in same layout

## Common Causes

- AndroidView not properly embedding XML view
- ComposeView not finding correct parent
- View not updating when Compose state changes
- Interop causing layout measurement issues

## Fixes

- Use AndroidView for embedding XML in Compose
- Use ComposeView for embedding Compose in XML
- Bridge state between Compose and XML views
- Measure interop layouts carefully

## Code Example

```kotlin
// Compose in XML layout:
class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Find ComposeView in XML
        findViewById<ComposeView>(R.id.compose_view).setContent {
            MyComposeContent()
        }
    }
}

// XML in Compose:
@Composable
fun MapScreen() {
    AndroidView(
        factory = { context ->
            MapView(context).apply {
                onCreate(null)
                onResume()
            }
        },
        update = { mapView ->
            mapView.getMapAsync { map ->
                // Update map
            }
        }
    )
}
```

# AndroidView: XML view in Compose
# ComposeView: Compose in XML layout
# State bridge with callback or shared ViewModel
