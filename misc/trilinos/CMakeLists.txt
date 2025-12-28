cmake_minimum_required(VERSION 3.16)
project(test_trilinos LANGUAGES CXX)

# Find MPI first
find_package(MPI REQUIRED)

# Find Trilinos
find_package(Trilinos REQUIRED)

add_executable(trilinos_linear linear.cpp)

# Include Trilinos headers + MPI headers
target_include_directories(trilinos_linear PRIVATE ${Trilinos_INCLUDE_DIRS} ${MPI_INCLUDE_PATH})

# Link Trilinos libraries + MPI
target_link_libraries(trilinos_linear PRIVATE ${Trilinos_LIBRARIES} MPI::MPI_CXX)


# COmpile using:
# Make sure Trilinos has been built in:
#   <Trilinos dir>/build
# and installed in
#   <Trilinos dir>/install
# using make install DESTDIR=<... path to ...>/Trilinos/install
#
# Then use this cmake file to compile your app using
#  cmake -DTrilinos_DIR=< Trilinos Dir>/install/lib/cmake/Trilinos .. \
#  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON 