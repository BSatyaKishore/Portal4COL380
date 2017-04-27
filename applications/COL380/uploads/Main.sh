cd $1/

echo "#!/bin/bash -i" >> compile2.sh
echo "module load compiler/cuda/8.0/compilervars" >> compile2.sh
echo "module load compiler/gcc/5.1.0/compilervars" >> compile2.sh
echo "module load mpi/mpich/3.1.4/gcc/mpivars" >> compile2.sh
cat compile2.sh compile.sh > temp && mv temp compile.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run1.sh
echo "(time bash run.sh /home/cse/dual/cs5120284/input_1024.txt output1.txt)  > 1.o 2> 1.e" >> run1.sh
# echo "python sendStatus.py 1" >> run1.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run2.sh
echo "(time bash run.sh /home/cse/dual/cs5120284/input_10000.txt output2.txt) > 2.o 2> 2.e" >> run2.sh
# echo "python sendStatus.py 2" >> run2.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run3.sh
echo "(time bash run.sh /home/cse/dual/cs5120284/input_20000.txt output3.txt) > 3.o 2> 3.e" >> run3.sh
# echo "python sendStatus.py 3" >> run3.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run4.sh
echo "(time bash run.sh /home/cse/dual/cs5120284/input_30000.txt output4.txt) > 4.o 2> 4.e" >> run4.sh
# echo "python sendStatus.py 4" >> run4.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run5.sh
echo "(time bash run.sh /home/cse/dual/cs5120284/input_40000.txt output5.txt) > 5.o 2> 5.e" >> run5.sh
# echo "python sendStatus.py 5" >> run5.sh

echo "cd /home/cse/dual/cs5120284/$1/" > SendStatus.sh
echo "python sendStatus.py $2" >> SendStatus.sh

cp ../run.py .
cp ../SendStatus.py ./sendStatus.py
# cp ../SendStatus.sh ./

# cp input1.txt $1/
