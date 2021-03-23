This is the file that contains the positional data. 

Upon review of the CSV that my CAD exporter outputs, and the JSON that I then convert it to, it would be best to use the CSV. It outputs actual mm distance, whereas the JSON convert script I have converts it to pixels (for web interface). 
Eventually I want to work with the simulator software enough to be able to work out how I can "pass through" the positional data as well, so that there is only one input file to work with. I will work on that in the coming months to make this whole process easier. 

Format is:

ID,X,Y

Units is MM
