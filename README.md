# 🇦🇿 YERAZ-98 ULTIMATE STRESS TESTER (V1.0)

Bu alət şəbəkə təhlükəsizliyini yoxlamaq və serverlərin yükə davamlılığını sınaqdan keçirmək üçün **yeraz98** tərəfindən hazırlanmışdır. Professional stress-test alətidir.

## 🚀 Xüsusiyyətlər
* **Ağıllı Port Analizi:** Hədəf IP-də açıq portları avtomatik müəyyən edir.
* **Yüksək Sürət:** 1000-dən çox thread (axın) ilə maksimum paket göndərişi.
* **Anonimlik:** Paketlərin izlənilməsini çətinləşdirən struktur.
* **İstifadəçi Dostu:** Sadə interfeys və sürətli nəticə.

## 🛠️ Quraşdırılma (Termux)
Əgər aracı yenidən yükləmək istəsəniz:
```bash
pkg update && pkg upgrade
pkg install python git -y
git clone [https://github.com/yeraz98/Yeraz-98-Ultimate-Stress-Tester](https://github.com/yeraz98/Yeraz-98-Ultimate-Stress-Tester)
cd Yeraz-98-Ultimate-Stress-Tester
python yeraz_test.py
