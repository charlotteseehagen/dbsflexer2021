import csv
import time

def main():

    #DATA CLEANING-------------------------------------------------------------
    reader_gdp = csv.DictReader(open("gdp.csv", encoding='utf-8-sig'))
    reader_popgrowth= csv.DictReader(open("population_growth.csv", encoding='utf-8-sig'))
    reader_poptotal= csv.DictReader(open("population_total.csv", encoding='utf-8-sig'))
    reader_co2= csv.DictReader(open("co2_emission.csv", encoding='utf-8-sig'))
    reader_elec = csv.DictReader(open("electric_sources.csv",encoding='utf-8-sig'))

    start_0= time.time()
    print("Cleaning and Merging first half of our dataset")
    
    #first place every reader object in a dictonary and clear unneccesary cols 
    dic_country = {'Country_Code' : [], 'Country_Name' : []}
      
    valid_codes= []
    valid_names= []
    # -> then make the country code the id
    #in gdp
    dic_gdp = {"Country_Code" : [], "Year" : [], "GDP" : []}

    for row in reader_gdp:
        row.pop("1960")
        row.pop("2020")
        row.pop("Indicator Name")
        row.pop("Indicator Code")

        if row["Country Code"] != "INX":
            dic_country["Country_Code"].append(row["Country Code"])
            valid_codes.append(row["Country Code"])
            valid_names.append(row["Country Name"])
            dic_country["Country_Name"].append(row["Country Name"])

            for k, v in row.items():

                if k != "Country Code" and k != "Country Name":
                    dic_gdp["Country_Code"].append(row["Country Code"])
                    dic_gdp["Year"].append(k)
                    dic_gdp["GDP"].append(v)

    """
    FIRST CSV-DUMP
    csv_file = "country_clean.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, fieldnames=["Country_Code", "Country_Name"])
            for cc, cn in zip(dic_country["Country_Code"], dic_country["Country_Name"]):
                writer.writerow([cc, cn])

    except IOError:
        print("I/O error")

    """
    #in population_growth
    dic_popg = {"Country_Code" : [], "Year" : [], "POP_growth" : []}

    for row in reader_popgrowth:
        row.pop("1960")
        row.pop("Indicator Name")
        row.pop("Indicator Code")

        if row["Country Code"] != "INX":

            for k, v in row.items():

                if k != "Country Code" and k != "Country Name":
                    dic_popg["Country_Code"].append(row["Country Code"])
                    dic_popg["Year"].append(k)
                    dic_popg["POP_growth"].append(v)

    #in electric_sources
    dic_elec = {"Country_Code" : [], "Year": [], "ElectricSource" : []}

    for row in reader_elec:

        row.pop("1960")
        row.pop("2016")
        row.pop("2017")
        row.pop("2018")
        row.pop("2019")
        row.pop("2020")
        row.pop("Indicator Name")
        row.pop("Indicator Code")
        row.pop("Country Name")

        for k, v in row.items():

            if k != "Country Code" and k != "Country Name":
                dic_elec["Country_Code"].append(row["Country Code"])
                dic_elec["Year"].append(k)
                dic_elec["ElectricSource"].append(v)

    #First Half
    dic_part0 = {"Country_Code" : [], "Year" : [], "Pop_Growth" : [], "Gdp" : [], "Electric_Source" : []}

    #merge of first 3 dicts
    for i in range(len(dic_gdp["Country_Code"])):
        for j in range(len(dic_elec["Country_Code"])):

            if dic_gdp["Country_Code"][i] == dic_popg["Country_Code"][i] and \
                dic_gdp["Country_Code"][i] == dic_elec["Country_Code"][j] and \
                dic_gdp["Year"][i] == dic_popg["Year"][i] and \
                dic_gdp["Year"][i] == dic_elec["Year"][j]:

                    dic_part0["Country_Code"].append(dic_gdp["Country_Code"][i])
                    dic_part0["Year"].append(dic_gdp["Year"][i])
                    dic_part0["Gdp"].append(dic_gdp["GDP"][i])
                    dic_part0["Pop_Growth"].append(dic_popg["POP_growth"][i])
                    dic_part0["Electric_Source"].append(dic_elec["ElectricSource"][j])

    print("Done!")
    end_1 = time.time()
    print(f"Elapsed time for the first half: {end_1-start_0}")
    #in CO2 
    print("Cleaning and Merging second half of our dataset")
    start_1 = time.time()

    dic_co2 = {"Country_Name" : [], "Country_Code" : [], "Year" : [], "Co2" : []}

    for row in reader_co2:
        if int(row["Year"]) > 1960 and row["Entity"] in valid_names:
            dic_co2["Country_Name"].append(row["Entity"])
            dic_co2["Country_Code"].append(row["Code"])
            dic_co2["Year"].append(row["Year"])
            dic_co2["Co2"].append(row["co2"])
    
    #in population_total
    dic_poptotal = {"Country_Name" : [], "Year" : [], "Pop_total" : []}

    for row in reader_poptotal:
        if int(row["Year"]) > 1960 and row["Country Name"] in valid_names:
            dic_poptotal["Country_Name"].append(row["Country Name"])
            dic_poptotal["Year"].append(row["Year"])
            dic_poptotal["Pop_total"].append(row["Count"])

    #second half merge
    print("Second half merge starting ...")
    dic_part1= {"Country_Name" : [], "Country_Code" : [], "Year" : [], "Co2" : [], "Pop_total" : []}

    for i in range(len(dic_poptotal["Country_Name"])):
        for j in range(len(dic_co2["Country_Name"])):
            if dic_co2["Country_Name"][j] == dic_poptotal["Country_Name"][i] and dic_co2["Year"][j] == dic_poptotal["Year"][i]:
                dic_part1["Country_Name"].append(dic_co2["Country_Name"][j])
                dic_part1["Country_Code"].append(dic_co2["Country_Code"][j])
                dic_part1["Year"].append(dic_co2["Year"][j])
                dic_part1["Co2"].append(dic_co2["Co2"][j])
                dic_part1["Pop_total"].append(dic_poptotal["Pop_total"][i])
                
    end_2 = time.time()
    print(f"Elapsed time for the second half: {end_2-start_1}")


    #FULL MERGE 
    print("FULL MERGE STARTING ...")
    dic_FULL = {"Country_Code" : [], "Country_Name" : [], "Year" : [], "Co2(tonnes)" : [], \
                "Gdp(USD)" : [], "Pop_rel": [], "Pop_tot": [], "Electric_Source(Kwh)" : []}

    for i in range(len(dic_part0["Country_Code"])):
        for j in range(len(dic_part1["Country_Code"])):
            if dic_part0["Country_Code"][i] == dic_part1["Country_Code"][j] and \
               dic_part0["Year"][i] == dic_part1["Year"][j]:
                   dic_FULL["Country_Code"].append(dic_part1["Country_Code"][j])
                   dic_FULL["Country_Name"].append(dic_part1["Country_Name"][j])
                   dic_FULL["Year"].append(dic_part1["Year"][j])
                   dic_FULL["Co2(tonnes)"].append(dic_part1["Co2"][j])
                   dic_FULL["Gdp(USD)"].append(dic_part0["Gdp"][i])
                   dic_FULL["Pop_rel"].append(dic_part0["Pop_Growth"][i])
                   dic_FULL["Pop_tot"].append(dic_part1["Pop_total"][j])
                   dic_FULL["Electric_Source(Kwh)"].append(dic_part0["Electric_Source"][i])


    print("DONE")
    end_0 = time.time()
    print(f"Total elpased time: {end_0-start_0}")

    csv_file = "data_clean.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for cc, ye, co, gd, pr, pt, es in zip( \
                   dic_FULL["Country_Code"], dic_FULL["Year"], dic_FULL["Co2(tonnes)"],\
                   dic_FULL["Gdp(USD)"], dic_FULL["Pop_rel"], dic_FULL["Pop_tot"], dic_FULL["Electric_Source(Kwh)"]):
                writer.writerow([cc, ye, co, gd, pr, pt , es])

    except IOError:
        print("I/O error")



if __name__ == '__main__':


    main()

