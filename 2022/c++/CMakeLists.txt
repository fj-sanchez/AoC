cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

# Change to something passed at compile time
set(day 1)

set(This AoC22)
project(${This})

set(DataDir ${PROJECT_SOURCE_DIR}/data/${day})
set(TestInput ${DataDir}/test_input)
set(SolutionInput ${DataDir}/input)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS NO)

include(dependencies.cmake)

enable_testing()
include_directories(include)
add_subdirectory(src)
add_subdirectory(test)