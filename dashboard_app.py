import streamlit as st
import scrape_schedule
import schedule_analytics

st.set_page_config(page_title="홈쇼핑 대시보드", layout="wide")
st.title("📊 홈쇼핑 방송 데이터 대시보드")

if st.button("📥 오늘 데이터 수집"):
    scrape_schedule.main()
    st.success("데이터 수집 완료 ✅")

df = schedule_analytics.load_data()
st.dataframe(df)
