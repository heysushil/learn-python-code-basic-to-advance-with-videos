# मैं एक यूट्यूब चैनल सुरू किया हूँ और आप यहाँ से सही तरीके से प्रोग्रामिंग सीख सकते हो साथ ही थोड़ा साहियोग ये भी चाहिए की इसे अपने दोस्तों से भी जरूर सेयर करो ताकि वो भी इस का फायदा ले सके क्यों की ज्ञान बांटने से ही बढ़ता हैं - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# अगर डेवलपमेंट फील्ड मे आना चाहते हो और समझ नहीं आ रहा है की कैसे क्या करू को तो मुझे कान्टैक्ट कर सकते हो heykyakaru@gmail.com पर और मैं कोसिस करूंगा सही गाइड करने की। क्योंकी बिना सही गाइड के कई बार हम काफी परेसान हो जाते हैं की क्या करे और कैसे करे।

# Contact for: College Project | Project Reporting | Documentation | Project Training | Website Development | SEO @ heykyakaru@gmail.com

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP
# 4. Python Project https://www.youtube.com/watch?v=3lrbbB38zpU&list=PLK6wiPavf7Qj-NLJhbkxw9QfonweHafcN
# 5. Tips and Trick for Development: https://www.youtube.com/watch?v=vPL6ODrfcwI&list=PLK6wiPavf7QiVLYXrC2TW_fdcZp57MgMB

print('Welcome to the Party List Creater paltform')

# Get number of party members
try:
    partyMembersNumber = int(input('Enter Number of Party Members: '))

    if partyMembersNumber > 0:
        print('Thanks for varifying the partymemeres number. \n\nYour party have {} members right.\n\nIf its right click y other wise n'.format(partyMembersNumber))
        # verify the memebrs
        yn = input('Enter y/n: ')
        if yn == 'y':
            print('Greate you verifyed your party members numebr. Lets create the list.')

            # create list of party members
            partyMembers = []
            # for 
        else:
            print('You want to change party memebres number. Lets start again with new numbers')
except:
    print('Only Numbers are allowed try again.')
