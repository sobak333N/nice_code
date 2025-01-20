def read_file_by_word(filename: str):
    with open(filename, 'r') as file:
        words = []
        cur_limit: int | None = None
        for line in file:
            for word in line.split():
                if cur_limit:
                    words.append(word)
                    if len(words) == cur_limit:
                        cur_limit = (yield words)
                        words = []
                else:
                    words.append(word)
                    cur_limit = (yield words)
                    words = []


rfbw = read_file_by_word('file.txt')
print(next(rfbw))
for i in range(1,7):
    print(rfbw.send(i))

for word in rfbw:
    print(word)