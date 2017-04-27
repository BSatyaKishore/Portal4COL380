#!/bin/bash -i
module load compiler/cuda/8.0/compilervars
module load compiler/gcc/5.1.0/compilervars
module load mpi/mpich/3.1.4/gcc/mpivars

nvcc -I/home/soft/mpich-3.1.4/include/ -L/home/soft/mpich-3.1.4/lib/ -lmpi main.cu -o main