#!/bin/bash
#
# ==========================================================================
# The objective of this file is to compute the K-fibonacci series
#
# Inputes:
# - K {The type of fibonacci series}
# - N {the number of outputs of the K-fibonacci series}
#
# Output:
# - Output will be an array, the size of the array is given by input <N>
#
# Callout: [login001; abc123] k_fib.sh K N
# - where K and N are integer numbers 
#
K=$1
N=$2

# If statement to verify that the input <N> is a real integer
#if [[ "$N" =~ ^[0-9]+$ ]]; then
#	echo "Error: Please enter a valid integer number for N."
#	exit 1
#fi

# If statement to verify that the input <K> is a real integer
#if [[ "$K" =~ ^[0-9]+$ ]]; then
#	echo "Error: Please enter a valid integer number for K."
#	exit 1
#fi

# If statement to verify that N is greater than K
#if [[ $K -gt $N]]; then
#	echo "Error: N should be greater than K"
#	exit 1
#fi


# First create the array of 1s for the fibinocci series
# There are K number of 1s that begin the series
for ((i=0; i<=$(($K-1)); i++));do
	series[$i]=1
done

echo "The first $K K number of elements are 1s in the K-fibonacci series as shown here: ${series[@]}"


