cd $1/
echo "cd /home/cse/dual/cs5120284/$1/" > run1.sh
echo "bash run.sh input1.txt output1.txt" >> run1.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run2.sh
echo "bash run.sh input2.txt output2.txt" >> run2.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run3.sh
echo "bash run.sh input3.txt output3.txt" >> run3.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run4.sh
echo "bash run.sh input4.txt output4.txt" >> run4.sh

echo "cd /home/cse/dual/cs5120284/$1/" > run5.sh
echo "bash run.sh input5.txt output5.txt" >> run5.sh

cp ../run.py .

# cp input1.txt $1/
