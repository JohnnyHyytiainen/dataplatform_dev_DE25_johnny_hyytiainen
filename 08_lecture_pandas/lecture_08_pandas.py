# Lektion 8 Pandas
import pandas as pd

##################

# DataFrame (Table) Normala dataframes för att visa upp exemplet
product_df = pd.DataFrame(
    {
        "id": ["SKU-1", "SKU-2", "SKU-3", "SKU-4", "SKU-5"],
        "name": ["shoes", "pants", "shirts", "sweaters", "jackets"],
        "price": [700, 520, 315, 550, 1500],
        "currency": ["SEK", "SEK", "SEK", "SEK", "SEK"]


    }

)
print(f"{product_df}")
print("=================")
print("=================")
# ==========
# Helper Methods / Utility Methods (Pandas)
# ==========
print(product_df["price"].max())    # printar högsta värdet
print(product_df["price"].min())    # printar minsta värdet 
print(product_df["price"].mean())   # medelvärdet
print(product_df["price"].median()) # median värde
print(f"{product_df["price"].sort_values()}") # sorterar alla values 
print("=================")
print("=================")
print(product_df["price"].describe()) # visar statistiken över den numeriska datan
print("=================")
print("=================")


# if __name__ == "__main__":

