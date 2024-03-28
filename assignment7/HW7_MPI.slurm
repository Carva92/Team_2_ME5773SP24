#!/bin/bash
#
# Authors: Julian Carvajal Rico
#          James Platt Standard
#          Roberto Enriquez Vargas
#
# ======================================================================
#SBATCH -J HW7_mpi                 # Job name
#SBATCH -o out_HW7.%j.txt          # Name of 'stdout' output file (%j expands to jobId)
#SBATCH -e err_HW7.%j.txt          # Name of 'stderr' error file (%j expands to jobId)
#SBATCH -p compute1                # Partition
#SBATCH -N 2                       # Total number of nodes to be requested
#SBATCH -n 21                      # Total number of mpi tasks to be requested
#SBATCH -t 00:10:00                # Maximum run time (hh:mm:ss)
#SBATCH --mail-type=ALL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=your_email@edu # Your email for notifications
     

echo "Starting HW7_MPI.slurm"

# Load one of these
module load anaconda3
source activate hpc


mpirun -n $SLURM_NTASKS python3 HW7_MPI.py
