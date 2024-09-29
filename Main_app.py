import streamlit as st

# Set page configuration
st.set_page_config(page_title="Welcome to My Data Analytics Portfolio", page_icon="🕸️", layout="wide", initial_sidebar_state="collapsed")

# Define columns
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

# Define URLs for buttons
resume_url = "https://drive.google.com/file/d/1IFtuPv36fZb0AI9j3Rt9Argh9vEuzwem/view?usp=sharing"
linkedin_url = "https://linkedin.com/in/abhinav-sharma-work21/"
github_url = "https://github.com/abhinav-Katiyan"
kaggle_url = "https://www.kaggle.com/abhinavkatiyan"

# Button display function using Streamlit native buttons
def display_button(url, text):
    st.markdown(f'<a href="{url}" target="_blank" class="button">{text}</a>', unsafe_allow_html=True)

with body:
    # Home Section
    st.header("Welcome to My Data Science Portfolio", divider='rainbow')

    col1, col2, col3 = st.columns([1.3, 0.2, 1])

    with col1:
        st.write("""
        Hi there! I'm Abhinav Sharma, a student with a passion for data and a goal to become a skilled Data Analyst. I enjoy turning raw data into meaningful insights and working with data visualization, statistical analysis, and problem-solving.

        Take a look at my portfolio to explore some of my projects and learn more about the tools and techniques I'm using along the way!
        """)


        # Display buttons using Streamlit native buttons
        display_button(resume_url, "Resume")
        display_button(linkedin_url, "LinkedIn")
        display_button(github_url, "GitHub")
        display_button(kaggle_url, "Kaggle")

    with col3:
        st.markdown(
            '<img src="https://storage.googleapis.com/kaggle-avatars/images/12609714-kg.jpg?t=2024-06-07-13-10-03&quot" class="profile-photo" width="360">', 
            unsafe_allow_html=True
        )

   # Overview Section
    st.subheader("Overview of My Data Analytics and Data Science Expertise", divider='rainbow')
    st.write("""
    With a strong background in data analytics and data science, I offer a diverse set of skills across both domains. My expertise includes:
    
    - **Exploratory Data Analysis (EDA):** Discovering meaningful patterns and insights in data to guide business strategy.
    - **Predictive Modeling:** Developing accurate models that predict trends and optimize business decisions.
    - **Data Visualization:** Creating dynamic, user-friendly dashboards and visualizations using Power BI and Python to present actionable insights.
    - **Statistical Analysis:** Leveraging statistical methods to analyze datasets and extract key insights that drive decision-making.
    - **Natural Language Processing (NLP):** Implementing NLP techniques for tasks such as sentiment analysis, text classification, and entity recognition.
    - **Machine Learning:** Crafting machine learning solutions for classification, regression, and clustering problems to improve business efficiency and outcomes.
    
    I work with a range of technologies, including Python, SQL, Power BI, and key libraries such as Pandas, NumPy, and Scikit-learn. My work consistently demonstrates the ability to translate complex data into valuable insights that inform business decisions.
    """)


    # Project Demonstrations
    st.subheader("Project Demonstrations", divider='rainbow')

    with st.expander("Global Economic and Population EDA", expanded=True):
        st.write("This video demonstrates the Exploratory Data Analysis process.")
        st.write("Created a web app that pulls real-time data from the World Bank API, allowing users to analyze economic indicators like GDP, inflation, and population across different countries.")
        st.video("EDA(1).mp4", format="mp4", start_time=0, loop=True, autoplay=True, muted=True)
        st.write("""
        **Global Economic and Population Metrics Analyzer**  
        *Technologies: Pandas, NumPy, Matplotlib*  

        - **Automated Data Collection:** Constructed an automated solution using Python to gather economic indicators of BRICS nations from the World Bank API, saving the research team over 30 hours per month in manual data handling.

        - **Data Analysis and Trend Identification:** Analyzed GDP, population, FDI, and inflation data using Pandas, identifying and reporting five key economic trends of 2022. These insights supported strategic investment decisions and informed policy recommendations.
        """)

        # GitHub button
        st.markdown('<a href="https://github.com/abhinav-Katiyan/Economic-and-Population-Comparison-Tool" target="_blank" class="button">GitHub</a>', unsafe_allow_html=True)

        # Web App button
        st.markdown('<a href="https://economic-and-population-comparison-tool.streamlit.app/" target="_blank" class="button">Web App</a>', unsafe_allow_html=True)

    with st.expander("Sentiment Analysis Web App", expanded=True):
        st.write(
        "I developed a sophisticated web application designed to perform sentiment analysis on both user-input text and CSV files.")
        
        # Displaying video in the app
        st.video("EDA(2).mp4", format="mp4", start_time=0, loop=True, autoplay=True, muted=True)
        
        # Description of the project
        st.write("""
        **Sentiment Analysis Web App Project**  
        *Technologies & Model: NLP, Python DistilBERT*

        - **Sentiment Analysis:** Developed a web app that performs sentiment analysis on user-input text and CSV files. The app analyzes the sentiment of the text and identifies the most frequently repeated words, providing valuable insights into user opinions and trends.

        - **Model Customization:** Customized and trained the DistilBERT model for sentiment analysis, leading to a 30% improvement in detecting customer satisfaction levels, which informed strategic decisions for product enhancements.

        - **Text Classification:** Engineered a text classification feature utilizing advanced sentiment analysis techniques, achieving a 95% accuracy rate in categorizing user feedback, thereby streamlining the review process.
        """)

        # GitHub and Web App buttons
        st.markdown('<a href="https://github.com/abhinav-Katiyan/Sentiment-Analysis-Web-App" target="_blank" class="button">GitHub</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://sentiment-analysis-by-abhinav-katiyan.streamlit.app/" target="_blank" class="button">Web App</a>', unsafe_allow_html=True)

    # Power BI Report Section
    st.subheader("Power BI Reports", divider='rainbow')

    with st.expander("In-Depth Analysis: Atliq Financial Overview", expanded=True):
        st.write("Detailed Power BI report highlighting Atliq's financial performance with key insights and trends.")

    # Embedding the Power BI report using iframe
        st.markdown("""
            <iframe src="https://app.powerbi.com/view?r=eyJrIjoiM2EwZDYxYmMtNDA1Zi00MTE5LWFmMWUtNjQ4OTE1YmY2NDQ4IiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9" 
                    width="100%" height="450" frameborder="0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

    # Detailed report analysis with key points
        st.write("""
        **Atliq Financial Performance: Key Metrics Overview**  
        *Technologies: Power BI*  
    
        - **Net Sales**: Total revenue generated before deducting expenses.
        - **Gross Margin %**: Profitability measure showing the percentage of sales revenue remaining after covering production costs.
        - **Net Profit %**: Percentage of revenue left as profit after all expenses.
        - **Market Share %**: Atliq's industry market share percentage.
        - **By Fiscal Year**: Data segmented by fiscal years to identify trends and performance over time.
        """)

    with st.expander("Credit Card Analysis ", expanded=True):
        st.write("Comprehensive Power BI Dashboard Unveiling Key Insights on Credit Card Usage Patterns and Opportunities for Optimization")
        
        # Embedding the Power BI report using iframe
        st.markdown("""
            <iframe src="https://app.powerbi.com/view?r=eyJrIjoiNDY0YTQ2YjQtMzc4Ny00NmVlLWE2N2YtMmUzMzYwYjVmYzkxIiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9" 
                    width="100%" height="450" frameborder="0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)
        
        # Detailed report analysis with key points
        st.write("""
        **# Credit Card Analysis: Key Insights Overview  
        *Technologies: Power BI*  

        - **Age, Gender, and Income Groups:** Analysis focuses on identifying key spending patterns across different demographics.
        - **Spending Patterns:** Highlights how various groups utilize their credit cards, including high and low spenders.
        - **Potential for Improvement:** Insights into opportunities for enhancing credit card usage by targeted age, gender, and income segments.
        - **By Demographic Segmentation:** The data is segmented by demographics to uncover trends and potential areas for increased engagement.

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
