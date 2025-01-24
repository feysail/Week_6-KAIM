import matplotlib.pyplot as plt
import seaborn as sns
def histogram(data):
    column=data.describe().columns.to_list()
    fig,axes=plt.subplots(2,2,figsize=(10,8))
    axes=axes.flatten()
    for i,col in enumerate(column):
      axes[i-1].hist(data[col])
      axes[i-1].set_title(col)
        
        



    