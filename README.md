# Lightning Insights

Lightning Insights is a web application that utilizes Large Language Models via APIs from OpenAI to summarize and analyze customer reviews from e-commerce platforms. 

This tool can generate comprehensive, as well as tailored, insights based on the user's role and specific areas of interest. It also allows the user to pose specific questions regarding customer feedback. 

It provides an intuitive user interface, enabling users to upload raw review data, select their roles, choose the focus of the analysis, and receive detailed, role-specific reports generated from the analysis.

##  About the Application

[Lightning Insights](https://lightning-insights-bpmtrgvl6rigzde2xu8umo.streamlit.app/) consists of 2 main pages, each designed with the end user in mind:

1. **Home**: This page serves as an introduction to the application. It showcases the value and functionality of the tool to potential users, offering a detailed overview of what the tool can achieve.

2. **Functionality**: The core of the application resides on this page. Here, users can upload review data, select their preferred analysis parameters, and generate comprehensive, tailored insights into customer feedback.

## Project Structure

The project has a modular structure, with key directories and files serving a specific purpose:
- services: Contains files related to business logic, such as processing Excel files and interacting with LLM APIs (filereader.py, analyze.py).
  - filereader.py: Contains the methods for reading and processing Excel files.
  - analyze.py: Contains functions related to the OpenAI API and generating prompts for the AI model. Please be aware that this web application serves only as a functional demonstration of the official version of the e-commerce review analysis application, and the prompts in this file is not used in the official application.
- app.py: The main application file that uses Streamlit to create a web interface.
- app_pages: Contains files related to the presentation logic of the Streamlit application, such as creating and managing different pages (function.py, home.py).
- tests: Contains test files for the code in the main application.
- assets: Contains static files like images.
- styles: Styling files. 
- configs.py: Configuration constants used across the application.

## Future Steps
1. Enhance Our Web Application
 - Implementing comprehensive testing to ensure robustness
 - Expanding compatibility with additional e-commerce platforms
2. Browser Extension
 - On-page product reviews capture and analyze
 - Directly use without redirecting to the web application
 - Further enhance user experience
3. Automated Review Monitoring Platform
 - Customers can set up a list of products for continuous monitoring
 - Automatic review capture and analysis with periodic reporting 
 - Real-time alerts for critical reviews (e.g. negative reviews) 
4. Integration with CRM Systems
 - Build connections between user profiles and their reviews
 - Deeper understanding for each user's shopping preference
 - Enable personalized marketing campaigns based on user preferences
