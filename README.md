# rassam-challenge
First, install the software packages with the following command.

$ pip install -r requirements.txt

Then there is an .env file where you can import postgresql database information.

Then run a file called install.py first of all to create the required table inside the database and import csv data into the database. There is a point here that in this file, the time to import data is simultaneously translating the country field, which prolongs the installation process. If necessary, you can disable this part of the code.

Then the menu.py file is the main menu, which has several main menus. 1- Adding new information to the database 2- It is also a statistic of the number of users based on gender in relation to the country entered.

There are a number of other folders, such as classes, that try to use object-orientation and factory method design pattern to cover that part as well.





در ابتدا با دستور زیر پکیج های نرم افزار رو نصب کنید.

$ pip install -r requirements.txt

سپس یک فایل .env هستش که می تونید اطلاعات دیتابیس postgresql رو واردکنید.

بعدش یک فایل با نام install.py اون اول از همه اجرا بگیرید تا جدول مورد نیاز در داخل دیتابیس ایجاد بشه و داده های csv هم به داخل دیتابیس import بشه .
یک نکته ای اینجا وجود داره که داخل این فایل زمان import داده همزمان داره translate شدن فیلد countryانجام میشه که این عمل باعث طولانی شدن پروسه نصب میشه . 
اگر نیاز بود میتونید این بخش رو از کد غیرفعال کنید . 


سپس فایل menu.py منوی اصلی هستش .که چندید منوی اصلی داره . 
1-افزودن اطلاعات جدید به دیتابیس 2- یه آماری از تعداد کاربران براساس جنسیت نسبت به کشور وارد شده هم هستش

یه سری پوشه های دیگه هم هستش مثل classes که سعی شده از شی گرایی و الگوی طراحی factory method استفاده بشه که اون بخش هم پوشش داده بشه. 
