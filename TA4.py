import copy as c

def main():
    file = open("MyInput.txt")
    n = int(file.readline())
    array = []
    with file as f:
        for line in file:
            array.append([int(x) for x in line.split()])
    
    partition = [Partition, MedianaPartition, Pivot3Partition]
    
    file_res = open('MyOutput.txt', 'w')
    for n in partition:
        count = quick_sort(c.deepcopy(array), 0, len(array)-1, n)
        print(count)
        file_res.write(str(count) + " ")
    file_res.close()


def quick_sort(A, p, r, n):
    count = 0
    if p<r:
        pi, c_temp = n(A, p, r)
        count += c_temp
        count += quick_sort(A, p, pi-1, n)
        count += quick_sort(A, pi + 1, r, n)
    #print arr
    return count



def Partition(A, p, r):
    count = 0
    i = p - 1
    x = A[r]
    for j in range(p, r):
        count += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1, count

def MedianaPartition(A, p, r):
    count = 0
    if len(A)>3:
        x0 = [A[p], A[r], A[int((p+r)/2)]]   
        if (x0[0] > x0[1] and x0[2] > x0[0]) or (x0[0] < x0[1] and x0[2] < x0[0]) :
            median = x0[0]
        elif (x0[0] > x0[1] and x0[1] > x0[2]) or (x0[0] < x0[1] and x0[1] < x0[2]) :
            median = x0[1] 
        else: median = x0[2]
        index = A.index(median)
        A[r], A[index] = A[index], A[r]
    i = p - 1
    x = A[r]
    for j in range(p, r):
        count += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1, count



def Pivot3Partition(A, left, right): 
    counter = 0 
    a = left+2 
    b = left+2 
    c = right -1 
    d = right -1 
    p = A[left] 
    q = A[left+1] 
    r = A[right] 
    while b <= c: 
        while A[b] < q and b <= c: 
            counter+=1 
            if A[b] < p: 
                A[a], A[b] = A[b], A[a] 
                a+=1 
            b+=1 
            counter+=1 
        counter+=1 
        while A[c] > q and b <= c: 
            counter+=1 
            if A[c] > r: 
                A[c], A[d] = A[d], A[c] 
                d-=1 
            c-=1 
            counter+=1 
        counter+=1 
        if b<=c: 
            counter+=1 
            if A[b]>r: 
                counter+=1 
                if A[c] < p: 
                    A[b], A[a] = A[a], A[b] 
                    A[a], A[c] = A[c], A[a] 
                else: 
                    A[b], A[c]= A[c], A[b] 
                A[c], A[d] = A[d], A[c] 
                b+=1 
                c-=1 
                d-=1 
            else: 
                counter+=1 
                if A[c]<p: 
                    A[b], A[a]= A[a], A[b] 
                    A[a], A[c]= A[c], A[a] 
                    a+=1 
                else: 
                    A[b], A[c]= A[c], A[b] 
    a-=1 
    b-=1 
    c+=1 
    d+=1 
    A[left+1], A[a]= A[a], A[left+1] 
    A[a], A[b]= A[b], A[a] 
    a-=1 
    A[left], A[a]= A[a], A[left] 
    A[right], A[d]= A[d], A[right] 
    return c, counter 

if __name__ =="__main__":
    main()