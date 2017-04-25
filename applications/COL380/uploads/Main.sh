cd $1/
echo "cd /home/cse/dual/cs5120284/$1/" > run1.sh
echo "time bash run.sh input1.txt output1.txt > 1.o 2> 1.e" >> run1.sh
# echo "python sendStatus.py 1" >> run1.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run2.sh
echo "time bash run.sh input2.txt output2.txt > 2.o 2> 2.e" >> run2.sh
# echo "python sendStatus.py 2" >> run2.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run3.sh
echo "time bash run.sh input3.txt output3.txt > 3.o 2> 3.e" >> run3.sh
# echo "python sendStatus.py 3" >> run3.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run4.sh
echo "time bash run.sh input4.txt output4.txt > 4.o 2> 4.e" >> run4.sh
# echo "python sendStatus.py 4" >> run4.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run5.sh
echo "time bash run.sh input5.txt output5.txt > 5.o 2> 5.e" >> run5.sh
# echo "python sendStatus.py 5" >> run5.sh

echo "cd /home/cse/dual/cs5120284/$1/" > SendStatus.sh
echo "sleep 5 ">> SendStatus.sh
echo "python sendStatus.py 1 $2" >> SendStatus.sh
echo "python sendStatus.py 2 $2" >> SendStatus.sh
echo "python sendStatus.py 3 $2" >> SendStatus.sh
echo "python sendStatus.py 4 $2" >> SendStatus.sh
echo "python sendStatus.py 5 $2" >> SendStatus.sh

cp ../run.py .
cp ../SendStatus.py ./sendStatus.py
# cp ../SendStatus.sh ./

# cp input1.txt $1/
