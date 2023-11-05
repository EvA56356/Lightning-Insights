# --- System Config ---

# --- Model Selection ---
OPENAI_GPT3 = "gpt-3.5-turbo-16k"
OPENAI_GPT4 = "gpt-4"
CLAUDE_DEFAULT = "claude-2"

# 单次读取评价条数上限
REVIEW_NUM_CAP = 300
OPENAI_CAP = 75

USER_POSITION = {
    "en": ["Not Selected", "👨🏻‍💻 E-commerce Operations", "🤵🏻‍♂️ Customer Service", "👩🏻‍🔬 Product R&D", "👩🏻‍🔧 Production/QC", "✈️ Logistics/Supply Chain"]
}
ANALYSIS_FOCUS = {
    "en": ["Not Selected", "⚙️ Product Features", "💎 Product Quality", "🎨 Design & Appearance", "🖐️ User Experience", "💰 Pricing", "💳 Customer Service & Ordering", "📦 Packaging & Logistics"]
}

# --- Container Config ---
CONTENT_COL_CONFIG = [1, 6, 1]