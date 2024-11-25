def check_even_list(num_list):
    even_numbers = []
    odd_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return(odd_numbers,even_numbers)
a,b = check_even_list([1,2,3,4])
print("even number: ",b)
print("odd number: ",a)
