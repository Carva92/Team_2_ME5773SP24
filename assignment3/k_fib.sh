#!/bin/bash
#
# ==========================================================================
# The objective of this file is to compute the K-fibonacci series
#
# Inputs:
# - N {the number of outputs of the K-fibonacci series}
# - K {The type of fibonacci series}
#
# Output:
# - Output will be an array, the size of the array is given by input <N>
#
# Callout: [login001; abc123] k_fib.sh N K
# - where K and N are integer numbers 
#
#
#
N=$1
K=$2

# If statement to verify that the input <N> is a real integer
if ! [[ "$N" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid integer number for N."
    exit 1
fi

# If statement to verify that the input <K> is a real integer
if ! [[ "$K" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid integer number for K."
    exit 1
fi

# Initialize the series with empty array
series=()


for ((i=0; i<K; i++)); do
    series[$i]=1
done

# Compute the rest of the K-Fibonacci series up to N elements
for ((i=K; i<N; i++)); do
    sum=0
    # Sum the last K elements
    for ((j=i-K; j<i; j++)); do
        sum=$((sum + series[j]))
    done
    series[$i]=$sum
done

echo "The K-Fibonacci series up to element $N is: ${series[@]}"



