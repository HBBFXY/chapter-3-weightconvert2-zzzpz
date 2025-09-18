def main():
    initial_weight = 60.0
    print("年份\t地球体重(kg)\t月球体重(kg)")
    for year in range(10):
        earth_weight = initial_weight + 0.5 * year
        moon_weight = earth_weight * 0.165
        print(f"{year}\t{earth_weight:.1f}\t\t{moon_weight:.3f}")

if __name__ == "__main__":
    main()
