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
        st.session_state.page = "options"
        st.rerun()

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

                # Show results on a new page
                st.session_state.page = "results"
                st.session_state.selected_map = selected_map
                st.session_state.selected_colonies = selected_colonies
                st.session_state.first_player = first_player
                st.rerun()
        else:
            st.write("Please enter player names.")

# Results Page (display the final result on a clean page)
elif st.session_state.page == "results":
    st.markdown("<div style='text-align: center;'><h3 style='color: #FF6F20;'>Game Setup</h3></div>", unsafe_allow_html=True)
    st.write(f"**Selected Map**: {st.session_state.selected_map}")
    st.write(f"**Selected Colonies ({len(st.session_state.selected_colonies)})**:")
    for colony in st.session_state.selected_colonies:
        st.write(f"- {colony}")
    st.write(f"\n**First Player**: {st.session_state.first_player}")

    # Button to go back to the main page
    if st.button("Back to Main Page"):
        st.session_state.page = "main"
        st.rerun()

