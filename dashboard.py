
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load dataset from the same folder
DATA_FILE = Path(__file__).parent / "Student_Performance_Analysis_Dataset.csv"
df = pd.read_csv(DATA_FILE)

st.title("📊 Student Performance Analysis")
st.caption("Explore study habits and exam performance using Python")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

min_hours = float(df["Study_Hours_Per_Day"].min())
max_hours = float(df["Study_Hours_Per_Day"].max())

study_range = st.sidebar.slider(
    "Study Hours Per Day",
    min_value=min_hours,
    max_value=max_hours,
    value=(min_hours, max_hours)
)

filtered = df[
    df["Study_Hours_Per_Day"].between(study_range[0], study_range[1])
]

if filtered.empty:
    st.warning("No students match these filters.")
    st.stop()

# KPI cards
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Students", len(filtered))
c2.metric("Average Exam Score", f"{filtered['Exam_Score_Out_of_100'].mean():.1f}/100")
c3.metric("Average Study Hours", f"{filtered['Study_Hours_Per_Day'].mean():.1f} hrs")
c4.metric("Average Attendance", f"{filtered['Attendance_Percent'].mean():.1f}%")

st.divider()

# Tabs
tab1, tab2, tab3 = st.tabs(
    ["📚 Study Analysis", "📈 Attendance & Sleep", "📋 Student Data"]
)

with tab1:
    st.subheader("Study Hours vs Exam Scores")
    fig1 = px.scatter(
        filtered,
        x="Study_Hours_Per_Day",
        y="Exam_Score_Out_of_100",
        hover_data=["Student_ID"],
        trendline="ols",
        title="Do More Study Hours Relate to Higher Scores?"
    )
    st.plotly_chart(fig1, use_container_width=True)

    corr = filtered["Study_Hours_Per_Day"].corr(
        filtered["Exam_Score_Out_of_100"]
    )
    st.info(f"Study hours and exam score correlation in filtered data: {corr:.3f}")

with tab2:
    left, right = st.columns(2)

    with left:
        st.subheader("Attendance vs Exam Scores")
        fig2 = px.scatter(
            filtered,
            x="Attendance_Percent",
            y="Exam_Score_Out_of_100",
            hover_data=["Student_ID"]
        )
        st.plotly_chart(fig2, use_container_width=True)

    with right:
        st.subheader("Sleep Hours vs Exam Scores")
        fig3 = px.scatter(
            filtered,
            x="Sleep_Hours_Per_Day",
            y="Exam_Score_Out_of_100",
            hover_data=["Student_ID"]
        )
        st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Correlation Heatmap")
    numeric = filtered[
        [
            "Study_Hours_Per_Day",
            "Attendance_Percent",
            "Sleep_Hours_Per_Day",
            "Exam_Score_Out_of_100"
        ]
    ]
    corr_matrix = numeric.corr()
    fig4 = px.imshow(
        corr_matrix,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="RdBu",
        zmin=-1,
        zmax=1,
        title="Correlation Between Numeric Variables"
    )
    st.plotly_chart(fig4, use_container_width=True)

with tab3:
    st.subheader("Student Records")
    st.dataframe(filtered, use_container_width=True)

    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_student_performance.csv",
        mime="text/csv"
    )

st.caption(
    "Note: This is synthetic practice data. Correlation does not prove causation."
)
