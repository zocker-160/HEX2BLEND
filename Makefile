build:
	mkdir tmp
	cp -r src/*.py tmp
	zip -r -o hex2blend.zip tmp
	rm -rf tmp
clean:
	rm *.zip
