The results are in, and the performance gains are fantastic! By comparing the two profiler logs, we can see exactly how much time we saved by streamlining the math and eliminating overhead. 

Overall, the **`GO` procedure's total inclusive time dropped from ~31,442 to ~24,467**, representing an **overall simulation speedup of about 22%**! 

Here is a breakdown of the most significant improvements (times are in relative NetLogo profiler units):

### Vector Operations (Huge Wins!)
The transition from map-based calculations to direct index arithmetic, combined with the reduction in unnecessary calls, slashed the vector math overhead drastically.
| Procedure | Old Inclusive Time | New Inclusive Time | Speedup | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **`MAGNITUDE`** | 2,664 | 434 | **~83% faster** | Calls dropped from 8.4M to 5.6M! |
| **`NORMALIZE`** | 3,167 | 911 | **~71% faster** | Calls dropped from 5.1M to 3.6M! |
| **`ADD`** | 1,443 | 523 | **~63% faster** | Same number of calls, just faster code. |
| **`SCALE`** | 1,391 | 498 | **~64% faster** | Same number of calls, just faster code. |
| **`SUBTRACT`** | 536 | *0* | **100% eliminated** | Replaced with direct subtraction. |

### Urge Generators
By eliminating temporary lists and redundant normalization, almost all urges are now generating their vectors significantly faster:
| Procedure | Old Inclusive Time | New Inclusive Time | Speedup |
| :--- | :--- | :--- | :--- |
| **`ADD-URGE`** | 5,453 | 2,801 | **~48% faster** |
| **`WANDER-URGE`** | 249 | 114 | **~54% faster** |
| **`REST-URGE`** | 233 | 119 | **~48% faster** |
| **`SPACING-URGE`** | 608 | 365 | **~40% faster** |
| **`CENTER-URGE`** | 519 | 308 | **~40% faster** |
| **`ALIGN-URGE`** | 782 | 563 | **~28% faster** |

### `DO.FISH.MOVEMENT`
As the core loop representing the vast majority of the simulation's work, `DO.FISH.MOVEMENT` saw its total inclusive time drop from **37,355 to 29,299** (a ~21% reduction). 

These are phenomenal results for a set of optimizations that didn't change a single rule of the simulation's logic. Let me know if there's anything else you'd like to dive into!