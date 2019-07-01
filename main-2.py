import os
import downloadDataset as dd
import unzip
import findticker
import cleanDataset
import readAPI
import drawPlot
import getQuery
import sendMail

# Pedimos por terminal el nombre de la empresa
query, data_plot = getQuery.getQuery()

# Descargamos el dataset. El wifi de Ironhack es un poco lento y suele tardar...
pg = dd.PageGetter('firefox')
soup = pg.getPage("https://www.cnmv.es/ipps/default.aspx", query)
pg.close()

# Descomprimimos los archivos descargados
path = unzip.unzip(query)
f_data = sorted(os.listdir(path))

# Limpieza de datos. Obtenemos los datos que nos interesan de los xblr descargados
df_fund = cleanDataset.clean(f_data, path)

# Obtén datos de cotización de la API
df = readAPI.read_api(query)

# Crea los gráficos
img_file = drawPlot.drawPlot(df, df_fund, query, data_plot)

# Enviamos un correo electrónico
sendMail.sendMail(img_file)