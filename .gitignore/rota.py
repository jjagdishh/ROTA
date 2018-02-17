def main():
    import pandas as pd
    import numpy as np
    import numpy.core._methods
    import numpy.lib.format
    from bs4 import BeautifulSoup
    import lxml
    import urllib.request
    from urllib.request import urlopen
    import csv
    print("       Welcome to my tool \n       This is an tool to calculate the Out Of office Hours duties for any GROUP !! ")
    print("url Hint: 'file:///D:/userdata/jmathpal/Desktop/Schedule.cgi'")
    url = input("Please enter the URL:")
    page = urlopen(url)
    soup = BeautifulSoup(page, 'lxml')  # Parse the html in the 'page' variable, and store it in Beautiful Soup format
    table = soup.find('table')

    # month = input("Please enter the month (Format - 'January : ")
    # year = input("Please enter the Year (Format - '2018 : ")
    month_year = input("Please enter the month (Format - 'January 2018: ")

    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]

    for row in table.findAll("tr"):
        cells = row.findAll('td')
    #    states=row.findAll('th') #To store second column data
        if len(cells)==6: #Only extract table body not heading
            A.append(cells[0].find(text=True))
    #        B.append(cells[0].find(text=True))
            C.append(cells[1].find(text=True))
            D.append(cells[2].find(text=True))
            E.append(cells[3].find(text=True))
            F.append(cells[4].find(text=True))
            G.append(cells[5].find(text=True))


    df=pd.DataFrame(A,columns=['date'])
    #df['Date']=B
    df['Day']=C
    df['In_Hour']=D
    df["A"] = 1
    #df['In_Hour-2']=E
    df['Out_Hour']=F
    df["B"] = 1

    df.head()

    #df.to_csv('C:/R/Rota.csv') # if you want to save the data in CSV format

    ######Calculating the data

    from collections import defaultdict

    #df = pd.read_csv('C:/R/Rota.csv','w',skipinitialspace=True) # Import the file if it is saved in local directory

    #Note: here we are now filtering the data Month vise

    df = df[df.date.str.endswith(month_year)] # in date column we are checking for the string ends with like "January 2018"

    df1=df[df["Day"].isin(['Sat','Sun'])]
    df2=df[df["Day"].isin(['Mon','Tue','Wed','Thu','Fri'])]


   # !!! Note We need to enter the Holiday list which are only held in a Week Day !!!
    holiday=df[df["date"].isin(['1 January 2018','26 January 2018','2 March 2018','30 March 2018','15 August 2018','22 August 2018',
               '2 October 2018','19 October 2018', '7 November 2018','8 November 2018','9 November 2018','25 December 2018'])]
    # !!! Note We need to enter the Holiday list which are only held in a Week Day !!!

    def main1():
        name= input("Please Enter the Name of Employee: ")
        df3=df1[df1["In_Hour"].isin([name])]
        week_end_1 = (df3.In_Hour.count())
        df4=df1[df1["Out_Hour"].isin([name])]
        week_end_2= (df4.Out_Hour.count())
        df5 =df2[df2["Out_Hour"].isin([name])]
        week_day_count = (df5.Out_Hour.count())
        df6 =holiday[holiday["In_Hour"].isin([name])]
        h1 = (df6.In_Hour.count())
        df7 =holiday[holiday["Out_Hour"].isin([name])]
        h2 = (df7.Out_Hour.count())
        OOH = (week_end_1 + week_end_2) / 2 + (week_day_count - (h2)) + (h1 / 2) + (h2 / 2)
        output = "%s Out Of Hour Count is %r" % (name,OOH)
        print(output)
        # Now I am Restarting my Program as per user wish if he/she again want to run the program
        # for this we need to define this complete program under def main(): -- main().

        restart=input("Do You want to OOH for next Employee ? : ").lower()
        if restart == 'yes':
            main1()
        elif restart == 'y':
            main1()
        else:
            main()
    main1()
main()
