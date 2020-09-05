# You're working on a secret team solving coded transmissions. Your team is scrambling to decipher a recent
# message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly
# deciphered, but all the words are backward! Your colleagues have handed off the last step to you. Write a
# function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.
#
# For Example:
# message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]
#
# reverse_words(message)
# Prints: 'steal pound cake'
# print(''.join(message))


def reverse_words(listChars):

    start = 0
    end = len(listChars) - 1

    while start < end:
        listChars[start], listChars[end] = listChars[end], listChars[start]
        start += 1
        end -= 1

    start = 0
    end = 0
    length = len(listChars)
    for index in range(length + 1):
        if index == length or listChars[index] == ' ':
            end = index - 1
            reverseWord(start, end, listChars)
            start = index + 1

def reverseWord(start, end, word):

    while start < end:
        tmp = word[start]
        word[start] = word[end]
        word[end] = tmp
        start += 1
        end -= 1

message = ['p', 'o', 'o', 'r', ' ', 'I', 'm', ' ', 'm', 'e', ' ', 'h', 'e', 'l', 'p']
reverse_words(message)
print(''.join(message))
