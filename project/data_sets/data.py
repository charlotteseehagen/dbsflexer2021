import csv

def main():

    #DATA CLEANING-------------------------------------------------------------
    """
    Predefined data 
        -We dont need the indicator column
    """
    reader_gdp = csv.DictReader(open("gdp.csv", encoding='utf-8-sig'))
    reader_popgrowth= csv.DictReader(open("population_growth.csv", encoding='utf-8-sig'))
    reader_poptotal= csv.DictReader(open("population_total.csv", encoding='utf-8-sig'))
    reader_co2= csv.DictReader(open("co2_emission.csv", encoding='utf-8-sig'))
    reader_elec = csv.DictReader(open("electric_sources.csv"))

    #first place every reader object in a dictonary and clear unneccesary cols 
    dic_country = {'Country_Code' : [], 'Country_Name' : []}
      
    valid_codes= []
    valid_names= []
    # -> then make the country code the id
    #in gdp
    dic_gdp = {"Country_Code" : [], "Year" : [], "GDP" : []}

    for row in reader_gdp:
        row.pop("1960")
        row.pop("Indicator Name")
        row.pop("Indicator Code")

        if row["Country Code"] != "INX":
            dic_country["Country_Code"].append(row["Country Code"])
            valid_codes.append(row["Country Code"])
            valid_names.append(row["Country Name"])
            dic_country["Country_Name"].append(row["Country Name"])

            for k, v in row.items():

                if k == "Country Code":
                    dic_gdp["Country_Code"].append(v)

                elif k != "Country Code" and k != "Country Name":
                    dic_gdp["Year"].append(k)
                    dic_gdp["GDP"].append(v)


    """
    FIRST CSV-DUMP
    csv_file = "country_clean.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for cc, cn in zip(dic_country["Country_Code"], dic_country["Country_Name"]):
                writer.writerow([cc, cn])

    except IOError:
        print("I/O error")

    """
    dic_popg = {"Country_Code" : [], "Year" : [], "POP_growth" : []}
    #in population_growth
    for row in reader_popgrowth:
        row.pop("1960")
        row.pop("Indicator Name")
        row.pop("Indicator Code")

        if row["Country Code"] != "INX":

            for k, v in row.items():
                if k == "Country Code":
                    dic_popg["Country_Code"].append(v)

                elif k != "Country Code" and k != "Country Name":
                    dic_popg["Year"].append(k)
                    dic_popg["POP_growth"].append(v)

    dic_elec = {"Country_Code" : [], "Year": [], "ElectricSource" : []}

    """
    print(reader_elec.keys())
    for row in reader_elec:
        row.pop("1960")
        row.pop("Indicator Name")
        row.pop("Indicator Code")
        row.pop("Country Name")
        for k, v in row.items():
            if k == "Country Code":
                dic_elec["Country_Code"].append(v)
            elif k != "Country Code" and k != "Country Name":
                dic_elec["Year"].append(k)
                dic_elec["ElectricSource"].append(v)

            
    print(len(dic_elec["Country_Code"]))
    print(len(dic_popg["Country_Code"]))
    """

    test_dic = {"Country_Name" : [], "Country_Code" : [], "Year" : [], "Co2" : [], "Pop_total" : []}
    test_dic0 = {"Country_Name" : [], "Year" : [], "Pop_total" : []}
    #in population_total
    for row in reader_co2:
        if int(row["Year"]) > 1960 and row["Code"] in valid_codes:

            test_dic["Country_Name"].append(row["Entity"])
            test_dic["Country_Code"].append(row["Code"])
            test_dic["Year"].append(row["Year"])
            test_dic["Co2"].append(row["co2"])
    
    for row in reader_poptotal:
        if int(row["Year"]) > 1960 and row["Country Name"] in valid_names:
            test_dic0["Country_Name"].append(row["Country Name"])
            test_dic0["Year"].append(row["Year"])
            test_dic0["Pop_total"].append(row["Count"])

    for i in range(len(test_dic0["Country_Name"])):
        for j in range(len(test_dic["Country_Name"])):
            if test_dic["Country_Name"][j] == test_dic0["Country_Name"][i] and test_dic["Year"][j] == test_dic0["Year"][i]:
                test_dic["Pop_total"].append(test_dic0["Pop_total"][i])

    csv_file = "tmp_clean.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for cc, y, co, pt in zip(test_dic["Country_Code"], test_dic["Year"], test_dic["Co2"], test_dic["Pop_total"]):
                writer.writerow([cc, y, co, pt])

    except IOError:
        print("I/O error")



if __name__ == '__main__':


    main()

