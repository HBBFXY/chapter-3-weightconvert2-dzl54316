# 初始体重（单位：kg，可根据实际情况修改）
initial_weight = 60
# 每年体重增长（单位：kg）
yearly_gain = 0.5
# 月球重量是地球的比例
moon_ratio = 0.165

print("未来10年地球和月球体重变化：")
for year in range(1, 11):
    # 计算地球上的体重
    earth_weight = initial_weight + yearly_gain * year
    # 计算月球上的体重
    moon_weight = earth_weight * moon_ratio
    print(f"第{year}年：地球上体重 {earth_weight:.2f}kg，月球上体重 {moon_weight:.2f}kg")
