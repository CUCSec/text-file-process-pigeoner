###学号201811113013###
import re
result=[]
pattern=re.compile(r'(?<=学号：)\w+(?=, 时间：)')
with open('log_files/201811113013.log',encoding='utf8') as f:
    for line in f:
        result.append(pattern.findall(line)[0])
print(result.count('201811113013'))
# 结果是109
        