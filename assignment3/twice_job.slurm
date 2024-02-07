#!/bin/bash
#
# ======================================================================
#
# Authors: Julian Carvajal Rico
#          James Platt Standard
#          Roberto Enriquez Vargas
#
# ======================================================================
#
#
#The following commands specify SLURM configuration:
#more information can be found on 
#https://slurm.schedmd.com/sbatch.html
#
#SBATCH -J Twice_Job
#SBATCH -o outFile.%j.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of threads used by each task.
#SBATCH -t 00:10:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user julian.carvajal@my.utsa.edu # Put your utsa-email here.
#

# start time
start_time=$(date +%s)

srun bash twice.sh 5 &
srun bash twice.sh 2 &
srun bash twice.sh 7 &
srun bash twice.sh 6 &
srun bash twice.sh 1 &
srun bash twice.sh 3 &

# Wait for all background jobs to finish
wait

# Calculate and print the execution time
end_time=$(date +%s)
execution_time=$((end_time - start_time))
echo "Execution time: $execution_time seconds"