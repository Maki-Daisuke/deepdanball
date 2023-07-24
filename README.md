# Deepdanball

Docker image to interrogate multiple images in a batch by DeepDanbooru.


## Usage

```
git clone [THIS REPOSITORY]
cd deepdanball
docker build -t deepdanball .
cd [YOUR IMAGES DIRECTORY]
docker run -it --mount "type=bind,src=$(realpath .),dst=/mnt" deepdanball *.png
```


## License

MIT License
