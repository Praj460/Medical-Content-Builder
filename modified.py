import os
import re
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from sentence_transformers import SentenceTransformer, util

# Load environment variables
load_dotenv()

# Configure the Google Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not found in environment variables.")

# Initialize Streamlit app
st.set_page_config(page_title="medical_content")
st.header("Medical Content builder")

# Function to load Gemini model and get responses
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
       # model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None

# Function to extract URLs from text
def extract_urls(text):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text)
    return urls

# Function to simulate content fetching from a URL (replace this with actual content fetching logic)
def fetch_url_content(url):
    # Placeholder: return a dummy string for now, you would replace this with actual URL fetching
    return f"Simulated content from {url}"

# Function to calculate similarity between the generated content and the reference content
def calculate_similarity(text1, text2):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(embeddings1, embeddings2).item()
    return similarity_score * 100  # Convert to percentage

# Get user input
user_input = st.text_input("Input your question:", key="input")

# Submit button
submit = st.button("Ask the question")

# If the button is clicked
if submit and user_input:
    # Step 1: Get response from Gemini
    response = get_gemini_response(user_input)
    
    if response:
        st.subheader("Generated Response:")
        st.write(response)
        
        # Step 2: Extract URLs from the response
        urls = extract_urls(response)
        
        if urls:
            st.subheader("Extracted URLs:")
            for url in urls:
                st.write(url)
            
            # Step 3: Calculate similarity for each URL and find the highest similarity
            highest_similarity = 0
            res=[]
            x=""
            most_similar_url = None
            for url in urls:
                reference_content = fetch_url_content(url)  # Simulate fetching content from the URL
                x=x+reference_content
                similarity_percentage = calculate_similarity(response, reference_content)
                res.append(similarity_percentage)
                
                if similarity_percentage > highest_similarity:
                    highest_similarity = similarity_percentage
                    most_similar_url = url
                    
            ## use llm for the generating from x
            x=x+"generate content from this"
            x=get_gemini_response(x)
            
            
            total=calculate_similarity(response,x)
        
            # Step 4: Display the highest similarity percentage and corresponding URL
            st.subheader("Highest Similarity Check:")
            if most_similar_url:
                st.write(f"The content is most similar to {most_similar_url} with a similarity of {highest_similarity:.2f}%.")
                for i in res:
                    st.write(res.index(i)+1," url -->",i)
                st.write("total percentage", total)
                    
        else:
            st.write("No URLs found in the response.")
    else:
        st.write("No response received from Gemini API.")
