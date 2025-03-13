# JUMPDEST Analysis Benchmark Report

## Summary

- **Date:** 2025-03-13 12:49:11
- **Number of tests:** 24
- **Bytecode size range:** 128 bytes to 15.00 MB

### Key Findings

- Maximum analysis time for JUMPDEST-only bytecode: 22.86 ms
- Maximum analysis time for PUSH1 0x5b sequences: 19.85 ms
- Performance ratio (15MB / 48KB) for JUMPDEST-only: 326.61x
- Performance ratio (15MB / 48KB) for PUSH1 sequences: 287.72x
- Normalized time for largest JUMPDEST-only bytecode: 1.488 us/KB
- Normalized time for largest PUSH1 sequences: 1.293 us/KB

## Detailed Results

### JUMPDEST-only Bytecode

| Size | Size (KB) | Average Time (ms) | Time per KB (us/KB) | JUMPDESTs Found | Ratio to 48KB |
|------|-----------|-------------------|---------------------|-----------------|---------------|
| 128 | 0.12 KB | 0.000 ms | 0.000 us/KB | 128 | 0.00x |
| 1024 | 1.00 KB | 0.002 ms | 2.000 us/KB | 1024 | 0.03x |
| 49152 | 48.00 KB | 0.070 ms | 1.458 us/KB | 49152 | 1.00x |
| 65536 | 64.00 KB | 0.095 ms | 1.484 us/KB | 65536 | 1.36x |
| 131072 | 128.00 KB | 0.201 ms | 1.570 us/KB | 131072 | 2.87x |
| 262144 | 256.00 KB | 0.376 ms | 1.469 us/KB | 262144 | 5.37x |
| 524288 | 512.00 KB | 0.749 ms | 1.463 us/KB | 524288 | 10.70x |
| 1048576 | 1024.00 KB | 1.500 ms | 1.465 us/KB | 1048576 | 21.43x |
| 2097152 | 2048.00 KB | 3.006 ms | 1.468 us/KB | 2097152 | 42.94x |
| 5242880 | 5120.00 KB | 7.541 ms | 1.473 us/KB | 5242880 | 107.73x |
| 10485760 | 10240.00 KB | 15.146 ms | 1.479 us/KB | 10485760 | 216.37x |
| 15728640 | 15360.00 KB | 22.863 ms | 1.488 us/KB | 15728640 | 326.61x |

### PUSH1 0x5b Sequence Bytecode

| Size | Size (KB) | Average Time (ms) | Time per KB (ms/KB) | JUMPDESTs Found | Ratio to 48KB |
|------|-----------|-------------------|---------------------|-----------------|---------------|
| 128 | 0.12 KB | 0.000 ms | 0.000 us/KB | 0 | 0.00x |
| 1024 | 1.00 KB | 0.001 ms | 1.000 us/KB | 0 | 0.01x |
| 49152 | 48.00 KB | 0.069 ms | 1.438 us/KB | 0 | 1.00x |
| 65536 | 64.00 KB | 0.083 ms | 1.297 us/KB | 0 | 1.20x |
| 131072 | 128.00 KB | 0.174 ms | 1.359 us/KB | 0 | 2.52x |
| 262144 | 256.00 KB | 0.341 ms | 1.332 us/KB | 0 | 4.94x |
| 524288 | 512.00 KB | 0.636 ms | 1.242 us/KB | 0 | 9.22x |
| 1048576 | 1024.00 KB | 1.266 ms | 1.236 us/KB | 0 | 18.35x |
| 2097152 | 2048.00 KB | 2.756 ms | 1.346 us/KB | 0 | 39.94x |
| 5242880 | 5120.00 KB | 6.576 ms | 1.284 us/KB | 0 | 95.30x |
| 10485760 | 10240.00 KB | 12.911 ms | 1.261 us/KB | 0 | 187.12x |
| 15728640 | 15360.00 KB | 19.853 ms | 1.293 us/KB | 0 | 287.72x |

