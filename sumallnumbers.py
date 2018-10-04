def sum_all(list):
    if list[0]==list[1]:
        return list[0]
    if list[0]>list[1]:
        min=list[1]
        max=list[0]
    else:
        min=list[0]
        max=list[1]
    sum=0;
    for i in range(min, max+1):
        sum=sum+i
    return sum
