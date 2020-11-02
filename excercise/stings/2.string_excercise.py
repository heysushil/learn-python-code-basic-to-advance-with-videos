'''
Python String Excercise Questions with Hey Sushil:

1. Kisi sentence me kaonse word kitni baar aaye hain ye count karna hai? Kaise karenge?
    Karte hain:

2. Is string me word ko alphabetically form me show karna hai kaise karenge? Aur yase hi agar user input string ko arrenge karna ho to kaise karenge?
    Sample Words : red, white, black, red, green, black
    Expected Result : black, green, red, white,red

3. Is string me kaise html tag add kiya jaye? Ayse hi input string me kaise kiya jayega?
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

4. In box ke bich me word ko kaise add kiya jaye? Aur isko function me kaise banaya jaye?
insert_sting_middle('[[]]', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
val[0][:2]

5. Is string ke liye function bana hai aur agar ayse hi koi aur input mile to uske last 2 char ki 4 copice kaise show karenge?
Sample function and result :
    insert_end('Python') -> onononon
    insert_end('Exercises') -> eseseses

6. Kaise is url me agar last me dash aa raha hai to uske pahle ka sara data get kar ke show karayen?
https://www.youtube.com/heysushil-hello
https://www.youtube.com/heysushil

7. Agar input string ke length even hai then show karo otherwise kuch nahi show karna hai?

8. Agar input string me at least 2 upper case letter hain then string ko upper case me convert kar ke show karna nahi to normal show?
Jaise ki:
    HeYsushil = HEYSUSHIL
    Heysushil = Heysushil

9. Kisi bhi string me se newline kaise remove karenge? rstrip()?

10. Koi input kisi specified word se start hua hai ya nahi kaise pata karenge? startswith()?
example: 'heysushil how are you?'

11. Caesar encryption ka use karke message ko encrypt karna hai. Aur kya hai Caesar encryption?
    Karke dekhte hain:

12. Kisi float number me kewal 2 deciamal values kaise show karenge?
    Dekhte hain:

13. Kaise kisi float number ke sath positive ya negative ka sign show karenge?
    Dekhte hain:

14. Kisi folat number me koi bhi decimal value nahi cahiye hain, kaise karenge?
    Dekhte hain:

15. Kisi integer number me pahle zero kaise show kare?
    Dekhte hain:
'''

# 1. Kisi sentence me kaonse word kitni baar aaye hain ye count karna hai? Kaise karenge?

def count_number_of_words_on_string(my_string):
    all_words = my_string.split(' ')
    # print('\n', all_words)

    # use for loop to get individual word
    # blank dict for showing count
    count = dict()
    for word in all_words:
        # print('\n', word)

        # agar word single time aaya to
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    print('\nFinal word count result: \n\n', count)


my_string = '1. Kisi sentence me kaonse word kitni baar aaye hain ye count karna hai? Kaise karenge? me and ye'

# call count_number_of_words_on_string
count_number_of_words_on_string(my_string)


# 2. Is string me word ko alphabetically form me show karna hai kaise karenge? Aur yase hi agar user input string ko arrenge karna ho to kaise karenge?

colors = 'red, white, black, red, green, black'
words = [word for word in colors.split(',')]

print('\n'+','.join(sorted(list(set(words)))))

# 5. Is string ke liye function bana hai aur agar ayse hi koi aur input mile to uske last 2 char ki 4 copice kaise show karenge?

name = 'HeySushil'
print('\nName: ', name[-2:])


# 8. Agar input string me at least 2 upper case letter hain then string ko upper case me convert kar ke show karna nahi to normal show?

print('\n\ncount_char_of_words:\n')
def count_char_of_words(message):
    count_upper = 0
    for m in message:
        # print(m)
        if m.upper() == m:
            count_upper += 1

    # final condtion to show output
    if count_upper >= 2:
        print('\nUpper case: ', message.upper())
    else:
        print('\nNormal case: ', message)

message = 'Heysushil'
count_char_of_words(message)


# 11. Caesar encryption ka use karke message ko encrypt karna hai. Aur kya hai Caesar encryption?
print('\n\ncaesar_encryption: \n')
def caesar_encryption(message, step):
    # blank list fro outptu
    output = []
    encrypt_text = []

    lower_case = ['a','b','c','d','e','f','g']

    for e in message:
        if e in lower_case:
            index = lower_case.index(e)
            encrypt = (index + step) % 7
            encrypt_text.append(encrypt)
            new_letter = lower_case[encrypt]
            output.append(new_letter)
    print('\nFinal encryted value: ', output)

caesar_encryption('ABC', 3)
