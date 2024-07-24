import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Welcome", "Try it", "Connect"])

# Import the other pages
if page == "Welcome":
    st.title("Island Survival Challenge 🌊🏝️")
    st.header("Ahoy there, intrepid problem solver! 🌊🏝️")
    st.markdown("""
    Picture this: you've stumbled upon a quaint island paradise, a serene patch of land blissfully floating in a vast ocean. This island, neatly divided into sections like a giant checkerboard, is your new playground. But, hold onto your sunhat—things are about to get interesting!

    Each year, the sea decides to throw a party, and by "party," we mean it rises a little bit higher, inch by inch, year by year. As the waves climb, they hungrily swallow up parts of the island, turning land into watery depths. Your mission, should you choose to accept it, is to figure out how much of this charming island remains above sea level after each year.

    Here's the twist: the island isn’t just sinking quietly. Oh no! When a section sinks, it drags its neighbors down with it, like a bad game of dominoes. Vertically or horizontally adjacent sections with lower or equal elevation to the sea level will join the underwater party. This chain reaction continues until all eligible sections are submerged.

    So, brave adventurer, for each year from 1 to Y, can you determine the area of the island that bravely stands above the ever-rising sea? Let's see if you can keep our island afloat (at least a little bit) and win this watery battle against nature! Good luck! 🚀🌴
    """)

    st.header("Problem Statement")

    st.markdown("""
    **Problem Statement**

    Consider an island of size \( H \times W \), surrounded by the sea. The island is divided into \( H \) rows and \( W \) columns of \( 1 \times 1 \) sections. The elevation of the section at the \( i \)-th row from the top and the \( j \)-th column from the left (relative to the current sea level) is given by \( A_{i,j} \).

    Starting from year 0, the sea level rises by 1 each year. A section \( (i, j) \) will sink into the sea if:
    - It is vertically or horizontally adjacent to the sea, or
    - It is vertically or horizontally adjacent to a section that has sunk, and its elevation \( A_{i,j} \) is less than or equal to the current sea level.

    This process continues iteratively for newly sunk sections.

    For each year \( i = 1, 2, \ldots, Y \), find the area of the island that remains above the sea level.

    **Mathematical Formulation**

    1. **Given:**
       - \( H \): Number of rows of the island.
       - \( W \): Number of columns of the island.
       - \( A \): Elevation matrix of size \( H \times W \) where \( A_{i,j} \) represents the elevation of the section at the \( i \)-th row and \( j \)-th column.
       - \( Y \): Number of years to evaluate.

    2. **Sea Level Rise:**
       - At year \( t \), the sea level is \( t \).

    3. **Sinking Criteria:**
       - At year \( t \), a section \( (i, j) \) sinks if:
         - \( A_{i,j} \leq t \) and it is adjacent to the sea or an already sunk section.

    4. **Remaining Area:**
       - For each year \( t \), calculate the number of sections \( (i, j) \) where \( A_{i,j} > t \) and are not sunk due to adjacency rules.

    5. **Output:**
       - For each year \( t = 1, 2, \ldots, Y \), output the area of the island that remains above sea level.

    **Example**

    **Input:**
    - \( H = 3 \)
    - \( W = 3 \)
    - \( A = \begin{bmatrix}
      4 & 3 & 2 \\
      3 & 2 & 1 \\
      2 & 1 & 0 
      \end{bmatrix} \)
    - \( Y = 3 \)

    **Output:**
    - For \( t = 1 \): Remaining area
    - For \( t = 2 \): Remaining area
    - For \( t = 3 \): Remaining area
    """)

elif page == "Try it":
    import page1
    page1.app()
elif page == "Connect":
    import page2
    page2.app()
