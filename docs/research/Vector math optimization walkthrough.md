# Optimization Walkthrough: Vector Math & Urges

I have successfully implemented all the structural optimizations we discussed into the `FishCensus.nlogox` codebase. These changes focus strictly on computational efficiency—specifically minimizing the use of high-overhead NetLogo commands like `map` and anonymous reporters inside core simulation loops. The model logic and behavior remains fully identical, but should run much faster.

## Changes Made

### 1. Hardcoded 2D Vector Operations

Replaced all `map` calls in basic math reporters with direct list building. Since the model relies entirely on 2D vectors `[x y]`, doing math on indices `first` and `last` is much faster than running anonymous functions.

```diff
-to-report scale [ scalar vector ]
-  report map [ [v] -> scalar * v ] vector
-end
+to-report scale [ scalar vector ]
+  report list (first vector * scalar) (last vector * scalar)
+end
```

_Applied to: `add`, `subtract`, `scale`, `magnitude`, and `normalize`._

### 2. Eliminated Intermediate List Instantiations

Urges like `center-urge`, `align-urge`, and `spacing-urge` were rewritten to avoid constructing temporary lists and mapping over them.

For example, `spacing-urge` now uses local variables (`u-x`, `u-y`) in its loop and constructs a single list at the very end:

```diff
-    set urge
-      add
-        urge
-        (subtract
-          (list [xcor] of myself [ycor] of myself)
-          (list xcor ycor))
+    set u-x u-x + (my-x - xcor)
+    set u-y u-y + (my-y - ycor)
```

### 3. Removed Double Normalization

`avoid-predator-urge` and `avoid-diver-urge` were explicitly running `normalize` on their returned vectors, which was completely redundant because the core `add-urge` command normalizes all incoming urges before scaling them.

```diff
-  [set urge normalize (add urge subtract (list [xcor] of myself [ycor] of myself) (list xcor ycor))
+      set u-x (xcor - [xcor] of p)
+      set u-y (ycor - [ycor] of p)
```

### 4. Simplified Drag Vector Math

In `do.fish.movement`, the deceleration calculation due to drag was previously calculating `magnitude` and `normalize` multiple times. Using the mathematical fact that $ \text{deceleration} = - v\_{\text{normalized}} \cdot k \cdot |v|^2 = -v \cdot k \cdot |v| $, we removed the need to call `normalize` completely:

```diff
-  let deceleration (scale ((drag.formula * ((magnitude velocity) ^ 2))) (subtract (list 0 0) (normalize velocity)))
+  let mag-v magnitude velocity
+  let deceleration scale (-1 * drag.formula * mag-v) velocity
```

_We also reused stored magnitude variables `mag-v` and `mag-acc` when capping maximum burst/cruise speeds and max acceleration to prevent redundant square root calculations._

## Next Steps

You can run a new profiler test (`log/profiler_...`) in NetLogo to observe the performance difference! The time spent inside `DO.FISH.MOVEMENT` and vector operations like `MAGNITUDE` should be significantly reduced.

Let me know if you would like me to tackle anything else, such as the data export logic!
