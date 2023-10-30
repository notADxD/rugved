#1

def triple_and(a, b, c):
    result = a and b and c
    return result

#2

string = input ("Enter String: -") 
string = sorted(list(string)) 
stri="" 
for i in range(len(string)): 
    stri += string[i] 
print(stri) 
a = set(string) 
for elem in a: 
    print (elem +" - " + str(string.count(elem))) 


#3

Number = input ("Enter Number: -") 
Change =0 
Ascend = True 
Hill = True 
Number = list(Number) 

for i in range (1, len(Number)): 
    if(Number[i]<Number[i-1] and Change ==0): 
        Ascend = False 
        Change =1 
    elif(Number[i]<Number[i-1] and Ascend  and Change ==1):
        Hill = False 
        print ("Not an Hill Number") 
    elif(Number[i]>Number[i-1] and not(Ascend) and Change ==1): 
        Hill = False 
        print ("Not a Hill Number") 
    elif(Number[i]==Number[i-1]): 
        Hill = False 
        print ("Not a Hill Number") 

if(Change==0): 
    print ("Not a Hill Number") 
elif(Hill==True): 
    print ("It’s a Hill Number") 


#4 took help from chatgpt and understand how it works

def selection_sort(input_string):
    
    charac_list = list(input_string)

    for i in range(len(charac_list)):
        min_index = i

       
        for j in range(i + 1, len(charac_list)):
            if charac_list[j] < charac_list[min_index]:
                min_index = j

        
        if i != min_index:
            charac_list[i], charac_list[min_index] = charac_list[min_index], charac_list[i]

  
    sorted_string = ''.join(charac_list)
    return sorted_string

input_string = input("Enter a string to be sorted: ")
sorted_result = selection_sort(input_string)
print(f"Sorted string: {sorted_result}")


#5

def factor(num):
    if(num==0):
        return 1
    else:
        return num*factor(num-1)
    
num = int(input("Enter Number : "))
print("Factorial of "+ str(num) + " is "+ str(factor(num)))


#6

word = sorted(list(input("Enter the original word :").upper()))
anagram = sorted(list(input("Enter the anagram :").upper()))

if(word == anagram):
    print("It's an Anagram")
else :
    print("Not an Anagram")


#7

def fibon(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    elif(num==2):
        return 1
    else:
        return fibon(num-1) + fibon(num-2)

n = int(input("Enter a number 'n' : "))
for i in range(n):
    print(str(fibon(i)),end=',')



#10 took some help from chatgpt

def is_valid_credit_card(card_number):
    
    digits = [int(digit) for digit in str(card_number)][::-1]

 
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)
    return total % 10 == 0

credit_card_number = input("Enter the credit card number: ")
if is_valid_credit_card(credit_card_number):
    print("Valid credit card number.")
else:
    print("Invalid credit card number.")


#11 taken from someone but don't understand code but understand logic

text = input("Enter a piece of text : ")
letters =0;
for char in text:
    letters = letters+1 if char.isalpha() else letters
sentences = text.count('.') + text.count('!') + text.count('?')
words = len(text.split())
L = (letters / words) * 100
S = (sentences / words) * 100
CLI = 0.0588 * L - 0.296 * S - 15.8
print(CLI)

