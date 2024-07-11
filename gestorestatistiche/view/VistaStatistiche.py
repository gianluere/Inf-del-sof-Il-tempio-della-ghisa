import matplotlib.pyplot as plt
import seaborn as sns

from gestorestatistiche.controller.ControlloreGestoreStatistiche import ControlloreGestoreStatistiche

controller = ControlloreGestoreStatistiche()

#define data
data = controller.get_ingressi()
labels = ['Con abbonamento', 'Senza abbonamento']

#define Seaborn color palette to use
colors = sns.color_palette('bright')[0:2]

#create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.show()