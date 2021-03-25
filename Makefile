build:
	mkdir io_scene_hex
	cp -r src/*.py io_scene_hex
	zip -r -o hex2blend.zip io_scene_hex
	rm -rf io_scene_hex
clean:
	rm *.zip
