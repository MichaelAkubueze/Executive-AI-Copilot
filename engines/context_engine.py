import streamlit as st


# ===========================================
# Initialize Memory
# ===========================================

def _init_memory():

    if "conversation_memory" not in st.session_state:

        st.session_state.conversation_memory = {}


# ===========================================
# Save
# ===========================================

def remember(key, value):

    _init_memory()

    st.session_state.conversation_memory[key] = value


# ===========================================
# Retrieve
# ===========================================

def recall(key):

    _init_memory()

    return st.session_state.conversation_memory.get(key)


# ===========================================
# Retrieve Entire Memory
# ===========================================

def get_memory():

    _init_memory()

    return st.session_state.conversation_memory


# ===========================================
# Clear Memory
# ===========================================

def clear_memory():

    st.session_state.conversation_memory = {}
    
    