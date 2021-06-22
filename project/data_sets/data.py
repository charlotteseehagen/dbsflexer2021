import sys
import csv

#calls function and generates input
def main():

    if len(sys.argv) == 1:
        print("You gotta give the script some cli-params, maybe myfile.csv?")

    inputfiles = sys.argv
    raw_data = []                   #raw unfiltered data
    print(inputfiles[1])
    
    #read file via commandline argument and get some rows
    for i in range(1, len(inputfiles)):
        with open(inputfiles[i], mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are: {", ".join(row)}')
                    line_count += 1
                    raw_data.append(row)
                            
                else:
                    raw_data.append(row)
                    line_count += 1
            print(f'Processed {line_count} lines.')
            

    #print(raw_data)

    for file in inputfiles:
        if file == "gdp.csv":
            for i in range(1, len(raw_data)):
                del raw_data[i][2:4]
                del raw_data[i][-1]
                
        if file == "population_growth.csv":
            for i in range(1, len(raw_data)):
                del raw_data[i][1:5]
                del raw_data[i][-1]
                                
        if file == "population_total.csv":
            for i in range(1, len(raw_data)):
                if raw_data[i][1] == '1960':
                    del raw_data[i][0:3]
                print(raw_data[i])
                

    
if __name__ == '__main__':


    main()

