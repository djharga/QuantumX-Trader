import openai, os
openai.api_key = os.getenv("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")

def generate_strategy(prompt, indicator="RSI"):
    sys_msg = f"أنت خبير في Pine Script تستخدم مؤشر {indicator}. رد فقط بالكود."
    resp = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[{"role":"system","content":sys_msg},{"role":"user","content":prompt}],
      temperature=0.3
    )
    return resp.choices[0].message.content
