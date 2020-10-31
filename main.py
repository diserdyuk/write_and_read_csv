import csv



def write_csv(d):    # var1 func.for write data to csv
    with open('cars.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow((d['brend'],
                        d['model'],
                        d['year']))


def write_csv2(d):    # var2 func.for write data to csv
    with open('cars2.csv', 'a') as f:
        order_rec = ['brend', 'model', 'year']
        write = csv.DictWriter(f, fieldnames=order_rec)    # dictwriter, class for write dictionary
        
        write.writerow(d)



def main():    # hub func.
    car1 = {'brend': 'bmw', 'model': '540', 'year': 2015}
    car2 = {'brend': 'audi', 'model': 's7', 'year': 2020}
    car3 = {'brend': 'reno', 'model': 'p5', 'year': 2018}

    cars = [car1, car2, car3]    # pack dict to one container

    # for i in cars:
        # write_csv2(i)

    # read var1
    with open('finance_yahoo.csv') as f:    # read file    
        orders = ['symbol', 'price', 'url']
        read = csv.DictReader(f, fieldnames=orders)

        for i in read:
            print(i)

    # read var2   
    '''
    with open('finance_yahoo.csv') as file:
        read = csv.reader(file)

        for i in read:
            print(i)
    '''



if __name__ == '__main__':
    main()