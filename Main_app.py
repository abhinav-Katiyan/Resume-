import streamlit as st
import webbrowser

# Set page configuration
st.set_page_config(page_title="My Data Science Portfolio", page_icon="🕸️", layout="wide", initial_sidebar_state="collapsed")

# Define columns
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

# Define URLs for buttons
resume_url = "https://drive.google.com/file/d/1IFtuPv36fZb0AI9j3Rt9Argh9vEuzwem/view?usp=sharing"
linkedin_url = "https://linkedin.com/in/abhinav-sharma-work21/"
github_url = "https://github.com/abhinav-Katiyan"
kaggle_url = "https://www.kaggle.com/abhinavkatiyan"

# Button display function using Streamlit native buttons
def display_button(url, text):
    if st.button(text):
        webbrowser.open_new_tab(url)

with body:
    # Home Section
    st.header("Welcome to My Data Science Portfolio", divider='rainbow')

    col1, col2, col3 = st.columns([1.3, 0.2, 1])

    with col1:
        st.write("""
        Hey! I'm Abhinav Sharma, a Data Scientist with a passion for transforming data into actionable insights. My expertise spans across various domains including predictive modeling, data visualization, and statistical analysis.

        Explore my portfolio to see some of my key projects and find out more about the tools and technologies I use.
        """)

        # Display buttons using Streamlit native buttons
        display_button(resume_url, "Resume")
        display_button(linkedin_url, "LinkedIn")
        display_button(github_url, "GitHub")
        display_button(kaggle_url, "Kaggle")

    with col3:
        st.markdown(
            '<img src="https://media.licdn.com/dms/image/v2/D5603AQEJGss-oF5RkA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1711951217355?e=1730937600&v=beta&t=X73HPQJ-4vxGrShStI8a_a8XUsn4VP-Y2MtaXRFLVIg" class="profile-photo" width="360">',
            unsafe_allow_html=True)

    # Overview Section
    st.subheader("Overview of My Data Science Expertise", divider='rainbow')
    st.write("""
    With a solid foundation in data analysis and machine learning, I bring a comprehensive skill set that spans various facets of data science. My expertise includes:

    - **Exploratory Data Analysis (EDA):** Uncovering hidden insights from data to inform strategic decisions.
    - **Predictive Modeling:** Building models that forecast future trends and business outcomes.
    - **Data Visualization:** Crafting intuitive dashboards and visualizations using tools like Power BI to communicate data-driven insights.
    - **Statistical Analysis:** Applying advanced statistical techniques to analyze data and derive actionable insights.
    - **Natural Language Processing (NLP):** Developing applications for sentiment analysis and text classification using state-of-the-art models like DistilBERT.
    - **Machine Learning:** Designing and implementing algorithms to solve complex problems, optimize processes, and enhance decision-making.

    I frequently utilize a diverse set of tools and technologies, including Python, SQL, Power BI, and various machine learning libraries like Pandas, NumPy, and Scikit-learn. My projects and work experience demonstrate a track record of driving meaningful business outcomes through data-driven strategies.
    """)

    # Project Demonstrations
    st.subheader("Project Demonstrations", divider='rainbow')

    with st.expander("Global Economic and Population EDA", expanded=True):
        st.write("This video demonstrates the Exploratory Data Analysis process.")
        st.video("EDA(1).mp4", format="mp4", start_time=0, loop=True, autoplay=True, muted=True)
        st.write("""
        **Global Economic and Population Metrics Analyzer**  
        *Technologies: Pandas, NumPy, Matplotlib*  

        - **Automated Data Collection:** Constructed an automated solution using Python to gather economic indicators of BRICS nations from the World Bank API, saving the research team over 30 hours per month in manual data handling.

        - **Data Analysis and Trend Identification:** Analyzed GDP, population, FDI, and inflation data using Pandas, identifying and reporting five key economic trends of 2022. These insights supported strategic investment decisions and informed policy recommendations.
        """)

        # GitHub button
        if st.button("GitHub", key="eda1_github"):
            webbrowser.open_new_tab("https://github.com/abhinav-Katiyan/Economic-and-Population-Comparison-Tool")

        # Web App button
        if st.button("Web App", key="eda1_webapp"):
            webbrowser.open_new_tab("https://economic-and-population-comparison-tool.streamlit.app/")

    with st.expander("Sentiment Analysis Web App", expanded=True):
        st.write(
            "I developed a sophisticated web application designed to perform sentiment analysis on both user-input text and CSV files.")
        st.video("EDA(2).mp4", format="mp4", start_time=0, loop=True, autoplay=True, muted=True)
        st.write("""
        **Sentiment Analysis Web App Project**  
        *Technologies & Model: NLP, Python DistilBERT*


        - **Sentiment Analysis:** Developed a web app that performs sentiment analysis on user-input text and CSV files. The app analyzes the sentiment of the text and identifies the most frequently repeated words, providing valuable insights into user opinions and trends.

        - **Model Customization:** Customized and trained the DistilBERT model for sentiment analysis, leading to a 30% improvement in detecting customer satisfaction levels, which informed strategic decisions for product enhancements.

        - **Text Classification:** Engineered a text classification feature utilizing advanced sentiment analysis techniques, achieving a 95% accuracy rate in categorizing user feedback, thereby streamlining the review process.
        """)

        if st.button("GitHub", key="eda2_github"):
            webbrowser.open_new_tab("https://github.com/abhinav-Katiyan/Sentiment-Analysis-Web-App")

        # Web App button
        if st.button("Web App", key="eda2_webapp"):
            webbrowser.open_new_tab("https://sentiment-analysis-by-abhinav-katiyan.streamlit.app/")

    # Power BI Report Section
    st.subheader("Power BI Reports", divider='rainbow')

    with st.expander("Credit Card Users Analysis Report", expanded=True):
        st.write("A comprehensive and live sales analysis report created using Power BI.")
        st.markdown("""
            <iframe src="https://app.powerbi.com/view?r=eyJrIjoiNDY0YTQ2YjQtMzc4Ny00NmVlLWE2N2YtMmUzMzYwYjVmYzkxIiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9" 
                    width="100%" height="450" frameborder="0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)
        st.write("""
        **Credit Card Users Analysis**  
        *Technologies: Power BI*  
        *Type: Dashboard*

        - **Customer Preferences Analysis:** Analyzed over 10,000 data points for a bank's new credit card launch, focusing on customer preferences. Identified trends that led to a 15% increase in targeted sign-ups within the first quarter.

        - **Segment Analysis:** Examined key customer segments and spending patterns to inform simplified marketing strategies, leading to increased spending by 15% among the 25-34 age group and enhanced engagement by 25% among IT professionals, driving significant revenue growth.
        """)

    with st.expander("Hotel Insights Report", expanded=True):
        st.write("Another insightful Power BI report showcasing additional analyses.")
        st.markdown("""
            <iframe src="https://app.powerbi.com/view?r=eyJrIjoiZTVjOTAxZWQtZjU2NC00YjY1LWJkZGQtYTlhMTdjNzVjNDczIiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9" 
                    width="100%" height="450" frameborder="0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)
        st.write("""
        **Hotel Insights Report Analysis**  
        *Technologies: Power BI*  

        - **Guest Preferences Analysis:** Analyzed over 10,000 data points for a hotel's guest experience management system. Focused on guest preferences and booking patterns, identifying key trends that resulted in a 15% increase in repeat bookings within the first quarter.

        - **Segment Analysis:** Investigated key guest segments and spending behaviors to refine marketing strategies. This analysis led to a 15% increase in average spending among the 25-34 age group and a 25% boost in engagement from business travelers, significantly enhancing revenue growth and customer satisfaction.
        """)

    # Skills Section
    st.subheader("Skills & Expertise", divider='rainbow')

    skills = [
        "SQL", "Python", "Power BI", "Excel", "Machine Learning",
        "Microsoft Fabric", "NLP", "Pandas", "NumPy", "Financial Modeling", "Plotly"
    ]

    for i in range(0, len(skills), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(skills):
                cols[j].button(skills[i + j])

    st.subheader("Contact", divider='rainbow')
    st.write("""
    **Email:** abhinavkatiyan21@gmail.com 
    **Contact:** +91 6388845388
    """)
