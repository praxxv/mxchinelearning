# mxchinelearning
this repo consists of all the ML projects Ive ever meade

**PROJECT 1 - HOUSE PRICE INDEX PREDICTION USING TIME SERIES DATA AND – MULTIVARIATE LSTM**

The House Price Index (HPI) is a measure that tracks changes in the prices of residential properties over time. It provides insights into real estate market trends, showing whether home prices are rising or falling. The index is typically calculated using repeat sales data or hedonic regression models, and is used by policymakers, economists, investors, and homebuyers to assess housing market health, inflation, and investment potential. 

THIS IS THE FIRST PROJECT I HAVE MADE FOR MY PORTFOLIO. AT THE START OF THIS PROJECT I HAD NO EXPERIENCE WHATSOVER IN BUILDING ANY ML PROJECT. 
THE MODEL IS AN RNN-RECURRENT NEURAL NETWORK AND AIMS TO PREDICT HPI - HOUSE PRICE INDEX USING TIME SERIES DATA. THE DATASET WAS OBTAINED FROM THE TEXAS A&M WEBSITE AND CONSISTED OF THREE COLUMNS - DATE, HPI , AND NUMSOLD. THE DATE COLUMN WAS USED TO CREATE A TIME SERIES MODEL. THE HPI COLUMN WAS THE TARGET VARIABLE AND NUMSOLD IS THE NUMBER OF HOUSES IN 1000S SOLD THAT YEAR. I DID GO ON TO MODIFY THE DATASET BY ADDING MORE COLUMNS TO CREATE A MULTIVARIATE LSTM MODEL AS I BELIEVED THAT SIMPLY USING THE TIME SERIES DATA WOULD BE TOO SIMPLE. THE COLUMNS I WENT ON TO ADD AND POPULATE ARE – THE CORRESPONDING YEAR’S INFLATION RATE, INTEREST RATE AND GDP GROWTH RATE. 

PROJECT RELEVANCE
 Governments, real estate investors, and banks rely on accurate HPI forecasts for decisions on lending, investment, and policy-making. A multivariate LSTM can provide a data-driven, forward-looking estimate.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**PROJECT 2- Keystroke Logger Using Synthetically created keystroke data**
A keystroke logger, or keylogger, is a software or hardware tool that records the keys a user types on a keyboard, often without their knowledge. It captures input in real time, storing details such as typed text, login credentials, or communication content. 

The main aspect of the project was  collecting the data. The datset for it was synthetically produced. To create it, I simply typed multiple paragraphs and using python I was able to capture the details of each key press into a csv file. The keystroke data corresponding to me is labelled 1 and that of my mom is labelled 0.  
After capturing and loading the keystroke data, I used data preprocessing to clean the data to make it fit to feed into an Artifical Neural Network which I then trained for classification. The ANN however performed poorly reaching only 67% accuracy , due to which I had to use other machine learning models which gave me better results. Random Forrest did give me the best result of 78% accuracy

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**PROJECT 3 - Counterfeit Currency Detection -  using Convolutional Neural Network**
Counterfeit currency detection is the process of identifying fake money designed to imitate legitimate currency. It plays a vital role in protecting national economies, businesses, and consumers from financial fraud

in this project , gathereing the data was the most critical and challenging aspect, as I needed thousands of pictures of genuine and counterfeit bills. This is not only hard to find but also, counterfeit bills being illegal are typically difficult to obtain. 
To find genuine banknotes, I downloaded roughly 100 photos of real currency and using data augmentation , I created thousands of copies of these photos by applying simple transformations in python . 
As for the counterfeit money dataset, I edited the photos of genuine banknotes, by changing contrast, saturation and blurring out parts of the note’s most important features such as the seal 

Then, I created a multi layered CNN using tensorflow that takes in these photos , understands patterns in each training set and is now able to make accurate classifications. The dataset for this project has been stored on my drive. 

**REAL WORLD SIGNIFICANCE** - 
Fights Financial Fraud
Supports Banks and Retailers
Scalable and Fast
Adapts to Sophisticated Fakes
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
