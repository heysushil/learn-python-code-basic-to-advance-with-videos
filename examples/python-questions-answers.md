# Python Basic and Advance Questions list - be ready to solve them

## Agar question realted koi porblem hai to mujhe [YouTube Discussion](https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion) par puch sakte ho.

> Note: Sabhi questions searial wise hain, to kosis karo ki inhe isi serial me solve karo. Good luck

> Note: Sabhi answer usi sequence me hain jinme questions hai

## Dictionary related answers

1. Diye gaye dict me brad ki salary update karke 8500 karni hai:

        sampleDict['emp3']['salary'] = 8500
        print(sampleDict)<

1. Ye do list hai inko dictionary me convert karna hai: 

        keys = ['Ten', 'Twenty', 'Thirty']
        values = [10, 20, 30]

        sampleDict = dict(zip(keys, values))
        print(sampleDict)

1. In 2 dictionary ko ek sath marg karo:

    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

        dict3 = dict1.copy()
        dict3.update(dict2)
        print(dict3)

1. Is diye gaye dict mese history ki value ko show karao:

        print(sampleDict['class']['student']['marks']['history'])

1. Diyegaye list ko as a key aur diyegaye dict ko as a value set karo:

        employees = ['Kelly', 'Emma', 'John']
        defaults = {"designation": 'Application Developer', "salary": 8000}

        resDict = dict.fromkeys(employees, defaults)
        print(resDict)

        # Individual data
        print(resDict["Kelly"])

1. Dict me check karna hai ki kya 200 value exist karta hai ya nahi:
	
        sampleDict = {'a': 100, 'b': 200, 'c': 300}
        print(200 in sampleDict.values())

1. Diye gaye dict me city ko rename karke location karna hai:

        sampleDict = {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "city": "New york"
        }
        
        sampleDict['location'] = sampleDict.pop('city')
        print(sampleDict)

1. Diye gaye dict me jis subject ka bhi marks sabse kam hai usko find kar ke show karna hai:

        sampleDict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
        }
        print(min(sampleDict, key=sampleDict.get))

1. Diye gaye dict mese niche bataye keys ka use kar ke new dict banao:

        sampleDict = { 
        "name": "Kelly",
        "age":25, 
        "salary": 8000, 
        "city": "New york" }

        keys = ["name", "salary"]

        newDict = {k: sampleDict[k] for k in keys}
        print(newDict)

1. Dict mese following keys ko remove karna hai:

        sampleDict = {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "city": "New york"
        }
        keysToRemove = ["name", "salary"]

        sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}
        print(sampleDict)


# Set answers:

1. Set me diye gaye list ko add karna hai:

        sampleSet = {"Yellow", "Orange", "Black"}
        sampleList = ["Blue", "Green", "Red"]
        sampleSet.update(sampleList)
        print(sampleSet)

1. 2no set me se identical item ko find karna hai:

        set1 = {10, 20, 30, 40, 50}
        set2 = {30, 40, 50, 60, 70}

        print(set1.intersection(set2))

1. 2no set mese unique items ko find karan hai:

        set1 = {10, 20, 30, 40, 50}
        set2 = {30, 40, 50, 60, 70}

        print(set1.union(set2))

1. 2no set me se 1st set me jobhi item unique hai kewal unko dikhana hai:
	
        set1 = {10, 20, 30}
        set2 = {20, 40, 50}

        set1.difference_update(set2)
        print(set1)

1. Diye gaye set mese 10,20,30 ek baar me hi remove karne hai:

        set1 = {10, 20, 30, 40, 50}
        set1.difference_update({10, 20, 30})
        print(set1)

1. Diye gaye set me jo bhi number dono set me common na ho unko dikhana hai:

        set1 = {10, 20, 30, 40, 50}
        set2 = {30, 40, 50, 60, 70}

        print(set1.symmetric_difference(set2))

1. Set 1 mese wo values ko remove karna hai jo set 2 me nahi hai:

        set1 = {10, 20, 30, 40, 50}
        set2 = {30, 40, 50, 60, 70}

        set1.intersection_update(set2)
        print(set1)

1. 2no set me jobhi common values hai wo show karna hai:

        set1 = {10, 20, 30, 40, 50}
        set2 = {60, 70, 80, 90, 10}

        if set1.isdisjoint(set2):
        print("Two sets have no items in common")
        else:
        print("Two sets have items in common")
        print(set1.intersection(set2))
