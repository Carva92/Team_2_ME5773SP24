#!/bin/bash

Var1=NameReceived_$1.txt
N=$1


# Function to calculate factorial
factorial() {
    if [ $1 -eq 0 ] || [ $1 -eq 1 ]; then
        echo 1
    else
        echo $(( $1 * $(factorial $(( $1 - 1 ))) ))
    fi
}

# Main script

if ! [[ "$N" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid number."
    exit 1
fi

echo "Factorials from 1 to $N:"
for ((i=1; i<=N; i++)); do
    echo "$i! = $(factorial $i)"
done

