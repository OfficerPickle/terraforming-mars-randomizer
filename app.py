import streamlit as st
import random

# List of available maps
maps = [
    "Tharsis",
    "Hellas",
    "Elysium",
    "Utopia Planitia",
    "Terra Cimmeria",
    "Vastitas Borealis"
]

# List of available colonies
colonies = [
    "Europa",
    "Ganymede",
    "Io",
    "Callisto",
    "Enceladus",
    "Titan",
    "Pluto",
    "Miranda",
    "Ceres",
    "Luna",
    "Triton"
]

# Function to randomize map and colonies
def randomize_setup(player_count):
    num_colonies = max(5, player_count + 2)
    selected_colonies = random.sample(colonies, num_colonies)
    selected_map = random.choice(maps)
    return selected_map, selected_colonies

# Streamlit user interface
st.title("Terraforming Mars Randomizer")

# Input player names
players = st.text_area("Enter player names, one per line:")

# Split the player names into a list
player_list = players.splitlines()

if len(player_list) > 0:
    # Randomize map and colonies
    selected_map, selected_colonies = randomize_setup(len(player_list))

    # Select a first player
    first_player = random.choice(player_list)

    # Display the results
    st.subheader(f"Game Setup for {', '.join(player_list)}")
    st.write(f"**Selected Map**: {selected_map}")
    st.write("**Selected Colonies**:")
    for colony in selected_colonies:
        st.write(f"- {colony}")
    st.write(f"\n**Starting Player**: {first_player}")
else:
    st.write("Please enter player names.")
