all: analyzer

analyzer: analyzer.c
	gcc -o analyzer analyzer.c

clean:
	rm -f analyzer