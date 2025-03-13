# JUMPDEST Analysis Benchmark Report

## Summary

- **Date:** 2025-03-13 12:29:01
- **Number of tests:** 24
- **Bytecode size range:** 128 bytes to 15.00 MB

### Key Findings

- Maximum analysis time for JUMPDEST-only bytecode: 37.05 ms
- Maximum analysis time for PUSH1 0x5b sequences: 20.17 ms
- Performance ratio (15MB / 48KB) for JUMPDEST-only: 324.97x
- Performance ratio (15MB / 48KB) for PUSH1 sequences: 305.67x
- Normalized time for largest JUMPDEST-only bytecode: 2.412 us/KB
- Normalized time for largest PUSH1 sequences: 1.313 us/KB

## Analysis Performance Charts

![Analysis Performance](benchmark_results/analysis_performance.png)

![Runtime Distribution](benchmark_results/runtime_distribution.png)

## Detailed Results

### JUMPDEST-only Bytecode

| Size | Size (KB) | Average Time (ms) | Time per KB (us/KB) | JUMPDESTs Found | Ratio to 48KB |
|------|-----------|-------------------|---------------------|-----------------|---------------|
| 128 | 0.12 KB | 0.000 ms | 0.000 us/KB | 128 | 0.00x |
| 1024 | 1.00 KB | 0.002 ms | 2.000 us/KB | 1024 | 0.02x |
| 49152 | 48.00 KB | 0.114 ms | 2.375 us/KB | 49152 | 1.00x |
| 65536 | 64.00 KB | 0.152 ms | 2.375 us/KB | 65536 | 1.33x |
| 131072 | 128.00 KB | 0.335 ms | 2.617 us/KB | 131072 | 2.94x |
| 262144 | 256.00 KB | 0.622 ms | 2.430 us/KB | 262144 | 5.46x |
| 524288 | 512.00 KB | 1.221 ms | 2.385 us/KB | 524288 | 10.71x |
| 1048576 | 1024.00 KB | 2.453 ms | 2.396 us/KB | 1048576 | 21.52x |
| 2097152 | 2048.00 KB | 4.883 ms | 2.384 us/KB | 2097152 | 42.83x |
| 5242880 | 5120.00 KB | 12.400 ms | 2.422 us/KB | 5242880 | 108.77x |
| 10485760 | 10240.00 KB | 24.940 ms | 2.436 us/KB | 10485760 | 218.77x |
| 15728640 | 15360.00 KB | 37.047 ms | 2.412 us/KB | 15728640 | 324.97x |

### PUSH1 0x5b Sequence Bytecode

| Size | Size (KB) | Average Time (ms) | Time per KB (ms/KB) | JUMPDESTs Found | Ratio to 48KB |
|------|-----------|-------------------|---------------------|-----------------|---------------|
| 128 | 0.12 KB | 0.000 ms | 0.000 us/KB | 0 | 0.00x |
| 1024 | 1.00 KB | 0.002 ms | 2.000 us/KB | 0 | 0.03x |
| 49152 | 48.00 KB | 0.066 ms | 1.375 us/KB | 0 | 1.00x |
| 65536 | 64.00 KB | 0.086 ms | 1.344 us/KB | 0 | 1.30x |
| 131072 | 128.00 KB | 0.163 ms | 1.273 us/KB | 0 | 2.47x |
| 262144 | 256.00 KB | 0.349 ms | 1.363 us/KB | 0 | 5.29x |
| 524288 | 512.00 KB | 0.693 ms | 1.354 us/KB | 0 | 10.50x |
| 1048576 | 1024.00 KB | 1.340 ms | 1.309 us/KB | 0 | 20.30x |
| 2097152 | 2048.00 KB | 3.080 ms | 1.504 us/KB | 0 | 46.67x |
| 5242880 | 5120.00 KB | 6.810 ms | 1.330 us/KB | 0 | 103.18x |
| 10485760 | 10240.00 KB | 13.058 ms | 1.275 us/KB | 0 | 197.85x |
| 15728640 | 15360.00 KB | 20.174 ms | 1.313 us/KB | 0 | 305.67x |

