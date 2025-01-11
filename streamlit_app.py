import streamlit as st

st.title('Подтипы инсультов')
st.header('Фоновые заболевания:')

columns = st.columns(2)

with columns[0]:
    mv_stenosis = st.checkbox('Стеноз митрального клапана')
    av_stenosis = st.checkbox('Стеноз аортального клапана')
    brachiocephalic_a_stenosis = st.checkbox('Стеноз брахиоцефальных артерий>50% и наличие атеросклеротической бляшки')
    arterial_hypertension = st.checkbox('Артериальная гипертензия 1-3 ст')
    fibrillation = st.checkbox('Фибрилляция или другие виды аритмии')
    chronic_card_fail = st.checkbox('ХСН с фракцией выброса<35%')

with columns[1]:
    mech_valve = st.checkbox('Механический клапан')
    acute_period_mi = st.checkbox('Острый период ИМ')
    pics = st.checkbox('ПИКС')
    coagpat = st.checkbox('Коагулопатии')
    vasculits = st.checkbox('Васкулиты')


columns2 = st.columns(2)

with columns2[0]:
    st.header('Размер очага поражения по МРТ')
    higher = st.checkbox('Больше 1,5 см')
    less = st.checkbox('Меньше 1,5 см')

with columns2[1]:
    st.header('Другие лабораторные показатели:')
    dimer = st.checkbox('Повышенный Д-димер')
    bnp = st.checkbox('Натрийуретический мозговой пептид(NT pro BNP)')
    lpld = st.checkbox('Повышенный уровень ЛПНП в крови')

diagnosis = ''
cardiac_complications = [mv_stenosis, mech_valve, av_stenosis,
                         fibrillation, chronic_card_fail,acute_period_mi, pics]

if any(cardiac_complications) and higher and bnp:
    diagnosis = 'Кардиоэмболический инсульт'
elif all([brachiocephalic_a_stenosis,lpld,higher]):
    diagnosis = 'Атеротромботический инсульт'
elif all([less, arterial_hypertension]):
    diagnosis = 'Лакунарный инсульт'
elif any([higher, less]) and arterial_hypertension:
    diagnosis = 'Инсульт неясной этиологии'
elif any([higher, less]) and any([coagpat, vasculits, dimer]) and not lpld:
    diagnosis = 'Инсульт редкой этиологии'


st.header(diagnosis)






