"""
函数得好处：
1.减少重复代码
2.保持一致性，易维护性
3.可扩展性
一个函数可以实现一个功能
"""

"""
函数即变量
局部变量，全局变量 
全局变量：
全局变量变量名，大写，局部变量变量名小写
1.顶头写的就是全局变量例如：
name = 'xf'

"""
name = "刚娘"
def weihou():
    name = "陈卓"
    def weiweihou():
        global name
        name = "冷静"
    weiweihou()
    print(name)
weihou()
print(name)

"""
递归
1.递归必须有一个结束条件
2.规模必须越来越小

"""
#例子1：
def calc(n):
    print(n)
    if int(n / 2) == 0:
        return n
    return calc(int(n / 2))
#例子2：
import time
person_list = ['alex','wupeiqi','yuanhao','linhaifeng']
def ask_way(person_list):
    print('-'*20)
    if len(person_list) == 0:
        return "没人知道"
    person = person_list.pop(0)
    if person == 'linhaifeng':
        return "%s说:我知道，老男孩就在沙河会的商厦，下地铁就是"%person
    print('hi 美男【%s】,敢问路在何方'%person)
    print('%s回答到：我不知道，但是你慧眼识猪，你等着，我帮你问问%s'%(person,person_list))
    time.sleep(2)
    res = ask_way(person_list)
    print('%s 问的结果是:%s'%(person,res))
    return res

res = ask_way(person_list)
print(res)