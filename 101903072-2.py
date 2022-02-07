try:
    import sys 
    import pandas as pd
    import numpy as np 
    import matplotlib.pyplot as plt 
    n = len(sys.argv)
    if '101903072-output.csv' not in sys.argv :
        raise ValueError("101903072-Output.csv file has not been found")
    if n>2 or n<=1:
        raise ValueError("Kindly provide the input in the correct format which is {python <program.py> <InputDataFile>}")
    #print("Total arguments passed:", n)
    #print("\nName of Python script:", sys.argv[1])
    # if n==2 and sys.argv[1]!='input.csv':
    #     raise ValueError("The csv file provided does not have the correct name")
except ValueError as ve:
    file = open("101903072-log.txt", "a")
    file.write(str(ve))
    file.write("\n")
    file.close()
except FileNotFoundError as fnfe:
    file = open("101903072-log.txt", "a")
    file.write(str(fnfe))
    file.write("\n")
    file.close()    
except ModuleNotFoundError as me:
    file = open("101903072-log.txt", "a")
    file.write(str(me))
    file.write("\n")
    file.close()
except ImportError as ie:
    file = open("101903072-log.txt", "a")
    file.write(str(ie))
    file.write("\n")
    file.close()
except OSError as ose:
    file = open("101903072-log.txt", "a")
    file.write(str(ose))
    file.write("\n")
    file.close()
except RuntimeError as rte:
    file = open("101903072-log.txt", "a")
    file.write(str(rte))
    file.write("\n")
    file.close()

else:
    data=pd.read_csv(sys.argv[1])
    data.head()
    mean_p1=data['P1'].mean()
    median_p1=data['P1'].median()
    std_p1=data['P1'].std()
    min_p1=data['P1'].min()
    max_p1=data['P1'].max()
    mean_p2=data['P2'].mean()
    median_p2=data['P2'].median()
    std_p2=data['P2'].std()
    min_p2=data['P2'].min()
    max_p2=data['P2'].max()
    mean_p3=data['P3'].mean()
    median_p3=data['P3'].median()
    std_p3=data['P3'].std()
    min_p3=data['P3'].min()
    max_p3=data['P3'].max()
    mean_p4=data['P4'].mean()
    median_p4=data['P4'].median()
    std_p4=data['P4'].std()
    min_p4=data['P4'].min()
    max_p4=data['P4'].max()
    mean_p5=data['P5'].mean()
    median_p5=data['P5'].median()
    std_p5=data['P5'].std()
    min_p5=data['P5'].min()
    max_p5=data['P5'].max()
    data['S']=data['P1']+data['P2']+data['P3']+data['P4']+data['P5']
    mean_s=data['S'].mean()
    median_s=data['S'].median()
    std_s=data['S'].std()
    max_s=data['S'].max()
    min_s=data['S'].min()
    f=open("101903072-statistics.txt","a")
    f.write("\n                                           Whole Dataset                                                         \n")
    f.write("_____________________________________________________________________________________________________\n")
    f.write("  there are "+str(41)+" NAN Values, "+ str(19)+" - values and "+str(27)+" values marked as X \n" )
    f.write(" Max marks of a student is "+str(max_s)+"\n")
    f.write(" Min marks of a students is "+str(min_s)+"\n")
    f.write(" Mean marks are "+str(mean_s)+"\n")
    f.write(" Median of marks is "+str(median_s)+"\n")
    f.write(" Standard Deviation of marks is "+str(std_s)+"\n")
    f.close()


    f=open("101903072-statistics.txt","a")
    f.write("\n                                           P1                                                          \n")
    f.write("_____________________________________________________________________________________________________\n")
    f.write(" In P1 there are "+str(8)+" NAN Values, "+ str(2)+" - values and "+str(8)+" values marked as X \n" )
    f.write(" Max marks in subject P1 is "+str(max_p1)+"\n")
    f.write(" Min marks in subject P1 is "+str(min_p1)+"\n")
    f.write(" Mean marks in subject P1 is "+str(mean_p1)+"\n")
    f.write(" Median of marks in subject P1 is "+str(median_p1)+"\n")
    f.write(" Standard Deviation of marks in subject P1 is "+str(std_p1)+"\n")
    f.close()
    f=open("101903072-statistics.txt","a")
    f.write("\n                                           P2                                                        \n")
    f.write("_____________________________________________________________________________________________________\n")
    f.write(" In P2 there are "+str(12)+" NAN Values, "+ str(7)+" - values and "+str(10)+" values marked as X \n" )
    f.write(" Max marks in subject P2 is "+str(max_p2)+"\n")
    f.write(" Min marks in subject P2 is "+str(min_p2)+"\n")
    f.write(" Mean marks in subject P2 is "+str(mean_p2)+"\n")
    f.write(" Median of marks in subject P2 is "+str(median_p2)+"\n")
    f.write(" Standard Deviation of marks in subject P2 is "+str(std_p2)+"\n")
    f.close()
    f=open("101903072-statistics.txt","a")
    f.write("\n                                           P3                                                        \n")
    f.write("_____________________________________________________________________________________________________\n")
    f.write(" In P3 there are "+str(16)+" NAN Values, "+ str(7)+" - values and "+str(5)+" values marked as X \n" )
    f.write(" Max marks in subject P3 is "+str(max_p3)+"\n")
    f.write(" Min marks in subject P3 is "+str(min_p3)+"\n")
    f.write(" Mean marks in subject P3 is "+str(mean_p3)+"\n")
    f.write(" Median of marks in subject P3 is "+str(median_p3)+"\n")
    f.write(" Standard Deviation of marks in subject P3 is "+str(std_p3)+"\n")
    f.close()
    f=open("101903072-statistics.txt","a")
    f.write("\n                                           P4                                                     \n")
    f.write("_____________________________________________________________________________________________________\n")
    f.write(" In P4 there are "+str(2)+" NAN Values, "+ str(0)+" - values and "+str(2)+" values marked as X \n" )
    f.write(" Max marks in subject P4 is "+str(max_p4)+"\n")
    f.write(" Min marks in subject P4 is "+str(min_p4)+"\n")
    f.write(" Mean marks in subject P4 is "+str(mean_p4)+"\n")
    f.write(" Median of marks in subject P4 is "+str(median_p4)+"\n")
    f.write(" Standard Deviation of marks in subject P4 is "+str(std_p4)+"\n")
    f.close()
    f=open("101903072-statistics.txt","a")
    f.write("\n                                           P5                                                      \n")
    f.write("_____________________________________________________________________________________________________\n")
    f.write(" In P5 there are "+str(3)+" NAN Values, "+ str(3)+" - values and "+str(2)+" values marked as X \n" )
    f.write(" Max marks in subject P5 is "+str(max_p5)+"\n")
    f.write(" Min marks in subject P5 is "+str(min_p5)+"\n")
    f.write(" Mean marks in subject P5 is "+str(mean_p5)+"\n")
    f.write(" Median of marks in subject P5 is "+str(median_p5)+"\n")
    f.write(" Standard Deviation of marks in subject P5 is "+str(std_p5)+"\n")
    f.close()
    data['P1'].value_counts()
    data['P2'].value_counts()
    data['P3'].value_counts()
    data['P4'].value_counts()
    data['P5'].value_counts()
    data_p1=[67,112,100,80]
    data_p2=[79,100,78,107]
    data_p3=[99,93,91,76]
    data_p4=[318,11,19,23]
    data_p5=[337,12,11,10]
    y=[0,13,14,15]
    plt.xlabel('Marks')
    plt.ylabel('No. of Students')
    plt.title('Histogram of Performance Analysis')
    plt.hist([data['P1'],data['P2'],data['P3'],data['P4'],data['P5']],bins=[13,14,15,16],rwidth=0.95,color=['blue','orange','green','red','purple'],label=['P1','P2','P3','P4','P5'])
    plt.legend()
    plt.savefig('101903072-histogram.png')
    fig, axes = plt.subplots(figsize=(9,5))

    axes.plot(y,data_p1 ,color="blue", linewidth=2 , ls='-', marker='s',label='P1')
    axes.plot(y,data_p2,color="orange", linewidth=2,ls='-', marker='o',label='P2')
    axes.plot(y,data_p3,color="green", linewidth=2,ls='-', marker='s',label='P3')
    axes.plot(y,data_p4,color="red", linewidth=2,ls='-', marker='o',label='P4')
    axes.plot(y,data_p5,color="purple", linewidth=2,ls='-', marker='s',label='P5')
    axes.set_ylim([0,350])
    axes.set_xlim([0,16])
    axes.set_title("Line Graph of Performance");
    axes.set_xlabel('Marks of Students')
    axes.set_ylabel('Frequency of students')
    axes.legend(loc=0)
    plt.savefig('101903072-line.png')
    exp_vals=[900,328,299,296]
    exp_label=["Freq of 0 marks","Freq of 13 marks","Freq of 14 marks","Freq of 15 marks"]
    plt.axis("equal")
    plt.pie(exp_vals,labels=exp_label,radius=1.5,autopct="%0.1f%%",shadow=True ,explode=[0.1,0.1,0.1,0.1],startangle=180)
    plt.title("Pie Chart of Performance")
    plt.legend(loc=4,title = "Marks")
    plt.savefig('101903072-pie.png')
    #data_p1=[112,100,80]
    #data_p2=[100,78,107]
    #data_p3=[93,91,76]
    #data_p4=[11,19,23]
    #data_p5=[12,11,10]
    #y=[13,14,15]
    data_p1=[67,112,100,80]
    data_p2=[79,100,78,107]
    data_p3=[99,93,91,76]
    data_p4=[318,11,19,23]
    data_p5=[337,12,11,10]
    y=[0,13,14,15]
    fig, axes = plt.subplots(figsize=(10,8))

    axes.scatter(y,data_p1 ,color="blue",label='P1')
    axes.scatter(y,data_p2,color="orange",label='P2')
    axes.scatter(y,data_p3,color="green",label='P3')
    axes.scatter(y,data_p4,color="red",label='P4')
    axes.scatter(y,data_p5,color="purple",label='P5')
    axes.set_ylim([0,125])
    axes.set_xlim([-1,16])
    axes.set_title("Scatter Plot of Performance");
    axes.set_xlabel('Marks of Students')
    axes.set_ylabel('Frequency of students')
    axes.legend(loc=3)
    plt.savefig('101903072-scatter.png')
    df=data
    df['Sum']=df['P1']+df['P2']+df['P3']+df['P4']+df['P5']
    df.head()
    df['Sum'].value_counts()
    arr1=[42,41,43,28,40,29,44,27,30,26,14,13,15,39,45,71]
    height=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    arr2=[54,49,47,35,34,22,20,20,13,13,10,9,8,5,4,1]
    fig, axes = plt.subplots(figsize=(5,5))
    axes.scatter(arr1,arr2)
    axes.set_xlabel("Sum of marks in all Subjects")
    axes.set_label("Freq of Students")
    axes.set_title("Plot to show freq of students with given amount of marks ")
    plt.savefig('101903072-graph.png')