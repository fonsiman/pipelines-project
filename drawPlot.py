from matplotlib import pyplot as plt
import numpy as np
import matplotlib.dates as dates

def drawPlot(df, df_fund, query, data_plot):

    if data_plot == "resultado":
        s_arg = df_fund["Resultado"]
    elif data_plot == "bpa":
        s_arg = df_fund["BPA"]
    elif data_plot == "activos":
        s_arg = df_fund["Activo"]
    else:
        s_arg = df_fund["Plantilla"]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax2 = ax.twinx()
    ax.bar(df_fund["mediumdate"], s_arg, width = 80, color=(190/255,190/255,190/255,0.7), label='s_arg')
    ax2.plot(df["fecha"], df["precio"], color='b', label='Cotización')
    ax.set_xticklabels(df["fecha"])
    fig.autofmt_xdate()
    ax2.xaxis.set_minor_locator(dates.MonthLocator(interval=1))  
    ax2.xaxis.set_minor_formatter(dates.DateFormatter('%m-%Y')) 
    plt.title("Cotización {} vs {}".format(df_fund["company"][0], data_plot.capitalize()),size=12,fontweight='bold')
    plt.yticks(np.arange(df["precio"].min(), df["precio"].max(),  round((df["precio"].max()-df["precio"].min())/25,1) ))

    df2 = df_fund.groupby(['year', 'semestre'])['EBITDA','EBIT',"Resultado", "BPA"].sum()
    df2['EBITDA']=df2['EBITDA'].apply(lambda x: "{} M".format(round(float(x)/1000000)))
    df2['EBIT']=df2['EBIT'].apply(lambda x: "{} M".format(round(float(x)/1000000)))
    df2['Resultado']=df2['Resultado'].apply(lambda x: "{} M".format(round(float(x)/1000000)))
    df2=df2.transpose()

    df3 = df_fund.groupby(['year', 'semestre'])['Activo','Pasivo',"PN"].sum()
    df3['Activo']=df3['Activo'].apply(lambda x: "{} M".format(round(float(x)/1000000)))
    df3['Pasivo']=df3['Pasivo'].apply(lambda x: "{} M".format(round(float(x)/1000000)))
    df3['PN']=df3['PN'].apply(lambda x: "{} MM".format(round(float(x)/1000000000000)))
    df3=df3.transpose()

    df4 = df_fund.groupby(['year', 'semestre'])['Plantilla','Hombres',"Mujeres"].sum().transpose()

    plt.savefig('./outputs/{}-{}-plot.png'.format(query,data_plot))

    plt.clf()
    
    fig2, table1 = plt.subplots(figsize=(8, 3))
    fig2.patch.set_visible(False)
    
    table1.axis('off')
    table1.axis('tight')
    the_table = table1.table(cellText=df2.values, rowLabels=df2.index ,colLabels=df2.columns, loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    #plt.title("Cuenta de resultados",size=12,fontweight='bold')

    plt.savefig('./outputs/{}-{}-resultados.png'.format(query,data_plot))

    plt.clf()

    fig2, table2 = plt.subplots(figsize=(8, 3))
    fig2.patch.set_visible(False)
        
    table2.axis('off')
    table2.axis('tight')
    the_table2 = table2.table(cellText=df3.values, rowLabels=df3.index ,colLabels=df3.columns, loc='center')
    the_table2.auto_set_font_size(False)
    the_table2.set_fontsize(8)
    #plt.title("Balance",size=12,fontweight='bold')
 
    plt.savefig('./outputs/{}-{}-balance.png'.format(query,data_plot))

    plt.clf()

    fig2, table3 = plt.subplots(figsize=(8, 3))
    fig2.patch.set_visible(False)

    table3.axis('off')
    table3.axis('tight')
    the_table3 = table3.table(cellText=df4.values, rowLabels=df4.index ,colLabels=df4.columns, loc='center')
    the_table3.auto_set_font_size(False)
    the_table3.set_fontsize(8)
    #plt.title("Plantilla",size=12,fontweight='bold')
 
    plt.savefig('./outputs/{}-{}-plantilla.png'.format(query,data_plot))

    plt.clf()

    return '{}-{}'.format(query,data_plot)