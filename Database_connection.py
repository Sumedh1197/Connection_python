class database:
    from sqlalchemy import create_engine 
    import pandas as pd

    engine = create_engine('mysql://username:password@hostname/database_name')

     #to get list of table_names 
    table_names= engine.table_names()
    print(table_names)

     #open connection 
    mySQLcon= engine.connect()
     #executing queries 
    query1= mySQLcon.execute('SELECT * FROM employees LIMIT 5')
    query2= mySQLcon.execute('SELECT * FROM dept_emp' )

     #saving result to data frame
    df1= pd.DataFrame(query1.fetchall())
    df2= pd.DataFrame(query2.fetchall())

    #Setting data frame column names to corresponding table column names 
    df1.columns= query1.keys()
    df2.columns= query2.keys()

    #closing connection 
    mySQLcon.close()

    #Printing result 
    print(df1.head())
    print(df2.head())

