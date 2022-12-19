#include <array>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

#include <solution.hpp>
#include <unordered_map>
#include <unordered_set>

struct GridLocation {
    int x, y;
};

bool operator==(GridLocation a, GridLocation b) {
    return a.x == b.x && a.y == b.y;
}

bool operator!=(GridLocation a, GridLocation b) {
    return !(a == b);
}

bool operator<(GridLocation a, GridLocation b) {
    return std::tie(a.x, a.y) < std::tie(b.x, b.y);
}

std::basic_iostream<char>::basic_ostream &
operator<<(std::basic_iostream<char>::basic_ostream &out, const GridLocation &loc) {
    out << '(' << loc.x << ',' << loc.y << ')';
    return out;
}

namespace std {
/* implement hash function so we can put GridLocation into an unordered_set */
    template<>
    struct hash<GridLocation> {
        std::size_t operator()(const GridLocation &id) const noexcept {
            // NOTE: better to use something like boost hash_combine
            return std::hash<int>()(id.x ^ (id.y << 16));
        }
    };
}


struct SquareGrid {
    const std::array<GridLocation, 4> DIRS{
            /* East, West, North, South */
            GridLocation{1, 0}, GridLocation{-1, 0},
            GridLocation{0, -1}, GridLocation{0, 1}
    };

    int width, height;
    std::unordered_map<GridLocation, char> &heightMap;

    SquareGrid(int width_, int height_, std::unordered_map<GridLocation, char> &heightMap)
            : width(width_), height(height_), heightMap(heightMap) {}

    bool in_bounds(GridLocation id) const {
        return 0 <= id.x && id.x < width
               && 0 <= id.y && id.y < height;
    }

    bool passable(GridLocation from, GridLocation to) const {
        auto fromValue = heightMap.at(from);
        auto toValue = heightMap.at(to);
        return toValue <= fromValue + 1;
    }

    std::vector<GridLocation> neighbors(GridLocation id) const {
        std::vector<GridLocation> results;

        for (GridLocation dir: DIRS) {
            GridLocation next{id.x + dir.x, id.y + dir.y};
            if (in_bounds(next) && passable(id, next)) {
                results.push_back(next);
            }
        }
        return results;
    }
};

template<typename Location, typename Graph>
std::unordered_map<Location, Location>
breadth_first_search(Graph graph, Location start, Location goal) {
    std::queue<Location> frontier;
    frontier.push(start);

    std::unordered_map<Location, Location> came_from;
    came_from[start] = start;

    while (!frontier.empty()) {
        Location current = frontier.front();
        frontier.pop();

        if (current == goal) {
            break;
        }

        for (Location next: graph.neighbors(current)) {
            if (came_from.find(next) == came_from.end()) {
                frontier.push(next);
                came_from[next] = current;
            }
        }
    }
    return came_from;
}

std::pair<int, int>
parseInput(const fs::path &inputPath, std::unordered_map<GridLocation, char> &heightMap, GridLocation &start,
           GridLocation &end) {

    std::string line;
    std::ifstream input = std::ifstream{inputPath};
    int y = 0;
    int x = 0;
    while (std::getline(input, line)) {
        for (x = 0; x < line.length(); ++x) {
            auto c = line[x];
            if (c == 'S') {
                start = GridLocation{x, y};
                c = 'a';
            } else if (c == 'E') {
                end = GridLocation{x, y};
                c = 'z';
            }
            heightMap[GridLocation{x, y}] = c;
        }
        ++y;
    }
    return std::pair<int, int>{x, y};
}

const std::string part1(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::unordered_map<GridLocation, char> heightMap{};
    GridLocation start;
    GridLocation end;
    auto [width, height] = parseInput(inputPath, heightMap, start, end);
    SquareGrid grid(width, height, heightMap);
    auto parents = breadth_first_search(grid, start, end);

    auto x = parents.at(end);
    int i = 1;
    while (true) {
        auto prev = parents.at(x);
        if (prev == x)
            break;
        x = prev;
        ++i;
    }

    return std::to_string(i);
}

const std::string test_part1_expected() { return "31"; }

const std::string part2(const fs::path &inputPath) {
    if (!fs::is_regular_file(inputPath)) {
        std::cout << "Cannot read input file: " << inputPath;
        exit(1);
    }

    std::unordered_map<GridLocation, char> heightMap{};
    GridLocation start;
    GridLocation end;
    auto [width, height] = parseInput(inputPath, heightMap, start, end);
    SquareGrid grid(width, height, heightMap);

    std::unordered_set<GridLocation> visited{};
    int min_len = 100000;
    for (auto &[coord, value]: heightMap) {
        if (value == 'a' && !visited.contains(coord)) {
            visited.insert(coord);
            auto parents = breadth_first_search(grid, coord, end);

            if (!parents.contains(end))
                continue;
            auto x = parents.at(end);
            int i = 1;
            while (true) {
                auto prev = parents.at(x);
                if (prev == x)
                    break;
                x = prev;
                ++i;
            }
            min_len = std::min(min_len, i);
        }
    }
    return std::to_string(min_len);
}

const std::string test_part2_expected() { return "29"; }