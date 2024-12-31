# Uses streamlit
import streamlit as st

# Define the page title and title 
st.set_page_config(page_title="Statistics Flashcards", layout="centered")
st.title("Machine Learninng Flashcards")

# Define the CSS for background color -- rgb(212, 245, 254)
page_bg_color = """
    <style>
    .stApp {
        background-color:rgb(212, 245, 254); /* Change this to any desired color */
    }
    </style>
"""

# Apply the CSS for bgcolor
st.markdown(page_bg_color, unsafe_allow_html=True)

# Functions
def add_flashcard(question, answer):
    st.session_state.flashcards.append({"question": question, "answer": answer})
def next_card():
    if st.session_state.flashcards:
        st.session_state.index = (st.session_state.index + 1) % len(st.session_state.flashcards)
def prev_card():
    if st.session_state.flashcards:
        st.session_state.index = (st.session_state.index - 1) % len(st.session_state.flashcards)
def get_current_card():
    if st.session_state.flashcards:
        return st.session_state.flashcards[st.session_state.index]
    return None

def load_flashcards(file_path):
    # Read and parse the flashcards from the text file
    flashcards = []
    with open(file_path, 'r') as file:
        # lines = file.readlines()
        contents = file.read()
        lines = contents.split('|')        

        for i in range(0, len(lines), 2):
            question = lines[i].strip()
            answer = lines[i + 1].strip() if i + 1 < len(lines) else "No answer provided"
            flashcards.append({"question": question, "answer": answer})
    return flashcards

if "flashcards" not in st.session_state:
    st.session_state.index = 0
st.session_state.flashcards = load_flashcards('ml_flashcard_data_v1.txt') # QA_stats.txt

st.markdown(
    """
    <style>
    .big-font {font-size:30px !important; font-weight: bold;}
    .small-font {font-size:18px !important;font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True,
)

# View Flashcards
if st.session_state.flashcards:
    current_card = get_current_card()

    st.markdown(f'<p class="big-font">{current_card['question']}</p>', unsafe_allow_html=True)

    if st.button("Show Answer"):
        custom_ans = f"""
            <div style="font-size:20px;">
            {current_card['answer'].replace(".\n", "  \n  \n")}
            </div>
            """
        st.write(custom_ans, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("Previous", on_click=prev_card)
    with col2:
        st.button("Next", on_click=next_card)
else:
    st.info("No flashcards available. Add one to get started!")

# Adds a horizontal line
st.divider() 

st.subheader("Rate yourself in Statistics")
values = st.slider("Rate between 0-10",0.0, 10.0, 1.0)
st.write("Your score:", values,'/10')

# Adds a horizontal line
st.divider() 

# Add image if needed
# st.image("stats_display image.png", caption="Stats",width=500, use_container_width =True )

# Footer
st.caption("Built with ❤️ by Atavale")