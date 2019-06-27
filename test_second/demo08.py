import pandas as pd
import matplotlib.pyplot as plt

# import seaborn as sb
#
# df = sb.get_dataset_names('tips')

df = pd.read_csv('../data/tips.csv')


plt.rcParams['font.sans-serif']=['SimHei']

ManTip = df[df['sex'] == 'Male']['tip'].mean()
WomenTip = df[df['sex'] == 'Female']['tip'].mean()

plt.bar(['male', 'female'], [ManTip, WomenTip], width=0.5, color='#000000')

plt.title('男女小费柱状图')

plt.show()