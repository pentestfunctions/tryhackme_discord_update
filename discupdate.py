import requests
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Mapping of Discord IDs to TryHackMe usernames
users = {
    "0day": "0day",
    "kalimaxx_": "KaliMax",
    "blackout8210": "Blackout",
    "ssuspect999": "SSuspect999",
    "hoodietramp": "h00dy",
    "_s_rn_m_": "lostmyoldacc",
    "l0g_lab": "l0g",
    "thor0411.": "thor0411",
    "gfyvhlvivt87dfgucvkutdc": "laksar1337",
    "thexmog": "M0G",
    "1_ycan": "1yc4n0rn0t",
    "smurfbox_": "smurfbox",
    "co0k1em0nst3r": "co0k1em0n5t3r",
    "warfare666": "warfare1337",
    "attacker543": "attacker543",
    "mtdembarcadero": "officialalex",
    "xiko0690": "Xik0",
    "kushed3d": "Kushed",
    "xboxcom": "dontwatchme",
    "synchronizity": "Synchronizity",
    "annuals": "mop",
    "tylerr1": "Tylerr1",
    "physcological": "cioto",
    "virtualvices": "vexiata",
    "uhlucid": "lucidBeginner",
    "tcpsolid": "tcpsolid",
    "0x1ak4sh": "0x1Ak4sh",
    "bornunique911": "Bornunique911",
    "obsidian_909":"0bsidian909",
    "youjsgotpwned":"Lamentomori"
}

# Function to get user data from TryHackMe
def get_user_data(username):
    rank_url = f"https://tryhackme.com/api/user/rank/{username}"
    rooms_url = f"https://tryhackme.com/api/no-completed-rooms-public/{username}"
    
    try:
        rank_response = requests.get(rank_url)
        rooms_response = requests.get(rooms_url)
        rank_response.raise_for_status()
        rooms_response.raise_for_status()
        
        rank = rank_response.json().get('userRank', 'N/A')
        
        # Check if the rooms_response is an integer or a JSON
        if rooms_response.headers.get('Content-Type') == 'application/json':
            rooms = rooms_response.json().get('noOfRooms', 'N/A')
        else:
            rooms = rooms_response.text
            
        return rank, rooms
    except requests.RequestException as e:
        print(f"Error retrieving data for {username}: {e}")
        return None, None

# List to store user data
leaderboard = []

# Retrieve data for each user
for discord_id, tryhackme_username in users.items():
    clear_screen()
    print(f"Retrieving data for Discord: {discord_id} TryHackMe: {tryhackme_username}")
    rank, rooms = get_user_data(tryhackme_username)
    if rank is not None and rooms is not None:
        leaderboard.append((discord_id, tryhackme_username, rank, rooms))

# Sort the leaderboard by rank
leaderboard.sort(key=lambda x: int(str(x[2]).replace(',', '')))

# Print the leaderboard
for i, (discord_id, tryhackme_username, rank, rooms) in enumerate(leaderboard, start=1):
    rank_with_commas = f"{int(rank):,}" if rank != 'N/A' else rank
    print(f"{i}. @{discord_id} https://tryhackme.com/p/{tryhackme_username} [Rank {rank_with_commas}] [Rooms {rooms}]")
