




def count_word(list_word, sort = True):
    count = {}
    for i in list_word:
        count[i] = count.get(i, 0) + 1
    if sort:
        count = dict(sorted(count.items(), key = lambda item : item[1], reverse = True))
    return count





def chunk(sequence, batch, stride, drop_last = False):
    buffer = []
    for i in sequence:
        buffer.append(i)
        if len(buffer) == batch:
            yield buffer
            buffer= buffer[stride:]
    if (not drop_last):
        yield buffer
        
        
        
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
