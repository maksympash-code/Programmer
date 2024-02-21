S_k_p , R_z = [float(d) for d in input().split()]
S_k = S_k_p / 3.141592
R_v = (R_z ** 2 - S_k) ** 0.5
print(f"{R_v: 0.2f}")