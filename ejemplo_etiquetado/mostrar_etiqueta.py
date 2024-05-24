import os
# pip install opencv-python
import cv2

#############################################
####### Anotar imagenes desde archivo #######
#############################################

# Estas anotaciones se consiguen desde roboflow, en raw data abajo izq, descargar la imagen y 
# ponerla en el dir local (ejemplo_etiquetado), luego el json de abajo en la pestaña de roboflow y ponerlo aca abajo:
annotations = {
    "boxes": [
        {
            "label": "ipomoea ",
            "x": 205,
            "y": 116.5,
            "width": 62,
            "height": 55
        },
        {
            "label": "ipomoea ",
            "x": 200,
            "y": 224.5,
            "width": 68,
            "height": 53
        },
        {
            "label": "ipomoea ",
            "x": 295.5,
            "y": 211,
            "width": 55,
            "height": 42
        },
        {
            "label": "ipomoea ",
            "x": 115.5,
            "y": 183,
            "width": 61,
            "height": 52
        },
        {
            "label": "ipomoea ",
            "x": 74,
            "y": 239,
            "width": 60,
            "height": 50
        },
        {
            "label": "ipomoea ",
            "x": 257.5,
            "y": 59.5,
            "width": 45,
            "height": 45
        },
        {
            "label": "ipomoea ",
            "x": 362,
            "y": 198,
            "width": 44,
            "height": 46
        }
    ],
    "height": 375,
    "key": "481d1af7d8c4a7a77fea581b4e25bb0a.jpeg",
    "width": 500
}

image_path = os.getcwd() + '/ejemplo_etiquetado/' + annotations["key"]
image = cv2.imread(image_path)
box_color = (0, 0, 255)
box_thickness = 2

for box in annotations["boxes"]:
    x_center = float(box["x"])
    y_center = float(box["y"])
    width = float(box["width"])
    height = float(box["height"])
    
    x_center *= image.shape[1] / annotations["width"]
    y_center *= image.shape[0] / annotations["height"]
    width *= image.shape[1] / annotations["width"]
    height *= image.shape[0] / annotations["height"]
    
    x = int(x_center - width / 2)
    y = int(y_center - height / 2)
    width = int(width)
    height = int(height)
    
    box["x"] = x
    box["y"] = y
    box["width"] = width
    box["height"] = height

for box in annotations["boxes"]:
    x = box["x"]
    y = box["y"]
    width = box["width"]
    height = box["height"]
    top_left = (x, y)
    bottom_right = (x + width, y + height)
    cv2.rectangle(image, top_left, bottom_right, box_color, box_thickness)


annotated_image_path = os.getcwd() + "/ejemplo_etiquetado/" + annotations["key"] + "_etiq" + ".jpg"
cv2.imwrite(annotated_image_path, image)

print(f"Imagen anotada guardada como {annotated_image_path}")
