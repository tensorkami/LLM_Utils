


def frquency_corpus(list_of_string):
    freq = {}
    for i in  list_of_string:
        for j in i:

            freq[j] = freq.get(j, 0) +1
    return freq






def count_n_gram1(sentence, n_gram = 3, stride = 1):

    count = {}
    chunck = n_gram
    for word in sentence:
        buffer = []
        word  = '.' + word + '$'
        for i in word:
            buffer.append(i)
            if len(buffer) ==chunck:
                st = "".join(buffer)
                count[st] = count.get(st, 0) + 1
                buffer = buffer[stride:]
            
    return count