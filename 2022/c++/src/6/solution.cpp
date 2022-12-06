#include <fstream>
#include <iostream>
#include <unordered_set>

#include <solution.hpp>

int getMarkerIndex(const int MARKER_LEN, const std::string &data) {
    int ix = MARKER_LEN;
    bool found = false;
    while (ix <= data.length() && !found) {
        auto ss = std::string_view(data).substr(ix - MARKER_LEN, MARKER_LEN);
        if (std::unordered_set<char>{ss.begin(), ss.end()}.size() == MARKER_LEN)
            found = true;
        else
            ++ix;
    }
    return ix;
}

const std::string part1(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::string data;
    std::getline(std::ifstream{inputPath}, data);
    const int MARKER_LEN = 4;
    int ix = getMarkerIndex(MARKER_LEN, data);

    return std::to_string(ix);
}

const std::string test_part1_expected() { return "7"; }

const std::string part2(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::string data;
    std::getline(std::ifstream{inputPath}, data);
    const int MARKER_LEN = 14;
    int ix = getMarkerIndex(MARKER_LEN, data);

    return std::to_string(ix);
}

const std::string test_part2_expected() { return "19"; }