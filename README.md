App requirements
https://docs.google.com/document/d/1CFEuRvc5_B8Tsdku0RrUd5ymLEP1HBnnFsGkR9xLesE/edit?usp=sharing

# GITIN KÄYTTÖOHJEET

**HUOM: Voit myös käyttää VSCoden sisäistä "Source Control" toimintoa näihin.**
1. Lisää muutokset komennolla `git add .`
2. Committaa muutokset `git commit -m "<MUUTOKSIA_KUVAILEVA_TEKSTI_TÄHÄN>`
3. Puske commit omaan branchiin `git push origin <BRANCHISI_NIMI>`

# ASENNUSOHJEET

## 1. Git branchin luominen

1. Asenna Git (https://git-scm.com/downloads)
2. Luo uusi kansio
3. Avaa GitBash kansion hakemistoon (kansion sisällä paina oikealla hiirellä -> Git Bash Here)
4. Kloonaa GitHub repository suorittamalla komento `git clone https://github.com/starxseeker/AppProg.git`
5. Siirry hakemistossa `AppProg` kansioon kirjoittamalla `cd AppProg/`</br>
Terminaalin pitäisi nyt näyttää jotakuinkin tältä</br>
![image](https://user-images.githubusercontent.com/18125997/141785619-97ec01cd-e369-4883-a6e2-deb774600095.png)

6. Luo oma git branchi suorittamalla komento `git checkout -b <YOUR_BRANCH_NAME>`
7. (master) tai (main) tilalla pitäisi nyt lukea sinun branchin nimi
![image](https://user-images.githubusercontent.com/18125997/141785967-70eae469-38dd-40e1-b638-0cfc9685cb73.png)

8. Puske oma branchisi GitHubiin suorittamalla komento `git push origin <YOUR_BRANCH_NAME>`
9. Tarkista että branchisi näkyy GitHubissa (https://github.com/starxseeker/AppProg/branches)
10. Pidä Git Bash edelleen auki, sillä sitä tarvitaan seuraavassa osiossa




## 2. Kehitysympäristön asennus
1. Asenna VSCode ja Python (versio 3.9.4 ainakin toimii) Version voi tarkistaa kirjoittamalla `python --version` terminaaliin
2. Asenna Python extension VSCodeen (https://marketplace.visualstudio.com/items?itemName=ms-python.python)
3. Asenna pip suorittamalla komento `python -m pip install --upgrade pip`</br>(tämä todennäköisesti löytyy jo mutta hyvä se on päivittää)
4. Varmista että olet juurihakemistossa eli `/AppProg` ja sitten luo virtual environment suorittamalla komento `python -m venv env`
5. Avaa VSCode ja avaa `AppProg` kansio **(File -> Open Folder)**
6. VSCodessa paina `CTRL + SHIFT + P` ja kirjoita `Python: Select Interpreter`</br>
-> Etsi ja valitse luomasi virtual environment</br>
![image](https://user-images.githubusercontent.com/18125997/141789454-80852a7c-3f13-4cb4-b9b1-18b52d9e6302.png)

7. VSCodessa paina `CTRL + SHIFT + P` ja kirjoita `Python: Create Terminal`</br>
VSCodeen pitäisi aueta Python terminaali, varmista että **(env)** teksti näkyy</br>
(tässä voi olla ongelmia/poikkeavuuksia joten jos ei toimi, kysy apua)</br>
![image](https://user-images.githubusercontent.com/18125997/141789680-4b7772ef-c185-41e1-b0e1-fdf8bd189e8a.png)

8. Asenna Django ja muut paketit suorittamalla komento `pip install -r requirements.txt` (VSCoden terminaaliin)
9. Tarkista että ne asentui suorittamalla komento `pip freeze`
10. Siirry hakemistossa `src` kansioon kirjoittamalla `cd src/`</br>
11. Suorita komento `py manage.py makemigrations`
12. Suorita komento `py manage.py migrate`
13. Käynnistä Django palvelin `py manage.py runserver`
14. Testaa toimiiko testisivu `http://127.0.0.1:8000/`
