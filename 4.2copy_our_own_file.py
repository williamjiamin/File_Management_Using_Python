# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

with open('test.txt', 'r') as our_read_file:
    with open('text_copy.txt', 'w') as our_write_file:
        for every_line in our_read_file:
            our_write_file.write(every_line)
