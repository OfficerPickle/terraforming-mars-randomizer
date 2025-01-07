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

# Handle "results page" separately
if st.session_state.show_results:
    # Display spinner before showing results
    with st.spinner("Randomizing game setup..."):
        time.sleep(2)  # Simulate delay for spinning animation

    # Retrieve player list and results
    player_list = st.session_state.get("player_list", [])
    
    # Add "and" before the last player in the list (if applicable)
    if len(player_list) > 1:
        player_list[-1] = "and " + player_list[-1]

    selected_map, selected_colonies = randomize_setup(
        len(player_list), st.session_state.selected_maps, st.session_state.selected_colonies
    )
    first_player = random.choice(player_list)

    # Display results
    st.image("Terraforming-Mars-logo-with-shadow.png", width=500, use_container_width=True)
    st.markdown(f"<div style='text-align: center;'><h3 style='color: #FF6F20;'>Game Setup for {', '.join(player_list)}</h3></div>", unsafe_allow_html=True)
    st.write(f"**Selected Map**: {selected_map}")
    st.write(f"**Selected Colonies ({len(selected_colonies)})**:")
    for colony in selected_colonies:
        st.write(f"- {colony}")
    st.write(f"\n**First Player**: {first_player}")

    # Button to go back to the main page
    if st.button("Back to Main Page"):
        st.session_state.show_results = False
        st.session_state.player_list = []
        st.rerun()

# Main Page (where players input their names and set options)
elif st.session_state.page == "main":
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

    # Display copyright notice at the bottom of the results page
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

    # Initialize custom map state
    if "custom_map_1" not in st.session_state:
        st.session_state.custom_map_1 = ""
    if "custom_map_2" not in st.session_state:
        st.session_state.custom_map_2 = ""

    # Display default maps with checkboxes
    for map in default_maps:
        # Add special note for Amazonis Planitia
        if map == "Amazonis Planitia":
            checkbox = st.checkbox(
                f"{map} *",
                value=(map in st.session_state.selected_maps),
                help="Not recommended for smaller groups",
            )
        else:
            checkbox = st.checkbox(map, value=(map in st.session_state.selected_maps))

        # Update session state based on checkbox
        if checkbox:
            if map not in st.session_state.selected_maps:
                st.session_state.selected_maps.append(map)
        else:
            if map in st.session_state.selected_maps:
                st.session_state.selected_maps.remove(map)

    # Add custom maps text boxes with checkboxes
    custom_map_1 = st.text_input(st.session_state.custom_map_1, placeholder="Enter custom map")
    custom_checkbox_1 = st.checkbox(
        "Enable Custom Map 1",
        value=(custom_map_1 in st.session_state.selected_maps),
        key="custom_map_1_checkbox",
    )
    if custom_checkbox_1 and custom_map_1:
        if custom_map_1 not in st.session_state.selected_maps:
            st.session_state.selected_maps.append(custom_map_1)
    else:
        if custom_map_1 in st.session_state.selected_maps:
            st.session_state.selected_maps.remove(custom_map_1)
    st.session_state.custom_map_1 = custom_map_1

    custom_map_2 = st.text_input(st.session_state.custom_map_2, placeholder="Enter custom map")
    custom_checkbox_2 = st.checkbox(
        "Enable Custom Map 2",
        value=(custom_map_2 in st.session_state.selected_maps),
        key="custom_map_2_checkbox",
    )
    if custom_checkbox_2 and custom_map_2:
        if custom_map_2 not in st.session_state.selected_maps:
            st.session_state.selected_maps.append(custom_map_2)
    else:
        if custom_map_2 in st.session_state.selected_maps:
            st.session_state.selected_maps.remove(custom_map_2)
    st.session_state.custom_map_2 = custom_map_2

    st.subheader("Select Colonies")
    # Display colonies with checkboxes
    for colony in default_colonies:
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

