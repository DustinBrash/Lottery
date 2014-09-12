_name_ = "LotteryTrack"

import pickle

def clear_pick3():
    f = open("pick3.txt", 'w')
    l = []
    for i in range(3):
        l.append([])
        for j in range(10):
            l[i].append(0)
    l.append(0)
    pickle.dump(l, f)
    f.close()

def clear_pick4():
    f = open("pick4.txt", 'w')
    l = []
    for i in range(4):
        l.append([])
        for j in range(10):
            l[i].append(0)
    l.append(0)
    pickle.dump(l, f)
    f.close()

def clear_megamillions():
    f = open("pick3.txt", 'w')
    l = []
    for i in range(6):
        l.append([])
        for j in range(10):
            l[i].append(0)
    l.append(0)
    pickle.dump(l, f)
    f.close()

def update_pick3(updated_nums):
    f = open("pick3.txt", 'r')
    nums = pickle.load(f)
    f.close()
    n = updated_nums[0]
    m = updated_nums[1]
    o = updated_nums[2]
    nums[0][n] += 1
    nums[1][m] += 1
    nums[2][o] += 1
    nums[3] += 1
    f = open("pick3.txt", 'w')
    pickle.dump(nums, f)
    f.close()
    
def update_pick4(updated_nums):
    f = open("pick4.txt", 'r')
    nums = pickle.load(f)
    f.close()
    n = updated_nums[0]
    m = updated_nums[1]
    o = updated_nums[2]
    p = updated_nums[3]
    nums[0][n] += 1
    nums[1][m] += 1
    nums[2][o] += 1
    nums[3][p] += 1
    nums[4] += 1
    f = open("pick4.txt", 'w')
    pickle.dump(nums, f)
    f.close()
    
def update_megamillions(updated_nums):
    f= open("MegaMillions.txt", 'r')
    nums = pickle.load(f)
    f.close()
    n = updated_nums[0]
    m = updated_nums[1]
    o = updated_nums[2]
    p = updated_nums[3]
    q = updated_nums[4]
    r = updated_nums[5]
    nums[0][n] += 1
    nums[1][m] += 1
    nums[2][o] += 1
    nums[3][p] += 1
    nums[4][q] += 1
    nums[5][r] += 1
    nums[6] += 1
    f= open("MegaMillions.txt", 'w')
    pickle.dump(nums, f)
    f.close()

def get_largest_index(nums):
    total = 0
    index = 0
    for i in range(len(nums)):
        if nums[i] < total:
            continue
        total = nums[i]
        index = i
    return index

def get_pick3():
    f = open("pick3.txt", 'r')
    nums = pickle.load(f)
    fin = []
    for i in range(3):
        max_index = get_largest_index(nums[i])
        fin.append(max_index)
    fin.append(nums[3])
    f.close()
    return fin

def get_pick4():
    f = open("pick4.txt", 'r')
    nums = pickle.load(f)
    fin = []
    for i in range(4):
        max_index = get_largest_index(nums[i])
        fin.append(max_index)
    fin.append(nums[4])
    f.close()
    return fin

def get_megamillions():
    f= open("MegaMillions.txt", 'r')
    nums = pickle.load(f)
    fin = []
    for i in range(6):
        max_index = get_largest_index(nums[i])
        fin.append(max_index)
    fin.append(nums[6])
    f.close()
    return fin

while True:
    i = raw_input("Update numbers? Y or N ")
    if i == 'N':
        break
    
    i = raw_input("What numbers to work with? ")
    if i == 'pick3':
        numbers = i
        x = 3
    elif i == 'pick4':
        numbers = i
        x = 4
    elif i == 'megamillions':
        numbers = i
        x = 6
        
        
    i = raw_input("What do you want to do: get, clear, or update? ")
    if i == 'update':
        action = i
        new_nums = []
        for i in range(x):
            n = raw_input("Enter a number: ")
            n = int(n)
            new_nums.append(n)
        stri = action + '_' + numbers
        func = globals()[stri]
        func(new_nums)
    elif i == 'get':
        action = i
        stri = action + '_' + numbers
        func = globals()[stri]
        print func()
    elif i == 'clear':
        action = i
        stri = action + '_' + numbers
        func = globals()[stri]
        func()


    
    
