import os
import pandas as pd 
import streamlit as st
import joblib, json, re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import numpy as np
from PIL import Image  # Tambahan untuk menampilkan gambar

# ===================== Streamlit Config =====================
st.set_page_config(
    page_title="Analisis Sentimen Isu Publik",
    layout="wide",
    page_icon="📈"
)

# ===================== Load Model & Vectorizer =====================
model = joblib.load('model_sentimen.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# ===================== Load Kamus Normalisasi =====================
try:
    with open('norm_dict.json', 'r', encoding='utf-8') as f:
        norm_dict = json.load(f)
except:
    norm_dict = {}

# ===================== Preprocessing =====================
stemmer = StemmerFactory().create_stemmer()
stop_factory = StopWordRemoverFactory()
stopword = stop_factory.create_stop_word_remover()

def preprocess_text(text):
    text = text.lower()
    text = " ".join([norm_dict.get(word, word) for word in text.split()])
    text = stemmer.stem(text)
    text = stopword.remove(text)
    return text

# ===================== CSS =====================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body, div, p, span, label { font-family: 'Poppins', sans-serif !important; font-size: 18px !important; }
.hero {
  background: linear-gradient(135deg,#1e3c72,#2a5298,#d4af37);
  padding: 60px 30px;
  border-radius: 30px;
  text-align: center;
  color: white;
  margin-bottom: 40px;
  box-shadow:0 10px 30px rgba(0,0,0,0.2);
  position:relative;
  overflow:hidden;
}
.hero::after {
  content:"";
  position:absolute;
  top:-50px;left:-50px;
  width:200px;height:200px;
  background:rgba(255,255,255,0.1);
  border-radius:50%;
  animation:float 8s infinite alternate;
}
@keyframes float {to{transform:translate(50px,50px);}}
.hero h1 {font-size: 2.5rem;font-weight:700;margin-bottom: 15px;color: #ffffff;}
.hero p {font-size: 1.4rem;opacity: 0.95;}
.stButton button {
  background: linear-gradient(90deg,#2a5298,#1e3c72,#d4af37) !important;
  color: white !important;
  padding: 1rem 2rem;
  border-radius: 14px;
  border: none;
  font-weight: 700;
  font-size: 1.2rem !important;
  transition: 0.3s;
  box-shadow:0 6px 12px rgba(0,0,0,0.15);
}
.stButton button:hover {
  background: linear-gradient(90deg,#d4af37,#1e3c72,#2a5298) !important;
  transform: scale(1.07);
}
.sentiment-card {
  padding: 40px;
  border-radius: 24px;
  margin: 30px 0;
  text-align: center;
  font-size: 1.2rem !important;
  animation: fadeInUp 0.8s ease-in-out;
  background: var(--background-color);
  color: var(--text-color);
  box-shadow:0 8px 20px rgba(0,0,0,0.1);
  border-top:6px solid #2a5298;
}
textarea {
    font-size: 22px !important;
    font-weight: 600;
    color: #1e3c72;
    background-color: #f9f9ff;
    border-radius: 14px;
    border: 2px solid #2a5298;
    padding: 20px;
}
.sentiment-card.positive {border-color: #4caf50;}
.sentiment-card.negative {border-color: #f44336;}
.icon-badge { font-size: 5rem !important; margin-bottom:20px; }
.sent-title { font-size: 1.6rem !important; font-weight: 700; margin-bottom: 12px; }
.sent-value { font-size: 2rem !important; font-weight: 800; margin-bottom: 20px; }
.sent-value.positive {color: #1f1f69 !important;}
.sent-value.negative {color: #f44336 !important;}
.chips-container { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; justify-content: center; }
.chip { background:linear-gradient(90deg,#2a5298,#d4af37); color: #fff; border-radius:18px; padding:8px 16px; font-size: 1rem !important; font-weight: 600; box-shadow:0 4px 8px rgba(0,0,0,0.1); }
.daftar-kata-title { text-align:center; font-size:1.4rem !important; font-weight:700; margin-top:30px; margin-bottom:10px; }
.funfact { margin-top:30px; }
@keyframes fadeInUp {from {opacity:0;transform:translateY(20px);}to{opacity:1;transform:translateY(0);}}
</style>
""", unsafe_allow_html=True)

# ===================== Sidebar =====================
page = st.sidebar.selectbox("Menu", ["🏠 Home", "📊 Analisis", "📑 Dokumentasi"], index=0)

# ===================== Halaman Home =====================
if page == "🏠 Home":
    st.markdown(
        '<div class="hero"><h1>📊 Selamat Datang di Sistem Analisis Sentimen Isu Publik</h1><p>Tempat Anda mengukur opini publik secara mudah, cepat, dan menarik.</p></div>',
        unsafe_allow_html=True
    )
    st.write("### 🌟 Apa yang bisa Anda lakukan di sini?")
    st.write("- Analisis sentimen secara otomatis terhadap teks atau komentar.")
    st.write("- Melihat kata-kata dominan yang mempengaruhi sentimen.")
    st.write("- Mengambil insight cepat dari opini publik.")
    st.info("Klik menu **Analisis** di sebelah kiri untuk mencoba analisis sentimen secara langsung.")
    st.success("💡 Tips: Masukkan komentar, tweet, atau opini publik untuk melihat hasilnya.")

# ===================== Halaman Analisis =====================
if page == "📊 Analisis":
    st.markdown(
        '<div class="hero"><h1>📈 Analisis Sentimen Isu Publik</h1><p>Masukkan teks atau unggah file CSV/Excel untuk menganalisis sentimen secara otomatis!</p></div>',
        unsafe_allow_html=True
    )

    # Pilihan metode input
    option = st.radio("Pilih metode input:", [" Teks Manual", " Upload File (CSV/Excel)"], horizontal=True)

    if option == " Teks Manual":
        # --- Input teks seperti sebelumnya ---
        user_input = st.text_area("Masukkan teks Anda di sini", "")
        if st.button("Analisis Sentimen"):
            if not user_input.strip():
                st.warning("⚠️ Silakan masukkan teks terlebih dahulu.")
            else:
                processed = preprocess_text(user_input)
                X = vectorizer.transform([processed])
                probs = model.predict_proba(X)[0]

                if probs[1] >= probs[0]:
                    label_text = "Positif"
                    emoji = "😊"
                    css_class = "positive"
                else:
                    label_text = "Negatif"
                    emoji = "😠"
                    css_class = "negative"

                feature_names = np.array(vectorizer.get_feature_names_out())
                tfidf_scores = X.toarray()[0]

                top_word = None
                if tfidf_scores.sum() > 0:
                    idx_max = tfidf_scores.argmax()
                    if tfidf_scores[idx_max] > 0:
                        top_word = feature_names[idx_max]

                html_card = f"""
                <div class="sentiment-card {css_class}">
                    <div class="icon-badge">{emoji}</div>
                    <p class="sent-title">Sentimen Terdeteksi</p>
                    <p class="sent-value {css_class}">{label_text}</p>
                """
                if top_word:
                    html_card += f"""<div class='chip'>Kata Kunci: {top_word}</div>"""
                html_card += "</div>"

                st.markdown(html_card, unsafe_allow_html=True)

                sorted_idx = np.argsort(tfidf_scores)[::-1][:5]
                if tfidf_scores.sum() > 0:
                    st.markdown('<div class="daftar-kata-title">📚 Daftar Kata</div>', unsafe_allow_html=True)
                    chips_html = "<div class='chips-container'>"
                    for idx in sorted_idx:
                        if tfidf_scores[idx] > 0:
                            chips_html += f"<div class='chip'>{feature_names[idx]} ({tfidf_scores[idx]:.3f})</div>"
                    chips_html += "</div>"
                    st.markdown(chips_html, unsafe_allow_html=True)
                else:
                    st.info("Tidak ada kata yang terdeteksi.")

                st.markdown('<div class="funfact">💡 <i>Fun fact:</i> Analisis sentimen ini bisa membantu anda membaca hati dan pikiran secara otomatis.</div>', unsafe_allow_html=True)

    else:
        # --- Input file CSV/Excel ---
        uploaded_file = st.file_uploader("Unggah file CSV atau Excel yang berisi komentar", type=["csv", "xlsx"])

        if uploaded_file is not None:
            try:
                # Baca file sesuai format
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)

                st.write("## 📄 Preview Data:")
                st.dataframe(df.head())

                # Asumsi kolom teks bernama “komentar” (bisa diubah)
                text_col = st.selectbox("Pilih kolom yang berisi teks komentar:", df.columns)

                if st.button("Analisis File"):
                    with st.spinner("Sedang menganalisis sentimen... ⏳"):
                        df['preprocessed'] = df[text_col].apply(preprocess_text)
                        X = vectorizer.transform(df['preprocessed'])
                        probs = model.predict_proba(X)

                        df['sentimen'] = np.where(probs[:, 1] >= probs[:, 0], 'Positif', 'Negatif')
                        st.success("✅ Analisis selesai!")

                        # Tampilkan hasil
                        st.write("## 📊 Hasil Analisis Sentimen")
                        st.dataframe(df[[text_col, 'sentimen']])

                        # Unduh hasil
                        csv = df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="Unduh Hasil Analisis (CSV)",
                            data=csv,
                            file_name="hasil_analisis_sentimen.csv",
                            mime="text/csv"
                        )

            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses file: {e}")


# ===================== Halaman Dokumentasi =====================
elif page == "📑 Dokumentasi":
    st.markdown("<h2 id='dokumentasi'>📑 Dokumentasi</h2>", unsafe_allow_html=True)
    st.markdown("### Tahapan Analisis Sentimen")
    st.markdown("""
1. Pengumpulan data komentar dari sumber.
2. Preprocessing: case folding, cleaning, normalization, tokenization, stopword removal, dan stemming.
3. TF-IDF vectorizer
4. Penyeimbangan (opsional): SMOTE atau sampling
5. Split data: train/test (misal 80/20)
6. Modelling dengan algoritma Machine Learning
7. Evaluasi: accuracy, precision, recall, f1-score, confusion matrix
8. Visualisasi: wordcloud, distribusi label.
""")

    st.markdown("### Hasil Evaluasi Model Terbaik")
    st.code("""
                    precision  recall  f1-score   support
negatif       0.88      0.96      0.92       127
positif       0.96      0.87      0.91       127

accuracy                          0.92       254
macro avg     0.92      0.92      0.92       254
weighted avg  0.92      0.92      0.92       254
""", language="text")

    example_images = [
        ("Confusion Matrix", "confusion_matrix.png"),
        ("WordCloud Umum", "wordcloud_umum.png"),
        ("WordCloud Negatif", "wordcloud_negatif.png"),
        ("WordCloud Positif", "wordcloud_positif.png"),
    ]
    for title, path in example_images:
        if os.path.exists(path):
            try:
                img = Image.open(path)
                st.subheader(title)
                # Perubahan: gunakan use_container_width (pengganti use_column_width)
                st.image(img, width=400)
            except Exception:
                st.write(f"File {path} ada tapi gagal dibuka.")
        else:
            st.write(f"{title}: (file `{path}` tidak ditemukan)")

