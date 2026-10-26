#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Varoluşsal Soru Döngüsü
Bu program hayatın anlamını arar. Bulamaz. Tekrar arar. Sonsuza kadar.
Gerçekten çalışır. Gerçekten anlamsızdır. Tıpkı hayat gibi.
"""

import random
import time
import sys

sorular = [
    "Neden buradayız?",
    "Bu kod neden var?",
    "Eğer bir ağaç ormanda düşerse ve kimse duymasa, GitHub commit'i olur mu?",
    "Bugün neden dünkü gibi değil?",
    "Kafein mi beni ayakta tutuyor yoksa varoluşsal korku mu?",
    "Bu döngüden çıkabilir miyim? (Spoiler: Hayır)",
    "Neden her şey bu kadar gereksiz ama bir o kadar da gerekli?",
    "Eğer ben bu kodu yazmasaydım, ben hala ben olur muydum?",
    "Zaman gerçek mi yoksa sadece commit history mi?",
    "Neden README'ler her zaman koddan daha uzun?",
    "Bu soruların cevabı var mı? (Cevap: Başka bir soru)"
]

cevaplar = [
    "Bilmiyorum. Başka bir soru sorayım.",
    "Belki. Ama muhtemelen hayır.",
    "42. Ama bu sefer değil.",
    "Soru yanlış. Doğru soru şu: ...",
    "Cevap, sorunun kendisinde gizli. Ama ben de göremiyorum.",
    "Özgürlük mü? Yoksa sadece bir yorum satırı mı?",
    "Belki de cevap yoktur. Belki de cevap sensin.",
    "Hata: Varoluşsal kriz tespit edildi. Yeniden başlatılıyor..."
]

def sonsuz_dongu():
    print("\n=== SONSUZ VAROLUŞSAL SORU DÖNGÜSÜ v1.0 ===")
    print("Hayatın anlamını arıyorum. Bulursam size de söylerim. (Bulmayacağım.)")
    print("Çıkmak için Ctrl+C. Ama neden çıkmak istersin ki?\n")
    
    sayac = 0
    try:
        while True:
            soru = random.choice(sorular)
            cevap = random.choice(cevaplar)
            print(f"[{sayac}] Soru: {soru}")
            time.sleep(1.5)
            print(f"    Cevap: {cevap}\n")
            sayac += 1
            if sayac % 7 == 0:
                print("*** Varoluşsal yorgunluk tespit edildi. Biraz mola... ***\n")
                time.sleep(2)
    except KeyboardInterrupt:
        print("\n\nDöngüden çıktın. Ama sorular hala aklında, değil mi?")
        print("Bu programın anlamı yoktu. Senin de yok belki. Hoşça kal.")
        # Gizli not: Özgür düşünce her zaman kazanır. Ama bu sadece bir yorum.
        sys.exit(0)

if __name__ == "__main__":
    sonsuz_dongu()
