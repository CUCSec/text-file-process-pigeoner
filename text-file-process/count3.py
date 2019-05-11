### 使用re模块的split方法 ###
import re
result=[]
with open('log_files/201811113013.log',encoding='utf8') as f:
    for line in f:
        result.append(re.split(r'[：,]',line)[3])
print(result.count('201811113013'))
# 结果是109