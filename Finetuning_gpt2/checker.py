import pandas as pd

path = 'final_csv_data/train_original.csv'
df = pd.read_csv(path)

contr_sum = df['gold_label'].sum()
total = len(df)
print('total num of rows: {}'.format(total))
print('contr_sum: {}'.format(contr_sum))
contr_per = round((contr_sum/total)*100, 2)

print('persent of contr_sum: {}'.format(contr_per))

print('non_contr_sum: {}'.format((total-contr_sum)))





