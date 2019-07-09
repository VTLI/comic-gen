# COMIC-GEN - Generate Comics with Tensorflow 

**PREREQUISITES:**
Python, Tensorflow, own set of comics

**How to start your own training / generation of comics:**

* **1 |** Download the **'code'** folder [here](https://github.com/ARGNZXT/comic-gen/releases/tag/v0.2-beta)

* **2 |** Open the **'resize_comics.py'** script and edit following things:

  **(PLEASE DON'T USE SPACES IN YOUR PATHS!)**

  * **2.1 |** source_path = **'YOUR\COMICS\SOURCE\PATH'**
  * **2.2 |** resize_save_location = **'YOUR:\\SAVE\\LOCATION\\FOR\\RESIZED\\OUTPUT'**
  * **2.3 |** target_image_height = **250** (or whatever you prefer, the bigger the longer the training takes)

* **3 |** Open the **'main.py'** script and edit any parameters to your **likings**

  * **3.1  |** Change the epoch - the amount of time the training will go through your dataset
  
  > ("epoch", **25**, "Epoch to train [25]")** 
  
  * **3.2  |** Change the data_dir according to your comics that you resized before
  
  > ("data_dir", **"E:/Comics"**, "path to datasets [e.g. $HOME/data]")
  
  
  * **3.3  |** Change the input_height and input_width according to your resized comics height/width
  
  > ("input_height", **400**, "The size of image to use (will be center cropped))
  
  > ("input_width", **263**, "The size of image to use (will be center cropped))
  
   * **3.4  |** Change the output_height and output_width according to wishes
   
  > ("output_height", **400**, "The size of the output images to produce")
  
  > ("output_width", **263**, "The size of the output images to produce.)
                
   * **3.5  |** Change the output directory, where the generated comics [samples] will be exported  
                
  > ("out_dir", **"./out"**, "Root directory for outputs [e.g. $HOME/out]")


* **4 |** Download the **'code'** folder [here](https://github.com/ARGNZXT/comic-gen/releases/tag/v0.2-beta)

