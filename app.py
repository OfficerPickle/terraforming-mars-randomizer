import streamlit as st

# List of available maps and colonies
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

# Initialize session state for map and colony selection
if "selected_maps" not in st.session_state:
    st.session_state.selected_maps = default_maps[:-1]  # Exclude Amazonis Planitia by default
if "selected_colonies" not in st.session_state:
    st.session_state.selected_colonies = default_colonies

# Maps and Colonies Selection Page
st.title("Customize Game Options")

# Select Maps
st.subheader("Select Maps")
col1, col2 = st.columns(2)

# Display maps in two columns
for idx, map in enumerate(default_maps):
    with (col1 if idx % 2 == 0 else col2):
        if map == "Amazonis Planitia":
            checkbox = st.checkbox(
                f"{map} *",
                value=False,  # Ensure it is unchecked by default
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

# Select Colonies
st.subheader("Select Colonies")
col1, col2 = st.columns(2)

# Display colonies in two columns
for idx, colony in enumerate(default_colonies):
    with (col1 if idx % 2 == 0 else col2):
        checkbox = st.checkbox(
            colony, value=(colony in st.session_state.selected_colonies)
        )
        if checkbox:
            if colony not in st.session_state.selected_colonies:
                st.session_state.selected_colonies.append(colony)
        else:
            if colony in st.session_state.selected_colonies:
                st.session_state.selected_colonies.remove(colony)

# Display selected maps and colonies for debugging or confirmation
st.subheader("Selected Options")
st.write(f"**Selected Maps**: {', '.join(st.session_state.selected_maps)}")
st.write(f"**Selected Colonies**: {', '.join(st.session_state.selected_colonies)}")

# Submit button to proceed
if st.button("Submit"):
    st.write("Game setup options have been saved.")
