# 🎌 Anime Nexus: High-Fidelity Anime Generator

**Anime Nexus** is a specialized AI image generation platform focused on the aesthetic of modern anime and digital illustration. Built with **Streamlit**, it utilizes the **Hugging Face Inference API** to provide high-speed, server-side image processing.

## 🚀 Key Features
* **Hugging Face Integration**: Leverages the `stabilityai/stable-diffusion-xl-base-1.0` model for state-of-the-art anime rendering.
* **Secure User Authentication**: Features a custom-built login/signup system with **SHA-256 password hashing**.
* **Persistent User Data**: Utilizes a **JSON-based database** architecture to store user credentials securely without needing a heavy SQL server.
* **Session Memory**: Implements `st.session_state` to maintain a persistent gallery of generated artworks during active sessions.

## 🛠️ The Tech Stack
* **Frontend**: [Streamlit](https://streamlit.io/).
* **Backend Inference**: [Hugging Face Inference API](https://huggingface.co/inference-api).
* **Security**: Python `hashlib` for credential encryption.
* **Database**: Local **JSON** file storage for lightweight data persistence.

## 📖 Operational Guide
1. **Access Control**: Register a new account or log in via the secure portal.
2. **Prompt Engineering**: Enter anime-specific keywords (e.g., "Makoto Shinkai style," "vibrant colors").
3. **Model Handshake**: The app sends a request to Hugging Face and retrieves the generated image.
4. **Export**: Save your favorite generated anime art directly to your local device.

## 📦 Local Installation (HP Victus)
To run **Anime Nexus** on your local machine:

```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/Anime-Nexus.git](https://github.com/YOUR_USERNAME/Anime-Nexus.git)

# Install libraries
pip install streamlit requests Pillow

# Run the app
streamlit run app.py

📜 Repository Structure
app.py: Main application logic and UI.

users.json: Secure encrypted storage for user profiles.

requirements.txt: List of Python dependencies.
