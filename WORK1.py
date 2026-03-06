import math
import matplotlib.pyplot as plt


data =[
    274.773, 274.673, 274.244, 274.546, 274.580, 274.469, 274.543, 274.599, 274.127, 274.345,
    274.601, 274.440, 274.452, 274.278, 274.614, 274.470, 274.790, 274.709, 274.660, 274.965,
    274.759, 274.639, 274.945, 274.880, 274.684, 274.464, 274.627, 274.313, 274.412, 274.442,
    274.473, 274.457, 274.381, 274.235, 274.584, 274.882, 274.819, 274.510, 274.872, 274.648,
    275.020, 274.481, 274.539, 274.497, 274.241, 274.925, 274.853, 274.716, 274.653, 274.663
]

n = len(data)
t_student = 2.01
delta_prib = 0.1


def calc_mean(arr):
    return sum(arr) / len(arr)

def calc_variance(arr, mean):
    return sum((x - mean)**2 for x in arr) / (len(arr) - 1)

mean_val = calc_mean(data)
variance = calc_variance(data, mean_val)
std_dev = math.sqrt(variance)
std_err = std_dev / math.sqrt(n)
random_error = t_student * std_err
total_error = math.sqrt(random_error**2 + (delta_prib / 3)**2)

print(f"Среднее T: {mean_val:.3f} мс")
print(f"Случайная погрешность: {random_error:.3f} мс")
print(f"Полная погрешность: {total_error:.3f} мс")
print(f"РЕЗУЛЬТАТ: T = ({mean_val:.2f} +- {total_error:.2f}) мс\n")



def gaussian(x, mu, sigma):
    return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma)**2)

x_gauss =[min(data) + i*(max(data)-min(data))/100.0 for i in range(101)]
y_gauss =[gaussian(x, mean_val, std_dev) for x in x_gauss]


plt.figure(figsize=(8, 5))
plt.plot(range(1, n+1), data, marker='o', linestyle='-', color='tab:blue', markersize=4)
plt.axhline(mean_val, color='black', linestyle='--', label=f'Среднее = {mean_val:.3f} мс')
plt.xlabel('Номер измерения, $N$', fontsize=12)
plt.ylabel('Период, $T$, мс', fontsize=12)
plt.title('Проверка на отсутствие дрейфа)')
plt.grid(True, linestyle=':')
plt.legend()
plt.savefig('drift.png', dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(data, bins=10, density=True, color='lightblue', edgecolor='black', alpha=0.7, label='Эксперимент')
plt.plot(x_gauss, y_gauss, color='darkblue', linewidth=2, label='Распределение Гаусса')
plt.xlabel('Период, $T$, мс', fontsize=12)
plt.ylabel('Плотность вероятности, $f(T)$', fontsize=12)
plt.title('Распределение результатов')
plt.legend()
plt.grid(True, linestyle=':')
plt.savefig('hist.png', dpi=300)
plt.close()

print("Графики сохранены: style1_drift.png, style1_hist.png")