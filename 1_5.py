
income = int(input('введите прибыль: '))
outgoings = int(input('введите расходы: '))

profit = income - outgoings

profitability = profit / income * 100

print(f' рентабельность палатки шаурмы составила {profitability:.1f}%')

num_staff = int(input('enter number of staff: '))

profit_per_staff = profit / num_staff

print(f'прибыль на одного сотрудника составила {profit_per_staff:.1f} рублей')