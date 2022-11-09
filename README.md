# ngrokBeef

running this script basicly runs ```ngrok http 3000```, takes the tunnel url (the publicly usable one), puts it in config.yaml of Beef then finnaly runs beef.

# Setup
1. Download the script
2. put it in the dir above beef. (For example: have the beef executable in /home/<user>/beef/<beef executable> and have publicBeef.py in /home/<user>/publicBeef.py)
3. Make sure the path to ngrok is present in $PATH
4. follow the beef installation and configuration intructions <https://github.com/beefproject/beef/wiki/Installation>
5. ONLY THINGS YOU HAVE TO CHANGE IN config.yaml FILE ARE THE PASSWORD AND UNCOMMENT beef.http.public.* 
    ![image](https://user-images.githubusercontent.com/99650491/200859362-5c5ad832-465e-4f0b-985d-2593a69780d1.png)
    should look like this^^
6. run the script
7. If you get errors then idk fix it ya self or put it in issues tab

# Also it has only been tested on a kali linux vm of mine :)

# ERRORS:
