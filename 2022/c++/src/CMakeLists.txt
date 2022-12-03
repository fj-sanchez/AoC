cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

if (NOT DEFINED day)
    message(SEND_ERROR "Variable \"day\" not defined")
endif ()

set(This Day${day})

set(Sources ${day}/solution.cpp)

add_library(${This} STATIC ${Sources})