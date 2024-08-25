import torch
import cv2
import numpy as np

# Birinci model, plaka tespiti 
model = torch.hub.load('ultralytics/yolov5', 'custom', path=' Model Path ')
# İkinci model, plaka üzerindeki karakterleri tespit etmek için.
model2 = torch.hub.load('ultralytics/yolov5', 'custom', path=' Model Path ')

# Görüntüyü renkli olarak okunuyor.
img = cv2.imread(" Resim Path ")

# Birinci model ile tespit ve tahmin sonuçlarının alınması.
results = model(img)
predictions = results.pred[0]

for *box, conf, cls in predictions: 
    x1, y1, x2, y2 = map(int, box)  

    # Tespit edilen plaka kesilir
    cropped_img = img[y1:y2, x1:x2] 
    h, w = cropped_img.shape[:2]  # Yükseklik ve genişliği alınır.

    cropped_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    cropped_img = cv2.resize(cropped_img, (w * 10, h * 10)) # Kesilen kısmı büyüt.
    
    # Netleştirme (kontrastı artırma ve parlaklığı azaltma)
    cropped_img = cv2.convertScaleAbs(cropped_img, alpha=1.4, beta=-30)

    # İkinci model ile tahmin yapın (plaka üzerindeki karakterler için)
    results2 = model2(cropped_img)
    predictions2 = results2.pred[0]

    # Tanımlanan nesneleri ve etiketleri saklayın
    detected_objects = []
    object_labels = []
    for *box, conf, cls in predictions2:
        x1, y1, x2, y2 = map(int, box)
        detected_objects.append((x1, y1, x2, y2, conf, cls))

    # Nesneleri x1 koordinatına göre sıralama
    detected_objects_sorted = sorted(detected_objects, key=lambda obj: obj[0])
    for x1, y1, x2, y2, conf, cls in detected_objects_sorted:
        object_labels.append(str(model2.names[int(cls)]))

    # Etiketleri birleştirin ve görüntüye yazdırın
    label_text = " ".join(object_labels)
    cv2.putText(cropped_img, label_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    # Kesilen ve işlenen görüntüyü gösterin
    cv2.imshow("Cropped Image", cropped_img)
    cv2.waitKey(0) 

# Pencereleri kapat
cv2.destroyAllWindows()
