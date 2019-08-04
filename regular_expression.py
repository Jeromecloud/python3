import re
# pattern = re.compile('\\d+')
    # \ ：转义\
    # \d 匹配任意数字
    # \d+ ：匹配一个或一个以上前面的表达式 
    # 匹配结果：['8', '232']
pattern = re.compile('\\w+')
    # \w 字母数字
    # 匹配结果：['Tom', 'is', '8', 'years', 'old', 'Jerry', 'is', '232', 'years', 'old']

    # ？0 或 1 次，非贪婪模式
    # * 0 到 多次
    # + 1 到 多次
    # {n，m} 最少 n 次，最多 m 次
    # () 选定特定的组
        # 使用() 会使匹配到的字符被缓存，使用?:放在第一个选项之前可消除缓存
    # \b 选定单词边界
txt = 'Tom is 8 years old, Jerry is 232 years old'
print(pattern.findall(txt))
