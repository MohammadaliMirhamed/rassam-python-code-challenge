
from itertools import count
from time import sleep
from boot.config import db

text = ""
while text != '3':
    
    text = input("select by number: \n1. insert to DB \n2. show number of people per Sex of the given native-country \n3. exit \n\n#enter number : ")

    if text == '1':

        # show message that which menu user has selected
        print("\nyou chose -> insert to DB\n")

        # sql query for insert data to DB
        sql = "INSERT INTO people (age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country, salary, persian_native_country) VALUES ("
        
        # columns for making input box
        columns = ['age' ,'workclass','fnlwgt ','education','education_num ','marital_status','occupation','relationship','race','sex','capital_gain ','capital_loss ','hours_per_week ','native_country','salary','persian_native_country']

        # a loop for get data from user
        for i in range(0, 16):
            sql += "'" + input("enter value for column " + columns[i] + ": ") + "', "
        sql = sql[:-2] + ");"
        
        # execute query
        db.execute_query(sql, "write")
        
        # show message that query was successful
        print("\nrecord has been add\n")
        
    elif text == '2':
        # show message to user that which menu has selected
        print("\nyou chose -> show number of people per Sex of the given native-country\n")

        # input for which type of country user wants to search
        countery_type = input('select a number : \n1. english country name \n2. persian country name \n\n#enter number : ')
        countery_type = 'native_country' if countery_type == '1' else 'persian_native_country'

        # get the name from user
        countery_name = input('\nnow ,please enter the name of your country , like  United-States\n\n enter here : ')

        # execute query
        res = db.execute_query("select count(id) as count_of_people ,sex  from people where %s = '%s' group by sex" % (countery_type , countery_name), "read")
        
        # print message
        print('\nstatistics in ' + countery_name + ' : \n\n')

        # print result 
        for row in res:
            print("\ncount of peple : " + str(row['count_of_people']) + '   sex : ' + row['sex'] + '\n')
        sleep(3);

    elif text == '3':
        print("\nyou chose -> exit\n")
    else:
        print("wrong number")
    