# JUMPDEST Analysis Benchmark Report

## Summary

- **Date:** 2025-03-16 15:24:23
- **Number of tests:** 24
- **Bytecode size range:** 128 bytes to 15.00 MB

### Key Findings

- Maximum analysis time for JUMPDEST-only bytecode: 10.78 ms
- Maximum analysis time for PUSH1 0x5b sequences: 20.32 ms
- Performance ratio (15MB / 48KB) for JUMPDEST-only: 337.00x
- Performance ratio (15MB / 48KB) for PUSH1 sequences: 244.76x
- Normalized time for largest JUMPDEST-only bytecode: 0.702 us/KB
- Normalized time for largest PUSH1 sequences: 1.323 us/KB

## Detailed Results

### JUMPDEST-only Bytecode

| Size | Size (KB) | Average Time (ms) | Time per KB (us/KB) | JUMPDESTs Found | Ratio to 48KB |
|------|-----------|-------------------|---------------------|-----------------|---------------|
| 128 | 0.12 KB | 0.000 ms | 0.000 us/KB | 128 | 0.00x |
| 1024 | 1.00 KB | 0.001 ms | 1.000 us/KB | 1024 | 0.03x |
| 49152 | 48.00 KB | 0.032 ms | 0.667 us/KB | 49152 | 1.00x |
| 65536 | 64.00 KB | 0.041 ms | 0.641 us/KB | 65536 | 1.28x |
| 131072 | 128.00 KB | 0.089 ms | 0.695 us/KB | 131072 | 2.78x |
| 262144 | 256.00 KB | 0.169 ms | 0.660 us/KB | 262144 | 5.28x |
| 524288 | 512.00 KB | 0.328 ms | 0.641 us/KB | 524288 | 10.25x |
| 1048576 | 1024.00 KB | 0.639 ms | 0.624 us/KB | 1048576 | 19.97x |
| 2097152 | 2048.00 KB | 1.306 ms | 0.638 us/KB | 2097152 | 40.81x |
| 5242880 | 5120.00 KB | 4.203 ms | 0.821 us/KB | 5242880 | 131.34x |
| 10485760 | 10240.00 KB | 7.015 ms | 0.685 us/KB | 10485760 | 219.22x |
| 15728640 | 15360.00 KB | 10.784 ms | 0.702 us/KB | 15728640 | 337.00x |

### PUSH1 0x5b Sequence Bytecode

| Size | Size (KB) | Average Time (ms) | Time per KB (ms/KB) | JUMPDESTs Found | Ratio to 48KB |
|------|-----------|-------------------|---------------------|-----------------|---------------|
| 128 | 0.12 KB | 0.000 ms | 0.000 us/KB | 64 | 0.00x |
| 1024 | 1.00 KB | 0.001 ms | 1.000 us/KB | 512 | 0.01x |
| 49152 | 48.00 KB | 0.083 ms | 1.729 us/KB | 24576 | 1.00x |
| 65536 | 64.00 KB | 0.118 ms | 1.844 us/KB | 32768 | 1.42x |
| 131072 | 128.00 KB | 0.214 ms | 1.672 us/KB | 65536 | 2.58x |
| 262144 | 256.00 KB | 0.325 ms | 1.270 us/KB | 131072 | 3.92x |
| 524288 | 512.00 KB | 0.888 ms | 1.734 us/KB | 262144 | 10.70x |
| 1048576 | 1024.00 KB | 1.328 ms | 1.297 us/KB | 524288 | 16.00x |
| 2097152 | 2048.00 KB | 2.543 ms | 1.242 us/KB | 1048576 | 30.64x |
| 5242880 | 5120.00 KB | 6.661 ms | 1.301 us/KB | 2621440 | 80.25x |
| 10485760 | 10240.00 KB | 13.319 ms | 1.301 us/KB | 5242880 | 160.47x |
| 15728640 | 15360.00 KB | 20.315 ms | 1.323 us/KB | 7864320 | 244.76x |

