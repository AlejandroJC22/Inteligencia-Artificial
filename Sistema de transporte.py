import pandas as pd
import networkx as nx


# Definimos las conexiones entre estaciones con sus tiempos de viaje (en minutos)
data = {
    'Estaciones': ['Americas', 'Av. 68', 'Banderas', 'Caracas', 'Fontibon', 'Distrito grafiti', 'Esmeralda', 'Esperanza'],
    'Destinos': ['Esmeralda', 'Banderas', 'Caracas', 'Americas','Av. 68',  'Distrito grafiti',  'Esperanza', 'Fontibon'],
    'Tiempo_Viaje': [5, 10, 8, 7, 6, 4, 3, 9]  # tiempo de viaje en minutos
}

# Creamos el DataFrame
df = pd.DataFrame(data)

# Creamos un DataFrame para concatenar el tiempo al resultado
timedf = pd.DataFrame(data)
timedf['Tiempo_Viaje'] = timedf['Tiempo_Viaje'].astype(str) + ' minutos'

# Mostrar las rutas de transporte
print("\nMapa del sistema de transporte")
print(timedf.to_string(index=False))

# Crear un grafo desde el DataFrame
G = nx.from_pandas_edgelist(df, source='Estaciones', target='Destinos', edge_attr='Tiempo_Viaje')

# Definir el punto de inicio y el punto de destino
punto_inicio = 'Av. 68'
punto_destino = 'Esmeralda'

# Usar el algoritmo de Dijkstra para encontrar la mejor ruta (menor tiempo de viaje)
mejor_ruta = nx.dijkstra_path(G, source=punto_inicio, target=punto_destino, weight='Tiempo_Viaje')
mejor_tiempo = nx.dijkstra_path_length(G, source=punto_inicio, target=punto_destino, weight='Tiempo_Viaje')

print(f"\nComenzando en la estación {punto_inicio}, la mejor ruta es: \n")
for i in range(len(mejor_ruta) -1 ):
    estacion_a = mejor_ruta[i]
    proxima_estacion = mejor_ruta[i+1]

    print(f"De {estacion_a} tomar la estación {proxima_estacion}")

# Mostrar los resultados
print(f"\nEl tiempo total de viaje de {punto_inicio} hasta {punto_destino} es: {mejor_tiempo} minutos\n")
