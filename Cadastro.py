import cv2
import os

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    pasta = f"imagens/{nome}"
    
    if not os.path.exists("imagens"):
        os.makedirs("imagens")
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    camera = cv2.VideoCapture(0)
    amostra = 1
    numero_amostras = 25
    print("Capturando as faces... Olhe para a câmera.")

    while True:
        conectado, imagem = camera.read()
        if not conectado:
            print("Erro ao acessar a câmera.")
            break

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(imagem_cinza, scaleFactor=1.5, minSize=(150, 150))

        for (x, y, l, a) in faces:
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if amostra <= numero_amostras:
                nome_arquivo = f"{pasta}/foto_{amostra}.jpg"
                cv2.imwrite(nome_arquivo, imagem[y:y + a, x:x + l])
                print(f"[Foto {amostra}/{numero_amostras}] capturada com sucesso!")
                amostra += 1

        cv2.imshow("Captura de Faces", imagem)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if amostra > numero_amostras:
            break

    camera.release()
    cv2.destroyAllWindows()
    print(f"\nCaptura finalizada! As imagens foram salvas na pasta: {pasta}")

def main():
    cadastrar_usuario()

if __name__ == "__main__":
    main()