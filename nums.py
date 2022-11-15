Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
nums=[25,12,36,45,13]
nums
[25, 12, 36, 45, 13]
nums[0]
25

nums[2]
36
nums[2:]
[36, 45, 13]
nums[-1]
13
nums[-5:]
[25, 12, 36, 45, 13]
nums[-2:]
[45, 13]
names=['navin','kiran','john']
names
['navin', 'kiran', 'john']
values=[9.5,'anushka',23]

mils=[nums,names,values]
mils
[[25, 12, 36, 45, 13], ['navin', 'kiran', 'john'], [9.5, 'anushka', 23]]
nums.insert(2,33)
nums
[25, 12, 33, 36, 45, 13]
nums.remove(36)
nums
[25, 12, 33, 45, 13]
nums.pop(1)
12
nums.pop(2)
45
nums.pop(3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    nums.pop(3)
IndexError: pop index out of range
nums.pop(4)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    nums.pop(4)
IndexError: pop index out of range
nums.pop()
13

del nums[2:]
nums
[25, 33]
nums.extend([29,50,44])
nums
[25, 33, 29, 50, 44]
min(nums)
25
max(nums)
50
sum(nums)
181
nums.sort()
nums
[25, 29, 33, 44, 50]
