word = "aaaaaaaccddddeehhyiiiuuoooo"

count = 0
initial = word[0]
new_word = "" + initial


for i in range(len(word)):
    if initial == word[i]:
        count += 1
    else:
        new_word = new_word + str(count)
        initial = word[i]
        new_word = new_word + word[i]
        count = 1
new_word = new_word + str(count)
print(new_word)






















