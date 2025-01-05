import streamlit as st
import random
import time

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
def randomize_setup(player_count, maps):
    num_colonies = max(5, player_count + 2)
    selected_colonies = random.sample(colonies, num_colonies)
    selected_map = random.choice(maps)
    return selected_map, selected_colonies

# Add the logo at the top with increased size (image located in the same directory)
st.image("Terraforming-Mars-logo-with-shadow.png", width=500, use_container_width=True)

# Add the words "Game Randomizer" below the logo
st.markdown(
    """
    <div style="text-align: center;">
        <h2 style="color: #FF6F20;">Game Randomizer</h2>
    </div>
    """, unsafe_allow_html=True
)

# Change the background color to black
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: black;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: black;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

# Input player names in 5 smaller text boxes
player1 = st.text_input("Player 1", "")
player2 = st.text_input("Player 2", "", placeholder="Leave blank if not used")
player3 = st.text_input("Player 3", "", placeholder="Leave blank if not used")
player4 = st.text_input("Player 4", "", placeholder="Leave blank if not used")
player5 = st.text_input("Player 5", "", placeholder="Leave blank if not used")

# Collect non-empty player names into a list
player_list = [player for player in [player1, player2, player3, player4, player5] if player]

# Checkbox to include "Amazonis Planitia"
include_amazonis = st.checkbox("Include Amazonis Planitia in the map pool")

# If checkbox is checked, add "Amazonis Planitia" to the maps list
if include_amazonis:
    maps.append("Amazonis Planitia")

# Button to show available maps and colonies
if st.button("Show Options"):
    st.subheader("Available Maps:")
    for map in maps:
        st.write(f"- {map}")

    st.subheader("Available Colonies:")
    for colony in colonies:
        st.write(f"- {colony}")

# Add a submit button
if st.button("Submit"):
    if len(player_list) > 0:
        # Randomize map and colonies
        selected_map, selected_colonies = randomize_setup(len(player_list), maps)

        # Select a first player (we'll animate this)
        first_player = random.choice(player_list)

        # Slot machine animation effect for the map
        map_placeholder = st.empty()
        map_animation_duration = 0.5  # Reduced to make the spin faster
        num_spins = 10  # Fewer spins for faster animation
        for _ in range(num_spins):
            random_map = random.choice(maps)
            map_placeholder.text(f"Choosing map: {random_map}")
            time.sleep(map_animation_duration / num_spins)
        map_placeholder.empty()  # Clear the map animation once it finishes

        # Slot machine animation effect for the colonies
        colonies_placeholder = st.empty()
        colonies_animation_duration = 0.5  # Reduced to make the spin faster
        for _ in range(num_spins):
            random_colony = random.choice(colonies)
            colonies_placeholder.text(f"Choosing colonies: {random_colony}")
            time.sleep(colonies_animation_duration / num_spins)
        colonies_placeholder.empty()  # Clear the colonies animation once it finishes

        # Slot machine animation effect for the first player
        player_placeholder = st.empty()
        player_animation_duration = 0.5  # Reduced to make the spin faster
        for _ in range(num_spins):
            random_player = random.choice(player_list)
            player_placeholder.text(f"Choosing first player: {random_player}")
            time.sleep(player_animation_duration / num_spins)
        player_placeholder.empty()  # Clear the player animation once it finishes

        # Format the player list with "and" before the last player
        if len(player_list) > 1:
            player_display = ", ".join(player_list[:-1]) + " and " + player_list[-1]
        else:
            player_display = player_list[0]

        # Display the final results after all animations are complete
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h3 style="color: #FF6F20;">Game Setup for {player_display}</h3>
            </div>
            """, unsafe_allow_html=True
        )
        st.write(f"**Selected Map**: {selected_map}")

        # Display the number of selected colonies in the format "Selected Colonies(x)"
        st.write(f"**Selected Colonies ({len(selected_colonies)})**:")

        # Loop through and display each selected colony
        for colony in selected_colonies:
            st.write(f"- {colony}")

        # Display the first player
        st.write(f"\n**First Player**: {first_player}")
    else:
        st.write("Please enter player names.")
