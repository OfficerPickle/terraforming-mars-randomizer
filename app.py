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
    if include_amazonis:
        maps.append("Amazonis Planitia")

    # Button to go to the options page
    if st.button("Show Options"):
        st.session_state.page = "options"
        st.rerun()  # Force rerun to refresh the page and navigate to options

    # Submit button for game randomization
    if st.button("Submit"):
        if len(player_list) > 0:
            selected_map, selected_colonies = randomize_setup(len(player_list), maps)
            first_player = random.choice(player_list)

            # Show results
            st.markdown(f"<div style='text-align: center;'><h3 style='color: #FF6F20;'>Game Setup for {', '.join(player_list)}</h3></div>", unsafe_allow_html=True)
            st.write(f"**Selected Map**: {selected_map}")
            st.write(f"**Selected Colonies ({len(selected_colonies)})**:")
            for colony in selected_colonies:
                st.write(f"- {colony}")
            st.write(f"\n**First Player**: {first_player}")
        else:
            st.write("Please enter player names.")

# Options Page (where maps and colonies are listed)
elif st.session_state.page == "options":
    # Show available maps and colonies in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Available Maps:")
        for i, map in enumerate(maps[:len(maps)//2]):  # First half of the maps
            st.write(f"- {map}")
    
    with col2:
        st.subheader("Available Colonies:")
        for i, colony in enumerate(colonies[:len(colonies)//2]):  # First half of the colonies
            st.write(f"- {colony}")

    # Add the second half of maps and colonies in the opposite columns
    with col1:
        for i, map in enumerate(maps[len(maps)//2:]):  # Second half of the maps
            st.write(f"- {map}")
    
    with col2:
        for i, colony in enumerate(colonies[len(colonies)//2:]):  # Second half of the colonies
            st.write(f"- {colony}")

    # Button to go back to the main page
    if st.button("Back"):
        st.session_state.page = "main"
        st.rerun()  # Force rerun to refresh and go back to the main page
