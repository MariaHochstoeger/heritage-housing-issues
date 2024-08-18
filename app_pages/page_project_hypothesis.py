import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"* We hypothesize that the higher the overall quality "
        f" ('OverallQual') of a property, the higher the sale price. \n\n"
        f"  * The correlation study of the dataset supports that. \n\n"
        f"* We hypothesize that the higher the size of a property "
        f" ('TotalBsmtSF'), the higher the sale price. \n\n"
        f"  * The correlation study confirmed this. \n\n"
    )