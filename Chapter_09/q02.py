# Exercise 2
EUROPE = 1
ASIA = 2
AFRICA = 3
AMERICA = 4
AUSTRALIA_AND_OCEANIA = 5
ALL_WORLD = 6
EXIT = 7

import random

def main():
    print("Guess the capital!")
    choice = show_menu()
    while choice != EXIT:
        game(choice)
        choice = show_menu()
    print("Program exiting.")

def show_menu():
    print("Choose the part of the world you want to guess from:")
    print("1. Europe\n2. Asia\n3. Africa\n4. America\n5. Australia and Oceania\n6. Whole world\n7. Exit program")
    while True:
        try:
            choice = int(input("Select a menu item: "))
            if choice > EXIT or choice < EUROPE:
                print("This menu item is not available.")
            else:
                break
        except Exception:
            print("Error. Please try again.")
    return choice

def game(choice):
    countries = get_countries(choice)
    print("\nThe quiz begins!")
    correct_answers = 0
    while correct_answers < len(countries):
        key = random.choice(list(countries))
        value = input(f"Country: {key}\nCapital: ")
        value = value.strip()
        if countries[key] == value:
            print("Correct!")
            correct_answers += 1
            del countries[key]
        else:
            print("Incorrect!")
            print(f"The capital of this country is: {countries[key]}")
        cont = input("\nEnter 'y' to continue: ")
        if cont.lower() != 'y':
            break

def get_countries(choice):
    europe = {"Netherlands": "Amsterdam", "Andorra": "Andorra la Vella", "Greece": "Athens", "Serbia": "Belgrade",
              "Germany": "Berlin", "Switzerland": "Bern", "Slovakia": "Bratislava", "Belgium": "Brussels",
              "Hungary": "Budapest", "Romania": "Bucharest", "Liechtenstein": "Vaduz", "Malta": "Valletta",
              "Poland": "Warsaw", "Vatican": "Vatican", "Austria": "Vienna", "Lithuania": "Vilnius",
              "Ireland": "Dublin", "Croatia": "Zagreb", "Ukraine": "Kyiv", "Moldova": "Chisinau",
              "Denmark": "Copenhagen", "Portugal": "Lisbon", "United Kingdom": "London", "Slovenia": "Ljubljana",
              "Luxembourg": "Luxembourg", "Spain": "Madrid", "Belarus": "Minsk", "Monaco": "Monaco",
              "Russia": "Moscow", "Norway": "Oslo", "France": "Paris", "Montenegro": "Podgorica",
              "Czech Republic": "Prague", "Iceland": "Reykjavik", "Latvia": "Riga", "Italy": "Rome",
              "San Marino": "San Marino", "Bosnia and Herzegovina": "Sarajevo", "North Macedonia": "Skopje", "Bulgaria": "Sofia",
              "Sweden": "Stockholm", "Estonia": "Tallinn", "Albania": "Tirana", "Finland": "Helsinki",
              "Turkey": "Ankara", "Kazakhstan": "Astana", "Azerbaijan": "Baku", "Armenia": "Yerevan", "Cyprus": "Nicosia", "Georgia": "Tbilisi"}

    asia = {"Turkey": "Ankara", "Kazakhstan": "Astana", "Azerbaijan": "Baku", "Armenia": "Yerevan", "Cyprus": "Nicosia", "Georgia": "Tbilisi",
            "UAE": "Abu Dhabi", "Jordan": "Amman", "Turkmenistan": "Ashgabat", "Iraq": "Baghdad",
            "Thailand": "Bangkok", "Brunei": "Bandar Seri Begawan", "Lebanon": "Beirut", "Kyrgyzstan": "Bishkek",
            "Laos": "Vientiane", "Bangladesh": "Dhaka", "Syria": "Damascus", "India": "Delhi",
            "Indonesia": "Jakarta", "East Timor": "Dili", "Qatar": "Doha", "Tajikistan": "Dushanbe",
            "Israel": "Jerusalem", "Pakistan": "Islamabad", "Afghanistan": "Kabul", "Nepal": "Kathmandu",
            "Malaysia": "Kuala Lumpur", "Maldives": "Male", "Bahrain": "Manama", "Philippines": "Manila",
            "Oman": "Muscat", "Myanmar": "Naypyidaw", "China": "Beijing", "Cambodia": "Phnom Penh",
            "North Korea": "Pyongyang", "Yemen": "Sanaa", "South Korea": "Seoul", "Singapore": "Singapore",
            "Uzbekistan": "Tashkent", "Iran": "Tehran", "Japan": "Tokyo", "Bhutan": "Thimphu",
            "Mongolia": "Ulaanbaatar", "Vietnam": "Hanoi", "Sri Lanka": "Sri Jayawardenepura Kotte", "Kuwait": "Kuwait City", "Saudi Arabia": "Riyadh"}

    africa = {"Nigeria": "Abuja", "Ethiopia": "Addis Ababa", "Ghana": "Accra", "Algeria": "Algiers",
              "Madagascar": "Antananarivo", "Eritrea": "Asmara", "Mali": "Bamako", "CAR": "Bangui",
              "Gambia": "Banjul", "Guinea-Bissau": "Bissau", "Congo": "Brazzaville", "Seychelles": "Victoria",
              "Namibia": "Windhoek", "Botswana": "Gaborone", "Burundi": "Gitega", "Senegal": "Dakar",
              "Djibouti": "Djibouti", "South Sudan": "Juba", "Tanzania": "Dodoma", "Egypt": "Cairo",
              "Uganda": "Kampala", "Rwanda": "Kigali", "DR Congo": "Kinshasa", "Guinea": "Conakry",
              "Gabon": "Libreville", "Malawi": "Lilongwe", "Togo": "Lome", "Angola": "Luanda",
              "Zambia": "Lusaka", "Mozambique": "Maputo", "Lesotho": "Maseru", "Eswatini": "Mbabane",
              "Somalia": "Mogadishu", "Liberia": "Monrovia", "Comoros": "Moroni", "Kenya": "Nairobi",
              "Sudan": "Khartoum", "Morocco": "Rabat", "Libya": "Tripoli", "Tunisia": "Tunis"}

    america = {"Paraguay": "Asuncion", "USA": "Washington", "Canada": "Ottawa", "Mexico": "Mexico City"}

    australia_and_oceania = {"Australia": "Canberra", "New Zealand": "Wellington", "Fiji": "Suva"}

    continents = [europe, asia, africa, america, australia_and_oceania]
    if choice == ALL_WORLD:
        all_world = {}
        for continent in continents:
            all_world.update(continent)
        return all_world
    else:
        return continents[choice - 1]

main()

