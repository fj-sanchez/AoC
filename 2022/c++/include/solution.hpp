//
// Created by francisco on 01/12/22.
//

#ifndef INC_2022_SOLUTION_HPP
#define INC_2022_SOLUTION_HPP

#include <filesystem>

namespace fs = std::filesystem;

int part1(const fs::path &inputPath);

int part2(const fs::path &inputPath);

int test_part1_expected();

int test_part2_expected();

#endif //INC_2022_SOLUTION_HPP
