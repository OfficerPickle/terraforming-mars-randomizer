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
    # Exclude "Amazonis Planitia" by default
    st.session_state.selected_maps = [map for map in default_maps if map != "Amazonis Planitia"]
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
        st.session_state.page = "options"  # Transition to options page
        st.rerun()  # Use st.rerun instead of experimental_rerun

    # Submit button for game randomization
    if st.button("Submit"):
        if len(player_list) > 0:
            # Show slot machine animation
            with st.spinner('Spinning...'):
                time.sleep(2)  # Simulate a delay for animation

                # Create an empty container for animation
                animation_placeholder = st.empty()

                # Simulate the spinning animation
                for _ in range(10):  # Loop for a number of spins
                    selected_map = random.choice(st.session_state.selected_maps)
                    selected_colonies = random.sample(st.session_state.selected_colonies, max(5, len(player_list) + 2))
                    animation_placeholder.markdown(f"**Spinning...**\nMap: {selected_map}\nColonies: {', '.join(selected_colonies)}")
                    time.sleep(0.1)  # Simulate spin delay

                # Final results after spinning
                selected_map, selected_colonies = randomize_setup(len(player_list), st.session_state.selected_maps, st.session_state.selected_colonies)
                first_player = random.choice(player_list)

                # Store the results in session state for the results page
                st.session_state.page = "results"
                st.session_state.selected_map = selected_map
                st.session_state.selected_colonies = selected_colonies
                st.session_state.first_player = first_player
                st.rerun()  # Use st.rerun instead of experimental_rerun
        else:
            st.write("Please enter player names.")

# Options Page (where maps and colonies can be selected)
elif st.session_state.page == "options":
    st.subheader("Select Maps")
    col1, col2 = st.columns(2)

    # Display maps in two columns
    for idx, map in enumerate(default_maps):
        with (col1 if idx % 2 == 0 else col2):
            # Add special note for Amazonis Planitia
            if map == "Amazonis Planitia":
                checkbox = st.checkbox(
                    f"{map} *",
                    value=(map in st.session_state.selected_maps),
                    help="Not recommended for smaller groups",
                )
                if checkbox:
                    if map not in st.session_state.selected_maps:
                        st.session_state.selected_maps.append(map)
                else:
                    if map in st.session_state.selected_maps:
                        st.session_state.selected_maps.remove(map)
                st.markdown(
                    "<span style='font-size: small; font-style: italic;'>Not recommended for smaller groups</span>",
                    unsafe_allow_html=True,
                )
            else:
                checkbox = st.checkbox(map, value=(map in st.session_state.selected_maps))
                if checkbox:
                    if map not in st.session_state.selected_maps:
                        st.session_state.selected_maps.append(map)
                else:
                    if map in st.session_state.selected_maps:
                        st.session_state.selected_maps.remove(map)

    st.subheader("Select Colonies")
    col3, col4 = st.columns(2)

    # Display colonies in two columns
    for idx, colony in enumerate(default_colonies):
        with (col3 if idx % 2 == 0 else col4):
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
        st.rerun()  # Use st.rerun instead of experimental_rerun

# Results Page (display the final result on a clean page)
elif st.session_state.page == "results":
    st.markdown("<div style='text-align: center;'><h3 style='color: #FF6F20;'>Game Setup</h3></div>", unsafe_allow_html=True)
    
    # Show the slot machine animation on the results page
    with st.spinner('Spinning...'):
        time.sleep(2)  # Simulate a delay for animation
        animation_placeholder = st.empty()

        # Simulate the spinning animation
        for _ in range(10):  # Loop for a number of spins
            selected_map = random.choice(st.session_state.selected_maps)
            selected_colonies = random.sample(st.session_state.selected_colonies, max(5, len(player_list) + 2))
            animation_placeholder.markdown(f"**Spinning...**\nMap: {selected_map}\nColonies: {', '.join(selected_colonies)}")
            time.sleep(0.1)  # Simulate spin delay

    # Show the final results after the animation
    st.write(f"**Selected Map**: {st.session_state.selected_map}")
    st.write(f"**Selected Colonies ({len(st.session_state.selected_colonies)})**:")
    for colony in st.session_state.selected_colonies:
        st.write(f"- {colony}")
    st.write(f"\n**First Player**: {st.session_state.first_player}")

    # Button to go back to the main page
    if st.button("Back to Main Page"):
        st.session_state.page = "main"
        st.rerun()  # Use st.rerun instead of experimental_rerun
