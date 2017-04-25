import sys;

A = [""] * 200;

B = [""] * 300;


def CheckInfoSize( str ):
    if(sys.getsizeof(str) > 100):
        str = str[0:63];
    return str;

def ReadD( index ):
    if index < 0 or index > 499 :
        print "index out of range";
    elif index < len(A):
        return A[index];
    else:
        return B[index-len(A)]; 

def WriteD( index, info ):
    if index < 0 or index > 499 :
        print "index out of range";
    elif index < len(A):
        A[index] = CheckInfoSize(info);
    else:
        B[index-len(A)] = CheckInfoSize(info);

print "Writing at 216 -0 hello how are you"
WriteD(216, "hello how are you");

print "Writing at 113 - baranababarava masajasatataga"
WriteD(113, "baranababarava masajasatataga");

print "Writing at 476 - beta tumse na hopayega"
WriteD(476, "beta tumse na hopayega");

print "Readint at  600 :",ReadD(600);
print "Reading at  216 :",ReadD(216);
print "Readint at  113 :",ReadD(113);

