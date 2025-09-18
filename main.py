def calculate_weight_changes(initial_weight_earth):
    MOON_GRAVITY_RATIO = 0.165
    YEARLY_GAIN = 0.5
    results = []
    for year in range(11):
        earth_weight = initial_weight_earth + YEARLY_GAIN * year
        moon_weight = earth_weight * MOON_GRAVITY_RATIO
        results.append((year, earth_weight, moon_weight))    
    return results
def main():
    try:
        current_weight = float(input("请输入您当前的体重(kg): "))
    except ValueError:
        print("输入错误，请输入有效的数字。")
        return
    weight_data = calculate_weight_changes(current_weight)
    print("\n未来10年体重变化预测（每年增长0.5kg）")
    print("年份\t地球体重(kg)\t月球体重(kg)")
    print("-" * 40)
    for year, earth, moon in weight_data:
        print(f"{year}\t{earth:.2f}\t\t{moon:.2f}")
if __name__ == "__main__":
    main()
