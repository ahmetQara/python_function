def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 400 != 0 and year % 100 != 0:
        leap = True
        
    if year % 400 == 0 and year % 100 == 0:
        leap = True
    # Write your logic here
    
    return leap

year = int(input())