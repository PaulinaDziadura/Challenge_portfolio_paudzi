## Spis treści
* [Zadanie 1 - Konfiguracja oprogramowania](#zadanie-1)
  * [Podzadanie 1](#podzadanie-1)
  * [Podzadanie 4](#podzadanie-4)

* [Zadanie 2 - Selektory](#zadanie-2)
* [Zadanie 3 - Pierwszy test automatyczny i asserty](#zadanie-3)
* [Zadanie 4 - Refactor, debugger i przypadki testowe](#zadanie-4)
* [Zadanie 5 - Robot framework](#zadanie-5)
* [Zadanie 6 - Zgłaszanie bugów i raport z testów](#zadanie-6)
 
# Zadanie 1 
## Konfiguracja oprogramowania

## Podzadanie 1
### "Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?"

1. Mam na imię Paulina i jestem kulturoznawczynią zakochaną w Pythonie...Dysonans? Bynajmniej 😃.
Cenię sobie w życiu równowagę, chciałam więc sprawdzić jak poradzę sobie w czymś "z zupełnie innej beczki". 

2. Na 8-miesięcznym kursie Cyber Trainees organizowanym przez Instytut Kościuszki i Fundację Microsoft poznałam Pythona i...przepadłam 🤓. 

3. Nauczyłam się solidnych podstaw pisania w tym języku, ukończyłam również klasę testerską, tak więc wyzwanie **Dare IT - Wstęp do testów automatycznych** - które łączy testowanie z Pythonem - wydało mi się wyborem całkowicie naturalnym.

4. Chcę poznać lepiej Github, stworzyć własne portfolio i wykorzystać dotychczasową wiedzę w praktyce.

## Podzadanie 4:

Wynik testu PURPUROWEGO http://getistqb.com/quiz-purpurowy/:

![img_1.png](img_1.png)

# Zadanie 2 
### Selektory

To zadanie nauczyło mnie:

✅ czym są selektory,

✅ gdzie szukać selektorów,

✅ zapisu xPath’ów,

✅ czym się kierować, aby wyodrębnić te “najlepsze” selektory

#### Selektory do strony logowania 
**https://scouts-test.futbolkolektyw.pl/**

<details>
 <summary>scouts_panel_header_xpath</summary>
<p>

- ```//h5```
- ```//*[text()="Scouts Panel"]```
- ```//h5[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom"] ```
</p>
</details>
<details>
 <summary>login_field_xpath</summary>
<p>

- ```//*[@id="login"]```
- ```//input[@name="login"]```
- ```//*[@id="__next"]/form/div/div/div/div/input ```
</p>
</details>
<details>
 <summary>password_field_xpath</summary>
<p>

- ```//*[@id="password"]```
- ```//input[@name="password"]```
- ``` //form/div/div/div[2]/div/input ```
</p>
</details>
<details>
 <summary>remind_password_hyperlink_xpat</summary>
<p>

- ```//*[@id="__next"]/form/div/div[1]/a```
- ```//*[text()="Remind password"]```
- ``` //child::div/a ```
</p>
</details>
<details>
 <summary>language_button_xpath</summary>
<p>

- ```//*[@id="__next"]/form/div/div[2]/div/div```
- ```//*[text()="English"]]```
- ``` //*[contains(@class, "MuiSelect-root MuiSelect-select")]  ```
</p>
</details>
<details>
 <summary>sign_in_button_xpath</summary>
<p>

- ```//*[@id="__next"]/form/div/div[2]/button/span[1]```
- ```//*[text()="Sign in"]```
- ``` //*[contains(@class, "MuiButton-l")]   ```
</p>
</details>

# Zadanie 3 
### Pierwszy test automatyczny i asserty

To zadanie pozwoliło mi m.in.:

✅ poznać framework Selenium,

✅ klikać w elementy na stronie,

✅ wypełniać pola tekstem,

✅ wykorzystywać assert title, 

✅ uruchomić test

﻿🚨 **Zajrzyj do plików z kodem, by ocenić moją pracę!** 😊
https://github.com/PaulinaDziadura/Challenge_portfolio_paudzi.git

# Zadanie 4 
### Refactor, debugger i przypadki testowe

W tym zadaniu m.in.:

✅ wykonaliśmy refactor naszego kodu,

✅ dowiedzieliśmy się jak pracować z debuggerem,

✅ zaprojektowaliśmy i napisaliśmy własne test case’y,

✅ zautomatyzowaliśmy stronę internetową na podstawie TC.

﻿🚨 **Poniżej link do folderu, w którym znajdziesz moje Test Case'y:**

https://drive.google.com/drive/folders/1_ImIsMVBsofccNHl1ZmAkKrP1K7fJCOz?usp=share_link

# Zadanie 5 
### Robot framework

To zadanie pozwoliło mi m.in.:

✅ dowiedzieć się czym jest Smoke Tests

✅ dowiedzieć się jak skonfigurować Suite Test

✅ poznać nowy framework,

✅ wygenerować automatycznie raport


﻿🚨 **Poniżej link do mojego repo z robotem**😊

👉 https://github.com/PaulinaDziadura/dareit_challenge_portfolio_robotframework.git

# Zadanie 6 
### Zgłaszanie bugów i raport z testów

To zadanie pozwoliło mi m.in.:

✅ Wykorzystać projekty w celu wyłapywania bugów

✅ Zapoznać się ze strukturą prawidłowo zgłoszonego buga

✅ Zapoznać się ze strukturą raportów z testów

✅ Stworzyć repozytorium z funkcjonalnym portfolio w README file

﻿🚨 **Poniżej link do folderu z raportem i zgłoszonymi bugami**
👉https://docs.google.com/spreadsheets/d/1-PcKtRM2DiPMSbgT_pFD5FL2E60Hn9dbKGnShh4MmL8/edit?usp=share_link

**oraz do mojego portfolio:**
👉 https://github.com/PaulinaDziadura/Paulina-Dziadura.git


