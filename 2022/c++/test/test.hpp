//
// Created by francisco on 03/12/22.
//

#ifndef AOC22_TEST_HPP
#define AOC22_TEST_HPP

#include <filesystem>
#include <iostream>

#define GTEST_COUT std::cout << "[          ] "
#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)

namespace fs = std::filesystem;

extern int part1(const fs::path &inputPath);

extern int part2(const fs::path &inputPath);

extern int test_part1_expected();

extern int test_part2_expected();

const std::string TEST_INPUT_PATH = TOSTRING(TEST_INPUT);
const std::string SOLUTION_INPUT_PATH = TOSTRING(SOLUTION_INPUT);

#endif //AOC22_TEST_HPP
