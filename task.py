import random
import time


def generate_random_array(size):
    return [random.randint(-10000, 10000) for _ in range(size)]


def method_1_sorting(arr):
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[5]


def method_2_top6_array(arr):

    top6 = sorted(arr[:6], reverse=True)

    for num in arr[6:]:
        if num > top6[-1]:
            for i in range(6):
                if num > top6[i]:
                    top6.insert(i, num)
                    top6.pop()
                    break
    return top6[5]

def method_3_find_max_6_times(arr):
    arr_copy = arr.copy()
    max_val = None
    for _ in range(6):
        max_val = max(arr_copy)
        idx = arr_copy.index(max_val)
        arr_copy[idx] = -10001
    return max_val


def run_benchmarks():
    sizes = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    methods = [
        ("Спосіб 1 (Сортування)", method_1_sorting),
        ("Спосіб 2 (Масив Top-6)", method_2_top6_array),
        ("Спосіб 3 (Пошук Max 6 разів)", method_3_find_max_6_times)
    ]

    print(
        f"{'Розмір вхідних даних':<22} | {'Спосіб 1 (Сортування)':<25} | {'Спосіб 2 (Масив)':<25} | {'Спосіб 3 (Максимальні елементи)':<30}")
    print("-" * 110)

    for size in sizes:
        data = generate_random_array(size)

        row_results = []
        for name, func in methods:
            times = []
            for _ in range(3):
                t_start = time.perf_counter()
                func(data)
                t_end = time.perf_counter()

                elapsed_ms = (t_end - t_start) * 1000
                times.append(elapsed_ms)

            avg_time = sum(times) / 3
            times_str = f"{avg_time:.2f} ({times[0]:.1f}, {times[1]:.1f}, {times[2]:.1f})"
            row_results.append(times_str)

        print(
            f"{size:<22,}".replace(',', ' ') + f" | {row_results[0]:<25} | {row_results[1]:<25} | {row_results[2]:<30}")


if __name__ == "__main__":
    run_benchmarks()