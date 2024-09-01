from Booking.Booking import Booking

bot = Booking(driver_path=r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\Selenium")
bot.landing_page()
bot.dismiss_signin()
bot.select_currency()
print("Exiting ...")
    
    
     