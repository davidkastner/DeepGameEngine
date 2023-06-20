#!/bin/bash
#SBATCH --job-name=mimochrome
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=48

# Set up calculation environment
source ~/.bashrc
source activate dge

python --version
python train.py