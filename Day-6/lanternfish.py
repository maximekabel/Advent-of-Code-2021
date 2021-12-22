file = open("input.txt")
input = file.read().strip().split(",")
input = [int(i) for i in input]
dict =  {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for key in dict:
    dict[key] = input.count(key)
print(dict)
     
def count_feesh(days):
    for day in range(days):
        temp_dict = dict.copy()
        for key in temp_dict:
            if key != 8:
                dict[key] = temp_dict[key+1]
    
        for key in temp_dict:
            if key == 0:
                dict[8] = temp_dict[key]
                dict[6] += temp_dict[key]
    
    sum =0
    for key in dict:
        sum += dict[key]
    return str(sum)

print("Part 1: "+count_feesh(80))
print("Part 2: "+count_feesh(256))

