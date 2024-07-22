from numpy import *

def print_sudoko(arr):
    for i in range(0, 9):
        for j in range(0, 9):
            print(arr[i][j], end=" ")
        print("")

def check_rows(arr):
    end=0
    for i in range(0, 9):
        zero = 0
        sum = 0
        k=0
        for j in range(0, 9):
            sum=sum+arr[i][j]
            if (arr[i][j]==0):
                zero=zero+1
                k=j
        if (zero==1):
            arr[i][k]=45-sum
            end=1
    return end


def check_column(arr):
    end=0
    for j in range(0, 9):
        zero = 0
        sum = 0
        k = 0
        for i in range(0, 9):
            sum = sum + arr[i][j]
            if (arr[i][j] == 0):
                zero = zero + 1
                k = i
        if (zero == 1):
            arr[k][j] = 45 - sum
            end=1
    return end

def check_block(arr):
    end=0
    for i in range(0,9,3):
        for j in range(0,9,3):
            ro = 0
            co = 0
            zero = 0
            sum = 0
            for a in range(i,i+3):
                for b in range(j,j+3):
                    sum = sum + arr[a][b]
                    if (arr[a][b] == 0):
                        zero = zero + 1
                        ro=a
                        co=b
            if (zero == 1):
                arr[ro][co] = 45 - sum
                end=1
    return end

str = "183950246950106078726380195300812000472695813010473529501239784230740651847501032"

arr = array([], int)
for i in str:
    arr = append(arr, int(i))

arr = arr.reshape(9, 9)
end=1
while(end!=0):
    end=0
    end=end+check_rows(arr)
    end=end+check_column(arr)
    end=end+check_block(arr)
print_sudoko(arr)
