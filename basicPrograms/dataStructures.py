#List
#list is a collection which is ordered and changeable. Allows duplicate members.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#List items can be of any data type.    

list=[5,"True",3.5,"a"]

print(type(list))  #<class 'list'>


list_a=[5,"False",8.2]
list_b=[1,list_a]

print(list_b)   #[1, [5, 'False', 8.2]]

#length of list
list_c=[5,"False",8.2]
print(len(list_c))   #3

#accessing list items
list_d=[5,"True",9.0,"Raahg"]
print(list_d[2])   #9.0

#iterate through a list        
list_e=[5,"True",9.0,"Raahg"]   #5
for item in list_e:
    print(item)   


#concatenate two lists
list_a=[1,2,3]
list_b=["a","b","c"]
list_c=list_a+list_b
print(list_c)   #[1, 2, 3, 'a', 'b', 'c']


#empty list and adding items
list_f=[]
print(list_f)   #[]

for i in range(5):
    list_f +=[i]

print(list_f)   #[0, 1, 2, 3, 4]


#repeat items in a list
list_a=[1,2]
list_b=list_a*3
print(list_b)   #[1, 2, 3, 1, 2


#slicing a list
list_a=[5,"False",8.2]
list_b=list_a[0:2]
print(list_b)        #[5, 'False']

list_a=["R","G","B","Y","O"]
list_b=list_a[0:5:3]  #step size
print(list_b)        #['R', 'Y']

color="yellow"
list_a=list(color)
print(list_a)   #['y', 'e', 'l', 'l', '"

list_a=list(rang(11))
