import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from notebooks.analysis import(
    count_of_applications,
    count_by_remark,
    count_of_remarks,
    year_groups,
    orbit_type_labels,
    y_orbit_count
)


# --------------------------------
# 🌌 Page Config
# --------------------------------
st.set_page_config(
    page_title="Space Mission Dashboard 🚀",
    layout="wide"
)

st.title("🚀 Space Mission Analytics Dashboard")

# --------------------------------
# 🔢 KPI METRICS
# --------------------------------
col1, col2, col3, col4 = st.columns(4)

# col1.metric("Total Applications", int(count_by_application.sum()))
# col2.metric("Total Remarks", int(count_by_remark.sum()))
# col3.metric("Total Years Covered", len(year_groups))
# col4.metric("Orbit Types", len(orbit_type_labels))


# --------------------------------
# 📊 ROW 1 — Bar & Pie
# --------------------------------
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Applications Overview")
    fig_app = px.bar(
        x=count_of_applications.index,
        y=count_of_applications.values,
        labels={
            "x": "Application",
            "y": "Count"
        }
    )
    st.plotly_chart(fig_app, use_container_width=True)

with col_right:
    st.subheader("Remarks Distribution")

    fig_pie = px.pie(
        values=count_by_remark,
        names=count_of_remarks.index,
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True)


# --------------------------------
# 📈 ROW 2 — Line Chart
# --------------------------------
st.subheader("Year-wise Trend 📈")

fig_line = px.line(
    x=year_groups.index,
    y=year_groups.values,
    labels={"x": "Date", "y": "Count"},
    markers=True
)

fig_line.update_layout(
    xaxis_title="Years",
    yaxis_title="Count"
)

st.plotly_chart(fig_line, use_container_width=True)


# --------------------------------
# 🛰️ ROW 3 — Orbit Type Analysis
# --------------------------------
st.subheader("Orbit Type Distribution 🛰️")

fig_orbit = px.bar(
    x=orbit_type_labels,
    y=y_orbit_count,
    labels={"x": "Orbit Type", "y": "Count"}
)

st.plotly_chart(fig_orbit, use_container_width=True)