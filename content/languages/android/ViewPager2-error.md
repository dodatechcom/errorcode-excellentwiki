---
title: "ViewPager2 Error"
description: "Fix ViewPager2 and fragment adapter configuration errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ViewPager2 does not display pages or fragments correctly

## Common Causes

- FragmentStateAdapter not properly configured
- ViewPager2 not connected to TabLayout
- Page transformer causing visual glitches
- Offscreen page limit not set for performance

## Fixes

- Use FragmentStateAdapter with FragmentActivity
- Connect with TabLayoutMediator
- Set offscreenPageLimit for smooth swiping
- Avoid heavy operations in page creation

## Code Example

```kotlin
// Setup ViewPager2 with fragments
val adapter = ViewPagerAdapter(this)
viewPager2.adapter = adapter

// Connect with TabLayout:
TabLayoutMediator(tabLayout, viewPager2) { tab, position ->
    tab.text = titles[position]
}.attach()

// FragmentStateAdapter:
class ViewPagerAdapter(activity: FragmentActivity) :
    FragmentStateAdapter(activity) {
    override fun getItemCount() = 3
    override fun createFragment(position: Int): Fragment {
        return when (position) {
            0 -> HomeFragment()
            1 -> SearchFragment()
            2 -> ProfileFragment()
            else -> throw IllegalArgumentException()
        }
    }
}
```

# FragmentStateAdapter for fragments
# RecyclerView.Adapter for views
# offscreenPageLimit for preloading
