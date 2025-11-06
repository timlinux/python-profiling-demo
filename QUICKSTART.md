# Quick Start Guide 🚀

Get up and running with Python Profiling Demo in 5 minutes!

## Method 1: Using Nix (Recommended)

If you have Nix with flakes enabled:

```bash
# Clone the repository
git clone https://github.com/timlinux/python-profiling-demo.git
cd python-profiling-demo

# Enter the development environment (installs all dependencies)
nix develop

# Run the application
python profiler_demo.py
```

Or run directly:

```bash
nix run github:timlinux/python-profiling-demo
```

## Method 2: Using pip

```bash
# Clone the repository
git clone https://github.com/timlinux/python-profiling-demo.git
cd python-profiling-demo

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install snakeviz  # Optional: for profile visualization

# Run the application
python profiler_demo.py
```

## First Steps

Once the application is running, you'll see an interactive menu:

```
┌────────────────────────────────────────────────────────────────┐
│            Python Profiling Demo                               │
└────────────────────────────────────────────────────────────────┘

Option     Benchmark                    Description
1          Fibonacci (Recursive)        Compute Fibonacci recursively - O(2^n)
2          Fibonacci (Iterative)        Compute Fibonacci iteratively - O(n)
3          Matrix Multiplication        Multiply two matrices - O(n³)
4          Prime Factorization          Find prime factors of a large number
5          String Processing            Inefficient string concatenation
6          Run All Benchmarks           Execute all benchmarks with profiling
7          Generate Profile Data        Create profile dumps for analysis
8          Timeit Comparison            Compare performance of different implementations
q          Quit                         Exit the application
```

### Try These Commands:

1. **Start Simple**: Press `2` to run the iterative Fibonacci benchmark
2. **See Profiling**: Press `7` to generate profile data files
3. **Visualize**: Exit the app and run `snakeviz profile_output.prof`
4. **Compare**: Press `8` to see performance comparisons using timeit

## Next Steps

- Read [README.md](README.md) for detailed usage
- Check [PROFILING_GUIDE.md](PROFILING_GUIDE.md) for profiling techniques
- Try different benchmarks to see how they perform
- Experiment with the generated profile files

## Troubleshooting

### "ModuleNotFoundError: No module named 'rich'"

Install dependencies:
```bash
pip install -r requirements.txt
```

### Nix command not found

Either:
- Install Nix: https://nixos.org/download.html
- Use the pip method instead

### Snakeviz won't open

Check if it's installed:
```bash
pip install snakeviz
snakeviz profile_output.prof
```

### Permission denied

Make the script executable:
```bash
chmod +x profiler_demo.py
```

## Example Session

Here's what a typical session looks like:

```bash
$ python profiler_demo.py

# Select option 7 (Generate Profile Data)
Select an option [1/2/3/4/5/6/7/8/q] (q): 7

Generating Profile Data Files...

✓ Profile data saved to: profile_output.prof
  View with: snakeviz profile_output.prof

✓ Text profile saved to: profile_output.txt

✓ Valgrind script saved to: valgrind_script.py
  Run with: valgrind --tool=callgrind python3 valgrind_script.py
  View with: kcachegrind callgrind.out.*

# Press Enter to continue, then 'q' to quit
```

Now view the profile:
```bash
$ snakeviz profile_output.prof
# Opens in your web browser with interactive visualization
```

## What's Included

- ✅ **TUI Application** - Beautiful terminal interface with Rich
- ✅ **5 Benchmarks** - Different computational complexity patterns
- ✅ **Multiple Profiling Tools**:
  - cProfile (built-in)
  - timeit (built-in)
  - snakeviz (visual)
  - valgrind (memory)
- ✅ **Nix Environment** - Reproducible setup with Python 3.13
- ✅ **Documentation** - README, guides, and examples

## Resources

- Main README: [README.md](README.md)
- Profiling Guide: [PROFILING_GUIDE.md](PROFILING_GUIDE.md)
- Rich Documentation: https://rich.readthedocs.io/

Happy profiling! 📊
