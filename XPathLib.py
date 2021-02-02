# Two-function library to determine the XPATHs for the buttons that will be clicked in the for

buttonXPATH1 = '//*[@id="signupcontainer"]/table/tbody/tr['
buttonXPATH2 = ']/td[2]/table/tbody/tr/td[3]/div/span'

# Determines XPATHs of the buttons to click in the form
def getXPATHList(arguments):
    xpathLIST = []
    for arg in arguments:
        finalXPATH = buttonXPATH1 + str(arg) + buttonXPATH2
        xpathLIST.append(finalXPATH)
    return xpathLIST

# Determines the numbers of the XPATHs that have to be added
# Yes, this is super messy :(
def getXPATHNumbers(arguments):
    xpathLIST = []
    for arg in arguments:
        if (arg[0] == 'M'):
            if (arg[1:] == '1215'):
                insertXPATH = 2 
            elif (arg[1:] == '115'):
                insertXPATH = 3  
            elif (arg[1:] == '600'):
                insertXPATH = 4
            elif (arg[1:] == '700'):
                insertXPATH = 5   
            elif (arg[1:] == '800'):
                insertXPATH = 6   
            elif (arg[1:] == '900'):
                insertXPATH = 7   
            elif (arg[1:] == '1230'):
                insertXPATH = 8  
            elif (arg[1:] == '130'):
                insertXPATH = 9   
            elif (arg[1:] == '230'):
                insertXPATH = 10   
            elif (arg[1:] == '330'):
                insertXPATH = 11   
            elif (arg[1:] == '430'):
                insertXPATH = 12  
            elif (arg[1:] == '530'):
                insertXPATH = 13   
            elif (arg[1:] == '630'):
                insertXPATH = 14
            elif (arg[1:] == '730'):
                insertXPATH = 15
            elif (arg[1:] == '830'):
                insertXPATH = 16 
            elif (arg[1:] == '930'):
                insertXPATH = 17
            elif (arg[1:] == '1030'):
                insertXPATH = 18
            elif (arg[1:] == '1115'):
                insertXPATH = 19           
        elif (arg[0] == 'T'):
            if (arg[1:] == '1215'):
                insertXPATH = 20 
            elif (arg[1:] == '115'):
                insertXPATH = 21  
            elif (arg[1:] == '600'):
                insertXPATH = 22
            elif (arg[1:] == '700'):
                insertXPATH = 23   
            elif (arg[1:] == '800'):
                insertXPATH = 24   
            elif (arg[1:] == '900'):
                insertXPATH = 25   
            elif (arg[1:] == '1230'):
                insertXPATH = 26  
            elif (arg[1:] == '130'):
                insertXPATH = 27   
            elif (arg[1:] == '230'):
                insertXPATH = 28   
            elif (arg[1:] == '330'):
                insertXPATH = 29   
            elif (arg[1:] == '430'):
                insertXPATH = 30  
            elif (arg[1:] == '530'):
                insertXPATH = 31   
            elif (arg[1:] == '630'):
                insertXPATH = 32
            elif (arg[1:] == '730'):
                insertXPATH = 33
            elif (arg[1:] == '830'):
                insertXPATH = 34 
            elif (arg[1:] == '930'):
                insertXPATH = 35
            elif (arg[1:] == '1030'):
                insertXPATH = 36
            elif (arg[1:] == '1115'):
                insertXPATH = 37   
        elif (arg[0] == 'W'):
            if (arg[1:] == '1215'):
                insertXPATH = 38 
            elif (arg[1:] == '115'):
                insertXPATH = 39  
            elif (arg[1:] == '600'):
                insertXPATH = 40
            elif (arg[1:] == '700'):
                insertXPATH = 41   
            elif (arg[1:] == '800'):
                insertXPATH = 42   
            elif (arg[1:] == '900'):
                insertXPATH = 43   
            elif (arg[1:] == '1230'):
                insertXPATH = 44  
            elif (arg[1:] == '130'):
                insertXPATH = 45   
            elif (arg[1:] == '230'):
                insertXPATH = 46   
            elif (arg[1:] == '330'):
                insertXPATH = 47   
            elif (arg[1:] == '430'):
                insertXPATH = 48  
            elif (arg[1:] == '530'):
                insertXPATH = 49   
            elif (arg[1:] == '630'):
                insertXPATH = 50
            elif (arg[1:] == '730'):
                insertXPATH = 51
            elif (arg[1:] == '830'):
                insertXPATH = 52 
            elif (arg[1:] == '930'):
                insertXPATH = 53
            elif (arg[1:] == '1030'):
                insertXPATH = 54
            elif (arg[1:] == '1115'):
                insertXPATH = 55   
        elif (arg[0] == 'H'):
            if (arg[1:] == '1215'):
                insertXPATH = 56 
            elif (arg[1:] == '115'):
                insertXPATH = 57  
            elif (arg[1:] == '600'):
                insertXPATH = 58
            elif (arg[1:] == '700'):
                insertXPATH = 59   
            elif (arg[1:] == '800'):
                insertXPATH = 60   
            elif (arg[1:] == '900'):
                insertXPATH = 61   
            elif (arg[1:] == '1230'):
                insertXPATH = 62  
            elif (arg[1:] == '130'):
                insertXPATH = 63   
            elif (arg[1:] == '230'):
                insertXPATH = 64   
            elif (arg[1:] == '330'):
                insertXPATH = 65   
            elif (arg[1:] == '430'):
                insertXPATH = 66  
            elif (arg[1:] == '530'):
                insertXPATH = 67   
            elif (arg[1:] == '630'):
                insertXPATH = 68
            elif (arg[1:] == '730'):
                insertXPATH = 69
            elif (arg[1:] == '830'):
                insertXPATH = 70 
            elif (arg[1:] == '930'):
                insertXPATH = 71
            elif (arg[1:] == '1030'):
                insertXPATH = 72
            elif (arg[1:] == '1115'):
                insertXPATH = 73   
        elif (arg[0] == 'F'):
            if (arg[1:] == '1215'):
                insertXPATH = 74 
            elif (arg[1:] == '115'):
                insertXPATH = 75  
            elif (arg[1:] == '600'):
                insertXPATH = 76
            elif (arg[1:] == '700'):
                insertXPATH = 77   
            elif (arg[1:] == '800'):
                insertXPATH = 78   
            elif (arg[1:] == '900'):
                insertXPATH = 79   
            elif (arg[1:] == '1230'):
                insertXPATH = 80  
            elif (arg[1:] == '130'):
                insertXPATH = 81   
            elif (arg[1:] == '230'):
                insertXPATH = 82   
            elif (arg[1:] == '330'):
                insertXPATH = 83   
            elif (arg[1:] == '430'):
                insertXPATH = 84  
            elif (arg[1:] == '530'):
                insertXPATH = 85   
            elif (arg[1:] == '630'):
                insertXPATH = 86
            elif (arg[1:] == '730'):
                insertXPATH = 87
            elif (arg[1:] == '830'):
                insertXPATH = 88 
            elif (arg[1:] == '930'):
                insertXPATH = 89
            elif (arg[1:] == '1030'):
                insertXPATH = 90
            elif (arg[1:] == '1115'):
                insertXPATH = 91  
        elif (arg[0] == 'S'):
            if (arg[1:] == '1215'):
                insertXPATH = 92 
            elif (arg[1:] == '115'):
                insertXPATH = 93  
            elif (arg[1:] == '600'):
                insertXPATH = 94
            elif (arg[1:] == '700'):
                insertXPATH = 95   
            elif (arg[1:] == '800'):
                insertXPATH = 96   
            elif (arg[1:] == '900'):
                insertXPATH = 97   
            elif (arg[1:] == '1230'):
                insertXPATH = 98  
            elif (arg[1:] == '130'):
                insertXPATH = 99   
            elif (arg[1:] == '230'):
                insertXPATH = 100   
            elif (arg[1:] == '330'):
                insertXPATH = 101   
            elif (arg[1:] == '430'):
                insertXPATH = 102  
            elif (arg[1:] == '530'):
                insertXPATH = 103   
            elif (arg[1:] == '630'):
                insertXPATH = 104
            elif (arg[1:] == '730'):
                insertXPATH = 105
            elif (arg[1:] == '830'):
                insertXPATH = 106 
            elif (arg[1:] == '930'):
                insertXPATH = 107
            elif (arg[1:] == '1030'):
                insertXPATH = 108
            elif (arg[1:] == '1115'):
                insertXPATH = 109  
        elif (arg[0] == 'U'):
            if (arg[1:] == '1215'):
                insertXPATH = 110 
            elif (arg[1:] == '115'):
                insertXPATH = 111  
            elif (arg[1:] == '600'):
                insertXPATH = 112
            elif (arg[1:] == '700'):
                insertXPATH = 113   
            elif (arg[1:] == '800'):
                insertXPATH = 114   
            elif (arg[1:] == '900'):
                insertXPATH = 115   
            elif (arg[1:] == '1230'):
                insertXPATH = 116  
            elif (arg[1:] == '130'):
                insertXPATH = 117   
            elif (arg[1:] == '230'):
                insertXPATH = 118   
            elif (arg[1:] == '330'):
                insertXPATH = 119   
            elif (arg[1:] == '430'):
                insertXPATH = 120  
            elif (arg[1:] == '530'):
                insertXPATH = 121   
            elif (arg[1:] == '630'):
                insertXPATH = 122
            elif (arg[1:] == '730'):
                insertXPATH = 123
            elif (arg[1:] == '830'):
                insertXPATH = 124 
            elif (arg[1:] == '930'):
                insertXPATH = 125
            elif (arg[1:] == '1030'):
                insertXPATH = 126
            elif (arg[1:] == '1115'):
                insertXPATH = 127   
        xpathLIST.append(insertXPATH)
    return xpathLIST   