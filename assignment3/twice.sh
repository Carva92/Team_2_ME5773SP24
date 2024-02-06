#!/bin/bash
#
#
# ===========================================================================================
# This file provides the code to complete problem 4, on assignment 3, for the ME 5773 Course
# This bash script executes the following:
#   - Script is given an integer input <N>
#   - Sleeps for <2N> seconds
#   - outputs the following string: "Terminated a task that takes <2N> seconds"
#
#
# Example of the intended execution are as follows:
#  [c001: abc123]$ bash twice.sh 3
#  Terminated a task that takes 6 seconds
#
# ============================================================================================
#
# Inputs are can be called by $ followed by their respective indexing (starting at 1)
Input=$1

# In order to conduct numerical operations, the $ followed by double parenthases are required
Time=$(($Input*2))

sleep $Time

echo "Terminated a task that takes $Time seconds"

