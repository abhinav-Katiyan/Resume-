<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Science Portfolio Website</title>
</head>
<body>
    <h1>Data Science Portfolio Website</h1>

    <p>Welcome to my Data Science Portfolio website! This site showcases my projects, skills, and live PowerBI reports, and it’s built using Streamlit. Below is a guide to understanding and customizing the code.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Homepage</strong>: Introduces me and provides links to my resume, LinkedIn, GitHub, and Kaggle profiles.</li>
        <li><strong>Overview</strong>: Describes my data science expertise, including EDA, predictive modeling, data visualization, statistical analysis, NLP, and machine learning.</li>
        <li><strong>Project Demonstrations</strong>: Includes video demonstrations and details of key projects.</li>
        <li><strong>Power BI Reports</strong>: Embeds live Power BI reports for interactive data visualization.</li>
        <li><strong>Skills Section</strong>: Lists my key skills in data science and analytics.</li>
        <li><strong>Contact Information</strong>: Provides my contact details for networking and opportunities.</li>
    </ul>

    <h2>Getting Started</h2>
    <ol>
        <li><strong>Install Dependencies</strong>: Ensure you have Streamlit installed. You can install it using pip:
            <pre><code>pip install streamlit</code></pre>
        </li>
        <li><strong>Run the App</strong>: Save the code to a file, for example, <code>app.py</code>. Run the app using Streamlit:
            <pre><code>streamlit run app.py</code></pre>
        </li>
        <li><strong>Customize the Code</strong>:
            <ul>
                <li><strong>Resume, LinkedIn, GitHub, Kaggle URLs</strong>: Update the URLs in the <code>resume_url</code>, <code>linkedin_url</code>, <code>github_url</code>, and <code>kaggle_url</code> variables.</li>
                <li><strong>Project Details</strong>: Replace video files and project descriptions with your own content.</li>
                <li><strong>Power BI Reports</strong>: Embed your own Power BI report URLs in the iframes.</li>
            </ul>
        </li>
        <li><strong>GitHub Repository</strong>: You can find the code and instructions for customization in my GitHub repository: <a href="Your GitHub Link">Your GitHub Link</a>.</li>
    </ol>

    <h2>Code Breakdown</h2>
    <ul>
        <li><strong>Page Configuration</strong>: Sets up the page title, icon, layout, and sidebar state.</li>
        <li><strong>Columns</strong>: Defines the layout structure with margins and main content.</li>
        <li><strong>Button Display</strong>: Provides a function to create buttons for external links.</li>
        <li><strong>Sections</strong>: Includes the homepage, overview, project demonstrations, Power BI reports, skills, and contact information.</li>
        <li><strong>Skills Section</strong>: Displays a list of skills with buttons.</li>
    </ul>

    <p>Feel free to modify the code to fit your own portfolio needs. If you have any questions or need assistance, don’t hesitate to reach out!</p>
</body>
</html>
