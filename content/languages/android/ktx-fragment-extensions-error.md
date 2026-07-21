---
title: "Fragment KTX Error"
description: "Fix AndroidX Fragment KTX extensions and argument delegate errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Fragment argument delegates and KTX extensions produce wrong values

## Common Causes

- by navArgs() not finding navigation arguments
- Argument delegate returning null
- Fragment KTX dependency not added
- SavedStateHandle not properly initialized

## Fixes

- Add fragment-ktx dependency
- Use by navArgs() for Safe Args navigation
- Verify argument types match nav graph definition
- Use SavedStateHandle for process-death-safe state

## Code Example

```kotlin
dependencies {
    implementation "androidx.fragment:fragment-ktx:1.6.2"
}

// Navigation arguments:
class MyFragment : Fragment() {
    private val args: MyFragmentArgs by navArgs()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val itemId = args.itemId
    }
}

// Fragment factory:
class MyFragment : Fragment() {
    companion object {
        fun newInstance(itemId: Long): MyFragment {
            return MyFragment().apply {
                arguments = bundleOf("itemId" to itemId)
            }
        }
    }
}
```

# by navArgs(): navigation Safe Args
# by viewModels(): ViewModel delegate
# by activityViewModels(): shared ViewModel
