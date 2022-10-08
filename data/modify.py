import pandas as pd
import pycountry_convert as pc


world_happiness = pd.read_csv("./world_happiness_report_2019.csv")

world_happiness["Continent"] = ""
cont = world_happiness["Country or region"]
for index in range(len(cont)):
    try:
        continent_name = pc.convert_continent_code_to_continent_name(pc.country_alpha2_to_continent_code(pc.country_name_to_country_alpha2(cont[index])))
    except KeyError:
        continent_name = "Others"
    finally:
        world_happiness["Continent"][index] = continent_name

world_happiness.to_csv("world_happiness_report_clean_2019.csv", encoding="utf-8", index=False)