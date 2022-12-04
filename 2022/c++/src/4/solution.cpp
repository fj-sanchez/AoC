#include <fstream>
#include <iostream>
#include <regex>

#include <solution.hpp>


const std::regex SECTORS_REGEX{R"(^(\d+)-(\d+),(\d+)-(\d+)$)"};

void extractSectors(const std::string &line, std::array<int, 4> &sectors) {
    std::smatch matches;
    std::regex_search(line, matches, SECTORS_REGEX);
    if (matches.size() != 5) {
        std::cout << "Malformed line: " << line << std::endl;
        exit(1);
    }
    std::transform(matches.begin() + 1, matches.end(), sectors.begin(),
                   [](auto const &m) { return stoi(m.str()); });
}

int part1(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::ifstream input{inputPath};
    std::string line;

    int total{0};
    std::array<int, 4> sectors;
    while (std::getline(input, line)) {
        extractSectors(line, sectors);
        auto [s1_start, s1_end, s2_start, s2_end] = sectors;
        if ((s1_start <= s2_start && s1_end >= s2_end) || (s2_start <= s1_start && s2_end >= s1_end)) ++total;
    }

    return total;
}


int test_part1_expected() { return 2; }

int part2(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::ifstream input{inputPath};
    std::string line;

    int total{0};
    std::array<int, 4> sectors;
    while (std::getline(input, line)) {
        extractSectors(line, sectors);
        auto [s1_start, s1_end, s2_start, s2_end] = sectors;
        if (s1_start <= s2_end && s1_end >= s2_start) ++total;
    }

    return total;
}

int test_part2_expected() { return 4; }