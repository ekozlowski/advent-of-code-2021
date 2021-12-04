all: clean build run

default: clean build run

part2:
	gcc -Wall -o part2.exe part2.c
	./part2.exe

run:
	./part1.exe

build:
	gcc -Wall -o part1.exe part1.c


clean:
	rm part1.exe || true
	rm part2.exe || true

