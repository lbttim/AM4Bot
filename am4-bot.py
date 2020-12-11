from selenium import webdriver
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import Select


class AM4Bot():
   
    
    def __init__(self):
        self.driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe') 

    def login(self):
        try:
            
            # Go to website
            self.driver.get('https://www.airline4.net/')
    
            sleep(2)
            
            # Click to login button
            fb_btn = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[5]/button[1]')
            fb_btn.click()
            sleep(2)
    
            # Find username bar and enter it
            username_in = self.driver.find_element_by_xpath('//*[@id="lEmail"]')
            username_in.send_keys("YOUR_EMAIL") #Change this with your email which you are using for am4
            sleep(2)
            
            # Find password bar and enter it
            pw_in = self.driver.find_element_by_xpath('//*[@id="lPass"]')
            pw_in.send_keys("YOUR_PASSWORD") #Change this with password which you are using for am4
            sleep(2)
    
            # Click login button
            login_btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
            login_btn.click() 
            sleep(4)
            
            
            # Close Departure button
            Close_Depart_btn = self.driver.find_element_by_xpath(' //*[@id="flightInfo"]/div[4]/span')
            Close_Depart_btn.click()
        except:
            print("Login failure")
            
        sleep(2)
    
    def fuel_check (self) :
        
        try:
        
            # Click fuel button
            fuel_btn = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/div[3]')
            fuel_btn.click()
            sleep(2)
            
            ''' It reads the fuel price, then removes the dollar sign and comma from it.
                Finally convert the fuel price to an integer value. '''  
            fuel_price = self.driver.find_element_by_xpath("//*[@id=\"fuelMain\"]/div/div[1]/span[2]/b").text
            fuel_price = fuel_price.replace("$ ","")
            fuel_price = fuel_price.replace(",","")
            fuel_price = int(fuel_price)
            sleep(2)
            
            # Get fuel remaining amount and convert to integer
            fuel_remaining_amount = self.driver.find_element_by_xpath("//*[@id=\"holding\"]").text
            fuel_remaining_amount = fuel_remaining_amount.replace(",","")
            fuel_remaining_amount = int(fuel_remaining_amount)
            sleep(2)
            
            # Creating temporary variable to compare if after bought fuel amount increase
            temp = fuel_remaining_amount
            
            
           
            if fuel_price <= 400 or fuel_remaining_amount <= 8000000:
                ''' IF FUNCTION:
                If fuel price is lower or equal 400$  or we had only 1,000,000 lbs of fuel then:
                If conditions are true buy the maximum amount of fuel.
                If not then do. nothing
                '''
                
                # Find amount to purchase bar end enter max fuel amount to buy 
                fuel_amount = self.driver.find_element_by_xpath('//*[@id="amountInput"]')
                fuel_amount.send_keys(15000000)
                sleep(2)
                
                # Click fuel purchase button
                fuel_buy = self.driver.find_element_by_xpath('//*[@id="fuelMain"]/div/div[7]/div/button[2]')
                fuel_buy.click()
                sleep(2)
                
                # Get fuel remaining amount and convert to integer AGAIN
                fuel_remaining_amount = self.driver.find_element_by_xpath("//*[@id=\"holding\"]").text
                fuel_remaining_amount = fuel_remaining_amount.replace(",","")
                fuel_remaining_amount = int(fuel_remaining_amount)
                sleep(2)
            
                if temp < fuel_remaining_amount:
                    ''' IF FUNCTION:
                    Check if fuel amount before purchase is lover then after purchase, if:
                    yes -> Then print fuel was purchased
                    not -> Then print no fuel was purchased'''
                
                # Show in console info that fuel was bought
                    print("The warehouse was filled with fuel for: $",fuel_price)
                else:
                # Show in console info that fuel wasn't bought
                    print("Not enough money to fill the warehouse by fuel")
                
            
            # Close fuel panel
            fuel_close_btn = self.driver.find_element_by_xpath('//*[@id="popup"]/div/div/div[1]/div/span')
            fuel_close_btn.click()      
            sleep(2)
        
        except:
            None
    
    def CO2_check(self):
        try:
            # Click fuel button
            fuel_btn = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/div[3]')
            fuel_btn.click()
            sleep(2)
            
            # Click CO2 button
            CO2_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div[1]/button[2]')
            CO2_btn.click()
            sleep(2)
            
            # Get CO2 price
            CO2_price = self.driver.find_element_by_xpath("//*[@id=\"co2Main\"]/div/div[2]/span[2]/b").text
            CO2_price = CO2_price.replace("$ ","")
            CO2_price = int(CO2_price)
            sleep(2)
    
            # Get CO2 remaining amount
            CO2_remaining_amount = self.driver.find_element_by_xpath("//*[@id=\"holding\"]").text
            CO2_remaining_amount = CO2_remaining_amount.replace(",","")
            CO2_remaining_amount = int(CO2_remaining_amount)
            
            # Creating temp variable to compare if after bought fuel amount increase
            temp = CO2_remaining_amount
            
            
            if CO2_price <= 104 or CO2_remaining_amount <= 1000000:
                
                # Find end enter max CO2 amount with mean = 8,000,000
                CO2_amount = self.driver.find_element_by_xpath('//*[@id="amountInput"]')
                CO2_amount.send_keys(8000000)
                
                # Wait 2 seconds
                sleep(2)
                
                # Click fuel purchase button
                CO2_buy = self.driver.find_element_by_xpath('//*[@id="co2Main"]/div/div[8]/div/button[2]')
                CO2_buy.click()            
                sleep(2)
                
                # Get CO2 remaining amount AGAIN
                CO2_remaining_amount = self.driver.find_element_by_xpath("//*[@id=\"holding\"]").text
                CO2_remaining_amount = CO2_remaining_amount.replace(",","")
                CO2_remaining_amount = int(CO2_remaining_amount)
                sleep(2)
                
                if temp < CO2_remaining_amount:
                    ''' IF FUNCTION:
                    Check if CO2 amount before purchase is lover then after purchase, if:
                    yes -> Then print CO2 was purchased
                    not -> Then print no CO2 was purchased'''
                
                # Show in console info that fuel was bought
                    print("The warehouse was filled with CO2 for: $",CO2_price)
                else:
                # Show in console info that CO2 wasn't buy
                    print("Not enough money to fill the warehouse by fuel")    
                
            # Close CO2 panel
            CO2_close_btn = self.driver.find_element_by_xpath('//*[@id="popup"]/div/div/div[1]/div/span')
            CO2_close_btn.click()   
            sleep(2)
        
        except:
            None


    def Depart_All (self):
        try:
            # Click on Status list button
                Status_btn = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/div[1]')
                Status_btn.click()
                sleep(4)
                
            # Click on Landed button
                Landed_btn = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[6]/div[5]/div/div/div/button[2]')
                Landed_btn.click()
                sleep(4)
                
          
        # Click on Departure all button if plain wait to departure
                Depart_All_btn = self.driver.find_element_by_xpath('//*[@id="listDepartAll"]/div/button[2]')
                Depart_All_btn.click()
                sleep(2)
                
                
        # Time to finish operation
                sleep(4)
                print("Departure button click")
                
                # Close Departure button if plain not wait to departure
                Close_Depart_btn = self.driver.find_element_by_xpath(' //*[@id="flightInfo"]/div[4]/span')
                Close_Depart_btn.click()
                sleep(2)
                
        except:
                # Close Departure button if plain not wait to departure
                Close_Depart_btn = self.driver.find_element_by_xpath(' //*[@id="flightInfo"]/div[4]/span')
                Close_Depart_btn.click()
                sleep(2)
                
    
    def current_time(self):
        return datetime.now().time().strftime("%d/%m/%Y %H:%M:%S")

    
    def Bulk_repair(self):
        try:
                Maintenance_btn = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/div[4]')
                Maintenance_btn.click()
                sleep(4)
                
                
                Plan_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div[1]/button[2]')
                Plan_btn.click()
                sleep(4)
                
                Bulk_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div[2]/div[1]/div[1]/button[2]')
                Bulk_btn.click()
                sleep(4)
                
                select = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div[2]/div[3]/div/div[1]/select')
                select.click()
                sleep(2)
                
                s = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div[2]/div[3]/div/div[1]/select/option[2]')
                s.click()
                print("Aircrafts on repair")
                sleep(2)
                
                planbulk = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div[2]/div[3]/div/div[2]/div/button')
                planbulk.click()
                sleep(2)
                
                
        except:
            close_btn = self.driver.find_element_by_xpath('//*[@id="popup"]/div/div/div[1]/div/span')
            close_btn.click()
            sleep(2)  
    
    
# Creating shortout to AM4Bot Class
bot = AM4Bot()

# Call login function
bot.login()
# Check variable is used to run the program in a never-ending loop
check = False
# Time variable is used to count minutes to check fuel and CO2 price
time = 30

# This condition is always true
while check != True:
    
    # Every 15 minute check fuel and CO2 prices
    if time == 30:    
        # Call fuel check function
        bot.fuel_check()
        sleep(2)
        
        # Call CO2 function
        bot.CO2_check()
        # Reset time value
        time = 0
    
    
    # Check if plain wait for departure
    bot.Depart_All()
    
    # Print in console check and current time when program go through loop
    print('Checked:',bot.current_time())
    
    # Wait minute
    sleep(30)
    
    time +=1
    
    
    bot.Bulk_repair()
    sleep(30)
    time +=360
    
    
    

    
    
    
    
    