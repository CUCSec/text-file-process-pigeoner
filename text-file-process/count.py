### 学号201811113013 ###
import re
count=0
mynum=['201811113013']
pattern=re.compile(r'(?<=学号：)\w+(?=, 时间：)')
with open('log_files/201811113013.log',encoding='utf8') as f:
    for line in f:
        result=pattern.findall(line)
        if result==mynum:
            count=count+1    
print(count)
# 结果是109
        