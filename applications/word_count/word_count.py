def word_count(s):
    # Your code here
    #
    badchars = [",", ".", ":", ";", '"', "(", "/", ")", "-", "+",
                "=", "/", "\\", "|", "[]", "{}", "()", "*", "^", "&", "\t", "\r", "\n"]
    for i in badchars:
        s = s.lower().replace(i, " ")
    l = s.split(" ")
    d = {}
    for c in l:
        if c == "":
            continue

        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    return d


# if __name__ == "__main__":
#     print(word_count(""))
#     print(word_count("Hello"))
#     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
#     print(word_count(
#         'This is a test of the emergency broadcast network. This is only a test.'))

# word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.')


# word_count('a a\ra\na\ta \t\r\n')
