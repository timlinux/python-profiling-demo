#!/usr/bin/env python3
"""
Python Profiling Demo - A TUI application demonstrating various profiling techniques.

This application provides computationally expensive operations that can be profiled
using various Python profiling tools including cProfile, timeit, valgrind, and snakeviz.
"""

import cProfile
import pstats
import timeit
from io import StringIO
from typing import List

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text


console = Console()


def fibonacci_recursive(n: int) -> int:
    """
    Compute Fibonacci number recursively (inefficient, good for profiling).
    
    Args:
        n: The position in the Fibonacci sequence
        
    Returns:
        The Fibonacci number at position n
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """
    Compute Fibonacci number iteratively (efficient).
    
    Args:
        n: The position in the Fibonacci sequence
        
    Returns:
        The Fibonacci number at position n
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def matrix_multiplication(size: int) -> List[List[int]]:
    """
    Perform matrix multiplication (computationally expensive).
    
    Args:
        size: The size of the square matrices
        
    Returns:
        The resulting matrix
    """
    # Create two matrices
    matrix_a = [[i + j for j in range(size)] for i in range(size)]
    matrix_b = [[i * j for j in range(size)] for i in range(size)]
    
    # Multiply them
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result


def prime_factorization(n: int) -> List[int]:
    """
    Find prime factors of a number.
    
    Args:
        n: The number to factorize
        
    Returns:
        List of prime factors
    """
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def string_processing(iterations: int) -> str:
    """
    Perform string concatenation operations (inefficient for profiling).
    
    Args:
        iterations: Number of concatenation operations
        
    Returns:
        The resulting string
    """
    result = ""
    for i in range(iterations):
        result += str(i)
    return result


def display_menu():
    """Display the main menu."""
    console.clear()
    
    title = Text("Python Profiling Demo", style="bold magenta")
    console.print(Panel(title, expand=False))
    
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Option", style="cyan", width=10)
    table.add_column("Benchmark", style="green")
    table.add_column("Description", style="white")
    
    table.add_row("1", "Fibonacci (Recursive)", "Compute Fibonacci recursively - O(2^n)")
    table.add_row("2", "Fibonacci (Iterative)", "Compute Fibonacci iteratively - O(n)")
    table.add_row("3", "Matrix Multiplication", "Multiply two matrices - O(n³)")
    table.add_row("4", "Prime Factorization", "Find prime factors of a large number")
    table.add_row("5", "String Processing", "Inefficient string concatenation")
    table.add_row("6", "Run All Benchmarks", "Execute all benchmarks with profiling")
    table.add_row("7", "Generate Profile Data", "Create profile dumps for analysis")
    table.add_row("8", "Timeit Comparison", "Compare performance of different implementations")
    table.add_row("q", "Quit", "Exit the application")
    
    console.print(table)


def run_with_profiling(func, *args, **kwargs):
    """
    Run a function with cProfile and display results.
    
    Args:
        func: The function to profile
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function
        
    Returns:
        The result of the function
    """
    profiler = cProfile.Profile()
    profiler.enable()
    
    result = func(*args, **kwargs)
    
    profiler.disable()
    
    # Print profiling results
    s = StringIO()
    stats = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    stats.print_stats(10)  # Print top 10 functions
    
    console.print(Panel(s.getvalue(), title="Profiling Results", border_style="yellow"))
    
    return result


def benchmark_fibonacci_recursive():
    """Benchmark recursive Fibonacci."""
    console.print("\n[bold cyan]Running Fibonacci (Recursive) Benchmark...[/bold cyan]")
    n = 30
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Computing Fibonacci({n})...", total=None)
        result = run_with_profiling(fibonacci_recursive, n)
        progress.update(task, completed=True)
    
    console.print(f"[green]Result: {result}[/green]\n")


def benchmark_fibonacci_iterative():
    """Benchmark iterative Fibonacci."""
    console.print("\n[bold cyan]Running Fibonacci (Iterative) Benchmark...[/bold cyan]")
    n = 100000
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Computing Fibonacci({n})...", total=None)
        result = run_with_profiling(fibonacci_iterative, n)
        progress.update(task, completed=True)
    
    console.print(f"[green]Result length: {len(str(result))} digits[/green]\n")


def benchmark_matrix_multiplication():
    """Benchmark matrix multiplication."""
    console.print("\n[bold cyan]Running Matrix Multiplication Benchmark...[/bold cyan]")
    size = 100
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Multiplying {size}x{size} matrices...", total=None)
        result = run_with_profiling(matrix_multiplication, size)
        progress.update(task, completed=True)
    
    console.print(f"[green]Matrix multiplication complete![/green]\n")


def benchmark_prime_factorization():
    """Benchmark prime factorization."""
    console.print("\n[bold cyan]Running Prime Factorization Benchmark...[/bold cyan]")
    number = 123456789012345
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Factorizing {number}...", total=None)
        result = run_with_profiling(prime_factorization, number)
        progress.update(task, completed=True)
    
    console.print(f"[green]Prime factors: {result}[/green]\n")


def benchmark_string_processing():
    """Benchmark string processing."""
    console.print("\n[bold cyan]Running String Processing Benchmark...[/bold cyan]")
    iterations = 10000
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Processing {iterations} string operations...", total=None)
        result = run_with_profiling(string_processing, iterations)
        progress.update(task, completed=True)
    
    console.print(f"[green]String length: {len(result)} characters[/green]\n")


def run_all_benchmarks():
    """Run all benchmarks sequentially."""
    console.print("\n[bold magenta]Running All Benchmarks...[/bold magenta]\n")
    
    benchmark_fibonacci_recursive()
    benchmark_fibonacci_iterative()
    benchmark_matrix_multiplication()
    benchmark_prime_factorization()
    benchmark_string_processing()
    
    console.print("[bold green]All benchmarks complete![/bold green]")


def generate_profile_data():
    """Generate profile data files for external tools."""
    console.print("\n[bold cyan]Generating Profile Data Files...[/bold cyan]\n")
    
    # Generate cProfile output
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Run multiple operations
    fibonacci_recursive(25)
    fibonacci_iterative(10000)
    matrix_multiplication(50)
    prime_factorization(987654321)
    string_processing(5000)
    
    profiler.disable()
    
    # Save to file
    profile_file = "profile_output.prof"
    profiler.dump_stats(profile_file)
    console.print(f"[green]✓[/green] Profile data saved to: [cyan]{profile_file}[/cyan]")
    console.print(f"  View with: [yellow]snakeviz {profile_file}[/yellow]\n")
    
    # Create a text version
    with open("profile_output.txt", "w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats('cumulative')
        stats.print_stats()
    console.print(f"[green]✓[/green] Text profile saved to: [cyan]profile_output.txt[/cyan]\n")
    
    # Generate example script for valgrind
    valgrind_script = """#!/usr/bin/env python3
# This script is optimized for valgrind profiling
import sys
sys.path.insert(0, '.')
from profiler_demo import fibonacci_recursive, matrix_multiplication, prime_factorization

# Run a subset of operations for valgrind
fibonacci_recursive(25)
matrix_multiplication(50)
prime_factorization(987654321)
"""
    
    with open("valgrind_script.py", "w") as f:
        f.write(valgrind_script)
    
    console.print(f"[green]✓[/green] Valgrind script saved to: [cyan]valgrind_script.py[/cyan]")
    console.print(f"  Run with: [yellow]valgrind --tool=callgrind python3 valgrind_script.py[/yellow]")
    console.print(f"  View with: [yellow]kcachegrind callgrind.out.*[/yellow]\n")


def timeit_comparison():
    """Compare different implementations using timeit."""
    console.print("\n[bold cyan]Performance Comparison using timeit...[/bold cyan]\n")
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Function", style="cyan")
    table.add_column("Time (seconds)", style="green", justify="right")
    table.add_column("Iterations", style="yellow", justify="right")
    
    # Fibonacci comparison
    n = 20
    iterations = 100
    
    with console.status("[bold green]Running timeit benchmarks..."):
        time_recursive = timeit.timeit(
            f"fibonacci_recursive({n})",
            setup="from profiler_demo import fibonacci_recursive",
            number=iterations
        )
        
        time_iterative = timeit.timeit(
            f"fibonacci_iterative({n})",
            setup="from profiler_demo import fibonacci_iterative",
            number=iterations
        )
        
        time_matrix = timeit.timeit(
            "matrix_multiplication(30)",
            setup="from profiler_demo import matrix_multiplication",
            number=10
        )
    
    table.add_row(f"fibonacci_recursive({n})", f"{time_recursive:.6f}", str(iterations))
    table.add_row(f"fibonacci_iterative({n})", f"{time_iterative:.6f}", str(iterations))
    table.add_row(f"matrix_multiplication(30)", f"{time_matrix:.6f}", "10")
    
    console.print(table)
    
    speedup = time_recursive / time_iterative
    console.print(f"\n[bold green]Iterative is {speedup:.2f}x faster than recursive![/bold green]\n")


def main():
    """Main application loop."""
    while True:
        display_menu()
        
        choice = Prompt.ask(
            "\n[bold cyan]Select an option[/bold cyan]",
            choices=["1", "2", "3", "4", "5", "6", "7", "8", "q"],
            default="q"
        )
        
        if choice == "1":
            benchmark_fibonacci_recursive()
        elif choice == "2":
            benchmark_fibonacci_iterative()
        elif choice == "3":
            benchmark_matrix_multiplication()
        elif choice == "4":
            benchmark_prime_factorization()
        elif choice == "5":
            benchmark_string_processing()
        elif choice == "6":
            run_all_benchmarks()
        elif choice == "7":
            generate_profile_data()
        elif choice == "8":
            timeit_comparison()
        elif choice == "q":
            console.print("\n[bold green]Thank you for using Python Profiling Demo![/bold green]\n")
            break
        
        if choice != "q":
            Prompt.ask("\n[dim]Press Enter to continue[/dim]")


if __name__ == "__main__":
    main()
