import requests
import streamlit as st

LANGUAGE_TEXT = {
    "English": {
        "welcome_title": "What would you like to explore?",
        "welcome_copy": "Start with a question. Your conversation stays local.",
        "learn_title": "Learn clearly",
        "learn_copy": "Ask for simple explanations, examples, or step-by-step lessons.",
        "build_title": "Build with Python",
        "build_copy": "Get help creating scripts, websites, and Generative AI projects.",
        "try_title": "Explore languages",
        "try_copy": "Ask naturally in your selected language and keep learning.",
        "placeholder": "Ask anything...",
    },
    "తెలుగు": {
        "welcome_title": "మీరు ఏమి నేర్చుకోవాలనుకుంటున్నారు?",
        "welcome_copy": "ఒక ప్రశ్నతో ప్రారంభించండి. మీ సంభాషణ స్థానికంగానే ఉంటుంది.",
        "learn_title": "సులభంగా నేర్చుకోండి",
        "learn_copy": "సరళమైన వివరణలు, ఉదాహరణలు లేదా దశల వారీ పాఠాలు అడగండి.",
        "build_title": "Python తో నిర్మించండి",
        "build_copy": "స్క్రిప్ట్‌లు, వెబ్‌సైట్‌లు మరియు Generative AI ప్రాజెక్ట్‌లలో సహాయం పొందండి.",
        "try_title": "భాషలను ప్రయత్నించండి",
        "try_copy": "మీకు నచ్చిన భాషలో సహజంగా అడిగి నేర్చుకోండి.",
        "placeholder": "ఏదైనా అడగండి...",
    },
    "हिन्दी": {
        "welcome_title": "आप क्या सीखना चाहेंगे?",
        "welcome_copy": "एक सवाल से शुरुआत करें। आपकी बातचीत स्थानीय रहती है।",
        "learn_title": "आसानी से सीखें",
        "learn_copy": "सरल व्याख्या, उदाहरण या चरण-दर-चरण पाठ मांगें।",
        "build_title": "Python से बनाएं",
        "build_copy": "स्क्रिप्ट, वेबसाइट और Generative AI प्रोजेक्ट बनाने में मदद लें।",
        "try_title": "भाषाएं आजमाएं",
        "try_copy": "अपनी चुनी हुई भाषा में स्वाभाविक रूप से सवाल पूछें।",
        "placeholder": "कुछ भी पूछें...",
    },
    "தமிழ்": {
        "welcome_title": "நீங்கள் எதை கற்றுக்கொள்ள விரும்புகிறீர்கள்?",
        "welcome_copy": "ஒரு கேள்வியுடன் தொடங்குங்கள். உங்கள் உரையாடல் உள்ளூரிலேயே இருக்கும்.",
        "learn_title": "தெளிவாக கற்கவும்",
        "learn_copy": "எளிய விளக்கங்கள், உதாரணங்கள் அல்லது படிப்படியான பாடங்களைக் கேளுங்கள்.",
        "build_title": "Python மூலம் உருவாக்கவும்",
        "build_copy": "ஸ்கிரிப்ட், வலைத்தளம் மற்றும் Generative AI திட்டங்களுக்கு உதவி பெறுங்கள்.",
        "try_title": "மொழிகளை முயற்சிக்கவும்",
        "try_copy": "தேர்ந்தெடுத்த மொழியில் இயல்பாக கேள்வி கேளுங்கள்.",
        "placeholder": "எதையும் கேளுங்கள்...",
    },
    "ಕನ್ನಡ": {
        "welcome_title": "ನೀವು ಏನು ಕಲಿಯಲು ಬಯಸುತ್ತೀರಿ?",
        "welcome_copy": "ಒಂದು ಪ್ರಶ್ನೆಯಿಂದ ಪ್ರಾರಂಭಿಸಿ. ನಿಮ್ಮ ಸಂಭಾಷಣೆ ಸ್ಥಳೀಯವಾಗಿಯೇ ಇರುತ್ತದೆ.",
        "learn_title": "ಸ್ಪಷ್ಟವಾಗಿ ಕಲಿಯಿರಿ",
        "learn_copy": "ಸರಳ ವಿವರಣೆಗಳು, ಉದಾಹರಣೆಗಳು ಅಥವಾ ಹಂತ ಹಂತದ ಪಾಠಗಳನ್ನು ಕೇಳಿ.",
        "build_title": "Python ಬಳಸಿ ನಿರ್ಮಿಸಿ",
        "build_copy": "ಸ್ಕ್ರಿಪ್ಟ್, ವೆಬ್‌ಸೈಟ್ ಮತ್ತು Generative AI ಯೋಜನೆಗಳಿಗೆ ಸಹಾಯ ಪಡೆಯಿರಿ.",
        "try_title": "ಭಾಷೆಗಳನ್ನು ಪ್ರಯತ್ನಿಸಿ",
        "try_copy": "ಆಯ್ಕೆ ಮಾಡಿದ ಭಾಷೆಯಲ್ಲಿ ಸಹಜವಾಗಿ ಪ್ರಶ್ನೆ ಕೇಳಿ.",
        "placeholder": "ಏನು ಬೇಕಾದರೂ ಕೇಳಿ...",
    },
    "മലയാളം": {
        "welcome_title": "നിങ്ങൾ എന്താണ് പഠിക്കാൻ ആഗ്രഹിക്കുന്നത്?",
        "welcome_copy": "ഒരു ചോദ്യത്തോടെ ആരംഭിക്കൂ. നിങ്ങളുടെ സംഭാഷണം ലോക്കലായി തുടരും.",
        "learn_title": "വ്യക്തമായി പഠിക്കൂ",
        "learn_copy": "ലളിതമായ വിശദീകരണങ്ങളും ഉദാഹരണങ്ങളും ഘട്ടംഘട്ടമായ പാഠങ്ങളും ചോദിക്കൂ.",
        "build_title": "Python ഉപയോഗിച്ച് നിർമ്മിക്കൂ",
        "build_copy": "സ്ക്രിപ്റ്റുകളും വെബ്‌സൈറ്റുകളും Generative AI പ്രോജക്റ്റുകളും നിർമ്മിക്കാൻ സഹായം നേടൂ.",
        "try_title": "ഭാഷകൾ പരീക്ഷിക്കൂ",
        "try_copy": "തിരഞ്ഞെടുത്ത ഭാഷയിൽ സ്വാഭാവികമായി ചോദ്യങ്ങൾ ചോദിക്കൂ.",
        "placeholder": "എന്തും ചോദിക്കൂ...",
    },
    "বাংলা": {
        "welcome_title": "আপনি কী শিখতে চান?",
        "welcome_copy": "একটি প্রশ্ন দিয়ে শুরু করুন। আপনার কথোপকথন স্থানীয় থাকে।",
        "learn_title": "সহজে শিখুন",
        "learn_copy": "সহজ ব্যাখ্যা, উদাহরণ বা ধাপে ধাপে পাঠ চাইতে পারেন।",
        "build_title": "Python দিয়ে তৈরি করুন",
        "build_copy": "স্ক্রিপ্ট, ওয়েবসাইট এবং Generative AI প্রকল্প তৈরিতে সাহায্য নিন।",
        "try_title": "ভাষা চেষ্টা করুন",
        "try_copy": "আপনার নির্বাচিত ভাষায় স্বাভাবিকভাবে প্রশ্ন করুন।",
        "placeholder": "যেকোনো কিছু জিজ্ঞেস করুন...",
    },
    "मराठी": {
        "welcome_title": "तुम्हाला काय शिकायचे आहे?",
        "welcome_copy": "एका प्रश्नाने सुरुवात करा. तुमचे संभाषण स्थानिक राहते.",
        "learn_title": "सोप्या पद्धतीने शिका",
        "learn_copy": "सोपे स्पष्टीकरण, उदाहरणे किंवा टप्प्याटप्प्याने धडे विचारा.",
        "build_title": "Python वापरून तयार करा",
        "build_copy": "स्क्रिप्ट, वेबसाइट आणि Generative AI प्रकल्प तयार करण्यासाठी मदत घ्या.",
        "try_title": "भाषा वापरून पहा",
        "try_copy": "तुमच्या निवडलेल्या भाषेत सहज प्रश्न विचारा.",
        "placeholder": "काहीही विचारा...",
    },
}

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

with st.sidebar:
    language = st.selectbox("Interface Language", list(LANGUAGE_TEXT.keys()))

ui_text = LANGUAGE_TEXT[language]

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.block-container { max-width: 850px; padding-top: 2rem; }
.hero-card {
    background: linear-gradient(135deg, #111827, #020617);
    border: 1px solid rgba(34,197,94,0.40);
    border-radius: 24px;
    padding: 26px;
    margin-bottom: 20px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.20);
}
.brand-title { font-size: 34px; font-weight: 800; color: #f8fafc; margin-bottom: 6px; }
.brand-subtitle { font-size: 16px; color: #d1d5db; }
.green { color: #22c55e; }
.small-note { color: #9ca3af; font-size: 13px; margin-top: 8px; }
.eyebrow {
    color: #22c55e;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.welcome-title { font-size: 26px; font-weight: 750; color: #f8fafc; margin: 8px 0; }
.welcome-copy { color: #9ca3af; margin-bottom: 18px; }
.welcome-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 24px; }
.welcome-card {
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 14px;
    padding: 16px;
    background: rgba(30,41,59,0.42);
    min-height: 92px;
}
.welcome-card strong { color: #f8fafc; display: block; margin-bottom: 7px; }
.welcome-card span { color: #94a3b8; font-size: 13px; line-height: 1.4; }
.stButton button {
    border-radius: 12px;
    background-color: #22c55e;
    color: #052e16;
    font-weight: 700;
    border: none;
}
.stButton button:hover { background-color: #16a34a; color: #052e16; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero-card">
    <div class="eyebrow">Private local AI workspace</div>
    <div class="brand-title">AI <span class="green">Chatbot</span></div>
    <div class="brand-subtitle">A simple AI chatbot for answering questions and learning.</div>
    <div class="small-note">Python · Streamlit · Ollama · Conversation memory</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Ollama Settings
# -----------------------------
OLLAMA_URL = "http://localhost:11434/api/chat"

with st.sidebar:
    st.title("⚙️ Settings")

    model = st.selectbox(
        "Choose Ollama Model",
        ["llama3.2", "llama3.1", "llama3", "mistral", "gemma2", "qwen2.5", "qwen2.5:3b"],
        index=0
    )

    temperature = st.slider(
        "Temperature / Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="0 = focused/robotic, 1 = creative"
    )

    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful AI assistant. Explain concepts clearly and simply. When useful, respond with examples.",
        height=120
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Helper Function
# -----------------------------
def check_ollama_running():
    try:
        response = requests.get("http://localhost:11434", timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


# -----------------------------
# Session State / Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Ollama Health Check
# -----------------------------
if not check_ollama_running():
    st.error("Ollama is not running. Please open terminal and run: ollama serve")
    st.info("Then pull a model using: ollama pull llama3.2")
    st.stop()

if not st.session_state.messages:
    st.markdown(
        f"""
        <div class="welcome-title">{ui_text['welcome_title']}</div>
        <div class="welcome-copy">{ui_text['welcome_copy']}</div>
        <div class="welcome-grid">
            <div class="welcome-card"><strong>{ui_text['learn_title']}</strong><span>{ui_text['learn_copy']}</span></div>
            <div class="welcome-card"><strong>{ui_text['build_title']}</strong><span>{ui_text['build_copy']}</span></div>
            <div class="welcome-card"><strong>{ui_text['try_title']}</strong><span>{ui_text['try_copy']}</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Show Chat History
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_prompt = st.chat_input(ui_text["placeholder"])

if user_prompt:
    # 1. Display user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # 2. Build full messages list for Ollama
    language_instruction = (
        "Respond in English."
        if language == "English"
        else f"Respond in {language}. Keep technical names and code in their original form."
    )
    messages_for_ollama = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": language_instruction},
    ]
    messages_for_ollama.extend(st.session_state.messages)

    # 3. Stream assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            payload = {
                "model": model,
                "messages": messages_for_ollama,
                "stream": True,
                "options": {
                    "temperature": temperature
                }
            }

            with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120) as response:
                response.raise_for_status()

                for line in response.iter_lines():
                    if line:
                        data = line.decode("utf-8")
                        import json
                        chunk = json.loads(data)

                        if "message" in chunk and "content" in chunk["message"]:
                            content = chunk["message"]["content"]
                            full_response += content
                            response_placeholder.markdown(full_response + "▌")

                        if chunk.get("done", False):
                            break

            response_placeholder.markdown(full_response)

        except requests.exceptions.HTTPError as e:
            full_response = (
                f"HTTP Error: {str(e)}\n\n"
                f"Most likely the model '{model}' is not downloaded.\n\n"
                f"Run this command in terminal:\n\n"
                f"ollama pull {model}"
            )
            response_placeholder.error(full_response)

        except Exception as e:
            full_response = f"Error: {str(e)}"
            response_placeholder.error(full_response)

    # 4. Store assistant response in memory
    st.session_state.messages.append({"role": "assistant", "content": full_response})
