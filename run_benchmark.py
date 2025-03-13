#!/usr/bin/env python3
import os
import subprocess
import re
import csv
import time
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Warning: matplotlib is not available, charts will not be generated")
from collections import defaultdict

# Directory to store the bytecode samples
BYTECODE_DIR = 'bytecode_samples'
# Directory to store the benchmark results
RESULTS_DIR = 'benchmark_results'
# File to write the report to
REPORT_FILE = 'benchmark_results/summary_report.md'

def run_command(cmd, cwd=None):
    """Run a command and return its output"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {' '.join(cmd)}")
        print(f"Error: {result.stderr}")
        exit(1)
    return result.stdout

def generate_bytecode():
    """Generate bytecode samples for benchmarking"""
    print("\n--- Generating bytecode samples ---")
    run_command(['python3', 'generate_bytecode.py', '--output-dir', BYTECODE_DIR])
    
def run_analyzer(bytecode_file):
    """Run the jumpdest analyzer on a bytecode file and return the results"""
    print(f"Analyzing {bytecode_file}...")
    output = run_command(['./jumpdest_analyzer', bytecode_file])
    
    # Parse results
    result = {
        'bytecode_file': bytecode_file,
        'bytecode_size': 0,
        'runs': [],
        'jumpdests_found': 0,
        'average_ms': 0.0
    }
    
    # Extract bytecode size
    match = re.search(r'Bytecode size: (\d+) bytes', output)
    if match:
        result['bytecode_size'] = int(match.group(1))
        
    # Extract runs
    runs = re.findall(r'Run \d+: (\d+\.\d+) ms, (\d+) valid JUMPDESTs found', output)
    for run_time, jumpdests in runs:
        result['runs'].append(float(run_time))
        result['jumpdests_found'] = int(jumpdests)  # Will be the same for all runs
        
    # Extract average time
    match = re.search(r'Average time: (\d+\.\d+) ms', output)
    if match:
        result['average_ms'] = float(match.group(1))
    
    return result

def run_benchmarks():
    """Run benchmarks on all bytecode files"""
    print("\n--- Running benchmarks ---")
    
    # Create results directory if it doesn't exist
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    results = []
    
    # Find all bytecode files
    for file in sorted(os.listdir(BYTECODE_DIR)):
        if file.endswith('.hex'):
            bytecode_file = os.path.join(BYTECODE_DIR, file)
            result = run_analyzer(bytecode_file)
            results.append(result)
    
    return results

def save_results_to_csv(results):
    """Save benchmark results to CSV files"""
    print("\n--- Saving results to CSV ---")
    
    # Main results CSV
    csv_file = os.path.join(RESULTS_DIR, 'benchmark_results.csv')
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File', 'Size (bytes)', 'Average Time (ms)', 'JUMPDESTs Found'])
        
        for result in results:
            writer.writerow([
                os.path.basename(result['bytecode_file']),
                result['bytecode_size'],
                result['average_ms'],
                result['jumpdests_found']
            ])
    
    print(f"Results saved to {csv_file}")
    
    # Detailed run data for each test
    detailed_csv = os.path.join(RESULTS_DIR, 'detailed_runs.csv')
    with open(detailed_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File', 'Size (bytes)', 'Run Number', 'Time (ms)'])
        
        for result in results:
            file_name = os.path.basename(result['bytecode_file'])
            for i, run_time in enumerate(result['runs']):
                writer.writerow([
                    file_name,
                    result['bytecode_size'],
                    i+1,
                    run_time
                ])
    
    print(f"Detailed run data saved to {detailed_csv}")
    
    return csv_file, detailed_csv

def create_plots(results):
    """Create plots of the benchmark results"""
    if not MATPLOTLIB_AVAILABLE:
        print("\n--- Skipping plots (matplotlib not available) ---")
        return None, None
        
    print("\n--- Creating plots ---")
    
    # Group results by file type
    grouped_results = defaultdict(list)
    for result in results:
        file_name = os.path.basename(result['bytecode_file'])
        
        # Determine if this is a jumpdest or push1 file
        if 'jumpdest_monster' in file_name:
            key = 'JUMPDEST only'
        elif 'push1_monster' in file_name:
            key = 'PUSH1 0x5b sequences'
        else:
            key = 'Other'
            
        grouped_results[key].append(result)
    
    # Create plot for average time vs bytecode size
    plt.figure(figsize=(12, 8))
    
    markers = ['o', 's']
    colors = ['blue', 'red']
    
    for i, (file_type, group_results) in enumerate(grouped_results.items()):
        sizes = [r['bytecode_size'] for r in group_results]
        times = [r['average_ms'] for r in group_results]
        
        # Sort by size
        sorted_data = sorted(zip(sizes, times))
        sizes = [data[0] for data in sorted_data]
        times = [data[1] for data in sorted_data]
        
        plt.plot(sizes, times, marker=markers[i % len(markers)], 
                 linestyle='-', color=colors[i % len(colors)], label=file_type)
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Bytecode Size (bytes)')
    plt.ylabel('Average Analysis Time (ms)')
    plt.title('JUMPDEST Analysis Performance')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    
    plot_file = os.path.join(RESULTS_DIR, 'analysis_performance.png')
    plt.savefig(plot_file)
    
    print(f"Performance plot saved to {plot_file}")
    
    # Plot showing distribution of run times for each file size
    plt.figure(figsize=(12, 8))
    
    for i, (file_type, group_results) in enumerate(grouped_results.items()):
        for result in sorted(group_results, key=lambda r: r['bytecode_size']):
            file_name = os.path.basename(result['bytecode_file'])
            short_name = re.sub(r'_\d+b\.hex$', '', file_name)
            
            # Create a box plot for each file's runs
            size_label = f"{short_name}\n{result['bytecode_size']/1024:.0f}KB"
            plt.boxplot(result['runs'], positions=[result['bytecode_size']], 
                       widths=result['bytecode_size']/4, showfliers=True)
    
    plt.xscale('log')
    plt.yscale('log')  # Added log scale for y-axis
    plt.xlabel('Bytecode Size (bytes)')
    plt.ylabel('Run Time (ms)')
    plt.title('Run Time Distribution by Bytecode Size (Log Scale)')
    plt.grid(True, which="both", ls="--")
    
    distribution_plot = os.path.join(RESULTS_DIR, 'runtime_distribution.png')
    plt.savefig(distribution_plot)
    
    print(f"Runtime distribution plot saved to {distribution_plot}")
    
    return plot_file, distribution_plot

def generate_report(results, csv_file, plot_file, distribution_plot):
    """Generate a benchmark report in Markdown format"""
    print("\n--- Generating report ---")
    
    jumpdest_results = [r for r in results if 'jumpdest_monster' in r['bytecode_file']]
    push_results = [r for r in results if 'push1_monster' in r['bytecode_file']]
    
    # Sort results by size
    jumpdest_results.sort(key=lambda r: r['bytecode_size'])
    push_results.sort(key=lambda r: r['bytecode_size'])
    
    # Calculate stats
    max_jumpdest_time = max([r['average_ms'] for r in jumpdest_results])
    max_push_time = max([r['average_ms'] for r in push_results])
    
    # Find the 48KB files (EIP-3860 limit)
    eip_limit_jumpdest = next((r for r in jumpdest_results if r['bytecode_size'] == 48 * 1024))
    eip_limit_push = next((r for r in push_results if r['bytecode_size'] == 48 * 1024), None)

    jumpdest_ratio = max_jumpdest_time / eip_limit_jumpdest['average_ms']
    push_ratio = max_push_time / eip_limit_push['average_ms']

    with open(REPORT_FILE, 'w') as f:
        f.write("# JUMPDEST Analysis Benchmark Report\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- **Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **Number of tests:** {len(results)}\n")
        f.write(f"- **Bytecode size range:** {min([r['bytecode_size'] for r in results])} bytes to ")
        f.write(f"{max([r['bytecode_size'] for r in results])/1024/1024:.2f} MB\n\n")
        
        f.write("### Key Findings\n\n")
        f.write(f"- Maximum analysis time for JUMPDEST-only bytecode: {max_jumpdest_time:.2f} ms\n")
        f.write(f"- Maximum analysis time for PUSH1 0x5b sequences: {max_push_time:.2f} ms\n")
        f.write(f"- Performance ratio (15MB / 48KB) for JUMPDEST-only: {jumpdest_ratio:.2f}x\n")
        f.write(f"- Performance ratio (15MB / 48KB) for PUSH1 sequences: {push_ratio:.2f}x\n")
        
        # Calculate and write normalized performance metrics
        largest_jumpdest = jumpdest_results[-1]
        largest_push = push_results[-1]
        jumpdest_normalized = largest_jumpdest['average_ms'] * 1000 / (largest_jumpdest['bytecode_size'] / 1024)
        push_normalized = largest_push['average_ms'] * 1000 / (largest_push['bytecode_size'] / 1024)
        f.write(f"- Normalized time for largest JUMPDEST-only bytecode: {jumpdest_normalized:.3f} us/KB\n")
        f.write(f"- Normalized time for largest PUSH1 sequences: {push_normalized:.3f} us/KB\n\n")
        
        if MATPLOTLIB_AVAILABLE:
            f.write("## Analysis Performance Charts\n\n")
            f.write(f"![Analysis Performance]({os.path.relpath(plot_file)})\n\n")
            f.write(f"![Runtime Distribution]({os.path.relpath(distribution_plot)})\n\n")
        
        f.write("## Detailed Results\n\n")
        
        # JUMPDEST results
        f.write("### JUMPDEST-only Bytecode\n\n")
        f.write("| Size | Size (KB) | Average Time (ms) | Time per KB (us/KB) | JUMPDESTs Found | Ratio to 48KB |\n")
        f.write("|------|-----------|-------------------|---------------------|-----------------|---------------|\n")
        
        eip_time = eip_limit_jumpdest['average_ms'] if eip_limit_jumpdest else 1.0
        
        for result in jumpdest_results:
            ratio = result['average_ms'] / eip_time
            # Calculate normalized time (ms per KB)
            normalized_time = result['average_ms'] * 1000 / (result['bytecode_size'] / 1024) if result['bytecode_size'] > 0 else 0
            f.write(f"| {result['bytecode_size']} | {result['bytecode_size']/1024:.2f} KB | ")
            f.write(f"{result['average_ms']:.3f} ms | {normalized_time:.3f} us/KB | {result['jumpdests_found']} | {ratio:.2f}x |\n")
        
        f.write("\n")
        
        # PUSH results
        f.write("### PUSH1 0x5b Sequence Bytecode\n\n")
        f.write("| Size | Size (KB) | Average Time (ms) | Time per KB (ms/KB) | JUMPDESTs Found | Ratio to 48KB |\n")
        f.write("|------|-----------|-------------------|---------------------|-----------------|---------------|\n")
        
        eip_time = eip_limit_push['average_ms'] if eip_limit_push else 1.0
        
        for result in push_results:
            ratio = result['average_ms'] / eip_time
            # Calculate normalized time (us per KB)
            normalized_time = result['average_ms'] * 1000 / (result['bytecode_size'] / 1024) if result['bytecode_size'] > 0 else 0
            f.write(f"| {result['bytecode_size']} | {result['bytecode_size']/1024:.2f} KB | ")
            f.write(f"{result['average_ms']:.3f} ms | {normalized_time:.3f} us/KB | {result['jumpdests_found']} | {ratio:.2f}x |\n")
            
        f.write("\n")
   
    print(f"Report generated: {REPORT_FILE}")

def main():
    start_time = time.time()
    
    print("=== EIP-3860 Benchmark Suite ===")
    
    # Generate bytecode samples
    generate_bytecode()
    
    # Run the benchmarks
    results = run_benchmarks()
    
    # Verify we have results
    if not results:
        print("ERROR: No benchmark results were generated!")
        return
        
    jumpdest_results = [r for r in results if 'jumpdest_monster' in r['bytecode_file']]
    if not jumpdest_results:
        print("WARNING: No JUMPDEST benchmark results were found!")
    
    # Save results to CSV
    csv_file, detailed_csv = save_results_to_csv(results)
    
    # Create plots - these may be None if matplotlib is not available
    plot_file, distribution_plot = create_plots(results)
    
    # Generate report
    generate_report(results, csv_file, plot_file, distribution_plot)
    
    elapsed = time.time() - start_time
    print(f"\nBenchmark completed in {elapsed:.2f} seconds")
    print(f"Report available at: {REPORT_FILE}")

if __name__ == "__main__":
    main()
