import os

pokemon_list = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
    "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat",
    "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat",
    "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck",
    "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag",
    "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop",
    "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel",
    "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta",
    "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch’d",
    "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
    "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno",
    "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor",
    "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing",
    "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan",
    "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie",
    "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir",
    "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee",
    "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar",
    "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos",
    "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew",
    "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion",
    "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot",
    "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat",
    "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi",
    "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos",
    "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip",
    "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma",
    "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking",
    "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress",
    "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish",
    "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring",
    "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid",
    "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom",
    "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle",
    "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank",
    "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar",
    "Tyranitar", "Lugia", "Ho-Oh", "Celebi", "Glaceon", "Leafeon",
    "Sylveon", "Tangrowth", "Togekiss", "Weavile", "Honchcrow", "Mismagius",
    "Electivire", "Magmortar", "Magnezone", "Rhyperior", "Porygon-Z", "Yanmega",
    "Gliscor", "Mamoswine", "Munchlax"
]

def find_words_in_files(directory, words):
    """
    Search for words in files within a directory.

    Args:
        directory (str): Path to the directory to search.
        words (list): List of words to search for.

    Returns:
        dict: A dictionary where keys are filenames and values are lists of matching words.
    """
    matches = {}

    # Convert words list to a set for faster searching
    words_set = set(words)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    # Find matching words in the file content
                    file_matches = [word for word in words_set if word in content]
                    if file_matches:
                        matches[file_path] = file_matches
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")

    return matches

# Example usage
if __name__ == "__main__":
    directory_path = "./data/pokemon/dex_entries"
    words_to_search = pokemon_list

    result = find_words_in_files(directory_path.strip(), [word.strip() for word in words_to_search])


    if result:
        print(str(len(result.items())) + " Matches found:")
        for file, matched_words in sorted(result.items()):
            print(f"File: {file}")
            print(f"Matched Words: {', '.join(matched_words)}")
            print("-" * 40)
    else:
        print("No matches found.")
