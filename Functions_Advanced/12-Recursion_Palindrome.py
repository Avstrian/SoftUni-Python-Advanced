def palindrome(word, index):
    end_index = -index - 1

    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] == word[end_index]:
        end_index -= 1
        return palindrome(word, index+1)
    else:
        return f"{word} is not a palindrome"
