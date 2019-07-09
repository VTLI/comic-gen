# COMIC-GEN - Generate Comics with Tensorflow 

How to start your own training / generation of comics:

* **1 |** Download the **'code'** folder [here](https://github.com/ARGNZXT/comic-gen/releases/tag/v0.2-beta)

* **2 |** Open the **'resize_comics.py'** script and edit following things:

  **(PLEASE DON'T USE SPACES IN YOUR PATHS!)**

  * **2.1 |** source_path = **'YOUR\COMICS\SOURCE\PATH'**
  * **2.2 |** resize_save_location = **'YOUR:\\SAVE\\LOCATION\\FOR\\RESIZED\\OUTPUT'**
  * **2.3 |** target_image_height = **250** (or whatever you prefer, the bigger the longer the training takes)

* **3 |** Open the **'main.py'** script and edit any parameters to your likings

  (Change the epoch - the amount of time the training will go through your dataset)
  * **3.1  |** ("epoch", 25, "Epoch to train [25]")** 
  
  (Change the data_dir according to your comics that you resized before - 
  * **3.1  |** ("data_dir", "E:/Comics", "path to datasets [e.g. $HOME/data]")
  
  (Change the input_height and input_width according to your 
  * **3.1  |** source_path = **'YOUR\COMICS\SOURCE\PATH'**
