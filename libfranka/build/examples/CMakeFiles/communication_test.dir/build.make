# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /workspace/libfranka

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /workspace/libfranka/build

# Include any dependencies generated for this target.
include examples/CMakeFiles/communication_test.dir/depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/communication_test.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/communication_test.dir/flags.make

examples/CMakeFiles/communication_test.dir/communication_test.cpp.o: examples/CMakeFiles/communication_test.dir/flags.make
examples/CMakeFiles/communication_test.dir/communication_test.cpp.o: ../examples/communication_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspace/libfranka/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/CMakeFiles/communication_test.dir/communication_test.cpp.o"
	cd /workspace/libfranka/build/examples && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/communication_test.dir/communication_test.cpp.o -c /workspace/libfranka/examples/communication_test.cpp

examples/CMakeFiles/communication_test.dir/communication_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/communication_test.dir/communication_test.cpp.i"
	cd /workspace/libfranka/build/examples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspace/libfranka/examples/communication_test.cpp > CMakeFiles/communication_test.dir/communication_test.cpp.i

examples/CMakeFiles/communication_test.dir/communication_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/communication_test.dir/communication_test.cpp.s"
	cd /workspace/libfranka/build/examples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspace/libfranka/examples/communication_test.cpp -o CMakeFiles/communication_test.dir/communication_test.cpp.s

# Object files for target communication_test
communication_test_OBJECTS = \
"CMakeFiles/communication_test.dir/communication_test.cpp.o"

# External object files for target communication_test
communication_test_EXTERNAL_OBJECTS =

examples/communication_test: examples/CMakeFiles/communication_test.dir/communication_test.cpp.o
examples/communication_test: examples/CMakeFiles/communication_test.dir/build.make
examples/communication_test: examples/libexamples_common.a
examples/communication_test: libfranka.so.0.9.2
examples/communication_test: examples/CMakeFiles/communication_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspace/libfranka/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable communication_test"
	cd /workspace/libfranka/build/examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/communication_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/communication_test.dir/build: examples/communication_test

.PHONY : examples/CMakeFiles/communication_test.dir/build

examples/CMakeFiles/communication_test.dir/clean:
	cd /workspace/libfranka/build/examples && $(CMAKE_COMMAND) -P CMakeFiles/communication_test.dir/cmake_clean.cmake
.PHONY : examples/CMakeFiles/communication_test.dir/clean

examples/CMakeFiles/communication_test.dir/depend:
	cd /workspace/libfranka/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspace/libfranka /workspace/libfranka/examples /workspace/libfranka/build /workspace/libfranka/build/examples /workspace/libfranka/build/examples/CMakeFiles/communication_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/CMakeFiles/communication_test.dir/depend

