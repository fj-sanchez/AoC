cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

if (NOT DEFINED day)
    message(SEND_ERROR "Variable " day" not defined")
endif ()

set(This TestSolution)

set(Headers test.hpp)
set(Sources test.cpp)

add_compile_definitions(TEST_INPUT=${TestInput})
add_compile_definitions(SOLUTION_INPUT=${SolutionInput})

add_executable(${This} ${Sources})
target_link_libraries(
        ${This} PUBLIC
        gtest_main
        Day${day}
)

add_test(
        NAME ${This}
        COMMAND ${This}
)