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

# Function to randomize map and colonies
def randomize_setup(player_count, maps):
    num_colonies = max(5, player_count + 2)
    selected_map = random.choice(maps)
    return selected_map

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "main"  # Start on the main page

# Main Page (where players input their names)
if st.session_state.page == "main":
    st.image("Terraforming-Mars-logo-with-shadow.png", width=500, use_container_width=True)
    st.markdown("<div style='text-align: center;'><h2 style='color: #FF6F20;'>Game Randomizer</h2></div>", unsafe_allow_html=True)

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
    if include_amazonis and "Amazonis Planitia" not in maps:
        maps.append("Amazonis Planitia")

    # Button to go to the options page
    if st.button("Show Maps"):
        st.session_state.page = "options"
        st.rerun()  # Force rerun to refresh the page and navigate to options

    # Submit button for game randomization
    if st.button("Submit"):
        if len(player_list) > 0:
            selected_map = randomize_setup(len(player_list), maps)
            first_player = random.choice(player_list)

            # Show results
            st.markdown(f"<div style='text-align: center;'><h3 style='color: #FF6F20;'>Game Setup for {', '.join(player_list)}</h3></div>", unsafe_allow_html=True)
            st.write(f"**Selected Map**: {selected_map}")
            st.write(f"\n**First Player**: {first_player}")
        else:
            st.write("Please enter player names.")

# Options Page (where maps are listed)
elif st.session_state.page == "options":
    # Show available maps in a single column
    st.subheader("Maps Used:")
    for map in maps:
        st.write(f"- {map}")

    # Button to go back to the main page
    if st.button("Back"):
        st.session_state.page = "main"
        st.rerun()  # Force rerun to refresh and go back to the main page
