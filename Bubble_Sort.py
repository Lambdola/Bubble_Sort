def bubble(seq, n = 1):
    """
    Sort a list of numbers in ascending order, by default
    """
    
    if n == 1:
        i = 0
        flag = 0     
        for x in range(0,len(seq)-1):
            if  seq[i] > seq[(i + 1)]:
                seq[i], seq[(i + 1)] = seq[(i + 1)], seq[i]
                i += 1
                continue
            else:
                i += 1
                flag += 1
                if flag == len(seq) - 1:
                    return seq
                continue
        
        return bubble(seq,n)
        
    elif n == -1:
        i = 0
        flag = 0
        for x in range(0,len(seq)-1):
            if  seq[i] < seq[(i + 1)]:
                seq[i], seq[(i + 1)] = seq[(i + 1)], seq[i]
                i += 1
                continue
            else:
                i += 1
                flag += 1
                if flag == len(seq) - 1:
                    return seq
                continue
        
        return bubble(seq,n)



#Set n = 1 to sort list in ascending order or n = -1 to sort list in descending order
n = 1
#list of numbers to sort
unsorted_lst = [20,56,70,85,96]



if n == 1:
    x = "ascending"
elif n == -1:
    x = "descending"
print(f"Sorted list in {x} order = ", bubble(unsorted_lst, n)) 




       
