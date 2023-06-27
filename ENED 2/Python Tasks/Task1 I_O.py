# Download the text file, TempC.txt from the Community Site.  The file has a single column of 
# temperatures in degrees Celsius.
# 
# Develop a Python script that will open the text file for reading and save the temperatures in a list.  Within the Python script,
# convert each temperature in the list 
# to Fahrenheit then write the converted temperatures to a new text file, TempF.txt.
# The conversion formula is: 𝐹 = 9/5(𝐶)+32
TempsC = []
TempFile = open("TempC.txt", "r")
for each in TempFile:
    TempsC.append(float(each))
TempFile.close()
for each in TempsC:
    each = 9/5*(each)+32
    print(each)