#!/bin/bash

#chmod a+x (yourscriptname)

#!/bin/bash

# Získání adresáře, ve kterém je umístěný tento skript
script_dir="$(cd "$(dirname "$0")" && pwd)"

# Přejít do adresáře skriptu
cd "$script_dir"

# Vybrání souboru pomocí zenity
selected_file=$(zenity --file-selection --title="Vyberte Pythonový skript ke spuštění" --file-filter="Pythonové skripty (*.py) | *.py")

# Zkontrolovat, zda uživatel zvolil soubor
if [ -z "$selected_file" ]; then
  echo "Není vybrán žádný soubor. Ukončuji skript."
  exit 1
fi

# Spustit vybraný Pythonový skript pomocí Pythonu 3
python3 "$selected_file"
