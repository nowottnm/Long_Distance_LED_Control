#git clone https://github.com/nowottnm/Long_Distance_LED_Control
echo "alias python='/usr/bin/python3'" >> ~/.bashrc
echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
pip3 install ~/Long_Distance_LED_Control/
python3 ~/Long_Distance_LED_Control/install.py
echo "led_control&" >> ~/.bashrc
. ~/.bashrc
