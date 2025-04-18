import streamlit as st
import re 

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("Password Strength Checker")

st.markdown("""
### Welcome!
Check the strength of your password and get smart tips to improve it.  
""")

# CSS to prevent copying password input (optional)
st.markdown("""
    <style>
    .no-copy {
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="no-copy">', unsafe_allow_html=True)
password = st.text_input("Enter your password", type="password")
st.markdown('</div>', unsafe_allow_html=True)

feedback = []
score = 0

if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Minimum 8 characters required.")
    
    # Uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Use both uppercase and lowercase letters.")
    
    # Digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔸 Add at least one number.")
    
    # Special character
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("🔸 Include a special character (!@#$%&*).")

    # Final Strength Evaluation
    st.markdown("### Strength:")
    if score == 4:
        st.success("✅ Strong password!")
    elif score == 3:
        st.warning("⚠️ Medium strength. Can be improved.")
    else:
        st.error("❌ Weak password. Needs improvement.")

    # Tips
    if feedback:
        st.markdown("### Suggestions:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to analyze.")
