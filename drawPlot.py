from matplotlib import pyplot as plt
import numpy as np

def drawPlot(df, df_fund, query, data_plot):

    if data_plot == "resultado":
        s_arg = df_fund["resultado_consolidado"]
    elif data_plot == "bpa":
        s_arg = df_fund["bpa_basico"]
    elif data_plot == "activos":
        s_arg = df_fund["activo"]
    else:
        s_arg = df_fund["plantilla"]

    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax.bar(df_fund["mediumdate"], s_arg, width = 80, color=(190/255,190/255,190/255,0.7), label='Resultado consolidado')
    ax2.plot(df["fecha"], df["precio"], color='b', label='Cotización')
    ax.set_xticklabels(df["fecha"])
    plt.title("Cotización {} vs {}".format(query, data_plot.capitalize()),size=12,fontweight='bold')
    plt.yticks(np.arange(df["precio"].min(), df["precio"].max(),  round((df["precio"].max()-df["precio"].min())/25,1) ))
    
    plt.savefig('{}-{}.png'.format(query,data_plot))

    return '{}-{}.png'.format(query,data_plot)