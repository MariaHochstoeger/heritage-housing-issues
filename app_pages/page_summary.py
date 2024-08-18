import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Purpose and Motivation**\n\n"
        f" The general pupose of this project is to provide a tool that allows"
        f" a client to predict the potential sale price of a property in"
        f" Ames, Iowa.\n\n"
        f" The client has received an inheritance from a deceased "
        f" great-grandfather located in Ames, Iowa, and is looking for help "
        f" in maximising the sales price for the inherited properties. \n"
        f" Although the client has an excellent understanding of property "
        f" prices in her own state and residential area, she fears that "
        f" basing her estimates for property worth on her current knowledge "
        f" might lead to inaccurate appraisals. What makes a house desirable "
        f" and valuable where she comes from might not be the same in "
        f" Ames, Iowa. She found a public dataset with house prices for "
        f" Ames, Iowa, and provided that.\n \n"
        f"**Project Terminology**\n"
        f"* A **client** is a person who uses this service or product.\n"
        f"* The **sale price** is the estimated value of a home as it"
        f" might be realized on the free market. \n"
        f"* The home, the value of which is being estimated, may be refered to"
        f" as **property, real estate, house, or home**. \n"
        f"* The **features** or **attributes** of a home are characteristics"
        f" used to describe the home. \n \n"
        f"**Project Dataset**\n"
        f"* The data set is sourced from "
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)"  # noqa
        f" where it is hosted by Code Institute.\n"
        f"* The dataset has almost 1500 rows and represents housing records from "
        f" Ames, Iowa, indicating house profile (Floor Area, Basement, "
        f" Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its "
        f" respective sale price for houses built between 1872 and 2010.")


    # copied from README file - "Business Requirements" section
    st.success(
        f"**Business Requirements**\n\n"
        f"The project has 2 business requirements:\n"
        f"* Business Requirement 1 - The client is interested in discovering "
        f" how the house attributes correlate with the sale price. Therefore, "
        f" the client expects data visualisations of the correlated variables "
        f" against the sale price to show that.\n"
        f"* Business Requirement 2 - The client is interested in predicting "
        f" the house sale price from her four inherited houses and any other "
        f" house in Ames, Iowa."
    )

    # Link to README file, so the users can have access to full
    # project documentation
    st.write(
        f"* For additional information on this project please read the "
        f"[README](https://github.com/MariaHochstoeger/heritage-housing-issues/tree/main)"
        f" file for this project hosted on GitHub.\n"
        f"* The project was developed by Maria Hochstöger.")