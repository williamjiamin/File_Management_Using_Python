# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

with open('test.txt', 'r') as f:
    the_size_of_every_chunk = 20

    the_content_of_the_file = f.read(the_size_of_every_chunk)
    print(the_content_of_the_file, end='\n ***** \n又从头开始读取\n***** \n')

    # 强制性从头开始读取,如果将其中的参数进行更改，可以自定义从任意地方开始读取
    f.seek(5)

    the_content_of_the_file = f.read(the_size_of_every_chunk)
    print(the_content_of_the_file, end='')
