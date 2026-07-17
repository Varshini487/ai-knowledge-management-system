import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="🧠 Knowledge Management System", layout="wide")
st.title("🧠 AI Knowledge Management System")
st.markdown("Your intelligent enterprise knowledge base")

# Mock document store
if "docs" not in st.session_state:
    st.session_state.docs = [
        {"id": 1, "title": "API Design Guidelines", "content": "RESTful endpoints should use nouns for resources...", "tags": ["engineering", "api"], "created": "2026-01-15"},
        {"id": 2, "title": "Incident Response Playbook", "content": "When a critical alert fires, immediately page on-call...", "tags": ["devops", "incident"], "created": "2026-02-10"},
        {"id": 3, "title": "Onboarding Checklist", "content": "New hires should complete: Git setup, VPN access, Slack...", "tags": ["hr", "onboarding"], "created": "2026-03-05"},
    ]

if "queries" not in st.session_state:
    st.session_state.queries = []

tab1, tab2, tab3 = st.tabs(["📚 Documents", "🔍 Search", "💬 Q&A"])

with tab1:
    st.subheader("Uploaded Documents")
    for doc in st.session_state.docs:
        with st.expander(f"📄 {doc['title']} ({', '.join(doc['tags'])})"):
            st.write(doc["content"][:200] + "...")
            st.caption(f"Created: {doc['created']}")
    
    with st.form("upload_form"):
        title = st.text_input("Document Title")
        content = st.text_area("Document Content", height=150)
        tags_input = st.text_input("Tags (comma-separated)")
        if st.form_submit_button("📤 Upload Document"):
            if title and content:
                st.session_state.docs.append({
                    "id": len(st.session_state.docs) + 1,
                    "title": title,
                    "content": content,
                    "tags": [t.strip() for t in tags_input.split(",")],
                    "created": datetime.now().strftime("%Y-%m-%d")
                })
                st.success("Document uploaded!")

with tab2:
    st.subheader("Semantic Search")
    query = st.text_input("🔎 Search your knowledge base...")
    if query:
        # Mock semantic matching
        matches = []
        for doc in st.session_state.docs:
            if any(word in doc["content"].lower() for word in query.lower().split()):
                relevance = 0.85 if doc["title"].lower().count(query.lower()) else 0.65
                matches.append((doc, relevance))
        matches.sort(key=lambda x: x[1], reverse=True)
        
        if matches:
            for doc, score in matches[:5]:
                st.markdown(f"**{doc['title']}** — {score:.0%} relevance")
                st.write(doc["content"][:150] + "...")
                st.write(f"Tags: {', '.join(doc['tags'])}")
                st.divider()
        else:
            st.info("No documents found. Try a different search.")

with tab3:
    st.subheader("Ask Anything About Your Knowledge Base")
    user_q = st.text_input("💬 Your question:")
    
    if user_q:
        st.info("🔍 Searching knowledge base...")
        # Simulate RAG: retrieve relevant docs
        relevant = [d for d in st.session_state.docs if any(w in d["content"].lower() for w in user_q.lower().split())]
        
        if relevant:
            st.markdown("### Answer (based on your docs):")
            answer = f"Based on {len(relevant)} relevant document(s):

"
            for doc in relevant[:3]:
                answer += f"- **{doc['title']}**: {doc['content'][:100]}...
"
            st.write(answer)
            
            st.markdown("### 📚 Source Documents:")
            for doc in relevant[:3]:
                st.write(f"- {doc['title']}")
        else:
            st.warning("❓ I couldn't find relevant documents for this question. Try rephrasing.")
        
        st.session_state.queries.append({"q": user_q, "timestamp": datetime.now().isoformat()})
