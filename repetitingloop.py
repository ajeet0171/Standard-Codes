entries=[]
while True:
    num=int(input("Enter an integer (-1 to quit): "))
    if num==-1:
        break
    entries.append(num)
num_entries=len(entries)
max_entries=max(entries)
least_entries=min(entries)
sum_entries=sum(entries)
avg_num=sum_entries/num_entries
print(f"The number of entries you entered is {num_entries}.")
print(f"The greatest number you entered is {max_entries}.")
print(f"The least number you entered is {least_entries}.")
print(f"The sum of all the numbers you entered is {sum_entries}.")
print(f"The average of all the numbers is {avg_num:.2f}.")   /* .2f is used to make decimal number of point */
