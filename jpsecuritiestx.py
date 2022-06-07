import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt


data = pd.read_csv("https://www.mof.go.jp/policy/international_policy/reference/itn_transactions_in_securities/montha1.csv", encoding='cp932', header=None)
data2 = pd.read_csv("https://www.mof.go.jp/policy/international_policy/reference/itn_transactions_in_securities/montha1.csv", encoding='cp932', header=None, index_col=0)
data

def main(AL, ADN, YEAR):
    num = data2.index.get_loc(YEAR)
    print(num)
    month = []
    x = []
    label = []
    for i in range(12):
        month.append(i+1)
        x.append(int(data.iloc[num+i, 3].replace(",", "")))
        label.append(data.iloc[num+i, 2])
    print(month, x, label)

    month = np.array(month)
    x = np.array(x)
    
    title = "Portfolio Investment "+AL+"  "+ADN+"  in "+YEAR
    plt.title(title)
    plt.xticks(month, label)
    plt.bar(month, x)

    plt.savefig('result.png')
    plt.show()


if len(sys.argv) == 4:
    first = ["Assets", "Liabilities"]
    second = ["Acquisition", "Disposition", "Net"]
    if sys.argv[1] in first:
        AL = sys.argv[1]
        if sys.argv[2] in second:
            ADN = sys.argv[2]
            if 2005 <= int(sys.argv[3]) <= 2022:
                YEAR = sys.argv[3]
                main(AL, ADN, YEAR)
            else:
                print('The input is different  "', sys.argv[3], '"')
                print('Please enter the year from 2005 to 2022')
        else:
            print('The input is different  "', sys.argv[2], '"')
            print('Please enter either Acquisition or Disposition or Net')
    else:
        print('The input is different  "', sys.argv[1], '"')
        print('Please enter either Assets or Liabilities')
else: 
    print('The number of inputs is different')
