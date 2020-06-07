# 推荐使用context manager进行自动的资源分配与释放
with open('test.txt', 'r') as f:
	pass

print(f.read())
