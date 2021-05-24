import re

fh = open('regex_sum_1250707.txt')
sum = 0
for line in fh:
    nums = re.findall('[0-9]+', line)
    for num in nums:
        inum = int(num)
        sum = sum + inum
print(sum)
