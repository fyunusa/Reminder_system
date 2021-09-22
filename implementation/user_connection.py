import pymysql
#-----------------------------------------------------------#

def database_connect():
    connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='reminder_system',
    )
#-----------------------------------------------------------#
    users_Fname = 'farouk'
    users_Sname = 'yunusa'
    users_School = 'ui'
    users_Email =  'fyunu'
    users_Faculty = 'sci'
    users_Department = 'csc'
    users_username = 'umarfarouk'
    # users_password1 = self.ids.password1.text
    users_password2 = 'faroukclaire'
# #-----------------------------------------------------------#
    mycursor = connection.cursor()
#-----------------------------------------------------------#
    query1 = "INSERT INTO user_details(FirstName,Surname,School,email,Faculty,Department) VALUES (%s,%s,%s,%s,%s,%s)"
    vl = (users_Fname,users_Sname,users_School,users_Email,users_Faculty,users_Department)
#-----------------------------------------------------------#
    # query1 = "INSERT INTO user_credentials(username,password) VALUES (%s,%s)"
    # vl = (users_username,users_password2)
#-----------------------------------------------------------#
    mycursor.execute(query1,vl)
    connection.commit()
    print('data uploaded successfully')
    connection.close()

if __name__ == '__main__':
    database_connect()