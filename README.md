# 💧 Alert! Drink Water v1

## 📑 Index
- [♎ Personal Use Only](#-personal-use-only)
- [✅ How to Use?](#-how-to-use)
- [⚙️ Convert .py to .exe](#-to-convert-a-py-file-into-an-exe)
- [🇧🇷 Tradução em Português](#-tradução-em-português)

---

*🇺🇸 Tip: Browse using Emojis.*

*🇧🇷 Dica: Naveggue usando os Emojis.*

---

## ♎ Personal Use Only
- If you're downloading this for personal use or to learn something, don't worry about legal issues.
- However, **do not use it for harmful or malicious purposes**.

## ✅ How to Use?
- To receive hydration reminders, simply run the `.exe` file.
- To view or edit the source code, open the `main.py` file.

## ⚙️ To Convert a `.py` File into an `.exe`

```bash
pyinstaller --onefile --name="DrinkWaterAlert" --icon=image\icon.ico --add-data="image\icon.ico;image" --add-data="audio\SFX_waterdrip.wav;audio" --add-data="audio\SFX_minecraftdrink.wav;audio" --add-data="audio\SFX_drinkwaterIA.wav;audio" --add-data="audios.json;." --add-data="strings.json;." --hidden-import=plyer.platforms.win.notification --hidden-import=plyer.platforms.win --hidden-import=plyer.platforms main.py
```

- `--onefile` : Bundle everything into a single `.exe`  
- `--name` : Sets the name of the executable  
- `--icon` : Sets a custom icon  
- `--add-data` : Include additional files (such as sounds or media)
- `--hidden-import` : "Hidden" imports, usually from libraries that need
- `main.py` : Entry point (your main Python script)

❗ Unfortunately, changing just one file, such as audio or images, and renaming them, will not change the `.exe`, only if you run `main.py`. So to change it, you will have to run the code in the terminal in the section "⚙️ To Convert a `.py` into an `.exe`"

---

## 🇧🇷 Tradução em Português

### ♎ Uso Pessoal Somente
- Se você está baixando para uso pessoal ou para aprender, não se preocupe com questões legais.
- No entanto, **não use para fins maliciosos ou prejudiciais**.

### ✅ Como Usar?
- Para receber lembretes de hidratação, basta executar o arquivo `.exe`.
- Para ver ou editar o código-fonte, abra o arquivo `main.py`.

### ⚙️ Como Transformar um `.py` em `.exe`

```bash
pyinstaller --onefile --name="DrinkWaterAlert" --icon=image\icon.ico --add-data="image\icon.ico;image" --add-data="audio\SFX_waterdrip.wav;audio" --add-data="audio\SFX_minecraftdrink.wav;audio" --add-data="audio\SFX_drinkwaterIA.wav;audio" --add-data="audios.json;." --add-data="strings.json;." --hidden-import=plyer.platforms.win.notification --hidden-import=plyer.platforms.win --hidden-import=plyer.platforms main.py
```

- `--onefile` : Gera um único executável  
- `--name` : Nome do aplicativo  
- `--icon` : Ícone personalizado  
- `--add-data` : Adiciona arquivos extras (áudios, imagens, etc.)
- `--hidden-import` : Importações "ocultas", geralmente de bibliotecas que precisam
- `main.py` : Arquivo principal (script Python)

❗❗❗ Infelizmente, alterar apenas um arquivo, como os de áudio ou imagens, e renomea-los, não irá fazer o `.exe` mudar, apenas caso execute o `main.py`. Então para alterar, precisaria rodar no terminal o código da seção "⚙️ Como Transformar um `.py` em `.exe`"