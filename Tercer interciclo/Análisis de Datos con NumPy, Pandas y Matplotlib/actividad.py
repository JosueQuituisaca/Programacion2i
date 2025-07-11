import pandas as pd

# Cargar el archivo Excel desde la misma carpeta
file_path = 'Libro1.xlsx'

# Cargar el archivo Excel
df = pd.read_excel(file_path, sheet_name='Hoja1')

# Filtrar los datos para los clientes específicos mencionados
clientes_ids = [201006654366, 200000396834, 200000399374, 200000521415, 200000561577]
df_clientes = df[df['Codigo del Cliente'].isin(clientes_ids)]

# Definir las columnas de consumo para cada año
cols_2023 = [
    'feb 02- ene 01 (kWh/mes)', 'mar 03 - feb 02 (Kwh/mes)', 'abril 04 - mar 03 (kwh/mes)',
    'may 05 - abril 04 (kwh/mes)', 'jun 06 - may 05(kwh/mes)', 'juli 07 - jun 06(kwh/mes)',
    'agos 08 - juli 07(kwh/mes)', 'sep 09 - agos 08(kwh/mes)', 'oct 10 - sep 09(kwh/mes)',
    'nov 11 - oct 10(kwh/mes)', 'dic 12 - nov 11(kwh/mes)'
]
cols_2024 = [
    'feb 02- ene 01(kwh/mes)', 'mar 03 - feb 02(kwh/mes)', 'abril 04 - mar 03(Kwh/mes)',
    'may 05 - abril 04 (kwh/mes).1', 'jun 06 - may 05(kwh/mes).1', 'juli 07 - jun 06(kwh/mes).1',
    'agos 08 - juli 07(kwh/mes).1', 'sep 09 - agos 08(kwh/mes).1', 'oct 10 - sep 09(kwh/mes).1',
    'nov 11 - oct 10(kwh/mes).1', 'dic 12 - nov 11(kwh/mes).1'
]
cols_2025 = [
    ' feb 02- ene 01(kwh/mes)', 'mar 03 - feb 02(kwh/mes).1', ' abril 04 - mar 03(kwh/mes)',
    'may 05 - abril 04 (kwh/mes).2'
]

# Calcular el promedio anual para cada año
df_clientes_anos = pd.DataFrame({
    'Codigo del Cliente': df_clientes['Codigo del Cliente'],
    'AÑO 2023': df_clientes[cols_2023].mean(axis=1),
    'AÑO 2024': df_clientes[cols_2024].mean(axis=1),
    'AÑO 2025': df_clientes[cols_2025].mean(axis=1)
})
