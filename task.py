import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def show_pie(ser):
    x = ser.tolist()
    labels = ser.keys().tolist()
    plt.pie(x = x, labels = labels, autopct = '%1.1f%%', shadow = False, startangle = 90)
    plt.axis('equal')
    plt.show()


# 查看不同借贷状态的数据量
def get_loan_status(df):
    loan_status = df['loan_status'].value_counts()
    print(loan_status)
    return loan_status


# 按月份统计贷款总量
def get_total_loan_by_month(df):
    df['issue_d'] = pd.to_datetime(df['issue_d']).dt.month
    month_group = df['loan_amnt'].groupby(df['issue_d'])
    total_loan_by_month = month_group.sum()
    print(total_loan_by_month)
    return total_loan_by_month


# 按地区（州）统计借贷金额总量
def get_total_loan_by_state(df):
    addr_state_group = df['loan_amnt'].groupby(df['addr_state'])
    total_loan_by_state = addr_state_group.sum()
    print(total_loan_by_state)
    return total_loan_by_state


# 借贷评级、期限和利率(默认实际利率)的关系分析
# int_rate  grade  term
def analysis(df):
    term = df['term'].tolist()
    int_rate = df['int_rate'].tolist()
    grade = df['grade'].tolist()
    colors = []
    for item in term:
        colors.append(int(item[:2]))
    # plt.xticks(np.arange(len(grade)), grade)
    plt.scatter(grade, int_rate, c = colors, alpha = 0.5)
    plt.savefig('test.png')
    plt.show()
    print(grade)
    print(term)
    print(int_rate)


# 借贷目的
def get_purpose(df):
    loan_purpose = df['purpose'].value_counts()
    print(loan_purpose)
    return loan_purpose


def main():
    df = pd.read_csv('loan.csv', low_memory = False)
    print('0:查看不同借贷状态的数据量')
    print('1:按月份统计贷款总量')
    print('2:按地区（州）统计借贷金额总量')
    print('3:借贷目的')
    print('4:借贷评级、期限和利率(默认实际利率)的关系分析')
    key = int(input('请输入数字：'))
    if key == 0:
        s = get_loan_status(df)
        show_pie(s)
    elif key == 1:
        s = get_total_loan_by_month(df)
        show_pie(s)
    elif key == 2:
        s = get_total_loan_by_state(df)
        show_pie(s)
    elif key == 3:
        s = get_purpose(df)
        show_pie(s)
    elif key == 4:
        analysis(df)
    else:
        print('invalid input')


if __name__ == '__main__':
    main()
