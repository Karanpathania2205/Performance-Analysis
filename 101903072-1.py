try:
    import sys 
    import pandas as pd
    import numpy as np 
    import matplotlib.pyplot as plt 
    n = len(sys.argv)
    if 'input.csv' not in sys.argv :
        raise ValueError("Input.csv file has not been found")
    if n>2 or n<=1:
        raise ValueError("Kindly provide the input in the correct format which is {python <program.py> <InputDataFile>}")
    #print("Total arguments passed:", n)
    #print("\nName of Python script:", sys.argv[1])
    # if n==2 and sys.argv[1]!='input.csv':
    #     raise ValueError("The csv file provided does not have the correct name")
    else:
       data=pd.read_csv(sys.argv[1]) 
       if data.shape[1]!=3:
           raise ValueError("The input provided does not have 3 Coloumns")
except ValueError as ve:
    f = open("101903072-log.txt", "a")
    f.write(str(ve))
    f.write("\n")
    f.close()
except FileNotFoundError as fnfe:
    file = open("101903072-log.txt", "a")
    file.write(str(fnfe))
    file.write("\n")
    file.close() 
except ModuleNotFoundError as me:
    f = open("101903072-log.txt", "a")
    f.write(str(me))
    f.write("\n")
    f.close()
except ImportError as ie:
    f = open("101903072-log.txt", "a")
    f.write(str(ie))
    f.write("\n")
    f.close()
except OSError as ose:
    f = open("101903072_log.txt", "a")
    f.write(str(ose))
    f.write("\n")
    f.close()
except RuntimeError as rte:
    f = open("101903072-log.txt", "a")
    f.write(str(rte))
    f.write("\n")
    f.close()

else:
    data=pd.read_csv(sys.argv[1])
    data['RollNumber'].value_counts()
    indexNames = data[data['Marks'] == 'X'].index
    data.drop(indexNames , inplace=True)
    indexNames1 = data[data['Marks'] == 'NAN'].index
    data.drop(indexNames1 , inplace=True)
    indexNames2 = data[data['Marks'] == '-'].index
    data.drop(indexNames2 , inplace=True)
    data.head()
    grouped_df = data.groupby("RollNumber")
    grouped_list1 = grouped_df["Submission"].apply(list)
    grouped_list2 = grouped_df["Marks"].apply(list)

    grouped_lists1 = grouped_list1.reset_index()
    grouped_lists2 = grouped_list2.reset_index()
    df=pd.merge(grouped_lists1,grouped_lists2,on="RollNumber")
    df1 = pd.DataFrame(columns=['RollNumber', 'P1', 'P2','P3','P4','P5'])
    df_size=df.shape[0]
    for i in range(df_size):
        w=df.iloc[i]['RollNumber']
        q=df.iloc[i]['Submission']
        #print(q)
        #print(type(c))
        d=df.iloc[i]['Marks']
        z=0 
        x=0 
        c=0 
        v=0 
        b=0
        if 'P1' in q:
            z=q.index('P1')
            z=d[z]
        if 'P2' in q:
            x=q.index('P2')
            x=d[x]
        if 'P3' in q:
            c=q.index('P3')
            c=d[c]
        if 'P4' in q:
            v=q.index('P4')
            v=d[v]
        if 'P5' in q:
            b=q.index('P5')
            b=d[b]
        #print(z,x,c,v,b) 
        df1.loc[i]=[w,z,x,c,v,b]

    df1.to_csv('101903072-output.csv', index= False)
    





