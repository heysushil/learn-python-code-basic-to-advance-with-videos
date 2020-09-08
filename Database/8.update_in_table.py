'''
Table me agar koi data update karna ho to:

1. Data update karne ke liye ye dhyan rahe ki ham ek time par kisi ek row ke data ko update kanrege.
2. Table me multiple rows hain aur har ek row ka ek specific primary key hai.
3. Issi primary key ke behalf par hum row data ko update karenge.
4. Ya fir agar multiple rows me one time me update karna hai to hum name ya price ya date ke behalf par bhi update kar sakte hain.

'''

import installing_and_connecting_db as con

# update data behalft of sr number
updatePriceByID = "UPDATE aug_month SET price=20 WHERE sr=2"

# exucte this query
con.mycursor.execute(updatePriceByID)

# then commit
con.mydb.commit()

# check row updated or not
print(con.mycursor.rowcount, ' row is effected')

'''
Question:

1. Ek funciton bana hai jisme ki user se input me single id lena hai aur ye id table ki primary key se match karna hai agar ye match nahi hota hai then iske liye try excep ka use karke error handle karna hai.

Other wise use input id match karta hai then use row id par user kya update karna cahta hai uske liye user ko message show karna hai:
    Like as:
        a. agar price change karna hai to enter p:
        b. agar date change karna hai to enter d:
        c. agar name change karna hai to n:

user input me agar use inme se koi bhi input deta hai to uske behalf par user se fir: jaise ki
    a. user agar price update karna chata hai to.

User se price lena hai then useko update kar ke user to update message show karana hai.

Yahi same case baki ke liye bhi karna hai.

But agar user like: p ya d ya n mese kuch bhi nahi de raha hai then is problem ko handle bhi karna hai aur user ko message show karna hai ki user sahi input dooo.
'''