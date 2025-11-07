import cv2
import os


if not os.path.exists("imagens"):
    os.makedirs("imagens")

nome = input("Digite o nome do usuário: ")
pasta_usuario = f"imagens/{nome}"

if not os.path.exists(pasta_usuario):
    os.makedirs(pasta_usuario)


camera = cv2.VideoCapture(0)
count = 0

print("\nTirando fotos... Pressione 'q' para parar\n")

while True:
    ret, frame = camera.read()
    if not ret:
        print("Erro ao acessar a câmera.")
        break

    cv2.imshow("Captura", frame)

  
    if count % 5 == 0 and count < 100:
        img_path = f"{pasta_usuario}/{nome}_{count}.jpg"
        cv2.imwrite(img_path, frame)
        print(f"Foto salva: {img_path}")

    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 100:
        break

camera.release()
cv2.destroyAllWindows()

print("\nCadastro finalizado!")