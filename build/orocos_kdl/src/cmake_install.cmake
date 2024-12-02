# Install script for directory: /workspace/src/orocos_kinematics_dynamics/orocos_kdl/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/workspace/devel")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so.1.4.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so.1.4"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "$ORIGIN/../lib")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/workspace/build/orocos_kdl/src/liborocos-kdl.so.1.4.0"
    "/workspace/build/orocos_kdl/src/liborocos-kdl.so.1.4"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so.1.4.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so.1.4"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "::::::::::::::"
           NEW_RPATH "$ORIGIN/../lib")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so"
         RPATH "$ORIGIN/../lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/workspace/build/orocos_kdl/src/liborocos-kdl.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so"
         OLD_RPATH "::::::::::::::"
         NEW_RPATH "$ORIGIN/../lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/liborocos-kdl.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kdl" TYPE FILE FILES
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/articulatedbodyinertia.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chain.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chaindynparam.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainfdsolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainfdsolver_recursive_newton_euler.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainfksolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainfksolverpos_recursive.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainfksolvervel_recursive.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainidsolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainidsolver_recursive_newton_euler.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainidsolver_vereshchagin.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainiksolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainiksolverpos_lma.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainiksolverpos_nr.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainiksolverpos_nr_jl.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainiksolvervel_pinv.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainiksolvervel_pinv_givens.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainiksolvervel_pinv_nso.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainiksolvervel_wdls.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainjnttojacdotsolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/chainjnttojacsolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/frameacc.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/frameacc.inl"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/frameacc_io.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/frames.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/frames.inl"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/frames_io.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/framevel.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/framevel.inl"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/framevel_io.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/jacobian.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/jntarray.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/jntarrayacc.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/jntarrayvel.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/jntspaceinertiamatrix.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/joint.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/kdl.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/kinfam.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/kinfam_io.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/motion.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/path.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/path_circle.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/path_composite.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/path_cyclic_closed.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/path_line.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/path_point.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/path_roundedcomposite.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/rigidbodyinertia.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/rotational_interpolation.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/rotational_interpolation_sa.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/rotationalinertia.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/segment.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/solveri.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/stiffness.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/trajectory.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/trajectory_composite.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/trajectory_segment.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/trajectory_stationary.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/tree.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treefksolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treefksolverpos_recursive.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treeidsolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treeidsolver_recursive_newton_euler.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treeiksolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treeiksolverpos_nr_jl.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treeiksolverpos_online.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treeiksolvervel_wdls.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/treejnttojacsolver.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/velocityprofile.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/velocityprofile_dirac.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/velocityprofile_rect.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/velocityprofile_spline.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/velocityprofile_trap.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/velocityprofile_traphalf.hpp"
    "/workspace/build/orocos_kdl/src/config.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kdl/utilities" TYPE FILE FILES
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/error.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/error_stack.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/kdl-config.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/ldl_solver_eigen.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/rall1d.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/rall1d_io.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/rall2d.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/rall2d_io.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/rallNd.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/scoped_ptr.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/svd_HH.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/svd_eigen_HH.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/svd_eigen_Macie.hpp"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/traits.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/utility.h"
    "/workspace/src/orocos_kinematics_dynamics/orocos_kdl/src/utilities/utility_io.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/workspace/build/orocos_kdl/src/orocos-kdl.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/workspace/build/orocos_kdl/src/orocos_kdl.pc")
endif()

