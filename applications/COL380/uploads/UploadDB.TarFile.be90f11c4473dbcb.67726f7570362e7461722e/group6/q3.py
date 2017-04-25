import sys;

# total size is 100MB
TotalSize = 1048576;
UsedSize = 0;

disks={};
checkpts={};

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


def  CreateCheckpoint(ID,no):
    global disks,checkpts;
    if ID in checkpts:
        if no in checkpts[ID]:
            raise Exception("check point number already exists in DiskID: "+str(ID)) ;
        else:
            checkpts[ID][no]={}
            for index in disks[ID][0]:
                checkpts[ID][no][index]=disks[ID][0][index]

    else:
        checkpts[ID]={}
        checkpts[ID][no]={}
        for index in disks[ID][0]:
            checkpts[ID][no][index]=disks[ID][0][index]

def rollback(ID,no):
    global disks,checkpts;
    if ID in checkpts:
        if no in checkpts[ID]:
            disks[ID][0].clear();
            for index in checkpts[ID][no]:
                disks[ID][0][index]=checkpts[ID][no][index]
        else:
            raise Exception("check point number does not exist in DiskID: "+str(ID)) ;
    else:
        raise Exception("DiskID:"+str(ID)+" does not exists in checkpoints") ;

print "Creating  Disk 1";
CreateD(1, 5000);
print "Creating Disk 2";
CreateD(2,5000);


print "Writing at 1,216 -0 hello how are you"
WriteD(1,216, "hello how are you");

print "Writing at 1,113 - baranababarava masajasatataga"
WriteD(1,113, "baranababarava masajasatataga");

print "Check Point 1 for disk1 : ",disks;
CreateCheckpoint(1, 1);

print "Writing at 2,476 - beta tumse na hopayega"
WriteD(1,476, "beta tumse na hopayega");

print "Writing at 2,466 - hello beta tumse na hopayega"
WriteD(2,466, "hello beta tumse na hopayega");

print "Check Point 2 for disk 2 : ",disks;
CreateCheckpoint(2, 2);
rollback(1, 1);
print "\nRoll Back 1 : ",disks;
rollback(2,2);
print "\nRoll Back 2 : ",disks;
print "\nDelete Disk 1";
DeleteD(1);
print "\nDelete Disk 2";
DeleteD(2);
