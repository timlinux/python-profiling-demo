# Python Profiling Demo 🐍📊

A comprehensive demonstration of Python profiling techniques using a beautiful TUI (Text User Interface) built with [Rich](https://github.com/Textualize/rich). This project showcases various computationally expensive operations and demonstrates how to profile them using different tools.

## Features

- 🎨 **Beautiful TUI** - Interactive terminal interface using Rich library
- 🔥 **Computationally Expensive Operations** - Various benchmarks for profiling:
  - Recursive Fibonacci (exponential complexity)
  - Iterative Fibonacci (linear complexity)
  - Matrix multiplication (cubic complexity)
  - Prime factorization
  - String processing
- 📊 **Multiple Profiling Tools**:
  - `cProfile` - Built-in Python profiler
  - `timeit` - Performance comparison
  - `snakeviz` - Visual profile viewer
  - `valgrind/callgrind` - Memory and call profiling
- 🔧 **Nix Development Environment** - Reproducible setup with Python 3.13

## Quick Start with Nix

If you have Nix with flakes enabled:

```bash
# Enter the development environment
nix develop

# Run the application
python profiler_demo.py
```

Or run directly without entering the shell:

```bash
nix run
```

## Manual Setup

If you're not using Nix:

```bash
# Create a virtual environment (Python 3.13 recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install snakeviz  # For profile visualization

# Run the application
python profiler_demo.py
```

## Using the Application

The TUI provides an interactive menu with the following options:

1. **Fibonacci (Recursive)** - Demonstrates exponential time complexity
2. **Fibonacci (Iterative)** - Demonstrates linear time complexity
3. **Matrix Multiplication** - Demonstrates cubic time complexity
4. **Prime Factorization** - Factor large numbers
5. **String Processing** - Inefficient string concatenation
6. **Run All Benchmarks** - Execute all benchmarks sequentially
7. **Generate Profile Data** - Create profile dumps for external analysis
8. **Timeit Comparison** - Compare performance of different implementations

## Profiling Techniques

### 1. Built-in cProfile

The application automatically profiles each benchmark and displays results. You can also generate profile data files:

```bash
# Run the application and select option 7
python profiler_demo.py
# Select: 7 (Generate Profile Data)
```

This creates:
- `profile_output.prof` - Binary profile data
- `profile_output.txt` - Human-readable profile data

### 2. Snakeviz Visualization

Visualize the profile data with an interactive web interface:

```bash
# Generate profile data first (option 7 in the app)
python profiler_demo.py

# Then visualize
snakeviz profile_output.prof
```

This opens a web browser with an interactive visualization showing:
- Call graphs
- Time distribution
- Function call hierarchy

### 3. Using timeit

The application includes a built-in timeit comparison (option 8), or you can use it manually:

```bash
python -m timeit -s "from profiler_demo import fibonacci_recursive" "fibonacci_recursive(20)"
python -m timeit -s "from profiler_demo import fibonacci_iterative" "fibonacci_iterative(20)"
```

### 4. Valgrind/Callgrind

For low-level profiling and call graph analysis:

```bash
# Generate the valgrind script (option 7 in the app)
python profiler_demo.py

# Run with callgrind
valgrind --tool=callgrind python3 valgrind_script.py

# Visualize with kcachegrind (if available)
kcachegrind callgrind.out.*

# Or convert to callgraph
gprof2dot -f callgrind callgrind.out.* | dot -Tpng -o callgraph.png
```

### 5. Line Profiler (Optional)

For line-by-line profiling, install `line_profiler`:

```bash
pip install line_profiler

# Add @profile decorator to functions you want to profile
# Then run:
kernprof -l -v profiler_demo.py
```

### 6. Memory Profiler (Optional)

To profile memory usage:

```bash
pip install memory_profiler

# Run with memory profiling
python -m memory_profiler profiler_demo.py
```

## Understanding the Benchmarks

### Fibonacci Recursive vs Iterative

- **Recursive**: O(2^n) time complexity - Exponentially slow, great for demonstrating inefficiency
- **Iterative**: O(n) time complexity - Much faster, demonstrates the importance of algorithm choice

### Matrix Multiplication

- O(n³) time complexity
- Demonstrates the cost of nested loops
- Good for testing CPU performance

### Prime Factorization

- Time complexity depends on the number being factorized
- Demonstrates trial division algorithm
- Good for testing arithmetic operations

### String Processing

- Demonstrates the cost of string concatenation in a loop
- Shows why using `join()` or list comprehensions is better
- O(n²) time complexity due to string immutability

## Performance Tips Demonstrated

1. **Algorithm Choice Matters**: Recursive vs iterative Fibonacci shows dramatic differences
2. **Data Structure Selection**: String concatenation vs list joining
3. **Complexity Classes**: Visual demonstration of O(n), O(n²), O(n³), and O(2^n)
4. **Profiling Guides Optimization**: Use tools to find actual bottlenecks

## Nix Development Environment

The `flake.nix` provides a complete, reproducible development environment with:

- Python 3.13
- Rich library
- Valgrind for memory profiling
- GraphViz for visualization
- Snakeviz for profile visualization

### Nix Commands

```bash
# Enter development shell
nix develop

# Run the application
nix run

# Build the package
nix build
```

## Project Structure

```
.
├── flake.nix              # Nix flake configuration
├── profiler_demo.py       # Main application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── PROFILING_GUIDE.md    # Detailed profiling guide
```

## Contributing

Feel free to add more benchmarks or profiling techniques! Some ideas:

- More algorithms (sorting, searching, graph algorithms)
- Database operations
- File I/O operations
- Network operations
- Parallel processing examples

## License

MIT License - Feel free to use this for learning and teaching!

## Resources

- [Rich Documentation](https://rich.readthedocs.io/)
- [Python cProfile Documentation](https://docs.python.org/3/library/profile.html)
- [Snakeviz Documentation](https://jiffyclub.github.io/snakeviz/)
- [Valgrind Documentation](https://valgrind.org/docs/manual/quick-start.html)
- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
