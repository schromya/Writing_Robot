execute_process(COMMAND "/workspace/build/panda_sim_custom_action_server/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/workspace/build/panda_sim_custom_action_server/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
