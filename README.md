# Feodora


Feodora - Script for resaving images with GUI  V3 (python 3 and tkinter)
> Феодора - Скрипт для пересохранения изображений с графическим интерфейсом (python 3 и tkinter)

![Light screenshot](https://github.com/blyamur/Feodora/blob/main/ezgif-2-0b191cd9961c.png)

### Version 3.1 (current):

A small development of the script / program, which was laid out [earlier](https://github.com/blyamur/Python-Resaving-Image-with-GUI).

For general convenience and expansion of capabilities, some optional features have been added. For example, now you can select several images at once. Added the ability to compress images by lowering the quality when saving, taking into account the conversion process first into the .BMP format, which itself is quite weighty in volume, and then into the original format, such compression is sometimes necessary.

Also added the ability to enable or disable image enhancement by increasing contrast and sharpness. Well, in order not to produce a bunch of files, you can now enable overwriting of originals with new files. And the names of new files are now without random symbols, but with the addition of the work done, if compression was added "compressed", if improved "enhance". Well, what is not unimportant, the interface has become somewhat more modern. A general list of features will be below.


> Небольшое развитие скрипта\программы, который выкладывался ранее.
> Для общего удобства и расширения возможностей добавлены некоторые опциональные возможности. Например теперь можно выбрать сразу несколько изображений сразу. Добавлена возможность сжатия изображений за счет понижения качества при сохранении, учитывая процесс конвертации сначала в формат .BMP, который сам по себе довольно весомый по объему, а потом уже в исходный формат, такое сжатие бывает необходимо.
> Так же добавлена возможность включать или выключать улучшение изображения, за счет повышения контрастности и резкости. Ну и чтобы не плодить кучу файлов, теперь можно включить перезапись оригиналов новыми файлами. А названия новых файлов теперь без рандомным символов, но с добавлением проделанной работы, если было сжатие будет добавлено «compressed«, если улучшено «enhance«. Ну что не маловажно, интерфейс стал несколько более современным. Общий список возможностей будет ниже.


Simple to use. We turned on the options we needed, pressed the image selection button, selected all those images that need to be saved and are waiting for the end of the work. The finished images are in the same place as the originals.
> Пользоваться просто. Включили нужные нам опции, нажали кнопку выбора изображений, выбрали все те изображения, которые необходимо пересохранить и ждем окончания работы. Готовые изображения там же, где и оригиналы. 
> 
![Light screenshot](https://github.com/blyamur/Feodora/blob/main/ezgif-2-0b191cd9961c.gif)

The first photo is the original, then the photo after resaving with compression, the photo with compression and enhancement, and in the last version, only the enhancement option is enabled. The first two results are smaller than the original, somewhere much smaller, somewhere the difference is almost imperceptible. Visually, there is practically no difference between the original and the saved versions.
> Первое фото-оригинал, далее фотография после пересохранения с сжатием, фотография с сжатием и улучшением и в последнем варианте включена только опция улучшения. Первые два результата имеют размер меньше оригинала, где-то существенно меньше, где-то разница практически незаметна. Визуально практически не видно разницы между оригиналом и сохраненными вариантами.

![Light screenshot](https://github.com/blyamur/Feodora/blob/main/process_il_cat-1280x599.jpg)

In the latter case, the file size even increased by an order of magnitude, this is due to the fact that the amount of information in the image itself increased after increasing the contrast and sharpness. This enhancement parameter, like the compression parameter, can be changed as needed in the script (line 106 and line 141).
> В последнем случае размер файла даже вырос на порядок, это связано с тем, что увеличилось количество информации в самом изображении после повышения контрастности и резкости. Этот параметр улучшения, как и параметр сжатия, при необходимости можно изменить в скрипте (строка 106 и строка 141).

Inside, the following process takes place: the program makes a copy of the file, while saving it in .bmp, then opens only the created .bmp file and simply renames it to the format that was previously.
> Внутри происходит следующий процесс: программа делает копию файла, при этом сохраняя его в .bmp, затем открывает только созданный .bmp файл и просто переименовывает в тот формат, который был ранее. 


You can make your own version of the application by taking a script with the source code from Github python (it was written for Python 3.8), the necessary sources of the icon in the .PNG format and the finished icon file in the .ICO format. All this can be edited, removed or added to its functionality and, if desired, through pyinstaller, compile into one file, after unpacking all the contents of the archive into one folder (for example, Feodora_(lang)).
> Вы можете сделать свой вариант приложения, взяв с Github python скрипт с исходным кодом (писалось под версию Python 3.8), необходимые исходники иконки в формате .PNG и готовый файл иконки в формате .ICO. Все это можно отредактировать, что-то убрать или дописать свой функционал и при желании через pyinstaller собрать в один файл, предварительно распаковав все содержимое архива в одну папку (например Feodora_(язык)).


For convenience, two versions have been made:
> Для удобства сделаны две версии: 

#### Feodora_en.py - English version |  Feodora_ru.py  - Русская версия

You need to download the version of the script you need, the icon, the theme file and the folder with the theme design. Then it only remains to run the script on the PC if you have Python 3 installed or build it into an executable file through pyinstaller. For example, for windows, the assembly command for me looked like this:
> Необходимо скачать нужную вам версию скрипта, иконку, файл темы и папку с оформлением темы. Далее останется только запустить скрипт на пк, если у вас установлен Python 3 или через pyinstaller собрать в исполняемый файл. Например для windows команда на сборку у меня выглядела так:

``` 
pyinstaller Feodora_ru.py --noconsole --onefile --icon=icon.ico
```

#### Download programs in EXE | Скачать программы в EXE 

[Feodora__RU](https://3le.ru/aNQkwO)  - 14 Mb ZIP  From the author's server through the short link service

[Feodora_EN](https://3le.ru/RREe)  - 14 Мб Mb ZIP  From the author's server through the short link service

The performance was tested on Windows 7-10 | Работоспособность проверялась на Windows 7-10


#### What's new in version 3.1  | Что нового в версии 3.1

- New visual design based on TTK theme Spring-Noon
- Animation when enabling / disabling options
- Ability to enable replacement of original images with resaved ones
- Ability to enable Image Compression
- Ability to enable Image Enhancement
- Multi-selection, the ability to process multiple images at once
- Check for updates

#### Что нового в версии 3.1

- Новое визуальное оформление на базе TTK темы Spring-Noon
- Анимация при включении \ отключении опций
- Возможность включить замену оригиналов изображений, пересохраненными
- Возможность включить Сжатие изображений
- Возможность включить Сжатие изображений
- Возможность включить Улучшение изображений
- Мультивыбор,возможность обработки сразу нескольких изображений
- Проверка наличия обновлений



### Copyrights and Licenses
Not for commercial use.

© 2021  [Mons](https://blog.mons.ws)

### Special thanks
> Отдельная благодарность  

[rdbende](https://github.com/rdbende/Sun-Valley-ttk-theme) and his ttk Theme Sun-Valley-ttk-theme, based on which the current [Theme](https://github.com/blyamur/Spring-Noon-ttk-theme) was made.

### Did you find this useful?!
> Вы нашли это  полезным ?!

Happy to hear that :) *If You want to help me, you can buy me a cup of cup of coffee ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [PayPal](https://paypal.me/enkonu) )*

> Рад это слышать :) Если вы хотите мне помочь, вы можете угостить меня чашкой кофе


*Thanks for reading :heart_eyes_cat:*
> Спасибо за чтение!

~Mons

