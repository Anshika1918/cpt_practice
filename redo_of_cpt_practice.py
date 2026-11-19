day = ""
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"] # make this a list instead

def zodiac_sign(month, day):
  #your algo should live in a while loop that keeps running until they enter correct data
  while day <= 31:
  
    if month == months[11] and day >= 22 or month == months[0] and day <= 19:
      return "You are a Capricorn!"
    
    elif month == months[0] and day>=20 and day <= 31 or month==months[1] and day <=18:
     return "You are an Aquarius!"
        
    elif(month==months[1] and day>=19 and day <= 29) or(month==months[2] and day <=20):
      return "You are a Pisces!"
  
    elif(month==months[2] and day>=20 and day <= 31) or (month==months[3] and day <=19):
      return "You are an Aries!"
 
    elif(month==months[3] and day>=20 and day <= 30) or (month==months[4] and day<=20):
      return "You are a Taurus!"
 
    elif month ==months[4] and day>=21 and day <= 31 or month==months[5] and day<=20:
      return "You are a Gemini!"
 
    elif(month==months[5] and day>=22 and day <= 30) or(month==months[6] and day<=22):
      return "You are a Cancer!"
 
    elif(month==months[6] and day>=23 and day <= 31) or(month==months[7] and day<=22):
      return "You are are a Leo!"
  
    elif(month==months[7] and day>=23 and day <= 31) or(month== months[8] and day<=22):
      return "You are a Virgo!"
 
    elif (month==months[8] and day>=23 and day <= 30) or (month==months[9] and day<=22):
      return "You are a Libra!"
 
    elif(month==months[9] and day>=23 and day <= 31) or (month==months[10] and day<=21):
      return "You are a Scorpio!"

    elif (month==months[10] and day>=22 and day <= 30) or (month==months[11] and day<=21):
      return "You are a Saggitarrius!"
    else:
      print("You entered an invaild statement, please try again.") 
    



def main(): 

  day =int(input("What is your Birthday? \nPlease enter what day of the month you were born on: ").strip().lower())

  month=input("What month were you born? \nPlease enter your birth month: ")
  
  result = zodiac_sign(month, day)
  print(result)

main()