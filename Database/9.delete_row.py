import installing_and_connecting_db as con

# qeury for deleting row
deleteRowFromTable = "DELETE FROM aug_month WHERE sr=3"

# query execute
con.mycursor.execute(deleteRowFromTable)

# commit by mydb
con.mydb.commit()

print(con.mycursor.rowcount, 'row deleted.')

'''
Question:

1. Sab se pahle table me multiple entrys karo and then. Ek function create karna hai jis ka kaam hoga ki:

    a. user single input de raha hai aur user input me primary key id ya price ya person name ya date kuch bhi de.
    
    b. Iske liye alag-alag condtion ka use function me karna padega taki agar user input me id ya price ya jo kuch de raha hai usko alag se handle kiya ja sake.

    c. so, work ye hai ki agar use price diya to wo parice agar table me exist karti hai den useke behalf par wo sare row delete karne hai jisme wo price hai.

    d. Then user ko success ka message show karana hai.

    e. In case agar koi problem aati hai har ek condtion me to unke liye exception handel karna hai.
'''