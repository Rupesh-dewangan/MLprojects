import streamlit as st
import pickle
import pandas as pd
import  requests

# Load data
movies_list = pickle.load(open('movies.pkl', 'rb'))  # Ensure this is a DataFrame
movies_list1 = movies_list['title'].values  # Extract movie titles for the dropdown

similarity = pickle.load(open('similarity.pkl', 'rb'))  # Load similarity matrix

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return data['poster_path']


# Recommendation function
def recommend(movie):
    # Get the index of the selected movie
    movie_index = movies_list[movies_list['title'] == movie].index[0]

    # Get similarity scores for the selected movie
    distances = similarity[movie_index]

    # Sort and get the top 5 similar movies
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Retrieve movie titles for recommendations
    recommended_movies_name = []
    #recommended_movies_poster = []

    for i in movie_indices:
        #movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies_name.append([movies_list.iloc[i[0]].title])
        #recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies_name #,recommended_movies_poster


# Streamlit UI
st.title('Movie Recommender System')

# Dropdown for movie selection
select_movie_name = st.selectbox('What would you like to search for?', movies_list1)

# Recommend button
if st.button('Recommend'):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i[0])
    # recommended_movie_names,recommended_movie_posters = recommend(select_movie_name)

    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.text(recommended_movie_names[0])
    #     st.image(recommended_movie_posters[0])
    # with col2:
    #     st.text(recommended_movie_names[1])
    #     st.image(recommended_movie_posters[1])

    # with col3:
    #     st.text(recommended_movie_names[2])
    #     st.image(recommended_movie_posters[2])
    # with col4:
    #     st.text(recommended_movie_names[3])
    #     st.image(recommended_movie_posters[3])
    # with col5:
    #     st.text(recommended_movie_names[4])
    #     st.image(recommended_movie_posters[4])
