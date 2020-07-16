from appliances import DishWasher
from appliances import Dryer
from appliances import Washer
from appliances.kitchen.utility import Refrigerator
from appliances import Appliance
from appliances import CoffeeMaker

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

samsung_washer.wash_clothes()
samsung_dryer.dry_clothes()

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()
