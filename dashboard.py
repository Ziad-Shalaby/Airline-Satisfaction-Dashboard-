import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Airline Passenger Satisfaction', layout='wide')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title('🛫 Airline Passenger Satisfaction')

@st.cache_data
def get_data():
    df = pd.read_csv('airline.csv')
    return df

df = get_data()

tab1, tab2, tab3, tab4 = st.tabs([
    'Customer Distribution', 
    'Customer Satisfaction With Services', 
    'Customer Satisfaction based on Class and Type',
    'Satisfaction and Gender Distribution'
])

with tab1:
    st.subheader("Customer Demographics")

    fig = px.histogram(
            df,
            x='Age',
            color='satisfaction',
            barmode='overlay',
            histnorm='density',
            color_discrete_sequence=px.colors.qualitative.Set1
        )
    fig.update_layout(
            title="Age Distribution by Satisfaction Level",
            xaxis_title="Age",
            yaxis_title="Density",
            legend_title="Satisfaction Level"
        )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander('insights'):
            st.write("""- Younger customers (under 30) show higher dissatisfaction levels compared to older age groups.  
- Satisfaction improves gradually for customers aged 30-50, with a balanced distribution.  
- Customers over 50 are predominantly satisfied, with the highest satisfaction seen in the 50-60 age range.  
- The 20-30 age group presents an opportunity for targeted improvement to reduce dissatisfaction.  
- Retention strategies should focus on addressing younger customer needs while leveraging older customer loyalty.""")


    fig = px.histogram(
            df,
            x='Flight Distance',
            color='satisfaction',
            barmode='overlay',
            histnorm='density',
            color_discrete_sequence=px.colors.qualitative.Set1
        )
    fig.update_layout(
            title="Flight Distance Distribution by Satisfaction Level",
            xaxis_title="Flight Distance",
            yaxis_title="Density",
            legend_title="Satisfaction Level"
        )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander('insights'):
         st.write("""- Customers with shorter flight distances (under 500 miles) show a higher density of dissatisfaction.
- Satisfaction levels increase with longer flight distances, particularly for flights over 1,000 miles.
- The density of both satisfied and dissatisfied customers decreases significantly beyond 2,500 miles.
- Dissatisfaction is most prominent in the 0–1,000 mile range, signaling a need to improve short-haul flight experiences.
- Long-haul flights (2,000+ miles) generally exhibit better satisfaction levels, indicating higher service quality.""" )

with tab2:
    st.subheader("Service Ratings")

    fig_wifi = px.bar(
        df.groupby('Inflight wifi service').size().reset_index(name='Count'),
        x='Inflight wifi service',
        y='Count',
        title='Count of Inflight WiFi Service',
        labels={'Inflight wifi service': 'Inflight WiFi Service', 'Count': 'Number of Occurrences'},
        color='Inflight wifi service',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_wifi, use_container_width=True)
    with st.expander('Insights '):
        st.write(""" 
- Most users rated the inflight Wi-Fi service as "2" or "3," indicating average satisfaction.
- Fewer users gave high ratings ("4" or "5")
- Suggesting room for improvement in service quality.""") 

    fig_boarding = px.bar(
        df.groupby('Online boarding').size().reset_index(name='Count'),
        x='Online boarding',
        y='Count',
        title='Count of Online Boarding',
        labels={'Online boarding': 'Online Boarding', 'Count': 'Number of Occurrences'},
        color='Online boarding',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_boarding, use_container_width=True)
    with st.expander('Insights'):
               st.write(""" 
- Most users rated the Online boarding service as "3" or "4," indicating good satisfaction.  
- Fewer users gave lower ratings,  
- suggesting the majority find the online boarding service satisfactory.""") 

    fig_comfort = px.bar(
        df.groupby('Seat comfort').size().reset_index(name='Count'),
        x='Seat comfort',
        y='Count',
        title='Count of Seat Comfort',
        labels={'Seat comfort': 'Seat Comfort', 'Count': 'Number of Occurrences'},
        color='Seat comfort',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_comfort, use_container_width=True)
    with st.expander('Insights'):
        st.write("""
- Most users rated seat comfort as "4" or "5," indicating high satisfaction with seating. 
- Fewer users gave lower ratings, 
- suggesting the majority find the seating comfortable. """)

    fig_entertainment = px.bar(
        df.groupby('Inflight entertainment').size().reset_index(name='Count'),
        x='Inflight entertainment',
        y='Count',
        title='Count of Inflight Entertainment',
        labels={'Inflight entertainment': 'Inflight Entertainment', 'Count': 'Number of Occurrences'},
        color='Inflight entertainment',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_entertainment, use_container_width=True)
    with st.expander('Insights'):
        st.write("""- Most users rated inflight entertainment as "4" or "5," indicating high satisfaction with the service.  
- Fewer users gave lower ratings,  
- suggesting the majority find the inflight entertainment enjoyable.   """) 

    # On-board Service
    fig_onboard = px.bar(
        df.groupby('On-board service').size().reset_index(name='Count'),
        x='On-board service',
        y='Count',
        title='Count of On-board Service',
        labels={'On-board service': 'On-board Service', 'Count': 'Number of Occurrences'},
        color='On-board service',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_onboard, use_container_width=True)
    with st.expander('Insights'):
        st.write("""- Most users rated on-board service as "4" or "5," indicating high satisfaction with the service.  
- Fewer users gave lower ratings,  
- suggesting the majority find the on-board service satisfactory.""") 

    # Leg Room Service
    fig_legroom = px.bar(
        df.groupby('Leg room service').size().reset_index(name='Count'),
        x='Leg room service',
        y='Count',
        title='Count of Leg Room Service',
        labels={'Leg room service': 'Leg Room Service', 'Count': 'Number of Occurrences'},
        color='Leg room service',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_legroom, use_container_width=True)
    with st.expander('Insights'):
        st.write("""
- Most users rated legroom service as "4" or "5," indicating a high level of satisfaction. 
- Lower ratings are less frequent, 
- suggesting the majority of customers are comfortable with the legroom provided. """)


with tab3:
    st.subheader("Customer Types and Satisfaction")

    grouped_df = df.groupby(['Customer Type', 'satisfaction']).size().reset_index(name='Count')
    fig = px.bar(
        grouped_df,
        x='Count',
        y='Customer Type',
        title='Count of Customer Types by Satisfaction Level',
        labels={'Customer Type': 'Customer Type', 'Count': 'Number of Occurrences'},
        color='satisfaction',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander('insights'):
        st.write("""- Loyal customers are predominantly satisfied, forming the majority of occurrences.
- Disloyal customers are mostly neutral or dissatisfied, with only a small proportion satisfied.
- The significant satisfaction among loyal customers highlights the importance of retention strategies.
-  Addressing dissatisfaction in disloyal customers could help convert them into loyal customers.
- Customer loyalty is strongly linked to satisfaction levels, emphasizing its business impact.""")
    grouped_df = df.groupby(['Type of Travel', 'satisfaction']).size().reset_index(name='Count')
    fig = px.bar(
        grouped_df,
        x='Count',
        y='Type of Travel',
        title='Count of Type of Travel',
        labels={'Type of Travel': 'Type of Travel', 'Count': 'Number of Occurrences'},
        color='satisfaction',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander('insights'):
        st.write(""" - Business travelers show significantly higher satisfaction compared to personal travelers.
- Most personal travelers are neutral or dissatisfied with their travel experience.
- The number of business travel occurrences greatly exceeds personal travel occurrences.
- Improving satisfaction for personal travelers could enhance overall service perception.
- Tailored strategies might be needed to address different needs of business and personal travelers.
""")

    grouped_df = df.groupby(['Class', 'satisfaction']).size().reset_index(name='Count')
    fig = px.bar(
        grouped_df,
        x='Count',
        y='Class',
        title='Count of Class',
        labels={'Class': 'Class', 'Count': 'Number of Occurrences'},
        color='satisfaction',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander('insights'):
        st.write("""- Business Class has the highest proportion of satisfied customers, with satisfaction clearly exceeding neutral or dissatisfied responses.
- Economy (Eco) Class has a majority of neutral or dissatisfied customers, indicating lower satisfaction in this category.
- Economy Plus (Eco Plus) also leans towards dissatisfaction but has a relatively balanced distribution compared to Economy.""")

with tab4:
    st.subheader("Satisfaction and Gender Distribution")

    sat_counts = df['satisfaction'].value_counts()
    fig = px.pie(
        names=sat_counts.index,
        values=sat_counts.values,
        title='Satisfaction Distribution',
        labels={'satisfaction': 'Satisfaction'},
        color=sat_counts.index,
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander('insights'):
        st.write(""" -The majority of respondents (56.6%) are neutral or dissatisfied.
        - A smaller percentage (43.4%) are satisfied. 
        -This indicates that there is room for improvement in customer satisfaction.""")

    gender_counts = df['Gender'].value_counts()
    fig = px.pie(
        names=gender_counts.index,
        values=gender_counts.values,
        title='Gender Distribution',
        labels={'Gender': 'Gender'},
        color=gender_counts.index,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander('insights'):
        st.write("""- The gender distribution is nearly equal, with 50.7% female and 49.3% male respondents. 
        - This balance indicates that gender does not strongly skew the data and suggests the feedback is representative across genders.""")
