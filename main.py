import csv



def write_csv(d):
    with open('cars.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow((d['brend'],
                        d['model'],
                        d['year']))


def main():
    car1 = {'brend': 'bmw', 'model': '540', 'year': 5}
    car2 = {'brend': 'audi', 'model': 's7', 'year': 2}
    car3 = {'brend': 'reno', 'model': 'p5', 'year': 8}

    cars = [car1, car2, car3]

    # for i in cars:
        # print(i)



if __name__ == '__main__':
    main()