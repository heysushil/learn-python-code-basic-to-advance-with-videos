# formate method

def userDetails(**data):
    # print(data['name']); exit()
    print('''
    {name}'s details

    Name: {name}
    Subject: {subject}
    Mobile: {mobile}
    Fee: Rs. {fee:.2f}/-
    '''.format(name = data['name'],subject = data['subject'],mobile = data['mobile'], fee = data['fee']))

name = input('Enter your name: ')
subject = input('Enter your subject: ')
mobile = input('Enter your mobile number: ')
fee = int(input('Enter your fee: '))

# call function
userDetails(name = name, subject = subject, mobile = mobile, fee = fee)


'''
Work on this code:

1. validate karo ki user kewal 10 digit ka mobile number add kare agar wo 10 se jada ya kam number enter kar raha hai to useko message show others output show kar do.

2. agar user name, mobile, course, fee me se kisi ko bhi blank deta hai to bhi message show karo ki empty not allowed.

3. agar koi bhi error aata hai jaise ki agar user undefined input dera hai to ayse error ko handle bhi karo.

4. ye sara kam methods ka use karke karna hai, ki agar userne koi conditon galt di to kewal message show hota hai aur uske baad code ko fir se run karna padta hai. but is case me jaha par bhi conditon wrong hai usme message ke thik baad fucntion ko call karlo jo input maang raha hai.

Example: 
if user == empyt:
    print('EMpty name not allowed')
    userDetail()
'''