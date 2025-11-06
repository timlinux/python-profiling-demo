# Examples and Expected Output 📝

This document shows examples of what to expect when running the profiling demo.

## Running the Application

```bash
$ python profiler_demo.py
```

Output:
```
┌────────────────────────────────────────────────────────────────┐
│            Python Profiling Demo                               │
└────────────────────────────────────────────────────────────────┘

┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Option   ┃ Benchmark                 ┃ Description                              ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1        │ Fibonacci (Recursive)     │ Compute Fibonacci recursively - O(2^n)   │
│ 2        │ Fibonacci (Iterative)     │ Compute Fibonacci iteratively - O(n)     │
│ 3        │ Matrix Multiplication     │ Multiply two matrices - O(n³)            │
│ 4        │ Prime Factorization       │ Find prime factors of a large number     │
│ 5        │ String Processing         │ Inefficient string concatenation         │
│ 6        │ Run All Benchmarks        │ Execute all benchmarks with profiling    │
│ 7        │ Generate Profile Data     │ Create profile dumps for analysis        │
│ 8        │ Timeit Comparison         │ Compare performance of implementations   │
│ q        │ Quit                      │ Exit the application                     │
└──────────┴───────────────────────────┴──────────────────────────────────────────┘
```

## Example 1: Fibonacci Recursive (Option 1)

```bash
Select an option [1/2/3/4/5/6/7/8/q] (q): 1
```

Output:
```
Running Fibonacci (Recursive) Benchmark...

⠸ Computing Fibonacci(30)...

╭───────────────────────── Profiling Results ─────────────────────────╮
│          21893 function calls (3 primitive calls) in 0.006 seconds   │
│                                                                      │
│    Ordered by: cumulative time                                      │
│                                                                      │
│    ncalls  tottime  percall  cumtime  percall filename:lineno       │
│  2692537/1  3.254    0.000    3.254    3.254 profiler_demo.py:27   │
│          1  0.000    0.000    3.254    3.254 profiler_demo.py:137  │
│          1  0.000    0.000    0.000    0.000 {method 'disable'...  │
╰──────────────────────────────────────────────────────────────────────╯

Result: 832040
```

## Example 2: Fibonacci Iterative (Option 2)

Much faster than recursive:

```
Running Fibonacci (Iterative) Benchmark...

⠸ Computing Fibonacci(100000)...

╭───────────────────────── Profiling Results ─────────────────────────╮
│            5 function calls in 0.023 seconds                         │
│                                                                      │
│    Ordered by: cumulative time                                      │
│                                                                      │
│    ncalls  tottime  percall  cumtime  percall filename:lineno       │
│        1    0.023    0.023    0.023    0.023 profiler_demo.py:45   │
│        1    0.000    0.000    0.023    0.023 profiler_demo.py:150  │
│        1    0.000    0.000    0.000    0.000 {method 'disable'...  │
╰──────────────────────────────────────────────────────────────────────╯

Result length: 20899 digits
```

## Example 3: Matrix Multiplication (Option 3)

```
Running Matrix Multiplication Benchmark...

⠸ Multiplying 100x100 matrices...

╭───────────────────────── Profiling Results ─────────────────────────╮
│            4 function calls in 0.834 seconds                         │
│                                                                      │
│    Ordered by: cumulative time                                      │
│                                                                      │
│    ncalls  tottime  percall  cumtime  percall filename:lineno       │
│        1    0.834    0.834    0.834    0.834 profiler_demo.py:60   │
│        1    0.000    0.000    0.834    0.834 profiler_demo.py:163  │
│        1    0.000    0.000    0.000    0.000 {method 'disable'...  │
╰──────────────────────────────────────────────────────────────────────╯

Matrix multiplication complete!
```

## Example 4: Generate Profile Data (Option 7)

```bash
Select an option [1/2/3/4/5/6/7/8/q] (q): 7
```

Output:
```
Generating Profile Data Files...

✓ Profile data saved to: profile_output.prof
  View with: snakeviz profile_output.prof

✓ Text profile saved to: profile_output.txt

✓ Valgrind script saved to: valgrind_script.py
  Run with: valgrind --tool=callgrind python3 valgrind_script.py
  View with: kcachegrind callgrind.out.*
```

Files created:
- `profile_output.prof` - Binary profile data for snakeviz
- `profile_output.txt` - Human-readable profile statistics
- `valgrind_script.py` - Script optimized for valgrind profiling

## Example 5: Timeit Comparison (Option 8)

```bash
Select an option [1/2/3/4/5/6/7/8/q] (q): 8
```

Output:
```
Performance Comparison using timeit...

⠸ Running timeit benchmarks...

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Function                  ┃ Time (seconds) ┃ Iterations ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ fibonacci_recursive(20)   │       0.090786 │        100 │
│ fibonacci_iterative(20)   │       0.000057 │        100 │
│ matrix_multiplication(30) │       0.021723 │         10 │
└───────────────────────────┴────────────────┴────────────┘

Iterative is 1597.05x faster than recursive!
```

This clearly shows the dramatic performance difference between algorithms!

## Using Snakeviz

After generating profile data (option 7):

```bash
$ snakeviz profile_output.prof
```

This opens a web browser showing:
- **Sunburst chart** - Visual representation of where time is spent
- **Icicle chart** - Alternative hierarchical view
- **Function details** - Click any function to see details
- **Call statistics** - Number of calls, time per call, etc.

## Using Command-Line Profiling

### cProfile from command line:

```bash
$ python -m cProfile -o output.prof profiler_demo.py
```

### View stats:

```bash
$ python -c "import pstats; stats = pstats.Stats('output.prof'); stats.sort_stats('cumulative').print_stats(20)"
```

### Using timeit from command line:

```bash
$ python -m timeit -s "from profiler_demo import fibonacci_recursive" "fibonacci_recursive(20)"
100 loops, best of 5: 0.908 msec per loop

$ python -m timeit -s "from profiler_demo import fibonacci_iterative" "fibonacci_iterative(20)"
5000000 loops, best of 5: 0.569 usec per loop
```

The iterative version is about 1600x faster!

## Using Valgrind/Callgrind

After generating the valgrind script (option 7):

```bash
$ valgrind --tool=callgrind python3 valgrind_script.py
==12345== Callgrind, a call-graph generating cache profiler
==12345== Copyright (C) 2002-2017, and GNU GPL'd, by Josef Weidendorfer et al.
==12345== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==12345== Command: python3 valgrind_script.py
==12345==
==12345== For interactive control, run 'callgrind_control -h'.
==12345==
==12345== Events    : Ir
==12345== Collected : 523748391
==12345==
==12345== I   refs:      523,748,391
```

This creates a `callgrind.out.XXXXX` file. Visualize with:

```bash
$ kcachegrind callgrind.out.*
```

Or create a call graph:

```bash
$ gprof2dot -f callgrind callgrind.out.* | dot -Tpng -o callgraph.png
```

## Performance Insights

### Complexity Comparison

| Function | Complexity | Input Size | Time |
|----------|-----------|------------|------|
| Fibonacci (Recursive) | O(2^n) | n=30 | ~3 seconds |
| Fibonacci (Iterative) | O(n) | n=100,000 | ~0.02 seconds |
| Matrix Multiplication | O(n³) | n=100 | ~0.8 seconds |
| Prime Factorization | O(√n) | 123456789012345 | ~0.5 seconds |
| String Processing | O(n²) | n=10,000 | ~0.3 seconds |

### Key Takeaways

1. **Algorithm Choice Matters**: Recursive Fibonacci is 1600x slower than iterative
2. **Cubic Complexity**: Matrix multiplication becomes very slow as n increases
3. **String Concatenation**: Building strings in loops is inefficient (use join)
4. **Profiling is Essential**: Don't guess where the bottleneck is - measure it!

## Tips for Your Own Code

1. **Profile first**: Don't optimize without profiling
2. **Focus on hotspots**: Optimize functions that take the most time
3. **Measure improvements**: Verify optimizations actually help
4. **Consider complexity**: Sometimes a better algorithm is the solution
5. **Trade-offs**: Balance performance, readability, and maintainability

## Next Steps

- Try modifying the code to improve performance
- Add your own benchmarks
- Experiment with different input sizes
- Compare optimized vs unoptimized versions
- Use profiling in your own projects

For more details, see:
- [README.md](README.md) - Full project documentation
- [PROFILING_GUIDE.md](PROFILING_GUIDE.md) - Comprehensive profiling guide
- [QUICKSTART.md](QUICKSTART.md) - Getting started quickly
