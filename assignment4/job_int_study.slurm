#!/bin/bash
# 
#
# Authors: Julian Carvajal Rico
#          James Platt Standard
#          Roberto Enriquez Vargas
#
# ======================================================================
#SBATCH -J int_study
#SBATCH -o out_int.%j.txt    # Name of 'stdout' output file.
#SBATCH -e err_int.%j.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of threads used by each task.
#SBATCH -t 00:30:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user your_@email.edu # Put your utsa-email here.
#
# 
# # Environment variable setup: You may want to use $SLURM_CPUS_PER_TASK
# # This will be distributed onto each 
# # Restrain the total number of threads given to 
# # OpenMP-parallelized code.
# export OMP_NUM_THREADS=1
# 
# # These control the use of numexpr library.
# export NUMEXPR_NUM_THREADS=1


echo "Starting job_int_study.slurm"


# Load Anaconda3
module load anaconda3

# Acivate the environment
conda activate envTeam2


THREAD_VALUES=(1 2 4 8)

# Loop to go over all MKL_VALUES
for THREADS  in "${THREAD_VALUES[@]}"
do
    echo "Running with OMP_NUM_THREADS=$THREADS and NUMEXPR_NUM_THREADS=$THREADS"
    # Set the OMP_NUM_THREADS and NUMEXPR_NUM_THREADS
    export OMP_NUM_THREADS=$THREADS
    export NUMEXPR_NUM_THREADS=$THREADS
    
    # Run the linalg.py script
    srun --exclusive -N1 -n1 -c $SLURM_CPUS_PER_TASK python3 integral.py &
    
    wait
done