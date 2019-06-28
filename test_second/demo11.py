import pandas as pd
import matplotlib.pyplot as plt

# import seaborn as sb
#
# df = sb.get_dataset_names('tips')

df = pd.read_csv('../data/house.csv')

plt.rcParams['font.sans-serif']=['SimHei']

plt.scatter(df['area'], df['price'])
plt.xlabel('消费')
plt.ylabel('小费')

plt.title('消费与小费的散点图')

plt.show()