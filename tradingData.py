trades=[
  {"pair":"BTC/USDT","entry":"108000","sl":"107000","tp":"112000","risk":"منخفضة"},
  {"pair":"EUR/USD","entry":"1.0850","sl":"1.0820","tp":"1.0900","risk":"متوسطة"},
  {"pair":"USD/JPY","entry":"148.70","sl":"149.10","tp":"147.50","risk":"مرتفعة"},
]

def get_trade_text():
  return "\n".join(
    f"🔹 {t['pair']}: دخول {t['entry']} | وقف {t['sl']} | هدف {t['tp']} | خطورة {t['risk']}"
    for t in trades
  )
