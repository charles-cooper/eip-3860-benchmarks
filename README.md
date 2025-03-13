
prerequisites:
- g++
- matplotlib (for plotting results)

create a new virtualenv with matplotlib (`pip install matplotlib`)

compile the analyzer file:
```bash
g++ -o jumpdest_analyzer jumpdest_analysis.cpp -std=c++17 -O3
```

run the benchmark:
```bash
./run_benchmark.py
```
