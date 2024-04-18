import pandas as pd
from  main import Scraper
# Define a list of product names to search for
products = [ "pantalla 4k","i5 12400"]

# Create a dictionary to store the results of each search
results = []
bestseller=[]
# Loop through each product in the list and search for it on a search engine
for index,product in enumerate(products):
    print(product)
    print(index)
    s2=Scraper()
    s2.menu(mode="Argentina")
    s2.scraping(product=product)
    s2.export_to_csv()

    df = pd.read_csv("C:/Users/Utilisateur/OneDrive/Escritorio/1mercado/data/mercadolibre_scraped_data.csv",delimiter=';')

    # Extract the column containing the buyer information (e.g., email address)
    
    results.append(df[['seller','post link']])
    #print(results)
    # Create a dictionary to keep track of how many products each buyer has
    product_counts = {}
    optionseller=[]
    
    # Check if 'title' is in df.columns before iterating over rows
    if index>0:
       #set1 = set((sell,link) for 
        print(type(results[index-1]['seller']))
        set1 = [set(results[index-1]['seller']), set(results[index-1]['post link'])]

        set2 = [set(results[index]['seller']), set(results[index]['post link'])]
        print(set1)
        print(set2)
        # Encontrar la intersección de los dos conjuntos
        interseccion = list(set1[0] & set2[0]) + list(set1[1] & set2[1])
        # Convertir la intersección a una lista
        bestseller = list(interseccion)
        print("bestseller:  ",bestseller)


print(bestseller)
'''
for product in products:
    if product in results: print(results[product])
print(*[results[i] for i in results])
'''