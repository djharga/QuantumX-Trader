import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# ✅ imports بعد تعديل أسماء الملفات:
from aiEngine import generate_strategy
from tradingData import get_trade_text
from utils import timestamp

# 🧠 إعداد الواجهة
app = tk.Tk()
app.title("🔥 QuantumX Trader™")
app.geometry("750x700")
app.configure(bg="#1f1f1f")

# ⚙️ تبديل الوضع (Light/Dark)
theme = "Dark"
def switch_theme():
    global theme
    theme = "Light" if theme == "Dark" else "Dark"
    app.configure(bg="#f4f4f4" if theme == "Light" else "#1f1f1f")

# 🧩 واجهة اختيار المؤشر
tk.Label(app, text="اختر المؤشر:", fg="white", bg="#1f1f1f").pack(pady=5)
indicator_cb = ttk.Combobox(app, values=["RSI", "MACD", "EMA", "Bollinger", "ATR"])
indicator_cb.set("RSI")
indicator_cb.pack()

# 📝 إدخال وصف الاستراتيجية
tk.Label(app, text="وصف الاستراتيجية:", fg="white", bg="#1f1f1f").pack()
desc_input = scrolledtext.ScrolledText(app, height=4, bg="#2e2e2e", fg="white")
desc_input.pack(fill="x", padx=10, pady=5)

# 📤 مربع الإخراج
output_box = scrolledtext.ScrolledText(app, height=15, bg="#101010", fg="#00ff99")
output_box.pack(fill="both", padx=10, pady=10, expand=True)

# 🚀 توليد الكود
def on_generate():
    prompt = desc_input.get("1.0", "end").strip()
    ind = indicator_cb.get()
    if not prompt:
        messagebox.showerror("خطأ", "اكتب وصف الاستراتيجية")
        return

    code = generate_strategy(prompt, ind)
    output_box.delete("1.0", "end")
    output_box.insert("end", code)

    # حفظ الكود وكتابة في سجل الاستراتيجيات
    fname = f"strategy_{timestamp()}.pine"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(code)
    with open("history.log", "a", encoding="utf-8") as f:
        f.write(f"{timestamp()}|{ind}|{prompt[:30]}...\n")

    messagebox.showinfo("✅ تم", f"تم حفظ الكود في الملف: {fname}")

# 🔘 زر توليد الكود
tk.Button(app, text="🔄 توليد Pine Script", bg="#007acc", fg="white", command=on_generate).pack(pady=5)

# 📊 صفقات اليوم
tk.Label(app, text="🧾 صفقات اليوم:", fg="white", bg="#1f1f1f").pack()
trades_box = scrolledtext.ScrolledText(app, height=6, bg="#202020", fg="white")
trades_box.insert("end", get_trade_text())
trades_box.config(state="disabled")
trades_box.pack(fill="both", padx=10)

# 🌗 زر تغيير الوضع
tk.Button(app, text="🌓 تغيير الوضع", command=switch_theme).pack(pady=10)

# 🏁 تشغيل التطبيق
app.mainloop()
