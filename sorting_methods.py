l = [54,26,93,17,77,31,44,55,20]

# Bubble sort #######################################

# bringing the largest to the top then exclude the top spot for next serach
def bubble_sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l
# print bubble_sort(l)

# bringing smaller items towards bottom, longer runtime than previous
def bubble_sort2(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l
# print bubble_sort2(l)

# Short bubble, stops when recognize the list is sorted.
def bubble_sort3(l):
    changed = True
    while changed:
        changed = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                changed = True
    return l
# print bubble_sort3(l)




# Merge sort #######################################

# 2 parts, split until down to 1 item and merge

def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)
    return l

print mergeSort(l)
# print l



























