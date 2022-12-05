//
// Created by francisco on 01/12/22.
//

#ifndef INC_2022_SOLUTION_HPP
#define INC_2022_SOLUTION_HPP

#include <filesystem>

namespace fs = std::filesystem;

const std::string part1(const fs::path &inputPath);

const std::string part2(const fs::path &inputPath);

const std::string test_part1_expected();

const std::string test_part2_expected();

#endif //INC_2022_SOLUTION_HPP
