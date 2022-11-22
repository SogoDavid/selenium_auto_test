## Selenium tests with Pytest/Allure by Page Object
___
This project created by pattern PageObject. In this project integrated reporting system Allure with attach screenshot, severity settings, create epics and update marking to optimal version. Same, I upgraded configurations for cross-browser testing on different languages. In GitHub actions I created linter. 
___

**For check this project do next steps:**
- Clone this repository https://github.com/SogoDavid/selenium_auto_test
- Open project in your IDE
- Set requirements.txt file: $ pip -r install requirements.txt
- Set chromedriver and/or geckodriver on your host
- Use next scripts in IDE terminal:

```python
if   You want start tests on "ru" language(Chrome):
     $ pytest -s -v --language=ru --alluredir=allure_results 

elif You want start tests on "en" language(Chrome):
     $ pytest -s -v --alluredir=allure_results 

elif You want start tests on "ru" language(Firefox):
     $ pytest -s -v --browser_name=firefox --language=ru --alluredir=allure_results 

elif You want start tests on "en" language(Firefox):
     $ pytest -s -v --browser_name=firefox --alluredir=allure_results

elif You want start tests by markers:
     $ pytest -v -m "smoke or need_review" --alluredir=allure_results

else:
     You can start tests with browsers configuration and markers. Let us say:
     $ pytest -v -m "smoke or need_review" -s --browser_name=firefox --language=ru --alluredir=allure_results

```
```python
try: 
    You can retest if tests was crashed:
    $ pytest --lf

finally:
    You can open allure report after test runs:
    $ allure serve allure_results
```
___
Thank You for attention!
___

![Python](https://img.shields.io/badge/-Python-234E70?style=for-the-badge&logo=python&logoColor=FBF8BE)
![Pytest](https://img.shields.io/badge/-Pytest-234E70?style=for-the-badge&logo=pytest&logoColor=FBF8BE)
![Selenium](https://img.shields.io/badge/-Selenium-234E70?style=for-the-badge&logo=selenium&logoColor=FBF8BE)
![Allure](https://img.shields.io/badge/-Allure-234E70?style=for-the-badge&logo=allure&logoColor=FBF8BE)




