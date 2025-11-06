# Python Profiling Guide 📊

A comprehensive guide to profiling Python applications using various tools and techniques.

## Table of Contents

1. [Introduction to Profiling](#introduction-to-profiling)
2. [cProfile - Built-in Profiler](#cprofile---built-in-profiler)
3. [timeit - Timing Code Snippets](#timeit---timing-code-snippets)
4. [Snakeviz - Visual Profile Viewer](#snakeviz---visual-profile-viewer)
5. [Valgrind/Callgrind - Memory and Call Profiling](#valgrindcallgrind---memory-and-call-profiling)
6. [Advanced Techniques](#advanced-techniques)
7. [Best Practices](#best-practices)

## Introduction to Profiling

Profiling helps you understand where your program spends its time and which functions are called most frequently. This information is crucial for optimization.

### When to Profile

- ✅ After you have working code
- ✅ When you need to improve performance
- ✅ Before optimizing (measure first!)
- ❌ During initial development
- ❌ Before correctness is verified

### Types of Profiling

1. **Deterministic Profiling**: Measures all events (e.g., cProfile)
2. **Statistical Profiling**: Samples at intervals (e.g., py-spy)
3. **Memory Profiling**: Tracks memory allocation (e.g., memory_profiler)
4. **Line Profiling**: Profile line-by-line (e.g., line_profiler)

## cProfile - Built-in Profiler

cProfile is Python's built-in profiler, providing detailed statistics about function calls.

### Using cProfile in Code

```python
import cProfile
import pstats

def my_function():
    # Your code here
    pass

# Method 1: Direct profiling
profiler = cProfile.Profile()
profiler.enable()
my_function()
profiler.disable()

# Print stats
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 functions

# Method 2: Save to file
profiler.dump_stats('output.prof')
```

### Using cProfile from Command Line

```bash
# Basic usage
python -m cProfile profiler_demo.py

# Save to file
python -m cProfile -o output.prof profiler_demo.py

# Sort by different metrics
python -m cProfile -s cumulative profiler_demo.py
python -m cProfile -s time profiler_demo.py
python -m cProfile -s calls profiler_demo.py
```

### Understanding cProfile Output

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.003    0.000    0.010    0.000 profiler_demo.py:20(fibonacci_recursive)
```

- **ncalls**: Number of calls
- **tottime**: Total time spent in function (excluding sub-functions)
- **percall**: tottime / ncalls
- **cumtime**: Cumulative time (including sub-functions)
- **percall**: cumtime / ncalls

### Analyzing Profile Files

```python
import pstats

# Load profile data
stats = pstats.Stats('output.prof')

# Sort and print
stats.sort_stats('cumulative').print_stats(20)
stats.sort_stats('time').print_stats(20)

# Filter by function name
stats.print_stats('fibonacci')

# Print callers
stats.print_callers('fibonacci_recursive')

# Print callees
stats.print_callees('fibonacci_recursive')
```

## timeit - Timing Code Snippets

The `timeit` module is perfect for microbenchmarks and comparing small code snippets.

### Using timeit in Code

```python
import timeit

# Time a simple statement
time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Time: {time} seconds")

# Time with setup
time = timeit.timeit(
    'fibonacci_recursive(20)',
    setup='from profiler_demo import fibonacci_recursive',
    number=100
)

# Use Timer class for more control
timer = timeit.Timer(
    stmt='sum(range(1000))',
    setup='pass'
)
results = timer.repeat(repeat=5, number=10000)
print(f"Best of 5: {min(results)}")
```

### Using timeit from Command Line

```bash
# Basic usage
python -m timeit '"-".join(str(n) for n in range(100))'

# With setup
python -m timeit -s 'from profiler_demo import fibonacci_recursive' 'fibonacci_recursive(20)'

# Control number of runs
python -m timeit -n 1000 -r 5 'sum(range(1000))'

# Multiple statements
python -m timeit -s 'x = [1, 2, 3]' 'y = x[:]'
```

### Best Practices for timeit

1. **Run multiple times**: Use `repeat` to get consistent results
2. **Disable garbage collection**: Use `gc.disable()` for consistent timing
3. **Warm up**: First run may be slower due to caching
4. **Use appropriate number**: Balance between accuracy and time

```python
import timeit
import gc

# Disable GC for consistent results
gc.disable()

time = timeit.timeit('sum(range(1000))', number=100000)

gc.enable()
```

## Snakeviz - Visual Profile Viewer

Snakeviz provides an interactive, visual way to explore cProfile output.

### Installation

```bash
pip install snakeviz
```

### Usage

```bash
# Generate profile data
python -m cProfile -o profile.prof profiler_demo.py

# Visualize
snakeviz profile.prof
```

### Features

1. **Sunburst Chart**: Hierarchical view of function calls
2. **Icicle Chart**: Alternative hierarchical view
3. **Interactive**: Click to zoom, hover for details
4. **Function Details**: See time spent in each function
5. **Call Hierarchy**: Understand call relationships

### Interpreting Snakeviz

- **Larger sections** = More time spent
- **Click a section** = Zoom into that function
- **Hover** = See detailed statistics
- **Color** = Distinguishes different functions

## Valgrind/Callgrind - Memory and Call Profiling

Valgrind is a powerful suite of tools for debugging and profiling. Callgrind is a profiling tool that tracks function calls.

### Basic Usage

```bash
# Profile with callgrind
valgrind --tool=callgrind python3 profiler_demo.py

# This creates: callgrind.out.<pid>
```

### Analyzing Callgrind Output

```bash
# View with kcachegrind (GUI, Linux/Mac)
kcachegrind callgrind.out.*

# View with qcachegrind (GUI, Windows/Mac)
qcachegrind callgrind.out.*

# Command-line analysis
callgrind_annotate callgrind.out.*
```

### Creating Call Graphs

```bash
# Install gprof2dot
pip install gprof2dot

# Convert to dot format and create image
gprof2dot -f callgrind callgrind.out.* | dot -Tpng -o callgraph.png

# View the image
xdg-open callgraph.png  # Linux
open callgraph.png      # Mac
```

### Valgrind Options

```bash
# Basic profiling
valgrind --tool=callgrind python3 script.py

# Detailed profiling with cache simulation
valgrind --tool=callgrind --cache-sim=yes python3 script.py

# Profile specific function
valgrind --tool=callgrind --dump-instr=yes --collect-jumps=yes python3 script.py

# Memory leak detection
valgrind --leak-check=full python3 script.py
```

### Memory Profiling with Massif

```bash
# Profile heap usage
valgrind --tool=massif python3 profiler_demo.py

# Visualize
ms_print massif.out.*
```

## Advanced Techniques

### 1. Line Profiler

Profile code line by line:

```bash
# Install
pip install line_profiler

# Add @profile decorator to functions
# Then run:
kernprof -l -v profiler_demo.py
```

### 2. Memory Profiler

Track memory usage:

```bash
# Install
pip install memory_profiler

# Run
python -m memory_profiler profiler_demo.py

# Or use decorator
@profile
def my_function():
    pass
```

### 3. Py-Spy

Statistical profiler (no code changes needed):

```bash
# Install
pip install py-spy

# Profile a running process
py-spy top --pid <PID>

# Record and generate flamegraph
py-spy record -o profile.svg -- python profiler_demo.py
```

### 4. Python Profiling in Production

For production environments:

```python
import cProfile
import atexit

# Start profiling
profiler = cProfile.Profile()
profiler.enable()

# Stop profiling on exit
def save_profile():
    profiler.disable()
    profiler.dump_stats('production.prof')

atexit.register(save_profile)
```

### 5. Profiling Decorators

Create reusable profiling decorators:

```python
import cProfile
import pstats
from functools import wraps

def profile(func):
    """Decorator to profile a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        stats.print_stats()
        return result
    return wrapper

@profile
def my_function():
    # Your code here
    pass
```

### 6. Comparing Profile Results

```python
import pstats

# Load two profile files
stats1 = pstats.Stats('before.prof')
stats2 = pstats.Stats('after.prof')

# Compare
stats1.add(stats2)
stats1.sort_stats('cumulative')
stats1.print_stats()
```

## Best Practices

### 1. Profile Before Optimizing

> "Premature optimization is the root of all evil" - Donald Knuth

- Always measure before optimizing
- Focus on the biggest bottlenecks
- Profile in realistic conditions

### 2. Profile Representative Workloads

- Use production-like data
- Include typical user interactions
- Test edge cases separately

### 3. Interpreting Results

- Look for:
  - Functions with high cumulative time
  - Functions called many times
  - Unexpected function calls
  - I/O bottlenecks

### 4. Optimization Strategy

1. **Measure**: Profile to find bottlenecks
2. **Analyze**: Understand why it's slow
3. **Optimize**: Make targeted changes
4. **Verify**: Profile again to confirm improvement
5. **Repeat**: Continue until goals are met

### 5. Common Performance Issues

- **Algorithm complexity**: O(n²) vs O(n log n)
- **Unnecessary work**: Computing things multiple times
- **Memory allocation**: Creating too many objects
- **I/O bottlenecks**: Database queries, file operations
- **Python overhead**: Use NumPy/Cython for tight loops

### 6. When to Stop Optimizing

- Performance meets requirements
- Further optimization costs too much
- Code becomes unmaintainable
- Optimization yields diminishing returns

## Profiling Workflow Example

Here's a complete workflow for optimizing code:

```bash
# 1. Create initial profile
python -m cProfile -o before.prof profiler_demo.py

# 2. Visualize to find bottlenecks
snakeviz before.prof

# 3. Profile specific functions
python -m line_profiler -l profiler_demo.py

# 4. Make optimizations
# ... edit code ...

# 5. Profile again
python -m cProfile -o after.prof profiler_demo.py

# 6. Compare results
snakeviz after.prof

# 7. Verify improvement
python -m timeit -s 'from profiler_demo import optimized_function' 'optimized_function()'
```

## Troubleshooting

### cProfile shows no data

- Make sure code actually runs
- Check if profiler is enabled
- Verify output file is created

### Snakeviz won't open

- Check if port 8080 is available
- Try: `snakeviz -p 8081 profile.prof`
- Check firewall settings

### Valgrind is too slow

- Normal! Valgrind adds 10-50x overhead
- Use smaller test cases
- Profile only critical sections

### Profile data is too large

- Filter by function: `stats.print_stats('myfunction')`
- Increase threshold: `stats.print_stats(0.1)`
- Profile shorter runs

## Resources

- [Python Profilers Documentation](https://docs.python.org/3/library/profile.html)
- [Snakeviz Documentation](https://jiffyclub.github.io/snakeviz/)
- [Valgrind Documentation](https://valgrind.org/docs/)
- [Line Profiler](https://github.com/pyutils/line_profiler)
- [Memory Profiler](https://github.com/pythonprofilers/memory_profiler)
- [Py-Spy](https://github.com/benfred/py-spy)

## Summary

Profiling is essential for understanding and optimizing Python code. This guide covered:

- ✅ cProfile for detailed function profiling
- ✅ timeit for microbenchmarks
- ✅ Snakeviz for visual analysis
- ✅ Valgrind for memory and call profiling
- ✅ Advanced techniques and best practices

Remember: **Measure, don't guess!** Always profile before optimizing.
