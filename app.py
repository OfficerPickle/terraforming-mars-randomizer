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

# Add custom CSS for buttons and background image
st.markdown(
    """
    <style>
    /* Set Mars image as background */
    body {
        background-image: url('static/mars.jpg');
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    
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
    
    .stImage {
        width: 100%;
        margin-bottom: 20px;
    }
    
    .copyright {
        font-size: small;
        color: #555;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Handle "results page" separately
if st.session_state.show_results:
    with st.spinner("Randomizing game setup..."):
        time.sleep(2)

    player_list = st.session_state.get("player_list", [])
    if len(player_list) > 1:
        player_list[-1] = "and " + player_list[-1]

    selected_map, selected_colonies = randomize_setup(
        len(player_list), st.session_state.selected_maps, st.session_state.selected_colonies
    )
    first_player = random.choice(player_list)

    st.image("terraforming-mars-logo-with-shadow.png", use_container_width=True)
    st.markdown(f"<div style='text-align: center;'><h3 style='color: #FF6F20;'>Game Setup for {', '.join(player_list)}</h3></div>", unsafe_allow_html=True)
    st.write(f"**Selected Map**: {selected_map}")
    st.write(f"**Selected Colonies ({len(selected_colonies)})**:")
    for colony in selected_colonies:
        st.write(f"- {colony}")
    st.write(f"\n**First Player**: {first_player}")

    if st.button("Back to Main Page"):
        st.session_state.show_results = False
        st.session_state.player_list = []
        st.rerun()

# Main Page (where players input their names and set options)
elif st.session_state.page == "main":
    st.image("terraforming-mars-logo-with-shadow.png", use_container_width=True)
    st.markdown("<div style='text-align: center;'><h2 style='color: #FF6F20;'>Game Randomizer</h2></div>", unsafe_allow_html=True)

    player1 = st.text_input("Player 1", "")
    player2 = st.text_input("Player 2", "", placeholder="Leave blank if not used")
    player3 = st.text_input("Player 3", "", placeholder="Leave blank if not used")
    player4 = st.text_input("Player 4", "", placeholder="Leave blank if not used")
    player5 = st.text_input("Player 5", "", placeholder="Leave blank if not used")

    player_list = [player for player in [player1, player2, player3, player4, player5] if player]

    st.session_state.player_list = player_list

    if st.button("Select Maps & Colonies"):
        st.session_state.page = "options"
        st.rerun()

    randomize_button = st.button("Randomize!", key="randomize_button", use_container_width=True)

    if randomize_button:
        if len(player_list) > 0:
            st.session_state.show_results = True
            st.rerun()
        else:
            st.write("Please enter player names.")

    st.markdown(
        "<div class='copyright'>"
        "Copyright (c) 2025, John Piccirilli. All rights reserved."
        "</div>", unsafe_allow_html=True
    )

# Options Page (where maps and colonies can be selected)
elif st.session_state.page == "options":
    st.subheader("Select Maps")

    # Input custom maps and checkboxes
    custom_map_1 = st.text_input("Custom Map 1", "", key="custom_map_1")
    custom_map_2 = st.text_input("Custom Map 2", "", key="custom_map_2")

    col1, col2 = st.columns(2)

    for idx, map in enumerate(default_maps):
        with (col1 if idx % 2 == 0 else col2):
            checkbox = st.checkbox(map, value=(map in st.session_state.selected_maps))
            if checkbox:
                if map not in st.session_state.selected_maps:
                    st.session_state.selected_maps.append(map)
            else:
                if map in st.session_state.selected_maps:
                    st.session_state.selected_maps.remove(map)

    # Display custom map textboxes with checkboxes
    st.checkbox(custom_map_1, label=custom_map_1)
    st.checkbox(custom_map_2, label=custom_map_2)

    st.subheader("Select Colonies")

    for idx, colony in enumerate(default_colonies):
        checkbox = st.checkbox(colony, value=(colony in st.session_state.selected_colonies))
        if checkbox:
            if colony not in st.session_state.selected_colonies:
                st.session_state.selected_colonies.append(colony)
        else:
            if colony in st.session_state.selected_colonies:
                st.session_state.selected_colonies.remove(colony)

    if st.button("Back"):
        st.session_state.page = "main"
        st.rerun()
