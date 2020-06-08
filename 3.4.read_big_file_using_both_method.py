# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

with open('test.txt', 'r') as f:
    the_size_of_every_chunk = 20

    the_content_of_the_file = f.read(the_size_of_every_chunk)

    while len(the_content_of_the_file) > 0:
        print(the_content_of_the_file, end='/////20个字符分界线//////')
        the_content_of_the_file = f.read(the_size_of_every_chunk)

# csv