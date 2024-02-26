# interactsh-wrapper
Acto.io assignment repo

make sure -> you have installed python 3.9+

install pandas , django and other requirements using

pip install --no-cache-dir -r requirements.txt
To run the program, open the project folder and run following commnad

then run python manage.py runserver 8000


/getURL
/getInteraction
/getURL This endpoint returns a runs an instance of interactsh-client and returns the URL corresponding to it.

http://127.0.0.1:8000/getURL
/getInteraction This endpoint returns the interactions made by users on the url provided by the interactsh-client.

This api takes three query parameter

link -> this is the url for which you want to see interactions (needed)
startDateTime -> specifying this query parameter will filter the interactions to show only those interactions which happend after . Default is 1970-01-01 00:00:00
endDateTime -> specifying this query paramter will filer the interactions to show only those interactions which happened before Defailt is current time
usage examples

http://127.0.0.1:8000/getInteraction?link=ghdwsbgfoiawebgoihagirbg.oast.mov

http://127.0.0.1:8000/getInteraction?link=ghdwsbgfoiawebgoihagirbg.oast.mov&startDateTime=1970-01-01%2000:00:00 

http://127.0.0.1:8000/getInteraction?link=ghdwsbgfoiawebgoihagirbg.oast.mov&endDateTime=2024-02-01%2000:00:00

http://127.0.0.1:8000/getInteraction?link=ghdwsbgfoiawebgoihagirbg.oast.mov&startDateTime=1970-01-01%2000:00:00&endDateTime=2024-02-01%2000:00:00

