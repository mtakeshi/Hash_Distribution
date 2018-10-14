import hashlib
import statistics

l = [0] * 16

for count in range(0,200000,1):
	h = hashlib.md5(str(count).encode("utf-8")).hexdigest().upper()
	first = h[0:1]
	n = int(first,16)
	l[n] = l[n] + 1

# min(l)
# max(l)
# l


