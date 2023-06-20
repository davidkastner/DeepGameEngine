#! /bin/bash
#$ -N MC6-1
#$ -cwd
#$ -l h_rt=300:00:00
#$ -l h_rss=8G
#$ -q small
#$ -l gpus=1
#$ -pe smp 1
# -fin ./*
# -fout ./*

module load cuda/11.0
export OMP_NUM_THREADS=1

source ~/.bashrc
conda activate dge

python --version

python train.py