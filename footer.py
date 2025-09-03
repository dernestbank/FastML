# A footer for S@D@ lab pennstate chemical engineering
import streamlit as st

# st.markdown("""
#     <style>
#         .reportview-container .main footer {visibility: hidden;}
#     </style>
#     """,unsafe_allow_html=True)
# st.markdown("""
#     <div style="position: fixed; bottom: 0; width: 100%; text-align: center;">
#         <p style="font-size:12px;">Developed by <a href="https://www.linkedin.com/in/andrew-lee-2b0a73189/">Andrew Lee</a></p>
#     </div>
#     """,unsafe_allow_html=True)


def add_s2d2_footer():
    """Add the S2D2 Lab footer to the page."""
    st.markdown("""
    ---
    *Powered by [S2D2 LAB | PSU](https://s2d2lab.notion.site/) - Sustainable Design, Systems, and Decision-making (S2D2) Group  
    Department of Chemical Engineering at Penn State*
    """)
