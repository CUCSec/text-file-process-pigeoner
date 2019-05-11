### 使用字符串的split方法 ###
chouba=[]
with open('log_files/201811113013.log',encoding='utf8') as f:
    for line in f:
        chouba.append(line.split('：',3)[2].split(',',1)[0])
print(chouba.count('201811113013'))