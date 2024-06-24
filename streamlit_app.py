import streamlit as st
import pandas as pd
import altair as alt
import requests

st.title("Welcome To Pokemon Explorer!")

poke_num = st.text_input("Enter a number between 1 and 155")
url = f'https://pokeapi.co/api/v2/pokemon/{poke_num}'

poke_data = requests.get(url).json()
name = poke_data['name']
height = poke_data['height']
weight = poke_data['weight']

col1, col2 = st.columns(2)
with col1:
    st.title(name.title())
    st.text(f"Height = {height}cm")

    st.subheader("Height Bar Chart")
    graph_data = pd.DataFrame({
        'Height': [3, 10, height],
        'Pokemon Characters': ['Caterpie', 'Wartortle', name]
    })

    poke_bar_chart = alt.Chart(graph_data).mark_bar().encode(
        x='Pokemon Characters',
        y='Height'
    )
    st.altair_chart(poke_bar_chart, use_container_width=True)
with col2:
    st.image(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{poke_num}.gif')
    st.text(f"Weight = {weight}kg")

    st.subheader("Weight Bar Chart")
    graph_data = pd.DataFrame({
        'Weight': [3, 10, weight],
        'Pokemon Characters': ['Caterpie', 'Wartortle', name]
    })

    poke_bar_chart = alt.Chart(graph_data).mark_bar().encode(
        x='Pokemon Characters',
        y='Weight'
    )
    st.altair_chart(poke_bar_chart, use_container_width=True)