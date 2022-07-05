from dataclasses import dataclass
from random import choice
from dataclasses import dataclass

def roll_dice(number_of_dice: int):
    """
    >>> roll_dice(5) # doctest: +ELLIPSIS
    [...]

    >>> roll_dice(4) # doctest: +ELLIPSIS
    [...]
    >>> roll_dice(4) # doctest: +ELLIPSIS
    [...]

    :param number_of_dice:
    :return:
    """
    list_of_dice = []
    for x in range(1, number_of_dice + 1):
        dice_val = choice(range(1, 11))
        list_of_dice.insert(x-1, dice_val)
    return list_of_dice


def validate_value_of_dice(player_choice: list, list_of_dice: list, list_of_player_choices: list):
    """
    # it's user first turn and there are no previous inputs & user selects unequal dice
    >>> validate_value_of_dice([1,2,3],[5,6,5,1,7,8,5,10,9,5],[])
    False

    # it's user first turn and there are no previous inputs & user selects equal dice
    >>> validate_value_of_dice([1,3,7,10],[5,6,5,1,7,8,5,10,9,5],[])
    True

    # it's not users first turn, there are previous inputs & newly selected element is not equal to existing element
    >>> validate_value_of_dice([1,3,7,10],[5,6,5,1,7,8,5,10,9,5],[6])
    False

    # it's not users first turn, there are previous inputs & newly selected element is not equal to existing element
    >>> validate_value_of_dice([1,3,7,10],[5,6,5,1,7,8,5,10,9,5],[6,6])
    False

   # it's not users first turn, there are previous inputs & newly selected element is equal to existing element
    >>> validate_value_of_dice([1,3,7,10],[5,6,5,1,7,8,5,10,9,5],[5,5,5])
    True
    """
    result = False
    extracted_list = []
    for x in player_choice:
        extracted_list.append(list_of_dice[x-1])

    if not list_of_player_choices:
        result = all(ele == extracted_list[0] for ele in extracted_list)
        list_of_player_choices.extend(extracted_list)
        return result

    if list_of_player_choices[0] == extracted_list[0]:
        list_of_player_choices.extend(extracted_list)
        result = True

    return result


def choose_dice(list_of_dice: list):
    """

    >>> choose_dice(list_of_dice=[1,2,3,3])
    Input dice numbers you want to select [1, 2, 3, 3] separated by commas or 0 to roll next:[3, 4]

    >>> choose_dice(list_of_dice=[5,5,5,5])
    Input dice numbers you want to select [5, 5, 5, 5] separated by commas or 0 to roll next:[1, 2, 3, 4]

    """
    user_choices: list[int] = []
    user_choices: list[int] = [int(x) for x in input(f"Input dice numbers you want to select {list_of_dice} "
                                                     f"separated by commas or 0 to roll next:") if not x == ","]
    return user_choices


def play():
    list_of_player_choices = []
    number_of_dice = 10
    number_of_tries = 0
    while number_of_dice > 0:
        number_of_tries = number_of_tries + 1
        list_of_dice = roll_dice(number_of_dice=number_of_dice)
        player_choice = choose_dice(list_of_dice=list_of_dice)
        if 0 in player_choice:
            continue
        if validate_value_of_dice(player_choice, list_of_dice, list_of_player_choices):
            print(list_of_player_choices)
            number_of_dice = number_of_dice - len(player_choice)
        else:
            print("Wrong Choice")

    print(f"You won the game in {number_of_tries} tries")


if __name__ == "__main__":
    play()