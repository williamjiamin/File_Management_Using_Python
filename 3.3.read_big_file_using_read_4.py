# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

with open('test.txt', 'r') as f:
    the_content_of_our_file = f.read(20)
    print(the_content_of_our_file, end='\n')

    the_content_of_our_file = f.read(10)
    print(the_content_of_our_file, end='-------这个是10个字符的分界线-------')

    the_content_of_our_file = f.read(20)
    print(the_content_of_our_file, end='-------这个是10个字符的分界线-------')
