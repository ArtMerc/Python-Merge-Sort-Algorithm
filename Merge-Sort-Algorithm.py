# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:47:24 2021

@author: artem
"""

def merge_sort(arr):
    #this function will only do something if the length of the array is > 1
    if len(arr) > 1:
        #we need to create to arrays one that goes to the left and one that takes everything from the middle and goes to the right
        first_array = arr[0:len(arr)//2]   #<-------- returns the slice of original array starting at index 0 ending at len of array dividing by 2
        second_array = arr[len(arr)//2:len(arr)] #<---- starts at the len of array (the middle) integer division by 2 and goes till the end

    #I want to perform whole merge_sort algorithm to my first(left) array and my second(right) array
    #After these two lines the first_array(left array) and second_array(right array) are in sorted order
        merge_sort(first_array)
        merge_sort(second_array)
    
    #Merge them - since now my first_array and second_array are in sorted order I want to merge them to make a bigger array that is sorted
    # I want to compare left most of first array to left most of second array so lets do i for left j for right
    
        i = 0
        j = 0
        #I also need one for my merged index array so lets just use x
        x = 0
        
        #use a while loop to do my comparison
        while i < len(first_array) and j < len(second_array):
            if first_array[i] < second_array[j]:
                #No we can save the value of my left array inside x which is my merged array
                arr[x] = first_array[i]
                #now just increase i and increase x  
                i += 1
                x += 1
                #in the other case the right array is smaller or equal to my left(second) array so we do the same thing but save the right array into x 
                #which is my merge array
            else:
                arr[x] = second_array[j]
                #same thing here increase j and x 
                j += 1
                x += 1
        
        
       #Now consider I have to transfer every element in my  first_array (left array) into my merge array (x) without considering second_array (right array)
       #in this case i < then the len of my first_array(left array)
        while i < len(first_array):
            #transfer by assigining my first_array of index i to the merged array of index x
            arr[x] = first_array[i]
            #increase both index's
            i += 1
            x += 1
           
        #Need to implement the same thing  where every element in my first_array(left array) has already been sorted but there are still missing elements
        #in my second_array(right array)
        
        #I am doing the same thing as before but this time for my second_array basically below:
        while j < len(second_array):
            arr[x] = second_array[j]
            j += 1
            x += 1
     
    return arr

print("============= ### START OF MY PROGRAM ### =============")     
print()

my_list = [98,23,45,14,6,67,33,42]
print("My current list is: ", my_list)
print()

#call for my function merge_sort below
merge_sort(my_list)
print("After merge_sort function my list is: ")
print(my_list)      
        
print()
print("============= ### END OF MY PROGRAM ### =============")          
           