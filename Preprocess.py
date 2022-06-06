
model_gov = [{'128': 0,
  '131': 1,
  '200': 2,
  '316': 3,
  '318': 4,
  '320': 5,
  '325': 6,
  '520': 7,
  '523': 8,
  '525': 9,
  'A200': 10,
  'Accent': 11,
  'Avante': 12,
  'Aveo': 13,
  'C180': 14,
  'C200': 15,
  'Cruze': 16,
  'E200': 17,
  'Elantra': 18,
  'Excel': 19,
  'I10': 20,
  'Lanos': 21,
  'Matrix': 22,
  'Optra': 23,
  'Punto': 24,
  'Shahin': 25,
  'Tipo': 26,
  'Tucson': 27,
  'Uno': 28,
  'Verna': 29,
  'X1': 30,
  'X3': 31,
  'X6': 32},
 {'Alexandria': 0,
  'Aswan': 1,
  'Asyut': 2,
  'Beheira': 3,
  'Beni Suef': 4,
  'Cairo': 5,
  'Dakahlia': 6,
  'Damietta': 7,
  'Fayoum': 8,
  'Gharbia': 9,
  'Giza': 10,
  'Ismailia': 11,
  'Kafr al-Sheikh': 12,
  'Luxor': 13,
  'Matruh': 14,
  'Minya': 15,
  'Monufia': 16,
  'New Valley': 17,
  'Port Said': 18,
  'Qalyubia': 19,
  'Qena': 20,
  'Red Sea': 21,
  'Sharqia': 22,
  'Sohag': 23,
  'South Sinai': 24,
  'Suez': 25}]



def kilometer_frmt(kilometers):
    meters = {
        '100000 to 119999' : 10 ,
        '90000 to 99999' : 9, 
        '120000 to 139999' : 11,
        'More than 200000' : 15,
        '10000 to 19999' : 1, 
        '180000 to 199999' : 14,
        '140000 to 159999' : 12, 
        '160000 to 179999' : 13, 
        '20000 to 29999' : 2,
        '30000 to 39999' : 3, 
        '80000 to 89999' : 8, 
        '70000 to 79999' : 7, 
        '0 to 9999' : 0 ,
        '60000 to 69999' : 6, 
        '40000 to 49999' : 4, 
        '50000 to 59999' : 5
    }
    return meters[kilometers]


def color_frmt(color):
    colors = {
        'White' : 0,
        'Black' : 1, 
        'Silver' : 2,
        'Gray' : 3,
        'Red' : 4, 
        'Blue- Navy Blue' : 5, 
        'Other Color' : 6, 
        'Burgundy' : 7,
        'Green' : 8, 
        'Gold' : 9, 
        'Beige' : 10,
        'Brown' : 11,
        'Yellow' : 12,
        'Orange' :13
    }
    return colors[color]
    


def owner_frmt(year):
    if year > 2017 :
        return 1
    else:
        return 0
        


def engine_size(engine):
    if engine == 'More than 3000 CC':
        return 3.0
    elif engine == '1600 CC':
        return 1.6
    elif engine == '1400 - 1500 CC' :
        return 1.5
    elif engine == '1000 - 1300 CC':
        return 1.2
    elif engine  == '1800 - 2000 CC':
        return 2.0
    else:
        return 2.5



def fuel_type(fuel):
    if fuel == 'Benzine' :
        return 1
    else:
        return 0


def car_age (year):
    return(2022 - year)




model_ = model_gov[0]
gov_ = model_gov[1]
brand_ = {'Hyundai' : 0 , 'Fiat' :1 , 'Chevrolet' :2 , 'BMW' :3 , 'Mercedes-Benz':4}
body_={'Sedan' : 0 , 'Hatchback' :1 , 'SUV' :2 , 'Coupe' :3 , 'Cabriolet':4}


def transm(trans):
    return 1 if trans.lower().strip() == 'Automatic' else 0

def preprossecing(inputs):
    brand = brand_[inputs['Brand']]
    model = model_[inputs['Model']]
    body = body_[inputs['Body']]
    color = color_frmt(inputs['Color'])
    fuel = fuel_type(inputs['Fuel'])
    kilometer = kilometer_frmt(inputs['Kilometers'])
    engine = engine_size(inputs['Engine'])
    transmission = transm(inputs['Transmission'])
    gov = gov_[inputs['Gov']]
    owner = owner_frmt(inputs['Year'])
    age_car = car_age(inputs['Year'])
    
    final_data = [brand , model ,body , color , fuel , kilometer , engine , transmission , gov , owner , age_car ]
    return final_data