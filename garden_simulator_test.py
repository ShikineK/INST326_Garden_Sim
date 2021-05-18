import pytest
import builtins
from unittest import mock
import garden_simulator
from garden_simulator import Plant
from time import strftime


def test_season():
    """Does season() return the message confirming the current and ideal season?"""
    plant = Plant("plants.csv", 30)
    month = strftime("%B")
    month_season = {"January": "winter",
                    "February": "winter",
                    "March": "spring",
                    "April": "spring",
                    "May": "spring",
                    "June": "summer",
                    "July": "summer",
                    "August": "summer",
                    "September": "fall",
                    "October": "fall",
                    "November": "fall",
                    "December": "winter"}
    if month_season[month] == "spring":
        assert plant.season("sunflower") == "The ideal season for a sunflower is spring. The current season is spring. You can plant a sunflower!"
        assert plant.season("cactus") == "The ideal season for a cactus is summer. The current season is spring. You cannot plant a cactus. :/"
    elif month_season[month] == "summer":
        assert plant.season("cactus") == "The ideal season for a cactus is summer. The current season is summer. You can plant a cactus!"
        assert plant.season("sunflower") == "The ideal season for a sunflower is spring. The current season is summer. You cannot plant a sunflower. :/"
        
def test_water():
    """Does water() return the correct message and add HP to the current_HP"""
    name = self.plants['name']
    waterinfo = self.plants[self.plants['water'] == water]
    watering = self.current_HP + 10
    if water >= 2:
        assert plant.water("sunflower") == "Watering 2 liters of water to sunflower daily" 
        assert plant.water("potato")  == "Watering 5 liters of water to potato daily"
    elif water <2
        assert plant.water('catus') == "Watering 0.5 liter of water to potato daily"
    return watering


    
    
    
def main():
    """Does phase() return the stage of the plant?"""
    with mock.patch("builtins.input", side_effect=["Alice", "27"]):
        assert myproject.get_user_info() == ("Alice", 27)
