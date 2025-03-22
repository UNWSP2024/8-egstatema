# Eliya Statema
# 3/21/25
# Word Separator

def main():
    result = ''

    user_input = input('''Enter a sentence without spaces where 
every word starts with a capital letter: ''')

    result = result + user_input[0]

    for i in range(1, len(user_input)):
        char = user_input[i]

        if char.isupper():
            char = char.lower()
            result = result + ' '

        result = result + char

    print(result)

if __name__ == "__main__":
    main()