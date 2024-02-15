#A set is a collection of unique data. That is, elements of a set cannot be duplicate
#a set is an unordered and mutable collection of unique elements. Sets are defined using curly braces {} or the set() constructor

#merge list with set
#set with set and set with tuple


my_set={1,2,3,2, 3,"apple","orange","apple"}
print(my_set)
print(type(my_set))
my_set.add(10)
print(my_set)


#Update python set
set1={1,2,3}
list2=['apple', 'android']
set1.update(list2)
print(set1)


#remove elements from set
my_set.discard('orange')
print(my_set)


#Min and Maximun and remove duplicate normally with set
set2={2,3,4,56,98,23,56,34,34,56,2,3,4}
print('Set2', set2)
print('Min:', min(set2))
print('Max: ',max(set2))
print('Sum: ',sum(set2))
print('Len: ',len(set2))
print('Sorted: ',sorted(set2))

#union combines elements from two sets only, by removing duplcates
set3 ={1,2,3}
set4={3,4,5}
union_set=set3.union(set4)
print('Union set:', union_set)

#Intersection - returns common elements between two
#so for above it is 3

set3 ={1,2,3}
set4={3,4,5}
intersection_set =set3.intersection(set4)
print("intersection", intersection_set)


#differrence -will give the items in the first set that is not in #second set.
difference_set = set3.difference(set4)
print("difference", difference_set)

#symmetric difference --retuns element tht are  unique to each set
symmetric_difference_set=set3.symmetric_difference(set4)
print('symmetric differnce', symmetric_difference_set)


#SubSet- set 1 is a subset of set2
#set1 value is there in set2

set3 ={1,2,3}
set4={1,2,3,4,5}
subset=set3.issubset(set4)
print('subset', subset)



#Assignment 

#superset a superset typically refers to a set that contains all the elements of another set, possibly with additional elements. If you're referring to the concept of sets, you can use the issuperset() method to check if one set is a superset of another. 

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}

# Check if set1 is a superset of set2
is_superset = set1.issuperset(set2)

print(f"Is set1 a superset of set2? {is_superset}")


#disjoint-check whether two sets are disjoint using the isdisjoint() method. Two sets are disjoint if they have no elements in common.

# Define two sets
	set1 = {1, 2, 3}
	set2 = {4, 5, 6}

# Check if the sets are disjoint
are_disjoint = set1.isdisjoint(set2)

print(f"Are set1 and set2 disjoint? {are_disjoint}")
#copy

original_set = {1, 2, 3, 4, 5}

copied_set = original_set.copy()

print("Original Set:", original_set)
print("Copied Set:", copied_set)

#clear
my_set = {1, 2, 3, 4, 5}

print("Original Set:", my_set)

# Clear the set
my_set.clear()

print("Set after clearing:", my_set)


