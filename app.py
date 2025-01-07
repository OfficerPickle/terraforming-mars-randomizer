import streamlit as st
import random
import time

# Copyright Notice
# Copyright (c) 2025, John Piccirilli
# All rights reserved.

# Default list of available maps and colonies
default_maps = [
    "Tharsis",
    "Hellas",
    "Elysium",
    "Utopia Planitia",
    "Terra Cimmeria",
    "Vastitas Borealis",
    "Amazonis Planitia",
]

default_colonies = [
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
    "Triton",
]

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "main"
if "show_results" not in st.session_state:
    st.session_state.show_results = False
if "selected_maps" not in st.session_state:
    # Exclude "Amazonis Planitia" by default
    st.session_state.selected_maps = [map for map in default_maps if map != "Amazonis Planitia"]
if "selected_colonies" not in st.session_state:
    st.session_state.selected_colonies = default_colonies.copy()
if "player_list" not in st.session_state:
    st.session_state.player_list = []

# Function to randomize map and colonies
def randomize_setup(player_count, maps, colonies):
    num_colonies = max(5, player_count + 2)
    selected_colonies = random.sample(colonies, num_colonies)
    selected_map = random.choice(maps)
    return selected_map, selected_colonies

# Add custom CSS for buttons
st.markdown(
    """
    <style>
    .custom-button {
        background-color: #FF6F20;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.3s;
        display: inline-block;
        margin: 10px 0;
    }
    .custom-button:hover {
        background-color: #E65C1C;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Page (where players input their names and set options)
elif st.session_state.page == "main":
    # Display background image directly using st.image
    st.image("static/mars.jpg", use_column_width=True, clamp=True)
    
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

    # Store player list in session state to persist it
    st.session_state.player_list = player_list

    # Button to go to the map/colony selection page
    if st.button("Select Maps & Colonies"):
        st.session_state.page = "options"
        st.rerun()

    # Custom left-aligned "Randomize!" button (only triggers when clicked)
    randomize_button = st.button("Randomize!", key="randomize_button", use_container_width=True)

    # Display copyright notice at the bottom of the main page
    st.markdown(
        "<div style='text-align: center; font-size: small; color: #555;'>"
        "Copyright (c) 2025, John Piccirilli. All rights reserved."
        "</div>", unsafe_allow_html=True
    )

    # Only run the randomization when the "Randomize!" button is clicked
    if randomize_button:
        if len(player_list) > 0:
            st.session_state.show_results = True
            st.rerun()
        else:
            st.write("Please enter player names.")

# Options Page (where maps and colonies can be selected)
elif st.session_state.page == "options":
    st.subheader("Select Maps")

    # Display maps in one section
    for idx, map in enumerate(default_maps):
        checkbox = st.checkbox(map, value=(map in st.session_state.selected_maps))
        if checkbox:
            if map not in st.session_state.selected_maps:
                st.session_state.selected_maps.append(map)
        else:
            if map in st.session_state.selected_maps:
                st.session_state.selected_maps.remove(map)

    st.subheader("Add Custom Maps")

    # Custom map 1 text box with checkbox
    custom_map_1 = st.text_input("Custom Map 1", key="custom_map_1", max_chars=50)
    custom_map_1_checkbox = st.checkbox(f"Include {custom_map_1}", value=False, key="custom_map_1_checkbox")

    if custom_map_1_checkbox and custom_map_1 not in st.session_state.selected_maps:
        st.session_state.selected_maps.append(custom_map_1)
    elif not custom_map_1_checkbox and custom_map_1 in st.session_state.selected_maps:
        st.session_state.selected_maps.remove(custom_map_1)

    # Custom map 2 text box with checkbox
    custom_map_2 = st.text_input("Custom Map 2", key="custom_map_2", max_chars=50)
    custom_map_2_checkbox = st.checkbox(f"Include {custom_map_2}", value=False, key="custom_map_2_checkbox")

    if custom_map_2_checkbox and custom_map_2 not in st.session_state.selected_maps:
        st.session_state.selected_maps.append(custom_map_2)
    elif not custom_map_2_checkbox and custom_map_2 in st.session_state.selected_maps:
        st.session_state.selected_maps.remove(custom_map_2)

    st.subheader("Select Colonies")
    # Display colonies in one section
    for idx, colony in enumerate(default_colonies):
        checkbox = st.checkbox(colony, value=(colony in st.session_state.selected_colonies))
        if checkbox:
            if colony not in st.session_state.selected_colonies:
                st.session_state.selected_colonies.append(colony)
        else:
            if colony in st.session_state.selected_colonies:
                st.session_state.selected_colonies.remove(colony)

    # Button to go back to the main page
    if st.button("Back"):
        st.session_state.page = "main"
        st.rerun()
