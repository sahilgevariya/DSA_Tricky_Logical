import math 

one = [ "", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", 
        "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "];
		
ten = [ "", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "];

# 1/2 digit n
def numToWords2(n, s):
	res = "";
	if not n:
	    return res
	
	tenth = n // 10
	if tenth:   res += ten[tenth]
	    
	n %= 10
	res += one[n];

	res += s;
	return res
	
# 1/2/3 digit n
def numToWords3(n, s):
	res = "";
	if not n:
	    return res
	
	hundreds = n // 100;
	if hundreds:    res += one[hundreds] + "Hundred "
	
	n %= 100
	
	tenth = n // 10
	if tenth:   res += ten[tenth]
	    
	n %= 10
    res += one[n]
    res += s
	return res
	
def convertToWordsEnglish(n):
	out = "";
	floatN = int((n - math.floor(n)) * 100)
	n = int(math.floor(n))
	
	out += numToWords3( (n // 1000000000000), "Tillion, ");
	out += numToWords3(((n // 1000000000) % 1000), "Billion, ");
	out += numToWords3(((n // 1000000) % 1000) , "Million, ");
	out += numToWords3(((n // 1000) % 1000), "Thousand, ");
	out += numToWords3( (n  % 1000), "");
	
	if floatN:
	    out += numToWords3(floatN, ", Cents")

	return out
	
def convertToWordsIndian(n):

	out = "";
	floatN = int((n - math.floor(n)) * 100)
	n = int(math.floor(n))
	
	out += numToWords2( (n // 10000000000000), "Nil, ");
	out += numToWords2(((n // 100000000000) % 100), "Kharba, ");
	out += numToWords2(((n // 1000000000) % 100), "Arab, ");
	out += numToWords2(((n // 10000000) % 100), "Crore, ");
	out += numToWords2(((n // 100000) % 100),"Lakh, ");
	out += numToWords2(((n // 1000) % 100), "Thousand, ");
	out += numToWords2(((n // 100) % 10), "Hundred, ");
	out += numToWords2( (n  % 100), "");
	
	
	if floatN:
	    out += numToWords2(floatN, ", Paisa")

	return out
	
n = 494324345676.23
print(convertToWordsEnglish(n))
print(convertToWordsIndian(n))

''' 
   Output:

      Four Hundred Ninety Four Billion, Three Hundred Twenty Four Million, Three Hundred Forty Five Thousand, Six Hundred Seventy Six , Twenty Two Cents
      Four Kharba, Ninety Four Arab, Thirty Two Crore, Forty Three Lakh, Forty Five Thousand, Six Hundred, Seventy Six , Twenty Two Paisa
'''
