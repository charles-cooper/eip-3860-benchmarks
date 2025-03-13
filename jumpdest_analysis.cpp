#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <string>
#include <iomanip>
#include <sstream>
#include <algorithm>

// EVM opcodes
constexpr uint8_t OP_PUSH1 = 0x60;
constexpr uint8_t OP_PUSH32 = 0x7f;
constexpr uint8_t OP_JUMPDEST = 0x5b;

// Convert hex string to bytes
std::vector<uint8_t> hex_string_to_bytes(const std::string& hex_string) {
    std::vector<uint8_t> bytes;
    std::string clean_hex = hex_string;
    
    // Remove whitespace
    clean_hex.erase(std::remove_if(clean_hex.begin(), clean_hex.end(), isspace), clean_hex.end());
    
    // Remove '0x' prefix if present
    if (clean_hex.length() >= 2 && clean_hex.substr(0, 2) == "0x") {
        clean_hex = clean_hex.substr(2);
    }
    
    // Check for even length
    if (clean_hex.length() % 2 != 0) {
        std::cerr << "Error: Hex string must have even length" << std::endl;
        exit(1);
    }
    
    // Reserve space for better performance
    bytes.reserve(clean_hex.length() / 2);
    
    // Convert hex string to bytes using standard library
    for (size_t i = 0; i < clean_hex.length(); i += 2) {
        std::istringstream iss(clean_hex.substr(i, 2));
        unsigned int value;
        iss >> std::hex >> value;
        bytes.push_back(static_cast<uint8_t>(value));
    }
    
    return bytes;
}

std::vector<uint8_t> read_bytecode_from_file(const std::string& filename) {
    std::ifstream file(filename);
    if (!file) {
        std::cerr << "Error: Could not open file " << filename << std::endl;
        exit(1);
    }

    // Read the entire file at once
    std::stringstream buffer;
    buffer << file.rdbuf();
    
    return hex_string_to_bytes(buffer.str());
}

std::vector<bool> perform_jumpdest_analysis(const std::vector<uint8_t>& bytecode) {
    size_t bytecode_size = bytecode.size();

    std::vector<bool> valid_jumpdests(bytecode_size);

    for (size_t pc = 0; pc < bytecode_size; pc++) {
        uint8_t opcode = bytecode[pc];
        
        // Mark valid JUMPDEST
        if (opcode == OP_JUMPDEST) {
            valid_jumpdests[pc] = true;
        }
        
        // Skip push data
        else if (opcode >= OP_PUSH1 && opcode <= OP_PUSH32) {
            size_t push_bytes = opcode - OP_PUSH1 + 1;
            pc += push_bytes;
        }
    }
    
    return valid_jumpdests;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <bytecode_file>" << std::endl;
        return 1;
    }
    
    std::string filename = argv[1];
    std::vector<uint8_t> bytecode = read_bytecode_from_file(filename);
    
    std::cout << "Bytecode size: " << bytecode.size() << " bytes" << std::endl;
    
    // Benchmark jumpdest analysis
    const int num_runs = 10;
    double total_duration = 0.0;
    
    for (int i = 0; i < num_runs; i++) {
        auto start = std::chrono::high_resolution_clock::now();
        
        std::vector<bool> valid_jumpdests = perform_jumpdest_analysis(bytecode);
        
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> duration = end - start;
        
        total_duration += duration.count();
        
        // Count valid jumpdests so that perform_jumpdest_analysis is not optimized out
        int jumpdest_count = 0;
        for (bool is_valid : valid_jumpdests) {
            if (is_valid) jumpdest_count++;
        }
        
        std::cout << "Run " << (i + 1) << ": " 
                  << std::fixed << std::setprecision(3) << duration.count() << " ms, "
                  << jumpdest_count << " valid JUMPDESTs found" << std::endl;
    }
    
    double average_duration = total_duration / num_runs;
    std::cout << "Average time: " << std::fixed << std::setprecision(3) 
              << average_duration << " ms" << std::endl;
    
   
    return 0;
}
