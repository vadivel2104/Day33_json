def compress(str1):
    output = ''
    initial = str1[0]
    output = output + initial
    count = 1
    for item in str1[1:]:
        if item == initial:
            count = count + 1
        else:
            if count == 1:
                count = ''
            output = output + str(count)
            count = 1
            initial = item
            output = output + item
    print (output)

compress("aaaaaaaccddddeehhyiiiuuoooo")