# Python Basic and Advance Questions list - be ready to solve them

## Agar question realted koi porblem hai to mujhe [YouTube Discussion](https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion) par puch sakte ho.

> Note: Sabhi questions searial wise hain, to kosis karo ki inhe isi serial me solve karo. Good luck

## Dictinary related questions:

1. Diye gaye dict me brad ki salary update karke 8500 karni hai:

    sampleDict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 6500}
    }

        Expected output:
        sampleDict = {
            'emp1': {'name': 'Jhon', 'salary': 7500},
            'emp2': {'name': 'Emma', 'salary': 8000},
            'emp3': {'name': 'Brad', 'salary': 8500}
        }

1. Ye do list hai inko dictionary me convert karna hai:

    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
        
        Output kuch aysa hona chaiye: 
        {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

1. In 2 dictionary ko ek sath marg karo:

    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

        Aur iska output kuch aysa mulna cahiye:
        {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

1. Is diye gaye dict mese history ki value ko show karao:

    sampleDict = { 
    "class":{ 
        "student":{ 
            "name":"Mike",
            "marks":{ 
                "physics":70,
                "history":80
            }
        }
    }
    }

        Expected answer: 80

1. Diyegaye list ko as a key aur diyegaye dict ko as a value set karo:

    employees = ['Kelly', 'Emma', 'John']
    defaults = {"designation": 'Application Developer', "salary": 8000}

1. Dict me check karna hai ki kya 200 value exist karta hai ya nahi:
    
    sampleDict = {'a': 100, 'b': 200, 'c': 300}

        Expected output:
        True

1. Diye gaye dict me city ko rename karke location karna hai:

    sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
    }
 
        Expected output:
        {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "location": "New york"
        }

1. Diye gaye dict me jis subject ka bhi marks sabse kam hai usko find kar ke show karna hai:

    sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
    }

        Expected output:
        Math


## Set questions:

1. Set me diye gaye list ko add karna hai:

    sampleSet = {"Yellow", "Orange", "Black"}
    sampleList = ["Blue", "Green", "Red"]

        Expected output:
        In set item order is not a concern
        {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

1. 2no set me se identical item ko find karna hai:

    set1 = [10, 20, 30, 40, 50]
    set2 = [30, 40, 50, 60, 70]

        Expected output:

        {40, 50, 30}

1. 2no set mese unique items ko find karan hai:

    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

        Expected output:
        {70, 40, 10, 50, 20, 60, 30}

1. 2no set me se 1st set me jobhi item unique hai kewal unko dikhana hai:

    set1 = {10, 20, 30}
    set2 = {20, 40, 50}

        Expected output:
        set1 = {10, 30}

1. Diye gaye set mese 10,20,30 ek baar me hi remove karne hai:

	set1 = {10, 20, 30, 40, 50}

        Expected output:
        {40, 50}

1. Diye gaye set me jo bhi number dono set me common na ho unko dikhana hai:
	
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

        Expected output:
        {20, 70, 10, 60}

1. Set 1 mese wo values ko remove karna hai jo set 2 me nahi hai:
	
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

        Expected output:
        {40, 50, 30}

1. 2no set me jobhi common values hai wo show karna hai:

    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}

        Expected output:
        Two sets have items in common
        {10}





