import sys;

# total size is 100MB
TotalSize = 1048576;
UsedSize = 0;

disks={};

str1="Disk does not have enough size. The disk has only ",(TotalSize-UsedSize), " blocks"
str2="Disk ID already exists."
str3="Disk ID is not available."

def CheckInfoSize( str ):
    if(sys.getsizeof(str) > 100):
        str = str[0:63];
    return str;

def CreateD(ID, NumberOfBlocks):
    global UsedSize; 
    if(UsedSize + NumberOfBlocks > TotalSize):
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
    if(not disks.has_key(ID)):
        raise Exception(str3);

    NumBlocksOfDisk = disks[ID][1];
    if index < 0 or index > (NumBlocksOfDisk-1) :
        raise IndexError("index out of range");
    elif (not disks[ID][0].has_key(index)):
        return "";
    else:
        return disks[ID][0][index]; 


def WriteD(ID, index, info ):
    if(not disks.has_key(ID)):
        raise Exception(str3) ;

    NumBlocksOfDisk = disks[ID][1];
    if index < 0 or index > (NumBlocksOfDisk-1) :
        raise IndexError("index out of range");
    else:
        disks[ID][0][index] = CheckInfoSize(info);


print "Creating  Disk 1";
CreateD(1, 5000);
print "Creating Disk 2";
CreateD(2,5000);


print "Writing at 1,216 -0 hello how are you"
WriteD(1,216, "hello how are you");

print "Writing at 1,113 - baranababarava masajasatataga"
WriteD(1,113, "baranababarava masajasatataga");

print "Writing at 2,476 - beta tumse na hopayega"
WriteD(2,476, "beta tumse na hopayega");

print "Reading at  1,216 :",ReadD(1,216);
print "Readint at  1,113 :",ReadD(1,113);
print "Readint at  2,476 :",ReadD(2,476);

print "Deleting disk 1";
DeleteD(1);
print "Deleting disk 2";
DeleteD(2);
