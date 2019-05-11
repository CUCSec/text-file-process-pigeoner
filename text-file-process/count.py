with open('log_files/201811113013.log',encoding='utf8') as f:
    print(list(str(f.read()).split('：')).count('201811113013, 时间'))