def calculate_miss(x, y, z, n):
    xn_yn = x**n + y**n
    zn = z**n
    znp1 = (z+1)**n
    miss = min(abs(xn_yn - zn), abs(znp1 - xn_yn))
    relative_miss = (miss / xn_yn) * 100
    return xn_yn, zn, miss, relative_miss


def find_near_misses(n, k):
    smallest_relative_miss = float('inf')
    best_x, best_y, best_z = None, None, None

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            for z in range(max(x, y) + 1, k + 1):
                xn_yn, zn, miss, relative_miss = calculate_miss(x, y, z, n)
                
                if relative_miss < smallest_relative_miss:
                    smallest_relative_miss = relative_miss
                    best_x, best_y, best_z = x, y, z
                    best_miss, best_relative_miss = miss, relative_miss

    print(f"Best Near Miss (for n={n}):")
    print(f"----------------------------------------")
    print(f"x = {best_x}, y = {best_y}, z = {best_z}")
    print(f"(x^n + y^n) = {best_x**n} + {best_y**n} = {best_x**n + best_y**n}")
    print(f"z^n = {best_z**n}")
    print(f"Miss = {best_miss}")
    print(f"Relative Miss = {best_relative_miss:.6f}%")


def main():
    n = int(input("Enter the value of n (2 < n < 12): "))
    k = int(input("Enter the value of k (k > 10): "))

    if 2 < n < 12 and k > 10:
        find_near_misses(n, k)
    else:
        print("Invalid input. Please ensure 2 < n < 12 and k > 10.")


if __name__ == "__main__":
    main()
