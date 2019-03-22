from fractions import gcd
alphabet1 = "qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM"
alphabet2 = "abcdefghijklmnopqrstuvwxyz "
#m = len(alphabet)
#print(m)
def inverseMod(a, m):
    for i in range(1,m):
        if ( m*i + 1) % a == 0:
            return ( m*i + 1) // a
    return None

def converttonums(statement,alphabet_reference):
    nums = []
    for i in range(0,len(statement)):
        nums.append(alphabet_reference.index(statement[i]))
    return nums
#numbertest = converttonums(alphabet,alphabet)
#print(numbertest)

def converttostring(number_array,alphabet_reference):
    string = []
    for i in range(0,len(number_array)):
        string.append(alphabet_reference[number_array[i]])
    return string

def encodesimpleaffine(uncoded_statement,alphabet_reference,a,b):
    m = len(alphabet_reference)
    if (gcd(a,m)!=1):
        return "a and modulus are not coprime!"
    uncoded_numbers = converttonums(uncoded_statement,alphabet_reference)
    coded_numbers = []
    for i in range (0,len(uncoded_numbers)):
        coded_numbers.append((a*uncoded_numbers[i]+b)%m)
    return ''.join(converttostring(coded_numbers,alphabet_reference))

def decodesimpleaffine(coded_string,alphabet_reference,a,b):
    m = len(alphabet_reference)
    ainv = inverseMod(a,m)
    return encodesimpleaffine(coded_string,alphabet_reference,ainv,(-ainv*b)%m)

##test_encode = encodesimpleaffine("Five Whoopee Cushions one llama Strongin tonight at six",alphabet1,4,7)
##print(test_encode)
##
##print(decodesimpleaffine(test_encode,alphabet1,4,7))
document_test = decodesimpleaffine("oOHhyfgDDJhhyFTNgODBNyDBhy  XwXyqbzDBaOBybDBOagbyXbyNOI",alphabet1,4,7)
print(document_test)