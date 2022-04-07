total_cost = float(input())         # total_cost为当前房价
annual_salary = float(input())        # 年薪
portion_saved = float(input()) / 100        # 月存款比例，输入30转为0.30（即30%）
semi_annual_raise = float(input()) /100     # 输入每半年加薪比例，输入7转化为0.07（即7%）
portion_down_payment = 0.3      # 首付比例，浮点数

# 根据首付款比例计算首付款down_payment
down_payment = total_cost * portion_down_payment
print('首付',down_payment)



current_savings = 0     # 存款金额，从0开始
number_of_months = 0
monthly_salary = annual_salary / 12     #月工资
monthly_deposit = monthly_salary * portion_saved    # 月存款

# 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
# 每6个月涨一次工资，每年输出年底的存款总额
#每12个月输出一次存款，保留0位小数，使用千分符
while current_savings < down_payment:
    current_savings += monthly_deposit
    number_of_months += 1
    if number_of_months % 6 == 0:
        monthly_deposit += monthly_deposit * semi_annual_raise
    if number_of_months % 12 == 0:
        print("第{}个月月末有{:,.0f}元存款".format(number_of_months, current_savings))

print(f'需要{number_of_months}个月可以存够首付')
