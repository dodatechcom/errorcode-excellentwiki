---
title: "Fragment View Binding Error"
description: "Fix Fragment view binding lifecycle and null reference errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Fragment view binding causes null pointer exception or memory leak

## Common Causes

- Binding accessed after onDestroyView
- Fragment view binding not properly nulled
- ViewBinding inflated in wrong lifecycle method
- Binding used before onViewCreated

## Fixes

- Null binding in onDestroyView
- Use viewLifecycleOwner.lifecycleScope for coroutine scope
- Inflate binding in onCreateView or onViewCreated
- Do not store binding in Fragment instance

## Code Example

```kotlin
class MyFragment : Fragment() {
    private var _binding: FragmentMyBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentMyBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        // Use binding here
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null  // Prevent memory leak
    }
}
```

# Always null binding in onDestroyView
# Use viewLifecycleOwner for scopes
# Do not reference binding after onDestroyView
