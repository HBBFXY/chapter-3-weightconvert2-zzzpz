def main():
    initial_weight = 60.0
    print("Year\tEarth(kg)\tMoon(kg)")
    for year in range(10):  # 0到9年，共10年
        earth_weight = initial_weight + 0.5 * year
        moon_weight = earth_weight * 0.165
        print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
if __name__ == "__main__":
    main()
