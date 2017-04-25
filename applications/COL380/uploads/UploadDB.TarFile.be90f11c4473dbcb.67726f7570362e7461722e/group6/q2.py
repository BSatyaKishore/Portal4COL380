import sys;
from random import randint;

# total size is 100MB
TotalSize = 1048576;
UsedSize = 0;

disks={};
Duplicate = {}
DuplicateMap = {}
counter = 0
faultset = []


str1="Disk does not have enough size. The disk has only ",(TotalSize-UsedSize), " blocks"
str2="Disk ID already exists."
str3="Disk ID is not available."

def CheckInfoSize( str ):
    if(sys.getsizeof(str) > 100):
        str = str[0:63];
    return str;

def CreateD(ID, NumberOfBlocks):
    global UsedSize; 
    if(UsedSize + NumberOfBlocks + len(faultset) > TotalSize):
        raise Exception(str1) ;
    elif(disks.has_key(ID)):
        raise Exception(str2) ;
    else:
        disks[ID]=({},NumberOfBlocks);
        UsedSize = UsedSize + NumberOfBlocks;
    return;

def DeleteD(ID):
    global UsedSize; 
    global disks; 
    if(not disks.has_key(ID)):
        raise Exception(str3);
    UsedSize = UsedSize - disks[ID][1];
    del disks[ID];
    


def ReadD(ID, index ):
    global Duplicate,counter,DuplicateMap,UsedSize
    if(not disks.has_key(ID)):
        raise Exception(str3);

    NumBlocksOfDisk = disks[ID][1];
    if index < 0 or index > (NumBlocksOfDisk-1) :
        raise IndexError("index out of range");
    elif (not disks[ID][0].has_key(index)):
        return "";
    else:
        randomNum = randint(1,100);
        print "Random Number generated is ",randomNum;
        key = (ID,index);
        if(randomNum < 10):
            print "faultset...error occured";
            if(key in faultset):
                DuplicateMap[key][0] = DuplicateMap[key][1];
                DuplicateMap[key][1] = counter;
            else:
                faultset.append(key);
                DuplicateMap[key].append(counter);

            Duplicate[counter] = Duplicate[DuplicateMap[key][0]];
            counter=counter+1;
            UsedSize=UsedSize+1;
            return Duplicate[DuplicateMap[key][0]];
        else:
            if(key in faultset):
                return Duplicate[DuplicateMap[key][0]];
            else:
                return disks[ID][0][index];


def WriteD(ID, index, info ):
    global counter,UsedSize
    if(not disks.has_key(ID)):
        raise Exception(str3) ;

    NumBlocksOfDisk = disks[ID][1];
    if index < 0 or index > (NumBlocksOfDisk-1) :
        raise IndexError("index out of range");
    else:
        if ((ID,index) in faultset):
            Duplicate[DuplicateMap[(ID,index)][0]]=CheckInfoSize(info)
            Duplicate[DuplicateMap[(ID,index)][1]]=CheckInfoSize(info)
        else:
            disks[ID][0][index] = CheckInfoSize(info);
            if((ID,index) in DuplicateMap):
                mapindex=DuplicateMap[(ID,index)][0]
                Duplicate[mapindex]=CheckInfoSize(info)
            else:
                Duplicate[counter]=CheckInfoSize(info)
                counter=counter+1
                DuplicateMap[(ID,index)]=[counter-1]
        UsedSize=UsedSize+1


print "Creating  Disk 1";
CreateD(1, 5000);
print "Creating Disk 2";
CreateD(2,5000);
print "Writing at 1,216 -0 hello how are you"
WriteD(1,216, "hello how are you");

for tum in range(1,100):
    print "\nReading 216 from Disk 1";
    ReadD(1, 216);

print "Fault Set     :",faultset;
print "DuplicateMapping :", DuplicateMap;
print "\nDelete Disk 1";
DeleteD(1);