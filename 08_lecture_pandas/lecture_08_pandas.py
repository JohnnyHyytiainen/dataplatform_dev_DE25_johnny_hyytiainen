# Lektion 8 Pandas
import pandas as pd



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
print(f"{"================="}\n")
# ==========
# Helper Methods / Utility Methods (Pandas)
# ==========
print(product_df["price"].max())    # printar högsta värdet
print(product_df["price"].min())    # printar minsta värdet 
print(product_df["price"].mean())   # medelvärdet
print(product_df["price"].median()) # median värde
print("=================")
print(product_df.sort_values("price")) # sorterar alla values. En quick sort
print("=================")
print(product_df.describe()) # visar numerisk statistik över min dataframe
print("=================")
print("=================")

# ==========
# to_* (For exporting files) <-- Utility Method
# ==========
# product_df.to_csv("products_lecture_08.csv", index=False) # Path är project folder by default

# ====================================
# ====================================
# Klass exempel, dirty dataframe
# ====================================
# ====================================

dirty_df = pd.DataFrame(
   {
       "id": [" sku-1 ", "SKU- 2", "Sku-3", "sku_4", "SKU5 "],
       "name": [" Shoes", "pants ", "SHIRTS", " SweaTers ", "designer  jacket"],
       "price": [" 760 ", "520", " 450", "550 ", " 4500"],
       "currency": [" sek", "SEK ", "Sek", "sek ", " SEK"],
   }
)

unclean = dirty_df
print(f"{unclean.values}\n")

# detta ersätter inte values i Series(columns) raden under kommer flagga för error direkt. Jag behöver peka på att det är en string
# dirty_df["id"].strip()

# Detta fungerar även för att göra ID och CURRENCY till UPPER
"""
cols_to_upper = ["id", "currency"]
dirty_df[cols_to_upper] = dirty_df[cols_to_upper].apply(lambda x: x.str.upper())
"""
dirty_df["id"] = dirty_df["id"].str.upper() # Gör det till stora bokstäver
dirty_df["id"] = dirty_df["id"].str.strip() # Trimmar whitespace till höger och vänster 
dirty_df["id"] = dirty_df["id"].str.replace(" ", "").str.replace("_", "-") # Danger zone. Med _ till - ändrar du data och inte städar den(TRANSFORMERAR)

# Price
dirty_df["price"] = dirty_df["price"].astype(float) # gör om str till float om det ska vara t.ex 550.90 SEK
dirty_df["price"] = dirty_df["price"].astype(int)   # är det inte någonting med ören eller decimaler så _BÖR_ det vara okej med konvertering till hela integers

# Name
dirty_df["name"] = dirty_df["name"].str.strip() # Trimmar whitespace till höger och vänster 
dirty_df["name"] = dirty_df["name"].str.title() # Varje ord blir en titel(Varje ord är capitalized)
dirty_df["name"] = dirty_df["name"].str.replace(r"\s+", " ", regex = True) # Regex

# Currency
dirty_df["currency"] = dirty_df["currency"].str.strip().str.upper()

print(f"{dirty_df.values} \n\n")




# ====================================
# ====================================
# Missing data
# ====================================
# ====================================
missing_df = pd.DataFrame(
   {
       "id": [" sku-1 ", "SKU- 2", None, "sku_4", "SKU5 "],
       "name": [" Shoes", None, "SHIRTS", " SweaTers ", "designer  jacket"],
       "price": [" 760 ", "520", None, "550 ", " 4500"],
       "currency": [" sek", "SEK ", "Sek", None, " SEK"],
   }
)

# isna() är ett tool(verktyg) för att identifiera avsaknad av värden. True = missing value.
# isna() = visar True vart någonstans du har saknad data. Alltså vad som som saknar värde.
print(f"{missing_df.isna()} \n")


# Att flagga för missing values hjälper till med att välja strategi senare. Hur du ska gå till väga dvs.
missing_df["id_missing"] = missing_df["id"].isna()
missing_df["name_missing"] = missing_df["name"].isna()
missing_df["price_missing"] = missing_df["price"].isna()
missing_df["currency_missing"] = missing_df["currency"].isna()
print(f"{missing_df} \n\n")

# DRY exempel med en for-loop istället för 4 rows med variabler
"""
mdf_values = ["id", "name", "price", "currency"]
for mdf in mdf_values:
    missing_df[mdf+"-missing"] = missing_df[mdf].isna()
print(f"{missing_df} \n\n")
"""

