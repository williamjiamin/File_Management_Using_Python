# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

# 这样不行，因为r目前是以utf-8进行解码，无法读取图片信息
# with open('lxod_test_img.jpeg', 'r') as our_read_img_file:
#     with open('lxod_test_img_copy.jpeg', 'w') as our_write_img_file:
#         for every_line in our_read_img_file:
#             our_write_img_file.write(every_line)

# 我们通过直接读取字节信息
# https://docs.python.org/3/library/functions.html#open
# with open('lxod_test_img.jpeg', 'rb') as our_read_img_file:
#     with open('lxod_test_img_copy.jpeg', 'wb') as our_write_img_file:
#         for every_line in our_read_img_file:
#             our_write_img_file.write(every_line)


with open('lxod_test_img.jpeg', 'rb') as our_read_img_file:
    with open('lxod_test_img_copy.jpeg', 'wb') as our_write_img_file:
        for every_line in our_read_img_file:
            our_write_img_file.write(every_line)

