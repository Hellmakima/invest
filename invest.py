# Investment Plan for years to come
# Nov 29, 2025 1$ ≈ ₹88
# No tax is considered

# Min Value in 50 years at a=$1.5k 6% CR and 0% CIR:
# $ 177,362.00
# ₹ 1,56,07,856
# with inflation at 8%, value today ≈ ₹ 3Lk
# value in todays terms = (future_value / (1 + inflation_rate)**years)

# Max Value in 50 years at a=$1.5k 12% CR and 6% CIR
# $ 3,055,529.54
# ₹ 26,88,86,600
# with inflation at 1%, value today ≈ ₹ 15Cr
# with inflation at 2%, value today ≈ ₹ 9Cr

a = 130_000
YEARS = 50
values:list[float] = [a]
CONTRIB = 10_000


# max 6% min 0%. IDK just a guess
contribution_increment_rate = 1.06


# max 1.12 min 0.06 (more towards 12% in long term)
compound_rate = 1.12


for i in range(1,12*YEARS+1):
	a += CONTRIB
	if i % 12 == 0:
		a *= compound_rate
		values.append(a)
		CONTRIB *= contribution_increment_rate
		a *= 0.975 # 2.5% yearly donation

		print(f'{(a/88):20,.2f} $')
		print(f'value in year {2025+i//12}: {a:10,.0f} ₹')
		print(f'contrib rate in year {2025+i//12}: {CONTRIB:.0f}')

# Visualize
# import matplotlib.pyplot as plt
# plt.plot(values)
# plt.show()

