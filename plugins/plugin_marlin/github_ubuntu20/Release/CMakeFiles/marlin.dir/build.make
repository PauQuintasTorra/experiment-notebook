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
CMAKE_SOURCE_DIR = /home/miguelinux/Desktop/marlin/marlin

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/miguelinux/Desktop/marlin/marlin/Release

# Include any dependencies generated for this target.
include CMakeFiles/marlin.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/marlin.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/marlin.dir/flags.make

CMakeFiles/marlin.dir/src/configuration.cc.o: CMakeFiles/marlin.dir/flags.make
CMakeFiles/marlin.dir/src/configuration.cc.o: ../src/configuration.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/marlin.dir/src/configuration.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/marlin.dir/src/configuration.cc.o -c /home/miguelinux/Desktop/marlin/marlin/src/configuration.cc

CMakeFiles/marlin.dir/src/configuration.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/marlin.dir/src/configuration.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/miguelinux/Desktop/marlin/marlin/src/configuration.cc > CMakeFiles/marlin.dir/src/configuration.cc.i

CMakeFiles/marlin.dir/src/configuration.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/marlin.dir/src/configuration.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/miguelinux/Desktop/marlin/marlin/src/configuration.cc -o CMakeFiles/marlin.dir/src/configuration.cc.s

CMakeFiles/marlin.dir/src/dictionary.cc.o: CMakeFiles/marlin.dir/flags.make
CMakeFiles/marlin.dir/src/dictionary.cc.o: ../src/dictionary.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/marlin.dir/src/dictionary.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/marlin.dir/src/dictionary.cc.o -c /home/miguelinux/Desktop/marlin/marlin/src/dictionary.cc

CMakeFiles/marlin.dir/src/dictionary.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/marlin.dir/src/dictionary.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/miguelinux/Desktop/marlin/marlin/src/dictionary.cc > CMakeFiles/marlin.dir/src/dictionary.cc.i

CMakeFiles/marlin.dir/src/dictionary.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/marlin.dir/src/dictionary.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/miguelinux/Desktop/marlin/marlin/src/dictionary.cc -o CMakeFiles/marlin.dir/src/dictionary.cc.s

CMakeFiles/marlin.dir/src/entropyCoder.cc.o: CMakeFiles/marlin.dir/flags.make
CMakeFiles/marlin.dir/src/entropyCoder.cc.o: ../src/entropyCoder.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/marlin.dir/src/entropyCoder.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/marlin.dir/src/entropyCoder.cc.o -c /home/miguelinux/Desktop/marlin/marlin/src/entropyCoder.cc

CMakeFiles/marlin.dir/src/entropyCoder.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/marlin.dir/src/entropyCoder.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/miguelinux/Desktop/marlin/marlin/src/entropyCoder.cc > CMakeFiles/marlin.dir/src/entropyCoder.cc.i

CMakeFiles/marlin.dir/src/entropyCoder.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/marlin.dir/src/entropyCoder.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/miguelinux/Desktop/marlin/marlin/src/entropyCoder.cc -o CMakeFiles/marlin.dir/src/entropyCoder.cc.s

CMakeFiles/marlin.dir/src/entropyDecoder.cc.o: CMakeFiles/marlin.dir/flags.make
CMakeFiles/marlin.dir/src/entropyDecoder.cc.o: ../src/entropyDecoder.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/marlin.dir/src/entropyDecoder.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/marlin.dir/src/entropyDecoder.cc.o -c /home/miguelinux/Desktop/marlin/marlin/src/entropyDecoder.cc

CMakeFiles/marlin.dir/src/entropyDecoder.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/marlin.dir/src/entropyDecoder.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/miguelinux/Desktop/marlin/marlin/src/entropyDecoder.cc > CMakeFiles/marlin.dir/src/entropyDecoder.cc.i

CMakeFiles/marlin.dir/src/entropyDecoder.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/marlin.dir/src/entropyDecoder.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/miguelinux/Desktop/marlin/marlin/src/entropyDecoder.cc -o CMakeFiles/marlin.dir/src/entropyDecoder.cc.s

CMakeFiles/marlin.dir/src/marlin.cc.o: CMakeFiles/marlin.dir/flags.make
CMakeFiles/marlin.dir/src/marlin.cc.o: ../src/marlin.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/marlin.dir/src/marlin.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/marlin.dir/src/marlin.cc.o -c /home/miguelinux/Desktop/marlin/marlin/src/marlin.cc

CMakeFiles/marlin.dir/src/marlin.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/marlin.dir/src/marlin.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/miguelinux/Desktop/marlin/marlin/src/marlin.cc > CMakeFiles/marlin.dir/src/marlin.cc.i

CMakeFiles/marlin.dir/src/marlin.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/marlin.dir/src/marlin.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/miguelinux/Desktop/marlin/marlin/src/marlin.cc -o CMakeFiles/marlin.dir/src/marlin.cc.s

CMakeFiles/marlin.dir/src/prebuilt.cc.o: CMakeFiles/marlin.dir/flags.make
CMakeFiles/marlin.dir/src/prebuilt.cc.o: ../src/prebuilt.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/marlin.dir/src/prebuilt.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/marlin.dir/src/prebuilt.cc.o -c /home/miguelinux/Desktop/marlin/marlin/src/prebuilt.cc

CMakeFiles/marlin.dir/src/prebuilt.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/marlin.dir/src/prebuilt.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/miguelinux/Desktop/marlin/marlin/src/prebuilt.cc > CMakeFiles/marlin.dir/src/prebuilt.cc.i

CMakeFiles/marlin.dir/src/prebuilt.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/marlin.dir/src/prebuilt.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/miguelinux/Desktop/marlin/marlin/src/prebuilt.cc -o CMakeFiles/marlin.dir/src/prebuilt.cc.s

CMakeFiles/marlin.dir/src/profiler.cc.o: CMakeFiles/marlin.dir/flags.make
CMakeFiles/marlin.dir/src/profiler.cc.o: ../src/profiler.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object CMakeFiles/marlin.dir/src/profiler.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/marlin.dir/src/profiler.cc.o -c /home/miguelinux/Desktop/marlin/marlin/src/profiler.cc

CMakeFiles/marlin.dir/src/profiler.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/marlin.dir/src/profiler.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/miguelinux/Desktop/marlin/marlin/src/profiler.cc > CMakeFiles/marlin.dir/src/profiler.cc.i

CMakeFiles/marlin.dir/src/profiler.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/marlin.dir/src/profiler.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/miguelinux/Desktop/marlin/marlin/src/profiler.cc -o CMakeFiles/marlin.dir/src/profiler.cc.s

# Object files for target marlin
marlin_OBJECTS = \
"CMakeFiles/marlin.dir/src/configuration.cc.o" \
"CMakeFiles/marlin.dir/src/dictionary.cc.o" \
"CMakeFiles/marlin.dir/src/entropyCoder.cc.o" \
"CMakeFiles/marlin.dir/src/entropyDecoder.cc.o" \
"CMakeFiles/marlin.dir/src/marlin.cc.o" \
"CMakeFiles/marlin.dir/src/prebuilt.cc.o" \
"CMakeFiles/marlin.dir/src/profiler.cc.o"

# External object files for target marlin
marlin_EXTERNAL_OBJECTS =

libmarlin.a: CMakeFiles/marlin.dir/src/configuration.cc.o
libmarlin.a: CMakeFiles/marlin.dir/src/dictionary.cc.o
libmarlin.a: CMakeFiles/marlin.dir/src/entropyCoder.cc.o
libmarlin.a: CMakeFiles/marlin.dir/src/entropyDecoder.cc.o
libmarlin.a: CMakeFiles/marlin.dir/src/marlin.cc.o
libmarlin.a: CMakeFiles/marlin.dir/src/prebuilt.cc.o
libmarlin.a: CMakeFiles/marlin.dir/src/profiler.cc.o
libmarlin.a: CMakeFiles/marlin.dir/build.make
libmarlin.a: CMakeFiles/marlin.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Linking CXX static library libmarlin.a"
	$(CMAKE_COMMAND) -P CMakeFiles/marlin.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/marlin.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/marlin.dir/build: libmarlin.a

.PHONY : CMakeFiles/marlin.dir/build

CMakeFiles/marlin.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/marlin.dir/cmake_clean.cmake
.PHONY : CMakeFiles/marlin.dir/clean

CMakeFiles/marlin.dir/depend:
	cd /home/miguelinux/Desktop/marlin/marlin/Release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/miguelinux/Desktop/marlin/marlin /home/miguelinux/Desktop/marlin/marlin /home/miguelinux/Desktop/marlin/marlin/Release /home/miguelinux/Desktop/marlin/marlin/Release /home/miguelinux/Desktop/marlin/marlin/Release/CMakeFiles/marlin.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/marlin.dir/depend
