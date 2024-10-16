import streamlit as st

# Set the initial page configuration
st.set_page_config(page_title="Hobby Projects Portfolio", page_icon="🕸️", layout="wide", initial_sidebar_state="collapsed")

# Define columns for layout
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

# Define URLs for buttons
resume_url = "https://drive.google.com/file/d/16Jcp2uPwIZZzFPN1c59rbDxnOrYZWw6O/view?usp=sharing"
linkedin_url = "https://linkedin.com/in/abhinav-sharma-work21/"
github_url = "https://github.com/abhinav-Katiyan"
kaggle_url = "https://www.kaggle.com/abhinavkatiyan"

# Button display function
def display_button(url, text):
    st.markdown(f'<a href="{url}" target="_blank" class="button">{text}</a>', unsafe_allow_html=True)

# Layout for the main content
col1, col2, col3 = st.columns([1.3, 0.2, 1])

# Content for the left column
with col1:
    st.subheader("**Hello! I'm Abhinav Sharma**",divider='rainbow')
    st.write("""
    I'm a student passionate about data, aiming to become a skilled Data Analyst. I love transforming raw data into meaningful insights through data visualization, statistical analysis, and problem-solving.
    
    Explore my portfolio to discover my projects and the tools and techniques I'm utilizing!
    """)

    # Display buttons for external links
    display_button(resume_url, "Resume")
    display_button(linkedin_url, "LinkedIn")
    display_button(github_url, "GitHub")
    display_button(kaggle_url, "Kaggle")

# Content for the right column
with col3:
    st.markdown(
        '<img src="https://storage.googleapis.com/kaggle-avatars/images/12609714-kg.jpg?t=2024-06-07-13-10-03" class="profile-photo" width="360">',
        unsafe_allow_html=True
    )

# Overview Section
st.subheader("Overview of My Data Analytics Expertise", divider='rainbow')
st.write("""
With a solid background in data analytics, I possess a diverse skill set including:

- **Exploratory Data Analysis (EDA):** Discovering meaningful patterns to guide business strategy.
- **Predictive Modeling:** Developing accurate models for predicting trends and optimizing decisions.
- **Data Visualization:** Creating user-friendly dashboards with Power BI and Python for actionable insights.
- **Statistical Analysis:** Leveraging methods to analyze datasets and extract insights for decision-making.
- **Natural Language Processing (NLP):** Implementing techniques for sentiment analysis and text classification.
- **Machine Learning:** Crafting solutions for classification, regression, and clustering problems to improve efficiency.

I work with technologies like Python, SQL, Power BI, and key libraries such as Pandas, NumPy, and Scikit-learn, consistently translating complex data into valuable insights.
""")

# Project Demonstrations
st.subheader("Power BI Reports", divider='rainbow')

with st.expander("In-Depth Analysis: Atliq Financial Overview", expanded=True):
    st.write("Detailed Power BI report highlighting Atliq's financial performance with key insights and trends.")

    # Embedding the Power BI report using iframe
    st.markdown("""
        <iframe src="https://app.powerbi.com/view?r=eyJrIjoiMmJhYzhkMWYtZDgyZS00NTg0LWEzMjItZmI1ZTUxMmNkNWI3IiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9" 
                width="100%" height="450" frameborder="0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    st.write("""
    **Atliq Financial Performance: Key Metrics Overview**  
    *Technologies: Power BI*  

    - **Net Sales**: Total revenue before deducting expenses.
    - **Gross Margin %**: Profitability measure indicating sales revenue remaining after production costs.
    - **Net Profit %**: Percentage of revenue left as profit after expenses.
    - **Market Share %**: Atliq's market share percentage in the industry.
    - **By Fiscal Year**: Data segmented by fiscal years to identify trends over time.
    """)

with st.expander("Swiggy Order Analysis", expanded=True):
    st.write("In-Depth Power BI Dashboard: Uncovering Key Swiggy Order Insights and Optimization Opportunities")
    
    # Embedding the Power BI report using iframe
    st.markdown("""
        <iframe src="https://app.powerbi.com/view?r=eyJrIjoiZGYwMTE5YzYtNjY4My00ZDQyLTk2OWEtNzdiM2MzMWQxMWM1IiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9" 
                width="100%" height="450" frameborder="0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    st.write("""
        **Swiggy Order Analysis: Key Insights Overview**  
        *Technologies: Power BI*  
    
        - **Total Revenue and Monthly Revenue Comparison:** KPIs highlight the current month's revenue against the previous month, identifying trends in sales performance.
        - **Order Metrics:** Visualizations of total orders processed, providing insights into order frequency and customer engagement.
        - **Cuisine Performance:** Analysis of revenue and orders by cuisine type, offering insights into customer preferences for operational planning.
        - **Weekday vs. Weekend Analysis:** A pie chart distinguishes revenue and orders by weekday vs. weekend, aiding in identifying peak business hours.
        - **Customer Lifetime Value (CLV):** Insights on long-term profitability and strategies for customer retention.
        - **Peak Order Times:** Understanding peak order hours helps optimize delivery efficiency and marketing efforts.
    
        This Power BI project supports data-driven decisions for improved business performance and growth.
    """)

st.subheader("Project Demonstrations", divider='rainbow')

with st.expander("Global Economic and Population EDA", expanded=True):
    st.write("This video demonstrates the Exploratory Data Analysis process.")
    st.write("Created a web app that pulls real-time data from the World Bank API, allowing users to analyze economic indicators like GDP, inflation, and population across different countries.")
    st.video("EDA(1).mp4", format="mp4", start_time=0, loop=True, autoplay=True, muted=True)

    st.write("""
    **Global Economic and Population Metrics Analyzer**  
    *Technologies: Pandas, NumPy, Matplotlib*  

    - **Automated Data Collection:** Developed a solution to gather economic indicators of BRICS nations from the World Bank API, saving the research team over 30 hours per month.
    - **Data Analysis and Trend Identification:** Analyzed GDP, population, FDI, and inflation data, identifying five key economic trends of 2022 to support investment decisions.
    """)
    
    st.write("""
    After building a hard-coded Kaggle notebook in May 2024, I sought to explore real-time data access as a hobby. Thus, I developed this web app that utilizes the World Bank API to gather live economic data from various countries. It allows users to easily analyze and compare key economic indicators, automating data collection and making it enjoyable to explore trends.
    """)

    # GitHub and Web App buttons
    st.markdown('<a href="https://github.com/abhinav-Katiyan/Economic-and-Population-Comparison-Tool" target="_blank" class="button">GitHub</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://economic-and-population-comparison-tool.streamlit.app/" target="_blank" class="button">Web App</a>', unsafe_allow_html=True)

with st.expander("Sentiment Analysis Web App", expanded=True):
    st.write("I developed a sophisticated web application designed to perform sentiment analysis on both user-input text and CSV files.")
    
    # Displaying video in the app
    st.video("EDA(2).mp4", format="mp4", start_time=0, loop=True, autoplay=True, muted=True)
    
    # Description of the project
    st.write("""
    **Sentiment Analysis Web App Project**  
    *Technologies & Model: NLP, Python DistilBERT*

    - **Sentiment Analysis:** Developed a web app that performs sentiment analysis on user-input text and CSV files, identifying trends in user opinions.
    - **Model Customization:** Customized the DistilBERT model, achieving a 30% improvement in detecting customer satisfaction levels.
    - **Text Classification:** Engineered a feature for classifying user feedback, achieving a 95% accuracy rate.
    """)

    # GitHub and Web App buttons
    st.markdown('<a href="https://github.com/abhinav-Katiyan/Sentiment-Analysis-Web-App" target="_blank" class="button">GitHub</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://sentiment-analysis-by-abhinav-katiyan.streamlit.app/" target="_blank" class="button">Web App</a>', unsafe_allow_html=True)

# Power BI Report Section


# Skills Section
st.subheader("Skills & Expertise", divider='rainbow')

skills = [
    "SQL", "Python", "Power BI", "Excel", "Machine Learning",
    "Microsoft Fabric", "NLP", "Pandas", "NumPy", "Financial Modeling", "Plotly"
]

# Displaying skills in buttons
for i in range(0, len(skills), 3):
    cols = st.columns(3)
    for j, skill in enumerate(skills[i:i + 3]):
        cols[j].button(skill)


