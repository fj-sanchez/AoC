#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>

#include <solution.hpp>

const std::string part1(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::ifstream input{inputPath};
    std::vector<int> calories{0};
    std::string line;

    while (!input.eof()) {
        if (std::getline(input, line) && line.empty()) {
            calories.insert(calories.end(), 0);
        } else {
            *(--calories.end()) += std::stoi(line);
        }
    }

    return std::to_string(*std::max_element(calories.begin(), calories.end()));
}

const std::string test_part1_expected() { return "24000"; }

const std::string part2(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::ifstream input{inputPath};
    std::vector<int> calories{0};
    std::string line;

    while (!input.eof()) {
        if (std::getline(input, line) && line.empty()) {
            calories.insert(calories.end(), 0);
        } else {
            *(--calories.end()) += std::stoi(line);
        }
    }
    std::sort(calories.begin(), calories.end());
    return std::to_string(std::reduce(calories.end() - 3, calories.end()));
}

const std::string test_part2_expected() { return "45000"; }