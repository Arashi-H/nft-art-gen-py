# Python Generative Art Engine

Python program focused on creating generative NFT collections based on layers of art. 

## Project Goals

Making a platform-agnostic generative art program for programmers and non-programmers alike. 
Includes an extra focus for Fantom marketplaces e.g. PaintSwap. The source is written in **Python** to make it easy and more accesible to contribute to.


## Dependencies
* PyYAML
* Pillow (PIL Fork)
* All other dependencies come built-in with Python.

## How to use

### Organise Layers

Inside the `art-engine` directory, create a new folder called assets. Inside of should be
all of your organised folders of layers to be used to create your images. It should look
something like this:

    └── assets/
    
        ├── Body/
        
        │   ├── Alien
        │   ├── Human
        │   ├── Robot
        │   └── Monster
        
        ├── Beard/
        
        │   ├── Long Beard
        │   ├── Short Beard
        │   ├── Cool Beard
        │   └── Pink Beard
        
        └── Eye Accessory/
            ├── Sunglasses
            ├── Eyepatch
            └── Visor

In the `config.yaml` file add your layer folder names, exactly as they appear in your assets folder. Place them in the order you wish to appear, e.g. Background, then Body, then Eye
Accessory etc.

### Setting Rarities

The values in the rarities represent how often you want each layer to occur as a percentage out of 100.

For example, if you have two backgrounds, you may set the rarities to `[80, 20]`. 

The rarities should be in the same order as the layers are in the folder (typically alphabetical).

If the layer is *not* mandatory - e.g. a hat/accessory - add an extra value into rarities to represent the None value.

For example, if you have two hats, you could set the rarities as `[60, 30, 10]`. This means the first hat will occur 60% of the time, the second 30% of the time, and *no accessory* 10% of the time.

### Running The Program

Inside of the `py-nft-generator` folder, open a terminal and run `python art-engine` and your
images and metadata will start being created :partying_face:

## Contributing

1.  Fork it!
2.  Create your feature branch: `git checkout -b my-new-feature`
3.  Commit your changes: `git commit -m 'Add some feature'`
4.  Push to the branch: `git push origin my-new-feature`
5.  Submit a pull request

## License
MIT © [felwintrr](https://github.com/felwintrr)
