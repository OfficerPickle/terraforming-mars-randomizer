import streamlit as st
import random
import time

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
if "selected_maps" not in st.session_state:
    st.session_state.selected_maps = default_maps.copy()
if "selected_colonies" not in st.session_state:
    st.session_state.selected_colonies = default_colonies.copy()

# Function to randomize map and colonies
def randomize_setup(player_count, maps, colonies):
    num_colonies = max(5, player_count + 2)
    selected_colonies = random.sample(colonies, num_colonies)
    selected_map = random.choice(maps)
    return selected_map, selected_colonies

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

    # Button to go to the map/colony selection page
    if st.button("Select Maps & Colonies"):
        st.session_state.page = "options"
        st.rerun()

    # Submit button for game randomization
    if st.button("Submit"):
        if len(player_list) > 0:
            selected_map, selected_colonies = randomize_setup(
                len(player_list), st.session_state.selected_maps, st.session_state.selected_colonies
            )
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

# Options Page (where maps and colonies can be selected)
elif st.session_state.page == "options":
    st.subheader("Select Maps")
    for map in default_maps:
        if map not in st.session_state.selected_maps:
            st.session_state.selected_maps.append(map)  # Reset selection if it was removed
        checkbox = st.checkbox(map, value=(map in st.session_state.selected_maps))
        if checkbox:
            if map not in st.session_state.selected_maps:
                st.session_state.selected_maps.append(map)
        else:
            if map in st.session_state.selected_maps:
                st.session_state.selected_maps.remove(map)

    st.subheader("Select Colonies")
    for colony in default_colonies:
        if colony not in st.session_state.selected_colonies:
            st.session_state.selected_colonies.append(colony)  # Reset selection if it was removed
        checkbox = st.checkbox(colony, value=(colony in st.session_state.selected_colonies))
        if checkbox:
            if colony not in st.session_state.selected_colonies:
                st.session_state.selected_colonies.append(colony)
        else:
            if colony in st.session_state.selected_colonies:
                st.session_state.selected_colonies.remove(colony)

    st.markdown("<i>Amazonis Planitia map only used if selected</i>", unsafe_allow_html=True)

    # Button to go back to the main page
    if st.button("Back"):
        st.session_state.page = "main"
        st.rerun()
