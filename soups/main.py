from __future__ import annotations
from dataclasses import dataclass, field

from typing import List

OptionType = List[int]

@dataclass
class MenuOptions():
    Option1: OptionType = field(default_factory= lambda: [100, 0]) 
    Option2: OptionType = field(default_factory= lambda: [75, 25]) 
    Option3: OptionType = field(default_factory= lambda: [50, 50]) 
    Option4: OptionType = field(default_factory= lambda: [25, 75])


@dataclass
class IsPotEmpty():
    emptyA:bool = False
    emptyB:bool = False
    emptyAB:bool = False



@dataclass
class SoupStation():
    """We will use soup pots in our probability tree"""

    N_start:  int 
    Na: int = field(init=False)
    Nb: int = field(init=False)

    Options: MenuOptions = MenuOptions()
    PotState: IsPotEmpty = IsPotEmpty()

    def __post_init__(self):
        self.Na = self.N_start
        self.Nb = self.N_start

    def serve(self: SoupStation, soup_choice: OptionType) -> int:

        """Serves customer a soup option from the menu and changes the state of the Soup """

        #check if we can serve soup
        pot_state_list = [value for key, value in self.PotState.__dict__.items() if not key.startswith('__')]

        if any(pot_state_list):
            return -1
        
        soup_a_left, soup_b_left =  self.Na - soup_choice[0], self.Nb - soup_choice[1]

        if soup_a_left <= 0 and soup_b_left != 0 :
            soup_a_left = 0
            self.PotState.emptyA = True
            self.Na, self.Nb = soup_a_left, soup_b_left
            return -1


        if soup_b_left <= 0 and soup_a_left !=0:
            soup_b_left = 0 
            self.PotState.emptyB = True
            self.Na, self.Nb = soup_a_left, soup_b_left
            return -1
        
        if soup_a_left <=0 and soup_b_left<=0:
            soup_a_left, soup_b_left = 0, 0
            self.PotState.emptyAB = True
            self.Na, self.N.b = soup_a_left, soup_b_left
            return -1
        
        self.Na, self.Nb = soup_a_left, soup_b_left
        
        return 1



        




pot = SoupStation(250)

print("pot state: ", pot.PotState, "soup A ", pot.Na, "soup B ", pot.Nb)
print("result", pot.serve(MenuOptions().Option1))
print("pot state: ", pot.PotState, "soup A ", pot.Na, "soup B ", pot.Nb)
print("result", pot.serve(MenuOptions().Option1))
print("pot state: ", pot.PotState, "soup A ", pot.Na, "soup B ", pot.Nb)
print("result", pot.serve(MenuOptions().Option1))
print("pot state: ", pot.PotState, "soup A ", pot.Na, "soup B ", pot.Nb)


# print(IsPotEmpty(1))
    