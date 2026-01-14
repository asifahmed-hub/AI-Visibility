import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="CSV Prompt Runner (No API)", layout="wide")
st.title("📄 CSV Prompt Runner (Keyless Demo)")

st.info("This version runs WITHOUT any API keys and simulates ChatGPT responses.")

uploaded_file = st.file_uploader(
    "Upload CSV file with a column named 'prompt'",
    type=["csv"]
)

def fake_chatgpt(prompt: str) -> str:
    """
    Simulated ChatGPT response (replace later with real API if needed)
    """
    time.sleep(0.3)  # simulate latency
    return f"Simulated AI response for:\n\n{prompt}"

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "prompt" not in df.columns:
        st.error("CSV must contain a column named 'prompt'")
        st.stop()

    st.success(f"{len(df)} prompts loaded")
    st.dataframe(df)

    if st.button("🚀 Run Prompts"):
        responses = []
        progress = st.progress(0)

        for i, prompt in enumerate(df["prompt"]):
            response = fake_chatgpt(prompt)
            responses.append(response)
            progress.progress((i + 1) / len(df))

        df["response"] = responses

        st.success("✅ Done!")
        st.dataframe(df)

        st.download_button(
            "⬇️ Download Results",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="results.csv",
            mime="text/csv"
        )
