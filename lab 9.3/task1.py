#this is function to return sum of even and odd numbers in a list and it takes list of numbers as input
def sum_even_odd(list_num):
    """
    this function is used to return the sum of eevn and odd numbers in a list
    
    args:
        list_num: list of numbers

    Returns:
        sum_even: sum of even numbers
    """
    #initialize sum of even numbers
    sum_even = 0
    
     
    #initialize sum of odd numbers
    sum_odd = 0
    
    #this is the loop to iterate through the list and store sum of even numbers in sum_even and sum of odd numb ers in sum_odd
    for i in list_num:
        if i%2==0:
            sum_even+=i
        else:
            sum_odd+=i
    
    #return the sum of even and odd numbers        
    return sum_even,sum_odd

#list of numbers
list_num =[1,2,3,4,5,6,7,8,9,10]

#call the function and print the sum of even and odd numbers
sum_even,sum_odd=sum_even_odd (list_num)

#print the sum of even and odd numbers
print(f"sum of even number:{sum_even}")
print(f"sum of odd number:{sum_odd}")



