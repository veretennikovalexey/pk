class MagicString(str):
    def __new__(cls, text):
        text = f"✨ { text } ✨"
        return super().__new__(cls, text)
        
