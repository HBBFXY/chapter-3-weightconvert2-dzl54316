initial_weight = float(input("请输入您在的球上的初始体重："))
for year in range(1,11):
    earth_weigh = initial_weight + year * 0.5
    moon_weight = earth_weigh * 0.165
    print(f"第{year}年，地球上的体重：{earth_weigh:.2f} 公斤，月球上的体重：{moon_weight:.2f}")
