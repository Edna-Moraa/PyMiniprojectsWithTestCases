band = {
    "vocals" : "Plant",
    "guitar" : "Page"
}

band2 = dict(vocals="Plant",
             guitar="Page")

print(band)

print(type(band2))
print(len(band2))

#access items
print(band["guitar"])
print(band.get("vocals"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/value pairs as tuples
print(band.items())

#find if exists
print("guitar" in band)
print("red" in band)

#change values
band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})

print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

#delete and clear
band["drums"]= "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2


#copy dictionaries
band2 = band.copy()
band2["drums"]="Edu"
print(band)
print(band2)
#using constructor
band3 =  dict(band)
print(band3, "good")

# nested dictionaries

member1 = {
    "name" : "Plant",
    "instrument" : "Vocals",
}
member2 = {
    "name" : "Page",
    "instrument" : "guitar",
}
band = {
    "member1" : member1,
    "member2" : member2,
}

print(band)
print(band["member1"]["name"])


#sets

nums = {1, 2, 3, 4}
nums2 =set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))
print(nums)

#no duplicates allowed
# True is a dupe of 1, False is a dupe of 0

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#check if valueis in a set
print(2 in nums)
print(8 in nums)
#but you cannot refer to an element in the set with an index position or a key

#add a new element to a set
nums.add(8)
print(nums)

#add elements from 1 set to another
morenums ={ 5,6,7}
nums.update(morenums)
print(nums)
#you can use update with lists,tuple,dictionaries too

#merge 2 sets to create a new set
one = {1,2,3}
two = {4,5,6}
newset = one.union(two)
print(newset)


#keep only duplicates
one = {1,2,3}
two = {2,1,6}
one.intersection_update(two)
print(one)

#keep everything except the duplicates
one = {1,2,3}
two = {2,1,6}
one.symmetric_difference_update(two)
print(one)
