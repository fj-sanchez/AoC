#include <fstream>
#include <iostream>

#include <solution.hpp>

const std::string part1(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::ifstream input{inputPath};

    return "0";
}

const std::string test_part1_expected() { return "0"; }

const std::string part2(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::ifstream input{inputPath};

    return "0";
}

const std::string test_part2_expected() { return "0"; }