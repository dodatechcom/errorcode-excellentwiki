---
title: "Solved JavaScript framer-motion Error — How to Fix"
date: 2026-03-20T15:30:15+00:00
description: "Learn how to resolve JavaScript Framer Motion animation and React component motion errors."
categories: ["javascript"]
keywords: ["framer motion error", "motion animation", "react animation", "framer motion react", "animation error"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Framer Motion errors occur when animation components receive invalid props, use incompatible React versions, or have incorrect motion value configurations. The library requires proper prop types and animation controls.

Common causes include:
- Invalid animation prop values
- Motion component not properly exported
- Animation variants not resolving correctly
- Using `useAnimation` outside motion components
- React version mismatch

## Common Error Messages

```
Error: `motion` is not exported from "framer-motion"
```

```
TypeError: Cannot read properties of undefined (reading 'animation')
```

```
Warning: Function components cannot be given refs
```

## How to Fix It

### 1. Configure Motion Components

Use motion components correctly.

```jsx
import { motion, AnimatePresence } from "framer-motion";

// Basic motion component
function Box() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: "easeOut" }}
    >
      Animated content
    </motion.div>
  );
}

// Motion with variants
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 }
};

function List() {
  return (
    <motion.ul
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      {items.map((item) => (
        <motion.li key={item.id} variants={itemVariants}>
          {item.name}
        </motion.li>
      ))}
    </motion.ul>
  );
}
```

### 2. Use Animation Controls

Control animations programmatically.

```jsx
import { motion, useAnimation, useMotionValue } from "framer-motion";

function ControlledAnimation() {
  const controls = useAnimation();
  
  const sequence = async () => {
    await controls.start({ x: 100, transition: { duration: 0.5 } });
    await controls.start({ scale: 1.5, transition: { duration: 0.3 } });
    await controls.start({ x: 0, scale: 1 });
  };
  
  return (
    <motion.div
      animate={controls}
      onHoverStart={() => controls.start({ scale: 1.1 })}
      onHoverEnd={() => controls.start({ scale: 1 })}
    >
      Hover me
    </motion.div>
  );
}

// Use motion values
function DragExample() {
  const x = useMotionValue(0);
  const scale = useTransform(x, [-100, 0, 100], [1.5, 1, 1.5]);
  
  return (
    <motion.div
      drag="x"
      style={{ x, scale }}
      dragConstraints={{ left: -100, right: 100 }}
    >
      Drag me
    </motion.div>
  );
}
```

### 3. Handle AnimatePresence

Animate elements entering and leaving.

```jsx
import { motion, AnimatePresence } from "framer-motion";

function Modal({ isOpen, onClose, children }) {
  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 0.9 }}
          transition={{ duration: 0.2 }}
          onClick={onClose}
        >
          <motion.div
            initial={{ y: -50 }}
            animate={{ y: 0 }}
            exit={{ y: 50 }}
            onClick={(e) => e.stopPropagation()}
          >
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

// List animations
function AnimatedList({ items }) {
  return (
    <ul>
      <AnimatePresence>
        {items.map((item) => (
          <motion.li
            key={item.id}
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            layout
          >
            {item.text}
          </motion.li>
        ))}
      </AnimatePresence>
    </ul>
  );
}
```

## Common Scenarios

### Scenario 1: Scroll Animations

Animate based on scroll position:

```jsx
import { motion, useScroll, useTransform } from "framer-motion";

function ParallaxSection() {
  const { scrollYProgress } = useScroll();
  const y = useTransform(scrollYProgress, [0, 1], [0, -200]);
  const opacity = useTransform(scrollYProgress, [0, 0.5], [1, 0]);
  
  return (
    <motion.div style={{ y, opacity }}>
      Parallax content
    </motion.div>
  );
}

// Scroll-triggered animation
function ScrollReveal() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 100 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-100px" }}
      transition={{ duration: 0.5 }}
    >
      Revealed on scroll
    </motion.div>
  );
}
```

### Scenario 2: Gesture Animations

Handle user gestures:

```jsx
import { motion } from "framer-motion";

function InteractiveCard() {
  return (
    <motion.div
      whileHover={{ scale: 1.05, rotate: 2 }}
      whileTap={{ scale: 0.95 }}
      drag
      dragConstraints={{ left: 0, right: 300, top: 0, bottom: 300 }}
      dragElastic={0.1}
    >
      Interactive card
    </motion.div>
  );
}
```

## Prevent It

- Import `motion` and `AnimatePresence` from `"framer-motion"`
- Use `layout` prop for automatic layout animations
- Wrap conditional elements in `AnimatePresence` for exit animations
- Use `whileInView` with `viewport={{ once: true }}` for scroll reveals
- Keep animation values simple and test with React DevTools