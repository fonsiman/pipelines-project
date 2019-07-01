from matplotlib import pyplot as plt
import numpy as np

def drawPlot(df, df_fund):
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax.bar(df_fund["mediumdate"], df_fund["resultado_consolidado"], width = 80, color=(190/255,190/255,190/255,0.7), label='Resultado consolidado')
    ax2.plot(df["fecha"], df["precio"], color='b', label='Cotización')
    ax.set_xticklabels(df["fecha"])
    plt.title("Cotización ENCE",size=12,fontweight='bold')
    plt.yticks(np.arange(df["precio"].min(), df["precio"].max(),  round((df["precio"].max()-df["precio"].min())/25,1) ))
    plt.show()

    plt.savefig('foo.png')