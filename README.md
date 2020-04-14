# manual_tag
Web aplication for manual inspection of tags assigned to Web 2.0 objects


Instructions

1) Install requirements
   sudo pip3 install requirments.txt
   
2) Create a postgres database named "mantag" and a postgres database user named "mantag_user"

3) Populate database, running:
   python3 populate_db.py
   
4) Run application:
   python3 run.py
   
5) Access in your browser:
   http://127.0.0.1:5001/product
