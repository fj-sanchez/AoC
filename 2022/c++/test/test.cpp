//
// Created by francisco on 03/12/22.
//

#include <gtest/gtest.h>
#include <iostream>

#include "test.hpp"

TEST(AdventOfCode, Part1) {
    const fs::path test_input{TEST_INPUT_PATH};
    ASSERT_EQ(part1(test_input), test_part1_expected());
    const fs::path solution_input{SOLUTION_INPUT_PATH};
    auto result = part1(solution_input);
    GTEST_COUT << "PART 1 SOLUTION: " << result << std::endl;
}

TEST(AdventOfCode, Part2) {
    const fs::path test_input{TEST_INPUT_PATH};
    ASSERT_EQ(part2(test_input), test_part2_expected());
    const fs::path solution_input{SOLUTION_INPUT_PATH};
    auto result = part2(solution_input);
    GTEST_COUT << "PART 2 SOLUTION: " << result << std::endl;
}