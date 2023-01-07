#Importamos las librerias 
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import pickle 



#Extraemos los archivos
mc = pd.read_csv('superstore_data.csv')

#Lo convertimos a un objeto data frame
df = pd.DataFrame(mc, columns= ['Id','Year_Birth','Education','Marital_Status','Income','Kidhome','Teenhome','Dt_Customer','Recency','MntWines'
,'MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds','NumDealsPurchases','NumWebPurchases','NumCatalogPurchases'
,'NumStorePurchases','NumWebVisitsMonth','Response','Complain'])



def main():
    st.title('Superstore Marketing Campaign')

    st.markdown('* **Datos optenidos de**: [Kaggle](https://www.kaggle.com/datasets/ahsan81/superstore-marketing-campaign-dataset?resource=download)  ')
    st.markdown("""  Acerca de la campaña:\n
Una gran tienda está planeando la venta de fin de año. Quieren lanzar una nueva oferta: membresía dorada,
que otorga un 20% de descuento en todas las compras, por solo $ 499, que es $ 999 en otros días. 
Será válido solo para clientes existentes y actualmente se está planificando la campaña a través de llamadas
telefónicas para ellos.La gerencia siente que la mejor manera de reducir el costo de la campaña es hacer
un modelo predictivo que clasifique a los clientes que podrían comprar la oferta. """)

    st.markdown(""" **Tabla de datos de los clientes**: """)
    st.dataframe(df)
    st.title(""" Regresion Logistica\n """)
    st.markdown(""" Para obtener los clientes que compren la membresía utilizaremos Regresión Logística, ya que este se adaptó mejor a los datos,
     la precisión del modelo es de un 85%. Se hicieron pruebas con otros algoritmos como regresión lineal, Naive Bayes y Support Vector Machine
      y se llego a la Conclusión  de que el mejor fue Regresión logística. \n""")
    st.markdown(""" Para Para mostrar la efectividad utilizaremos una matriz de confusión, en el siguiente ejemplo tendremos 448 datos entrenados  de los cuales 378 son ejemplos positivos que el modelo predice como positivos, 0 ejemplos negativos que el modelo predice como positivos, 70 ejemplos positivos que el modelo predice como negativos y 
0 ejemplos negativos que el modelo predice como negativos, Mostrando que el algoritmo se adaptó bien a los datos e hizo buenas predicciones con un 15% de error al clasificar a los clientes . """)
    st.image('Matriz.png')
    

    
    

if __name__ == '__main__':
    main()