def ez(z, N):
	s = 0.0
	fact = 1  # k!
	pwr = 1.0  # z**k
	for k in range(N):
		if k > 0:
			fact *= k
			pwr *= z
		s += pwr / fact
	return s
print(ez(2, 10))