#!/usr/bin/env python3
"""Application Streamlit pour explorer les référentiels PMSI"""

import streamlit as st
import refpymsi as rp
import pandas as pd
import json

# Configuration
st.set_page_config(page_title="refpymsi Explorer", layout="wide")

# Cache
@st.cache_data
def get_tables():
    return rp.list_available_tables()

@st.cache_data
def get_listes():
    return rp.list_available_listes()

@st.cache_data
def load_table(name):
    return rp.get_table(name, plrs=False)

@st.cache_data
def load_liste(name):
    return rp.get_liste(name)

# Interface
st.title("refpymsi Explorer")

# Navigation
page = st.sidebar.radio("Navigation", ["Tables", "Listes", "Recherche"])
st.sidebar.caption(f"v2026.0.0 | {len(get_tables())} tables | {len(get_listes())} listes")

# Tables
if page == "Tables":
    st.header("Tables de référence")
    
    search_term = st.text_input("Rechercher", placeholder="ccam, tarifs, cim")
    tables = get_tables()
    
    if search_term:
        tables = [t for t in tables if search_term.lower() in t.lower()]
    
    selected = st.selectbox("Table", tables)
    
    if selected:
        with st.spinner("Chargement..."):
            try:
                df = load_table(selected)
                st.caption(f"{len(df):,} lignes × {len(df.columns)} colonnes")
                
                if st.checkbox("Afficher toutes les données"):
                    st.dataframe(df, use_container_width=True)
                else:
                    st.dataframe(df.head(100), use_container_width=True)
                
                st.download_button("CSV", df.to_csv(index=False), f"{selected}.csv", "text/csv")
                
            except Exception as e:
                st.error(f"Erreur: {e}")

# Listes
elif page == "Listes":
    st.header("Listes thématiques")
    
    search_term = st.text_input("Rechercher", placeholder="cancer, rea, chir")
    listes = get_listes()
    
    if search_term:
        listes = [l for l in listes if search_term.lower() in l.lower()]
    
    selected = st.selectbox("Liste", listes)
    
    if selected:
        with st.spinner("Chargement..."):
            try:
                data = load_liste(selected)
                st.json(data)
                st.download_button("JSON", json.dumps(data, indent=2), f"{selected}.json", "application/json")
                
            except Exception as e:
                st.error(f"Erreur: {e}")

# Recherche
elif page == "Recherche":
    st.header("Recherche")
    
    query = st.text_input("Mot-clé", placeholder="cancer, cardiologie")
    
    if query:
        matching_tables = [t for t in get_tables() if query.lower() in t.lower()]
        matching_listes = [l for l in get_listes() if query.lower() in l.lower()]
        
        st.subheader(f"Résultats ({len(matching_tables) + len(matching_listes)})")
        
        if matching_tables:
            st.markdown("**Tables:**")
            st.write(", ".join(matching_tables[:10]))
        
        if matching_listes:
            st.markdown("**Listes:**")
            st.write(", ".join(matching_listes[:10]))

st.caption("refpymsi v2026.0.0")
