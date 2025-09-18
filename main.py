def main():
    initial_weight = 60.0
    MOON_GRAVITY_RATIO = 0.165
    YEARLY_GAIN = 0.5
    print("Year\tEarth (kg)\tMoon (kg)")
    for year in range(11):  # 0到10年
        earth_weight = initial_weight + YEARLY_GAIN * year
        moon_weight = earth_weight * MOON_GRAVITY_RATIO
        print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
if __name__ == "__main__":
    main()
