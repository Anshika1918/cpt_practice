



zodiac_sign=["Aries","Taurus", "Gemini", "Cancer","Leo","Virgo","Libra","Scorpio","Sagitarrius","Capricorn","Aquarius","Pisces"]


   


aries_trait=["Bold", "Strong-headed","Resiliant","Direct", "Natural Leader" ]
taurus_trait=["Dependable", "Loyal","Patient","Slow-burning Temper","Sensual"]
gemini_trait=["Adaptable","Curious","Quick-Witted","Indecisive","Social"]
cancer_trait=["Empathetic", "Creative","Nurturing","Intuitive","Senstive"]
leo_trait=["Natural Swagger","Charismatic","Generous","Amitious","Optimistic"]
virgo_trait=["Hardworking","Meticulous","Perfectionist","Intelligent","Reliable"]
libra_trait=["Diplomatic","Social","Cooperative","Indesicive","Fair-Minded"]
scorpio_trait=["Intense","Protective","Resourceful","Secretive","Perceptive"]
sagitarrius_trait=["Jolly","Adventurous","Blunt& Direct","Optimistic","High-Energy"]
capricorn_trait=["Responsible","Pragmatic","Grounded Humor","Ridgid","Disciplined"]
aquarius_trait=["Innovative","Humanitarian","Intellectual","Independent","Unpredictable"]
pisces_trait=["Compassionate","Creative","Wise","Kind","Indecesive"]

day = ""
month = ""

def zodiac_sign(month, day):

   if month == "january" or month == "february" or month == "march" or month == "april" or month == "may" or month == "june" or month == "july" or month == "august" or month == "september" or month == "october" or month == "november" or month == "december" and day <= 31:
      if (month == "december" and day >= 22) or (month == "january" and day <= 19):
        return "You are a Capricorn!"
  
      elif(month=="january" and day>=20) or (month=="february" and day <=18):
        return "You are an Aquarius!"
  
      elif(month=="february" and day>=19) or(month=="march" and day <=20):
        return "You are a Pisces!"
  
      elif(month=="march" and day>=20) or (month=="april" and day <=19):
        return "You are an Aries!"
 
      elif(month=="april" and day>=20) or (month=="may" and day<=20):
        return "You are a Taurus!"
 
      elif(month=="may" and day>=21) or (month=="june" and day<=20):
        return "You are a Gemini!"
 
      elif(month=="june" and day>=22) or(month=="july" and day<=22):
        return "You are a Cancer!"
 
      elif(month=="july" and day>=23) or(month=="august" and day<=22):
        return "You are are a Leo!"
 
      elif(month=="august" and day>=23) or(month== "september" and day<=22):
        return "You are a Virgo!"
 
      elif (month=="september" and day>=23) or (month=="october" and day<=22):
        return "You are a Libra!"
 
      elif(month=="october" and day>=23) or (month=="november" and day<=21):
        return "You are a Scorpio!"

      else:
        return "You are a Saggitarrius!"

while True:
  day =input("What is your Birthday? \nPlease enter what day of the month you were born on: ").strip().lower()
  month=input("What month were you born? \nPlease enter your birth month: ")
  zodiac_sign(month, day)
  
 
  
      



  
   
   
