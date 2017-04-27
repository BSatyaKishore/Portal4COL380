#include <iostream>
#include <mpi.h>
#include <omp.h>
#include <cuda.h>
#include <stdio.h>

const int N = 7;
const int blocksize = 7;

__global__
void hello(char *a, int *b)
{
 a[threadIdx.x] += b[threadIdx.x];
}

int main(int argc, char* argv[])
{
 int myrank;
 MPI_Init(&argc,&argv);
 MPI_Comm_rank(MPI_COMM_WORLD,&myrank);

 #pragma omp parallel num_threads(2)
 {
   std::cout<<myrank;
 }
 std::cout << ":Hello, world!\n";
    
 char a[N] = "Hello ";
 int b[N] = {15, 10, 6, 0, -11, 1, 0};

 char *ad;
 int *bd;
 const int csize = N*sizeof(char);
 const int isize = N*sizeof(int);

 printf("%s", a);

 cudaMalloc( (void**)&ad, csize );
 cudaMalloc( (void**)&bd, isize );
 cudaMemcpy( ad, a, csize, cudaMemcpyHostToDevice );
 cudaMemcpy( bd, b, isize, cudaMemcpyHostToDevice );

 dim3 dimBlock( blocksize, 1 );
 dim3 dimGrid( 1, 1 );
 hello<<<dimGrid, dimBlock>>>(ad, bd);
 cudaMemcpy( a, ad, csize, cudaMemcpyDeviceToHost );
 cudaFree( ad );

 printf("%s\n", a);
 MPI_Finalize();
 return 0;
}

