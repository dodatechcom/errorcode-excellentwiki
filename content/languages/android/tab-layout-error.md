---
title: "TabLayout Integration Error"
description: "Fix Material TabLayout and ViewPager2 integration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
TabLayout does not sync with ViewPager2 or tabs do not display correctly

## Common Causes

- TabLayoutMediator not connecting TabLayout to ViewPager2
- Tab custom view not inflating correctly
- Tab icon and text not showing together
- Tab selection listener not firing

## Fixes

- Connect TabLayout with ViewPager2 using TabLayoutMediator
- Use custom view layout for complex tab design
- Use TabItem with icon and text attributes
- Register OnTabSelectedListener for tab changes

## Code Example

```kotlin
// Connect TabLayout and ViewPager2
TabLayoutMediator(tabLayout, viewPager2) { tab, position ->
    when (position) {
        0 -> tab.text = "Home"
        1 -> tab.text = "Search"
        2 -> tab.text = "Profile"
    }
}.attach()

// Tab selection listener:
tabLayout.addOnTabSelectedListener(object : TabLayout.OnTabSelectedListener {
    override fun onTabSelected(tab: TabLayout.Tab) {
        viewPager2.currentItem = tab.position
    }
    override fun onTabUnselected(tab: TabLayout.Tab) {}
    override fun onTabReselected(tab: TabLayout.Tab) {}
})
```

# TabLayoutMediator syncs tabs and ViewPager2
# Use TabItem for simple tabs
# Use custom view for complex tabs
