import streamlit as st
import pandas as pd
import plotly.express as px

# Создаем DataFrame
data = {
    'year': ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    'unique_clients': [64826, 585338, 1078481, 1363382, 1849379, 1770455, 1199990, 1126646],
    'card_limit_percent': [41.85, 40.17, 46.63, 18.34, 23.90, 11.95, 31.60, 43.84],
    'inst_limit_percent': [59.62, 47.09, 50.93, 54.29, 53.83, 21.54, 39.25, 47.89],
    'card_limit_avg': [19039.52, 9807.76, 10397.99, 7504.71, 12922.91, 12054.49, 14847.71, 17512.68],
    'inst_limit_avg': [21154.09, 12375.68, 8477.09, 8196.02, 9954.46, 9809.94, 12279.36, 15500.15]
}
df = pd.DataFrame(data)

st.title('Анализ метрик по годам')

# График уникальных клиентов
st.header('Количество уникальных клиентов')
fig_clients = px.line(df, x='year', y='unique_clients',
                      title='Динамика количества уникальных клиентов')
st.plotly_chart(fig_clients, use_container_width=True)

# График процентов лимитов
st.header('Процент одобренных лимитов')
fig_percents = px.line(df, x='year',
                       y=['card_limit_percent', 'inst_limit_percent'],
                       title='Динамика процента одобренных лимитов',
                       labels={'value': 'Процент',
                               'variable': 'Тип лимита'},
                       color_discrete_map={
                           'card_limit_percent': '#82ca9d',
                           'inst_limit_percent': '#8884d8'
                       })
fig_percents.update_traces(
    name='Карточные лимиты',
    selector=dict(name='card_limit_percent')
)
fig_percents.update_traces(
    name='Инсталментные лимиты',
    selector=dict(name='inst_limit_percent')
)
st.plotly_chart(fig_percents, use_container_width=True)

# График средних значений
st.header('Средние значения лимитов')
fig_avgs = px.line(df, x='year',
                   y=['card_limit_avg', 'inst_limit_avg'],
                   title='Динамика средних значений лимитов',
                   labels={'value': 'Значение',
                           'variable': 'Тип лимита'},
                   color_discrete_map={
                       'card_limit_avg': '#82ca9d',
                       'inst_limit_avg': '#8884d8'
                   })
fig_avgs.update_traces(
    name='Карточные лимиты',
    selector=dict(name='card_limit_avg')
)
fig_avgs.update_traces(
    name='Инсталментные лимиты',
    selector=dict(name='inst_limit_avg')
)
st.plotly_chart(fig_avgs, use_container_width=True)

# Таблица с данными
st.header('Исходные данные')
st.dataframe(df)
