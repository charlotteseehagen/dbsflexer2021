import sys
import csv

#calls function and generates input
def main():

    if len(sys.argv) == 1:
        print("You gotta give the script some cli-params, maybe myfile.csv?")

    inputfile = str(sys.argv[1])
    raw_data = []                   #raw unfiltered data

    #read file via commandline argument and get some rows
    with open(inputfile, mode='r') as csv_file:
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



if __name__ == '__main__':


    main()
