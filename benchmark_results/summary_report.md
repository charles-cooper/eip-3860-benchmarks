# JUMPDEST Analysis Benchmark Report

## Summary

- **Date:** 2025-03-13 12:45:03
- **Number of tests:** 24
- **Bytecode size range:** 128 bytes to 15.00 MB

### Key Findings

- Maximum analysis time for JUMPDEST-only bytecode: 22.85 ms
- Maximum analysis time for PUSH1 0x5b sequences: 19.38 ms
- Performance ratio (15MB / 48KB) for JUMPDEST-only: 317.32x
- Performance ratio (15MB / 48KB) for PUSH1 sequences: 317.62x
- Normalized time for largest JUMPDEST-only bytecode: 1.487 us/KB
- Normalized time for largest PUSH1 sequences: 1.261 us/KB

## Analysis Performance Charts

![Analysis Performance](benchmark_results/analysis_performance.png)

![Runtime Distribution](benchmark_results/runtime_distribution.png)

## Detailed Results

### JUMPDEST-only Bytecode

| Size | Size (KB) | Average Time (ms) | Time per KB (us/KB) | JUMPDESTs Found | Ratio to 48KB |
|------|-----------|-------------------|---------------------|-----------------|---------------|
| 128 | 0.12 KB | 0.000 ms | 0.000 us/KB | 128 | 0.00x |
| 1024 | 1.00 KB | 0.004 ms | 4.000 us/KB | 1024 | 0.06x |
| 49152 | 48.00 KB | 0.072 ms | 1.500 us/KB | 49152 | 1.00x |
| 65536 | 64.00 KB | 0.095 ms | 1.484 us/KB | 65536 | 1.32x |
| 131072 | 128.00 KB | 0.195 ms | 1.523 us/KB | 131072 | 2.71x |
| 262144 | 256.00 KB | 0.375 ms | 1.465 us/KB | 262144 | 5.21x |
| 524288 | 512.00 KB | 0.749 ms | 1.463 us/KB | 524288 | 10.40x |
| 1048576 | 1024.00 KB | 1.499 ms | 1.464 us/KB | 1048576 | 20.82x |
| 2097152 | 2048.00 KB | 3.005 ms | 1.467 us/KB | 2097152 | 41.74x |
| 5242880 | 5120.00 KB | 7.560 ms | 1.477 us/KB | 5242880 | 105.00x |
| 10485760 | 10240.00 KB | 15.366 ms | 1.501 us/KB | 10485760 | 213.42x |
| 15728640 | 15360.00 KB | 22.847 ms | 1.487 us/KB | 15728640 | 317.32x |

### PUSH1 0x5b Sequence Bytecode

| Size | Size (KB) | Average Time (ms) | Time per KB (ms/KB) | JUMPDESTs Found | Ratio to 48KB |
|------|-----------|-------------------|---------------------|-----------------|---------------|
| 128 | 0.12 KB | 0.000 ms | 0.000 us/KB | 0 | 0.00x |
| 1024 | 1.00 KB | 0.001 ms | 1.000 us/KB | 0 | 0.02x |
| 49152 | 48.00 KB | 0.061 ms | 1.271 us/KB | 0 | 1.00x |
| 65536 | 64.00 KB | 0.092 ms | 1.438 us/KB | 0 | 1.51x |
| 131072 | 128.00 KB | 0.161 ms | 1.258 us/KB | 0 | 2.64x |
| 262144 | 256.00 KB | 0.324 ms | 1.266 us/KB | 0 | 5.31x |
| 524288 | 512.00 KB | 0.649 ms | 1.268 us/KB | 0 | 10.64x |
| 1048576 | 1024.00 KB | 1.263 ms | 1.233 us/KB | 0 | 20.70x |
| 2097152 | 2048.00 KB | 2.535 ms | 1.238 us/KB | 0 | 41.56x |
| 5242880 | 5120.00 KB | 6.370 ms | 1.244 us/KB | 0 | 104.43x |
| 10485760 | 10240.00 KB | 12.855 ms | 1.255 us/KB | 0 | 210.74x |
| 15728640 | 15360.00 KB | 19.375 ms | 1.261 us/KB | 0 | 317.62x |

