# COMIC-GEN - Generate Comics with Tensorflow 

How to start your own training / generation of comics:

* **1 |** Download the **'code'** folder [here](https://github.com/ARGNZXT/comic-gen/releases/tag/v0.2-beta)

* **2 |** Open the **'resize_comics.py'** script and edit following things:

  * **2.1 |** source_path = **'YOUR\COMICS\SOURCE\PATH'**
  * **2.2 |** resize_save_location = **'YOUR:\\SAVE\\LOCATION\\FOR\\RESIZED\\OUTPUT'**
  * **2.3 |** target_image_height = **250** (or whatever you prefer, the bigger the longer the training takes)

* **3 |** Open the **'main.py'** script and edit any parameters to your likings

  (Recommmended edits)
  * **3.1  |** ("epoch", **25**, "Epoch to train [25]") / how often a set of comics will be read during training
  * **3.1  |** source_path = **'YOUR\COMICS\SOURCE\PATH'**
