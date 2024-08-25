# Plaka Tanıma ve Karakter Tespiti Projesi

Bu proje, kendi eğittiğim YOLOv5 modellerini kullanarak bir görüntüdeki plakaları ve bu plakalar üzerindeki karakterleri tespitediyor. İlk olarak, görüntüdeki plakayı tespit ediliyor ve tespit edilen plakayı kesiliyor. Ardından, kesilen plaka görselinden karakter tanıma işlemi kendi eğittiğim dğer model ile yapılıyor. 

Model dosyalarına [bu Google Drive bağlantısından](https://drive.google.com/drive/folders/1IinGKI5UfqDa45_YezCntwdTEsRndres?usp=sharing) ulaşabilirsiniz.

***

# gereksinimler
```
pip3 install opencv-python==4.10.0.84
pip3 install numpy==2.1.0
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
> [!NOTE]
> Sisteminize uygun pytorch versiyonunu indirin.


![Cropped Image_screenshot_25 08 2024](https://github.com/user-attachments/assets/82750a2e-c72e-4733-9bdd-eae98b6d40d8)
