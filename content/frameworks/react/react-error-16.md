---
title: "Concurrent features - startTransition errors"
description: "Error related to React's concurrent features using startTransition. This can happen when transitions are used incorrectly, when they cause state inconsistencies, or when combined with synchronous state updates."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "concurrent", "starttransition", "performance"]
severity: "error"
solution: "Use startTransition only for non-urgent updates like search filtering or tab switching. Combine with useTransition for pending states. Avoid using transitions for immediate user feedback like button clicks. Ensure state updates within transitions are consistent."
---

Error related to React's concurrent features using startTransition. This can happen when transitions are used incorrectly, when they cause state inconsistencies, or when combined with synchronous state updates.

## Solution

Use startTransition only for non-urgent updates like search filtering or tab switching. Combine with useTransition for pending states. Avoid using transitions for immediate user feedback like button clicks. Ensure state updates within transitions are consistent.

## Code Example

```javascript
  import { useTransition, useState, startTransition } from 'react';
  
  // BAD: Using transition for urgent update
  function BadSearch() {
    const [query, setQuery] = useState('');
    
    const handleChange = (e) => {
      startTransition(() => {
        setQuery(e.target.value); // Wrong: this is urgent
      });
    };
    
    return <input onChange={handleChange} value={query} />;
  }
  
  // GOOD: Proper useTransition usage
  function GoodSearch({ items }) {
    const [query, setQuery] = useState('');
    const [filteredItems, setFilteredItems] = useState(items);
    const [isPending, startTransition] = useTransition();
    
    const handleChange = (e) => {
      const value = e.target.value;
      setQuery(value); // Urgent: update input immediately
      
      startTransition(() => {
        // Non-urgent: filter items in background
        setFilteredItems(
          items.filter(item => 
            item.name.toLowerCase().includes(value.toLowerCase())
          )
        );
      });
    };
    
    return (
      <div>
        <input onChange={handleChange} value={query} />
        {isPending && <div>Filtering...</div>}
        <ItemList items={filteredItems} />
      </div>
    );
  }
  
  // GOOD: Tab switching with transitions
  function Tabs({ tabs }) {
    const [activeTab, setActiveTab] = useState(0);
    const [isPending, startTransition] = useTransition();
    
    const selectTab = (index) => {
      startTransition(() => {
        setActiveTab(index);
      });
    };
    
    return (
      <div>
        <div className="tabs">
          {tabs.map((tab, index) => (
            <button 
              key={tab.id}
              onClick={() => selectTab(index)}
              disabled={activeTab === index}
            >
              {tab.label}
            </button>
          ))}
        </div>
        <div style={{ opacity: isPending ? 0.7 : 1 }}>
          {tabs[activeTab].content}
        </div>
      </div>
    );
  }
```
