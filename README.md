# Performance-Analysis
Analysing the marks of the students in 5 subjects and creating statistical plots 


•	The program must be run from command line only: 
-	Usages: python <program.py> <InputDataFile>
-	Example: python 101903072-1.py input.csv
-	Example: python 101903072-2.py output.csv



101903072-1.py :- In the input.csv file there are certain fields which contain "NAN" , "-" values instead of marks . Hence firstly pre processing has been carried out on this original dataset . Further another dataset has been created from this original dataset . 

![image](https://user-images.githubusercontent.com/84843202/152729962-c853df7a-96d0-46f2-8c08-f2d5352d2863.png)

![image](https://user-images.githubusercontent.com/84843202/152730039-2104373f-740e-4387-b500-a429d790b33c.png)

 FIG1 IS THE INPUT FILE AND FIG 2 IS THE OUTPUT FILE 



The program is capable of handle exception (if any) and write then to a log file:
-	Correct number of parameters (inputFileName).
-	Show the appropriate message for wrong inputs.
-	Handling of “File not Found” exception
-	Input file must contain three columns only.
-	Any issue with the input record is written to a log file




2.	101903072-2.py:- python program that reads the output file (of 1.1) and generates 
-	Multiple plots such as Histogram, Line chart, Pie chart, etc for P1, P2, P3, RP1, RP2, Total-of-all. All the plots are saved into multiple .png files 
-	Generated the different statistics and save to a txt file: such as Min, Max, Mean, Median, SD, distribution, Count number of missing values, Count Non numeric Values, etc for P1, P2, P3, RP1, RP2, Total-of-all.


