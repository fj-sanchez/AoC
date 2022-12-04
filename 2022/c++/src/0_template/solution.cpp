#include <fstream>
#include <iostream>

#include <solution.hpp>

int part1(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::ifstream input{inputPath};

    return 0;
}

int test_part1_expected() { return 0; }

int part2(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::ifstream input{inputPath};

    return 0;
}

int test_part2_expected() { return 0; }