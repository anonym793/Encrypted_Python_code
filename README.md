pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git
termux-setup-storage
git clone https://github.com/anonym793/Encrypted_Python_code.git
cd grey_enc
python grey_enc.py
