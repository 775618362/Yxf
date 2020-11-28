"""
python 数据类型是由，列表（list）,字符串（str）,数字（Number）,元组（tuple）,字典（dict）,集合（set）组成

list,tuple,set,dict 区别：
有序： list,tuple
无序： dict,set
读写:  list,dict,set
只读:  tuple
添加方式:  list(append),tuple(只读)，set(add),dict(d['key']='value')
存储方式:  list(值),tuple(值),set(键，不可重复),dict(键值对,键不能重复)
初始化:    [],(),(,),{'a':1}
不可重复:   tuple
"""
#后续补充，太基础了
#1.列表list[]
list1 = ['google','baidu']
list2 = [1,2,3,4,5]

#增加
list2.append(6)
print(list2)
#删除
list2.pop()
print(list2)
#改
list2[0] = '0'
print(list2)
print(list1.count('google'))

